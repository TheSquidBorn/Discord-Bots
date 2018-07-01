import admin
import asyncio
import db
import discord
import gspread
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

class members():
	def __init__(self, client):
		self.client = client
		"""Commands for changing members statuses"""

	@commands.command(pass_context=True)
	async def lfg(self, ctx):
		"""Toggles role Looking for Group"""
		user = ctx.message.author
		role = discord.utils.get(ctx.message.server.roles, name="Looking For Group")
		await self.client.delete_message(ctx.message)
		if role in [r for r in user.roles]:
			await self.client.remove_roles(user, role)
		else:
			await self.client.add_roles(user, role)

	@commands.command(pass_context=True)
	async def addpoints(self, ctx):
		args = ctx.message.content.split(" ")
		user = args[1]
		points = args[2]
		db.AddPoints(user, points)

def setup(client):
	client.add_cog(members(client))