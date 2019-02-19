import asyncio
import sam_util
import discord
import getpass
import json
import os
import tasks
import logging

from discord import Game
from discord.ext import commands

if not os.path.exists("config.json"):
    print("Config file does not exist, creating new one and closing.")
    data = {}
    fields = ["token", "prefix", "game", "server", "logging", "apodkey"]
    for fi in fields:
        data[fi] = ""
    with open("config.json", 'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

config = sam_util.getCfg()

token   = config["token"]
prefix  = config["prefix"]
game    = config["game"]
server  = config["server"]
logging = config["logging"]

startup_extensions = ["sam"]
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=Game(name=game))

@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    server = ctx.message.server
    if sam_util.HasAdmin(ctx.message.author, server):
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
            await bot.say("{} loaded.".format(extension_name))
    else:
        await self.bot.say("Who dis")

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    server = ctx.message.server
    if sam_util.HasAdmin(ctx.message.author, server):
        bot.unload_extension(extension_name)
        await bot.say("{} unloaded.".format(extension_name))
    else:
        await self.bot.say("Who dis")

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
print(discord.__version__)
bot.loop.run_until_complete(bot.run(token))
