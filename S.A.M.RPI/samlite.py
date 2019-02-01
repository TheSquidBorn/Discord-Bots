import asyncio
import admin
import discord
import logging
import requests
import time
import urllib.request 
import tasks
import servers
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

logging.basicConfig(level=logging.INFO)

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

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
		else:
			print("{} loaded.".format(extension))

bot.loop.create_task(tasks.apod(bot))
bot.loop.create_task(servers.status(bot, "81.236.213.170"))
print(discord.__version__)

bot.loop.run_until_complete(bot.run(token))

