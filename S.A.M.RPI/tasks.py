import admin
import asyncio
import discord
import requests
import os
from datetime import datetime, timedelta
from discord.ext import commands

async def apod(client):
	await client.wait_until_ready()
	channel = discord.Object(id='485891401691955211')
	while not client.is_closed:
		seconds = getSeconds(16, 11)
		print("sleeping for " + str(seconds) + " seconds")
		await asyncio.sleep(seconds)
		channel = discord.Object(id='485891401691955211')
		r = requests.get("https://api.nasa.gov/planetary/apod?api_key=JxHACldWATN21OaEW2MGZfpuzIRYMJIeLqZd1SWV&date=2018-09-07").json()
		title = "**" + r["title"] + "**\n"
		text = r["explanation"]
		url = r["url"]
		if url.split(".")[-1] == "jpg":
			with open('apod/image.jpg', 'wb') as f:
				f.write(requests.get(url).content)
			await client.send_file(channel, "apod/image.jpg")
			os.remove("apod/image.jpg")
		elif url.split(".")[-1] == "gif":
			with open('apod/image.gif', 'wb') as f:
				f.write(requests.get(url).content)
			await client.send_file(channel, "apod/image.gif")
			os.remove("apod/image.gif")
		else:
			await client.send_message(channel, r["url"])
		await client.send_message(channel, (title + text))
		input()

def getSeconds(hour, minute):
	time = datetime.now() #+ timedelta(days=1)
	time = time.replace(hour=hour,minute=minute,second=0,microsecond=0)
	delta = time - datetime.today()
	seconds = int(delta.total_seconds())
	return seconds
