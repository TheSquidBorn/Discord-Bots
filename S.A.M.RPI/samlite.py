import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
f = open("token.txt", "r")
token = f.read()

client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True)
async def playing(ctx):
	game = ctx.message.content
	game = game.split(" ", 1)[1]
	await client.change_presence(game=Game(name=game))

@client.command(pass_context=True)
async def lfg(ctx):
	user = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Looking For Group")
	if role in [r for r in user.roles]:
		await client.remove_roles(user, role)
	else:
		await client.add_roles(user, role)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="fair, playing pharah"))
	print("Logged in as " + client.user.name)

client.run(token)