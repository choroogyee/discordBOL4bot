import discord
from discord import message
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
botname = 'BOL4봇'

class noti(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        pass

def setup(bot: commands.Bot):
    bot.add_cog(noti(bot))