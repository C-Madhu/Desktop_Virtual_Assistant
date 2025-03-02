import smtplib
from wsgiref import headers
import requests
import wikipedia
import pywhatkit as kit
from decouple import config
from email.message import EmailMessage
import requests

NEWS_API_KEY = "a6bb48eda85e406ba83b95a640439419"
TMDB_API_KEY = "5bfd5cd2882afc20040eb65bc225d1fb"
OPENWEATHER_APP_ID = "876516cdfb6f567e72955961e1abb8ad"


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]



def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)



def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/everything?q=apple&from=2022-01-16&to=2022-01-16&sortBy=popularity&apiKey={NEWS_API_KEY}").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

#https://newsapi.org/v2/everything?q=apple&from=2022-01-16&to=2022-01-16&sortBy=popularity&apiKey={NEWS_API_KEY}

#f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

#https://api.themoviedb.org/3/movie/550?api_key=5bfd5cd2882afc20040eb65bc225d1fb


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"