#this is task 1, a scheduler

#these are libraries and some configs , don't wanna explain again, check 'main.py' fyi
import discord
import json
from discord.ext import commands
import os
with open('./cmds/Scheduler_config.json', mode='r', encoding='utf8') as r:
    rs = json.load(r)
with open('./cmds/Scheduler_config.json', mode='w', encoding='utf8') as w:
    ws = json.load(w)

#a library to randomize something
import random

#just copied from Web to configure a class
from core.classes import Cog_Extension

#a class
class Task1(Cog_Extension):
    #a boring command to randomize a number from 0-100 and output it
    @commands.command()
    async def roll(self, ctx):
        x = random.randint(0,100)
        await ctx.send(x)

    #to generate a schedule
    @commands.command()
    async def schedule(self, ctx, com, char):
        if com == 'create':
            ws['Schedule'][0] = rs['STime'][0][random.randint(0,6)]
            json.dump(ws, w)
            w.close()
            if char == 'a':
                await ctx.send(r['Schedule'][0])

  

#just copied from Web to configure a class
def setup(bot):
    bot.add_cog(Task1(bot))