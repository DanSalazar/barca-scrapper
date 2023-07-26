import requests
from bs4 import BeautifulSoup, Tag

urls = {
	"players": "https://www.fcbarcelona.com/en/football/first-team/players",
	"results": "https://www.fcbarcelona.com/en/football/first-team/results",
	"clasification": "https://www.fcbarcelona.com/en/football/first-team/standings",
	"schedule": "https://www.fcbarcelona.com/en/football/first-team/schedule",
}

classes = {
	"players": "team-person",
	"results_container": "fixture-result-list__listings--desktop",
	"clasification": "table-standings-row",
	"schedule_container": "fixture-result-list__wrapper",
}


# '\\example.com => example.com'
def clean_src(src: str):
	return src.replace("//", "")


def navigables_to_string(tree, lower: bool, strip: bool):
	def mapping(el):
		string = str(el.string)
		if lower:
			string = string.lower()
		if strip:
			string = string.strip()
		return string

	return list(map(mapping, tree))


def get_players():
	''' 
		Returns all the players of the FC Barcelona Squad 
	'''
	players_data = []
	request = requests.get(urls["players"]).text
	soup = BeautifulSoup(request, "html.parser")
	players = soup.find_all("a", class_=classes["players"])

	players_classes = {
		"player_first_name": "team-person__first-name",
		"player_last_name": "team-person__last-name",
		"player_number": "team-person__number",
		"player_position": "team-person__position-meta",
		"player_stats": "player-stats-footer__title",
	}

	for player in players:
		first_name = player.find("span", class_=players_classes["player_first_name"])
		# Get the string attribute could be possibly None
		first_name = getattr(first_name, "string", "") or ""
		last_name = player.find(
				"span", class_=players_classes["player_last_name"]
		).string
		full_name = f"{first_name} {str(last_name).capitalize()}".strip()

		players_data.append(
			{
				"name": full_name,
				# It can't get the number of Gavi
				"number": "6"
				if last_name == "Gavi"
				else player.find(
						"span", class_=players_classes["player_number"]
				).string,
				"position": str(
						player.find("li", class_=players_classes["player_position"]).string
				).capitalize(),
				"img_url": player.find("img")["data-image-src"]
			}
		)

	return players_data

def get_results():
	''' 
		Returns all match results since July 
	'''
	results_data = {}
	request = requests.get(urls["results"]).text
	soup = BeautifulSoup(request, "html.parser")
	container = soup.find("div", class_=classes["results_container"])
	fixtures = None
	months = None

	if isinstance(container, Tag):
		fixtures_classes = {
			"result_month": "fixture-result-list__month-abbreviation",
			"result_fixture": "fixture-result-list__fixture",
			"competition": "visually-hidden",
			"date": "fixture-result-list__fixture-date",
			"stage": "fixture-result-list__stage",
			"location": "fixture-result-list__stage-location",
			"home_team": "fixture-info__name--home",
			"away_team": "fixture-info__name--away",
			"result": "fixture-info__score",
			"team_logo": "badge-image"
		}

		fixtures = container.find_all(
			"div", class_=fixtures_classes["result_fixture"]
		)
		# month = month year
		months = navigables_to_string(
			container.find_all("div", class_=fixtures_classes["result_month"]),
			lower=True,
			strip=False,
		)
		current_month = months[0] if months[0] else "unknown-date"
		index = 0
		results_data[current_month] = []

		for m in fixtures:
			logos = m.find_all("img", class_=fixtures_classes["team_logo"])
			current_date = (
				str(m.find("div", class_=fixtures_classes["date"]).string)
				.strip()
				.lower()
			)

			fixture = {
				"competition": m.find(
					"span", class_=fixtures_classes["competition"]
				).string,
				"date": current_date,
				"stage": m.find("div", class_=fixtures_classes["stage"]).string,
				"location": m.find("div", class_=fixtures_classes["location"]).string,
				"home_team": m.find(
					"div", class_=fixtures_classes["home_team"]
				).get_text(strip=True),
				"home_team_logo": clean_src(logos[0]["src"]),
				"away_team": m.find(
					"div", class_=fixtures_classes["away_team"]
				).get_text(strip=True),
				"away_team_logo": clean_src(logos[2]["src"]),
				"result": m.find("div", class_=fixtures_classes["result"]).span.string,
			}

			if current_date.find(current_month.split(" ")[0]) > 0 and index < len(months):
				results_data[current_month].append(fixture)
			else:
				index += 1
				current_month = months[index]
				results_data[current_month] = [fixture]

	return results_data

