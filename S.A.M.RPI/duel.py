import requests
import sam_util
import asyncio
import discord
from random import randrange
from bs4 import BeautifulSoup
from discord.ext import commands
from discord import Game

class duel():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def duel(self):
        r = requests.get("http://www.spela.se/spel/tva-spelare")
        soup = BeautifulSoup(r.text)
        games = soup.find_all("a",attrs={'class':'tile-title'})
        game = games[randrange(len(games))]
        title = game["title"]
        link = game["href"]
        await self.bot.say("The game is {}\nhttp://www.spela.se{}".format(title, link))

def setup(bot):
    bot.add_cog(duel(bot))
