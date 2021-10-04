#this is task 1, a scheduler

#these are libraries and some configs , don't wanna explain again, check 'main.py' fyi
import discord
import json
from discord.ext import commands
import os
with open('./cmds/Scheduler_config.json', mode='r+', encoding='utf8') as r:
    rs = json.load(r)

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
        if char == 'a':
          with open('./cmds/Scheduler_config.json', mode='r+', encoding='utf8') as r:
            rs = json.load(r)
            u = 0
            w = rs["STime"][1]
            while u<len(rs['Config']):
              v = 0
              z = [-1,-1,-1]
              while v<rs['Config'][u]:
                x = random.randint(0,len(rs['STime'][0])-1)
                if w[x]>0 and x!=z[0] and x!=z[1] and  x!=z[2]:
                  rs['Schedule'][u].append(rs["STime"][0][x])
                  w[x]=w[x]-1
                  z[v]=x
                  v=v+1
                  x = random.randint(0,len(rs['STime'][0])-1)
              await ctx.send(rs['Schedule'][u])
              u=u+1
              

  

#just copied from Web to configure a class
def setup(bot):
    bot.add_cog(Task1(bot))