def get_clasification():
	''' 
		Returns current clasification table in LaLiga in array 
	'''
	clasification_data = []
	request = requests.get(urls["clasification"]).text
	soup = BeautifulSoup(request, "html.parser")
	table = soup.find_all("tr", classes["clasification"])

	clasification_classes = {
		"position": "position-row__number",
		"team": "team-row__name",
		"team_logo": "badge-image",
		"stats": "table-stat-row",
		"next_match": "next-match",
		"last_results": "team-form__abbreviation"
	}

	for t in table:
		# Points, Matches played, Wins, Draws, Losses, Goals for, Goals against, Goals difference
		stats = navigables_to_string(
			t.find_all("td", class_=clasification_classes["stats"]),
			lower=False,
			strip=True,
		)
		last_results = navigables_to_string(
			t.find_all("abbr", class_=clasification_classes["last_results"]),
			lower=False,
			strip=False,
		)

		next_match = (
			t.find("td", class_=clasification_classes["next_match"]).contents[1].img
		)

		clasification_data.append(
			{
				"position": t.find(
					"span", class_=clasification_classes["position"]
				).string,
				"team": t.find("span", clasification_classes["team"]).string,
				"team_logo": clean_src(
					t.find("img", class_=clasification_classes["team_logo"])["src"]
				),
				"points": stats[0],
				"matches_played": stats[1],
				"wins": stats[2],
				"draws": stats[3],
				"losses": stats[4],
				"goals_for": stats[5],
				"goals_against": stats[6],
				"goals_difference": stats[7],
				"last_results": last_results,
				"next_match": next_match["alt"],
				"next_match_logo": clean_src(next_match["src"])
			}
		)

	return clasification_data


def get_schedule():
	''' 
		Returns all upcoming matches in the schedule
	'''
	next_fixtures_data = {}
	request = requests.get(urls["schedule"]).text
	soup = BeautifulSoup(request, "html.parser")
	container = soup.find("div", class_=classes["schedule_container"])

	if isinstance(container, Tag):
		schedule_classes = {
			"fixtures": "fixture-result-list__link",
			"month": "fixture-result-list__month-abbreviation",
			"competition": "fixture-result-list__fixture-competition",
			"date": "fixture-result-list__fixture-date",
			"date_hour": "fixture-info__time",
			"stage": "fixture-result-list__stage",
			"location": "fixture-result-list__stage-location",
			"home_team": "fixture-info__name--home",
			"away_team": "fixture-info__name--away",
			"team_logo": "badge-image",
		}

		months = navigables_to_string(
			container.find_all("div", class_=schedule_classes["month"]),
			lower=True,
			strip=False,
		)
		current_month = months[0] if months[0] else "unknown-date"
		index = 0
		next_fixtures_data[current_month] = []

		fixtures = container.find_all("a", class_=schedule_classes["fixtures"])

		for f in fixtures:
			logos = f.find_all("img", class_=schedule_classes["team_logo"])
			current_date = (
				str(f.find("div", class_=schedule_classes["date"]).string)
				.strip()
				.lower()
			)
			competition = (
				f.find("div", class_=schedule_classes["competition"])
				.find("span", class_="visually-hidden")
				.string
			)

			next_fixture = {
				"competition": competition,
				"date": str(
						f.find("div", class_=schedule_classes["date"]).string
				).strip(),
				"date_hour": str(
						f.find("div", class_=schedule_classes["date_hour"]).string
				).strip(),
				"stage": f.find("div", class_=schedule_classes["stage"]).string,
				"location": f.find("div", class_=schedule_classes["location"]).string,
				"home_team": str(
						f.find("div", class_=schedule_classes["home_team"]).string
				).strip(),
				"home_team_logo": clean_src(logos[0]["src"]),
				"away_team": str(
						f.find("div", class_=schedule_classes["away_team"]).string
				).strip(),
				"away_team_logo": clean_src(logos[2]["src"])
			}

			if current_date.find(current_month.split(" ")[0]) > 0 and index < len(months):
				next_fixtures_data[current_month].append(next_fixture)
			else:
				index += 1
				current_month = months[index]
				next_fixtures_data[current_month] = [next_fixture]

	return next_fixtures_data
