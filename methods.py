import os
from string import ascii_letters
from datetime import datetime

from dotenv import load_dotenv
import webbrowser as wb
import requests as rq


load_dotenv()


def eris_says(text):
    """Print what Eris says"""
    print(f'Eris: {text}')


def ask(question):
    """Ask Eris anything and she will try to answer (WIP)"""
    eris_says(f'You asked "{question}"')


def google_search(query):
    """Search in Google for the typed query"""
    eris_says(f'Searching in Google for "{query}"')
    wb.open(f'https://google.com/search?q={query}', new=0)
    eris_says('Opening your browser...')


def youtube_search(query):
    """Search in Youtube for the typed query"""
    eris_says(f'Searching in Youtube for "{query}"')
    wb.open(f'https://www.youtube.com/results?search_query={query}', new=0)
    eris_says('Hope you enjoy it!')


def calc(query):
    """Calculate any simple mathematical expression without letters"""
    for char in query:
        if char in ascii_letters:
            eris_says('Sorry, only arithmetic operations allowed.')

    eris_says(f'{eval(query)}')


def current_weather(query):
    """Display current weather data from the chosen location"""
    _res = rq.get(f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={os.getenv("WEATHER_API_KEY")}&units=metric').json()

    if _res['cod'] != 200:
        eris_says('I\'m terribly sorry! It seems there was an error while I was trying to get the weather data.')
        return

    _sunrise = datetime.fromtimestamp(int(_res["sys"]["sunrise"])).strftime('%H:%M:%S')
    _sunset = datetime.fromtimestamp(int(_res["sys"]["sunset"])).strftime('%H:%M:%S')
    eris_says(f'Here\'s the current weather for {query}.')
    _weather_res = \
        f'     - Weather Type: {_res["weather"][0]["main"]}\n' \
        f'     - Weather Description: {_res["weather"][0]["description"].title()}\n' \
        f'     - Temperature: {_res["main"]["temp"]} ºC\n' \
        f'     - Min. Temp.: {_res["main"]["temp_min"]} ºC - Max. Temp.: {_res["main"]["temp_max"]} ºC\n' \
        f'     - Sunrise: {_sunrise}\n' \
        f'     - Sunset: {_sunset}\n' \
        f'     - Wind Speed: {_res["wind"]["speed"]} KM/h\n' \
        f'     - Wind Direction: {_res["wind"]["deg"]}º'
    print(_weather_res)


def get_news(query):
    """Get the last 3 news from a given subject"""
    _res = rq.get(f'https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={os.getenv("NEWS_API_KEY")}&language=en&page=1').json()

    eris_says(f'Here\'s the news I found about "{query}":')
    _line_divider =   '\n----------------------------------------------------------------------------\n'
    print(_line_divider)

    for news in _res['articles'][:3]:
        # convert 2021-03-24T01:55:26Z to 2021-03-24 01:55:26
        _published_date = datetime.strptime(news["publishedAt"], '%Y-%m-%dT%H:%M:%SZ')
        _title =         f'- Title: {news["title"]}\n'
        _description =   f'- Description: {news["description"]}\n'
        _published_at =  f'- Published At: {_published_date}\n'
        _url =           f'- URL: {news["url"]}\n'
        
        print(_title + _description + _published_at + _url + _line_divider)
