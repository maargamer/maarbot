import os
from turtle import color
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import requests
from bs4 import BeautifulSoup

from requests.structures import CaseInsensitiveDict
err_color = discord.Color.red()
color = 0x0da2ff
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to the discord server")


@bot.command(
    help="Responds you with a Hey!",
    brief="Greets you when all of your friends are offline!"
)
async def hi(ctx):
    await ctx.reply(f"Hey there!")


@bot.command(
    help="uses me as a search engine",
	brief="Pong back to your channel with the latency."
)
async def search( ctx, *, query):
    url_news = f"https://maarweb.com/search.php?term={query}"
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
    response = requests.get(url_news,headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    match_items = soup.find_all("div", class_="resultContainer")
    if match_items:

     for match in match_items:
       link = match.find('a', class_='result')['href']
    
       print(link)
       await ctx.send(f'{link}')
    else:
     await ctx.send(embed=discord.Embed(title="not found", description="sorry your search was not found", color=0xf90101)
)
    # got a non-empty string

    # got an empty string
  

@bot.command(
    help="Gives you a motivation to cut a mountain :)",
    brief="Gives quotes to boost your confidence"
)
async def givequote(ctx):
    response = requests.get('https://api.quotable.io/random')
    r = response.json()
    quote = r["content"]
    await ctx.send(quote)

@bot.command(
    help="Gives the dumbest joke in the name of a Chuck Norris",
    brief="Gives a dumb joke on Chuck Norris"
)
async def givejoke(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()['value']
    await ctx.send(joke)


@bot.command(
    help="Gives the topmost prime headlines!",
    brief="Gives prime headline of the moment!"
)
async def giveheadline(ctx):
    news_api_key = "your_api_key_here"
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={news_api_key}")
    headline = response.json()['articles'][0]['title']
    url = response.json()['articles'][0]['url']
    await ctx.send(f"{headline}\nFor more info, click here: {url}")


@bot.command(
    help="Gives the weather of your place",
    brief="Temperatures falling or rising; get to know everything here!"
)
async def givetemp(ctx):
    lat = "your_latitude"
    lon = "your_longitude"
    weather_api_key = "your_api_key_here"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}")
    kelvin = response.json()['main']['temp']
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    humidity = response.json()['main']['humidity']
    await ctx.send(f"Local Temperature:\n{celsius} degree Celsius\n{fahrenheit} degree Fahrenheit\nHumidity: {humidity}%")

@bot.command(
    help="Gives the best memes from reddit",
    brief="Drops some best hilarious memes trending on the Internet!"
)
async def givememe(ctx):
    response = requests.get("https://meme-api.com/gimme")
    r = response.json()
    meme = r["url"]
    await ctx.send(meme)

@bot.command(
    help="Gives IMDb rating, plot and poster of the movies or series you enter",
    brief="Let\'s binge baby!(based on IMDb ratings:))"
)
async def giverating(ctx, *, title: str = commands.parameter(description="- Title of the Movie/Series to be retrieved")):
    omdb_api_key = 'your_api_key_here'
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={title}"
    response = requests.get(url)
    await ctx.send(f"The IMDb rating of the movie/series \"{response.json()['Title']}\"({response.json()['Year']}) is "
                   f"{response.json()['imdbRating']} stars out of 10.\n\nThe plot "
                   f"description"
                   f" goes like this: {response.json()['Plot']}\n{response.json()['Poster']}")


private_key=os.getenv("PRIVATE_KEY")

bot.run(private_key)