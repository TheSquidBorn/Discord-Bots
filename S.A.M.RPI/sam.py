import admin
import asyncio
import discord
from discord.ext import commands
from discord import Game

class sam():
	def __init__(self, client):
		self.client = client
		"""Commands to change S.A.M.s Status"""

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
		if admin.IsAdmin(ctx.message.author, server):
			await self.client.say("Ah fuck, can't belive you done this.")
			await self.client.logout()
		else:
			await self.client.say("Who dis")

def setup(client):
	client.add_cog(sam(client))