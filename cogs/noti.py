import discord
from discord import message
from discord.ext import commands
import json
import os.path

intents = discord.Intents.default()
intents.members = True
botname = 'BOL4봇'

class noti(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        pass

    @commands.command()
    async def set_noti_channel(self, ctx, channel):
        print(f'servers/{channel}')
        if os.path.isfile(f'servers/{channel}'):
            pass

def setup(bot: commands.Bot):
    bot.add_cog(noti(bot))