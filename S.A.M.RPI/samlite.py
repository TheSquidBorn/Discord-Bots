import asyncio
import discord
import logging
from discord import Game
from discord.ext import commands

prefix = ("!")
f = open("credentials/token.txt", "r")
token = f.read()

print("Do you want to use a custom Token?")
if (input() == "y"):
	token = input()

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

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
		else:
			print("{} loaded.".format(extension))

print(discord.__version__)
logging.basicConfig(level=logging.INFO)
bot.run(token)