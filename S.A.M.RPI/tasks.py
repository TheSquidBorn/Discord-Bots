import sam_util
import asyncio
import discord
import requests
import os
from datetime import datetime, timedelta
from discord.ext import commands

async def apod(bot):
    await bot.wait_until_ready()
    channel = discord.Object(id="485891401691955211")
    while not bot.is_closed:
        seconds = getSeconds(8, 00)
        print("sleeping for " + str(seconds) + " seconds")
        await asyncio.sleep(seconds)

        r = requests.get("https://api.nasa.gov/planetary/apod?api_key=JxHACldWATN21OaEW2MGZfpuzIRYMJIeLqZd1SWV").json()
        title = "**" + r["title"] + "**\n"
        text = r["explanation"]
        url = ["url"]
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
    if time.hour > hour - 1:
        time += timedelta(days=1)
    time = time.replace(hour=hour,minute=minute,second=0,microsecond=0)
    delta = time - datetime.today()
    seconds = int(delta.total_seconds())
    return seconds
