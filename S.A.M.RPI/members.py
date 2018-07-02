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

	@commands.command(pass_context=True)
	async def makepoll(self,ctx):
		user = ctx.message.author
		server = ctx.message.server
		if admin.HasAdmin(user, server):
			text = ctx.message.content.split(" ", 1)[1]
			name = text.split(" ")[0]
			text = text.split(" ", 1)[1]
			alternatives = text.split(",")
			for a in alternatives:
				a = a.strip(" ")
			db.MakePoll(name, alternatives)
			self.client.say("Made poll!")
		else:
			self.client.say("hey for security reasons(mostly bc squid is not that good at programming) polls can only be created by admins, just ask one and theyll set one up")

	@commands.command(pass_context=True)
	async def vote(self,ctx):
		id = ctx.message.author.id
		text = ctx.message.content.split(" ", 2)
		poll = text[1]
		alternative = text[2]
		if db.AddVote(id, poll, alternative):
			self.client.say("Voted")
		else:
			self.client.say("You have already Voted")

def setup(client):
	client.add_cog(members(client))