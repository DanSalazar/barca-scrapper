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
For production environments...

```sh
flask --app run run --debug
```

## Example
```py
    from server.scrapper import get_players

    print(get_players())
    
    # Output: {
        'name': 'Ronald Araújo', 
        'number': '4', 
        'position': 'Defender', 
        'img_url': 'https://www.fcbarcelona.com/photo-resources/2022/11/02/04daeacd-0023-4927-a9df-417a942806ba/04-RONALD_ARAUJO_.jpg?width=470&height=470'
    }
```
## License

MIT
