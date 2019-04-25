import sam_util
import asyncio
import discord
import json
from discord.ext import commands
from discord import Game

class monster():
    def __init__(self, bot):
        self.bot = bot
        '''How many monsters yall owe me'''

    @commands.command(pass_context=True)
    async def giveMonster(self, ctx, idRecive, amount):
        print("monstertime")
        with open('monster.json') as f:
            f = json.load(f)
        id = ctx.message.author.id
        if id not in f:
            f[id] = {}
            await self.bot.say("Added {}".format(id))
        if idRecive not in f:
            f[idRecive] = {}
            await self.bot.say("Added {}".format(idRecive))
        f[id][idRecive] += amount
        m = "{} added {} monsters to {}".format(id, amount, idRecive)
        print(m)
        m += "{} you now owe {} monsters to {}".format(id, amount, idRecive)
        await self.bot.say(m)
        with open("monster.json", "w") as outfile:
            json.dump(f, outfile, sort_keys=True, indent=4)

    @commands.command(pass_context=True)
    async def acommand(self, ctx):
       for s in self.bot.server:
           print(s.name)

def setup(bot):
    bot.add_cog(monster(bot))
