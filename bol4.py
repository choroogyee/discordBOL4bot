import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import date
import time
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request
import random
import os

async def is_whitelisted(ctx):
    return ctx.author.id in [487962402097332224]

botname = 'BOL4봇'
token = ''
uptime = time.time()

bot = commands.Bot(command_prefix='볼사봇 ', help_command=None, intents=discord.Intents.default())

@bot.event
async def on_ready():
    bol4 = (date.today() - date(2016, 4, 22)).days

    print(bot.user.name)
    print(bot.user.id)

    server = len(bot.guilds)
    users = 0
    for now_guild in bot.guilds:
        users += len(now_guild.members)
    
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('`볼사봇 도움말` 입력!'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('`볼사봇 도움` 으로도 확인가능!'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(str(server)+'개의 서버 | '+str(users)+'명의 유저'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('지금은 볼사가 데뷔한지 '+str(bol4)+'일째!'))
        await asyncio.sleep(10)


@commands.check(is_whitelisted)
@bot.command(name='재시작')
async def reload(ctx):
    [bot.reload_extension(f"cogs.{x.replace('.py', '')}") for x in os.listdir("cogs") if x.endswith('.py') and not x.startswith("_")]
    await ctx.send('✅')

[bot.load_extension(f"cogs.{x.replace('.py', '')}") for x in os.listdir("./cogs") if x.endswith('.py')]

bot.run(token)