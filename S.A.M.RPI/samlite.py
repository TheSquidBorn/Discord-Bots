import asyncio
import admin
import discord
import logging
import requests
from datetime import datetime, timedelta
from discord import Game
from discord.ext import commands

prefix = ("!")
f = open("credentials/token.txt", "r")
token = f.read()

startup_extensions = ["members", "sam"]

description = '''
S erver
A ssistance
M odule
'''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
		print('Logged in as')
		print(bot.user.name)
		print(bot.user.id)

		f = open("config/playing.txt", "r")
		game = f.read()
		f.close

		await bot.change_presence(game=Game(name=game))

@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
	server = ctx.message.server
	if admin.HasAdmin(ctx.message.author, server):
		try:
			bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await bot.say("{} loaded.".format(extension_name))
	else:
		await self.client.say("Who dis")

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
	server = ctx.message.server
	if admin.HasAdmin(ctx.message.author, server):
		bot.unload_extension(extension_name)
		await bot.say("{} unloaded.".format(extension_name))
	else:
		await self.client.say("Who dis")

async def apod_task():
	await bot.wait_until_ready()
	channel = discord.Object(id='485891401691955211')
	while not bot.is_closed:
		r = requests.get("https://api.nasa.gov/planetary/apod?api_key=JxHACldWATN21OaEW2MGZfpuzIRYMJIeLqZd1SWV").json()
		url = r["url"]
		if (url.startswith("https://www.youtube.com/embed/")):
			url = url.strip("https://www.youtube.com/embed/")
			url = "https://www.youtube.com/watch?v=" + url
		time = datetime.now() + timedelta(days=1)
		time.replace(hour=8,minute=0,second=0,microsecond=0)
		delta = time - datetime.today()
		seconds = delta.total_seconds() 
		await asyncio.sleep(60 * seconds)
		await bot.send_message(channel, url)

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
		else:
			print("{} loaded.".format(extension))

bot.loop.create_task(apod_task())
print(discord.__version__)
logging.basicConfig(level=logging.INFO)
bot.run(token)