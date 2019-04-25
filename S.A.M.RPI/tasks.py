import sam_util
import asyncio
import discord
import requests
import os
import math
from datetime import datetime, timedelta
from discord.ext import commands
from discord import Game
from mcstatus import MinecraftServer

async def apod(bot):
    await bot.wait_until_ready()
    channel = discord.Object(id="485891401691955211")
    while not bot.is_closed:
        config = sam_util.getCfg()
        seconds = getSeconds(config["apodtime"][0], config["apodtime"][1])
        print("sleeping for " + str(seconds) + " seconds")
        await asyncio.sleep(seconds)

        r = requests.get("https://api.nasa.gov/planetary/apod?api_key=JxHACldWATN21OaEW2MGZfpuzIRYMJIeLqZd1SWV").json()
        title = "**" + r["title"] + "**\n"
        text = r["explanation"]
        url = r["url"]
        if url.split(".")[-1] == "jpg":
            with open('image.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                await bot.send_file(channel, "image.jpg")
                os.remove("image.jpg")
        elif url.split(".")[-1] == "gif":
            with open('image.gif', 'wb') as f:
                f.write(requests.get(url).content)
            await bot.send_file(channel, "image.gif")
            os.remove("image.gif")
        else:
            await bot.send_message(channel, r["url"])
        await bot.send_message(channel, (title + text))

def getSeconds(hour, minute):
    time = datetime.now()
    time = time.replace(hour=hour,minute=minute,second=0,microsecond=0)
    if time < datetime.now():
        time += timedelta(days=1)
    delta = time - datetime.today()
    seconds = int(delta.total_seconds())
    return seconds

async def server(bot):
    await bot.wait_until_ready()
    server = MinecraftServer("81.236.213.170", 25565)
    while not bot.is_closed:
        msg = "Server did not respond"
        try:
            status = server.status()
        except AttributeError:
            print("Attribute Error")
        except:
            print("Uncaught Error")
        else:
            msg = ("{0} players and {1} ping").format(status.players.online, math.floor(status.latency))
        await bot.change_presence(game=Game(name=msg))
        await asyncio.sleep(30)
        #TCPSocketConnection
