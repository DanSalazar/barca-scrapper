#  Barca Scrapper
Get latest data of FC Barcelona from the website

## Features

- Latest data of FC Barcelona Squad
- Current clasification in the LaLiga Table
- Get latest results in matches
- Get all upcoming matches of the season

## Tech

- [Flask] - Flask is a lightweight Python web framework
- [requests] - Python library to make HTTP request
- [BeautifulSoup] - Python library for pulling data out of HTML and XML files

## Installation

Install the dependencies and devDependencies and start the server.
```sh
cd barca-scrapper
pip install -r requirements.txt 
python run.py
```
## Example
```py
from server.scrapper import get_clasification

print(get_clasification())

# Output: {
    'position': '1', 
    'team': 'FC Barcelona', 
    'team_logo': 'resources.fcbarcelona.pulselive.com/badges/club/40/BCN.png;', 
    'points': '62', 
    'matches_played': '24', 
    'wins': '20', 
    'draws': '2', 
    'losses': '2', 
    'goals_for': '46', 
    'goals_against': '8', 
    'goals_difference': '38', 
    'last_results': ['W', 'W', 'W', 'L', 'W'], 
    'next_match': 'Athletic Club', 
    'next_match_logo': 'resources.fcbarcelona.pulselive.com/badges/club/30/ATH.png;'
}
```
## License

MIT
