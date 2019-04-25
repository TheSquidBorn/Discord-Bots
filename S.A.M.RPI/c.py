import requests
import asyncio
import discord
from discord.ext import commands
from discord import Game

class c():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def c(self, v, base = "eur", *args):
        url = "https://api.exchangeratesapi.io/latest?"
        url += "base=" + base.upper()
        if not args:
            args  = ["sek", "eur", "gbp"]
        s = True
        for n in range(0, len(args)):
            if base.upper() == args[n].upper():
                continue
            if s:
                url += "&symbols="
                s = False
            else:
                url += ","
            url += args[n].upper()
        r = requests.get(url).json()
        print("\n")
        print(r)
        print("\n")
        print(url)
        print("\n")
        msg = str(round(float(v), 2)) + " in " + base + "\n"
        for currency, rate in r["rates"].items():
            msg += currency + ":\t" + str(round( float(rate) * float(v), 2)) + "\n"

        await self.bot.say(msg)

def setup(bot):
    bot.add_cog(c(bot))
