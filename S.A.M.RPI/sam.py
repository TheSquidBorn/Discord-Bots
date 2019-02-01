import admin
import asyncio
import discord
import requests
from datetime import datetime
from threading import Timer
from discord.ext import commands
from discord import Game

class sam():
	def __init__(self, client):
		self.client = client
		"""Commands to change S.A.M.s Status"""

	@commands.command()
	async def apod(self):
		r = requests.get("https://api.nasa.gov/planetary/apod?api_key=JxHACldWATN21OaEW2MGZfpuzIRYMJIeLqZd1SWV").json()
		url = r["url"]
		if (url.startswith("https://www.youtube.com/embed/")):
			url = url.strip("https://www.youtube.com/embed/")
			url = "https://www.youtube.com/watch?v=" + url
		await send_message(485891401691955211, content=url)

	@commands.command(pass_context=True)
	async def playing(self, ctx):
		"""Changes S.A.M.s status"""
		game = ctx.message.content
		game = game.split(" ", 1)[1]
		f = open("config/playing.txt", "w")
		f.write(game)
		await self.client.change_presence(game=Game(name=game))

	@commands.command(pass_context=True)
	async def stop(self, ctx):
		"""Stops the bot"""
		server = ctx.message.server
		print("User stopped bot")
		print(ctx.message.author)
		if admin.HasAdmin(ctx.message.author, server):
			await self.client.say("Ah fuck, can't belive you done this.")
			await self.client.logout()
		else:
			await self.client.say("Who dis")

	@commands.command()
	async def space(self):
		response = requests.get("http://api.open-notify.org/astros.json")
		data = response.json()
		string = "There are currently " + str(data["number"]) + " humans in space"
		await self.client.say(string)

	@commands.command()
	async def astro(self):
		response = requests.get("http://api.open-notify.org/astros.json")
		data = response.json()
		string = "```\nPeople in space:\n"
		for p in data["people"]:
			string += p["name"]
			string += " " * (30 - len(p["name"]))
			string += p["craft"] + "\n"
		string += "```"
		await self.client.say(string)

	@commands.command()
	async def adopt_maja(self):
		await self.client.say("Already did that")

def setup(client):
	client.add_cog(sam(client))
