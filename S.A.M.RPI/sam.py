import asyncio
import discord
from discord.ext import commands
from discord import Game

class sam():
	def __init__(self, client):
		self.client = client

	@commands.command(pass_context=True)
	async def playing(self, ctx):
			game = ctx.message.content
			game = game.split(" ", 1)[1]
			f = open("playing.txt", "w")
			f.write(game)
			await self.client.change_presence(game=Game(name=game))

def setup(client):
	client.add_cog(sam(client))