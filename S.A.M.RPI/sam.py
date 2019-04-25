import sam_util
import asyncio
import discord
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from threading import Timer
from discord.ext import commands
from discord import Game

class sam():
    def __init__(self, bot):
        self.bot = bot
        '''Commands to change S.A.M.s staus'''

    @commands.command(pass_context=True)
    async def playing(self, ctx):
        game = ctx.message.content
        game = game.split(" ", 1)[1]
        sam_util.changeCfg("playing", game)
        await self.bot.change_presence(game=Game(name=game))

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        """Stops the bot"""
        server = ctx.message.server
        print("User stopped bot")
        print(ctx.message.author)
        if sam_util.HasAdmin(ctx.message.author, server):
            await self.bot.say("F")
            await self.bot.logout()
        else:
            await self.bot.say("Who dis")

    @commands.command()
    async def space(self):
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        string = "There are currently " + str(data["number"]) + " humans in space"
        await self.bot.say(string)

    @commands.command()
    async def astro(self):
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        string = "```\nPeople in space:\n"
        for p in data["people"]:
            string += p["name"]
            string += " " * (30 - len(p["name"]))
            string += p["craft"] + "\n"
        string += "```"
        await self.bot.say(string)

    @commands.command()
    async def number(self, *, number):
        number = number.replace(" ","")
        response = requests.get("https://www.180.se/nummer/" + number)
        soup=BeautifulSoup(response.text)
        pct = soup.find('span',{'class':'ai-value ai-small'}).text
        await self.bot.say(pct + "\nhttps://www.180.se/nummer/" + number)

def setup(bot):
    bot.add_cog(sam(bot))
