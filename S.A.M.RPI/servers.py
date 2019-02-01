import admin
import asyncio
import discord
import requests
import os
from datetime import datetime, timedelta
from discord.ext import commands
from discord import Game


async def status(client, ip):
        await client.wait_until_ready()
        while not client.is_closed:
                seconds = 120
                await asyncio.sleep(seconds)
                r = requests.get("https://api.mcsrvstat.us/1/" + ip).json()
                if("offline" in r):
                        await client.change_presence(game=Game(name="Server is offline"))
                else:
                        if(r["players"]["online"] == 1):
                                await client.change_presence(game=Game(name="Server is up with " + str(r["players"]["online"]) + " player"))
                        else:
                                await client.change_presence(game=Game(name="Server is up with " + str(r["players"]["online"]) + " players"))
