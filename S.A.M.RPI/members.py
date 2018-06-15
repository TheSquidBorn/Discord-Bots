import asyncio
import discord
from discord.ext import commands

class members():
	def __init__(self, client):
		self.client = client

	@commands.command(pass_context=True)
	async def lfg(self, ctx):
	    user = ctx.message.author
	    role = discord.utils.get(ctx.message.server.roles, name="Looking For Group")
	    await self.client.delete_message(ctx.message)
	    if role in [r for r in user.roles]:
	        await self.client.remove_roles(user, role)
	    else:
	        await self.client.add_roles(user, role)

def setup(client):
	client.add_cog(members(client))