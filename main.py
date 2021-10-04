#just make the bot run 24/7
from webserver import keep_alive

#for calling out some private data like "TOKEN"
import os

#just some libraries for python discord bot
import discord
from discord.ext import commands

#json file library
import json

#just copied from Web and idk how it works
with open('./cmds/Scheduler_config.json', mode='r+', encoding='utf8') as j:
    s = json.load(j)


#some bot's properties
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
bot = commands.Bot(command_prefix="[", intents=intents, owner_id=633082846138990614)

#let the bot send a message on a specific channel when it has just gone online
@bot.event
async def on_ready():
    channel = bot.get_channel(795641935540912179)
    await channel.send("Sorry! I went offline. But now, I'm back!")

#three commands to let the bot to load, unload, and reload the classes in folder 'cmds'
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension}.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension}.')

#to run different classes in the folder 'cmds'
for Filename in os.listdir('./cmds'):
  if Filename.endswith('.py'):
    bot.load_extension(f'cmds.{Filename[:-3]}')

#to activate the bot
if __name__ == "__main__":
  keep_alive()
  TOKEN = os.environ["TOKEN"]
  bot.run(TOKEN)