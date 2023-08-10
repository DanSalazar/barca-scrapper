const EXAMPLES = [
  {
    name: "Pedri",
    number: "8",
    position: "Midfielder",
    img_url: "https://www.fcbarcelona.com/photo-resources/2022/11/02/a4065cd7-9b67-4073-b957-80679c96e6c0/08-PEDRI.jpg?width=470&height=470"
  },
  {
    competition: "Trofeo Joan Gamper",
    date: "August, Tuesday 08, 2023",
    stage: "Final",
    location: "Estadi Olímpic Lluís Companys",
    home_team: "FC Barcelona",
    home_team_logo: "resources.fcbarcelona.pulselive.com/badges/club/40/BCN.png;",
    away_team: "Tottenham Hotspur",
    away_team_logo: "resources.fcbarcelona.pulselive.com/badges/club/40/TOT.png;",
    result: "4 - 2"
  },
  {
    position: "1",
    team: "FC Barcelona",
    team_logo: "resources.fcbarcelona.pulselive.com/badges/club/40/BCN.png;",
    points: "88",
    matches_played: "38",
    wins: "28",
    draws: "4",
    losses: "6",
    goals_for: "70",
    goals_against: "20",
    goals_difference: "50",
    last_results: [
      "W",
      "L",
      "L",
      "W",
      "L"
    ]
  },
  {
    competition: "La Liga",
    date: "August, Sunday 13, 2023",
    date_hour: "21:30",
    stage: "Matchday 1",
    location: "Coliseum Alfonso Pérez",
    home_team: "Getafe",
    home_team_logo: "resources.fcbarcelona.pulselive.com/badges/club/40/GET.png;",
    away_team: "FC Barcelona",
    away_team_logo: "resources.fcbarcelona.pulselive.com/badges/club/40/BCN.png;"
  }
]

const preElements = document.querySelectorAll('pre')

preElements.forEach((e, i) => {
	const text = JSON.stringify(EXAMPLES[i], undefined, 2);
	e.innerHTML = `<code class="language-json">${text}</code>`
})
