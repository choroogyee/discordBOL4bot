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

    @commands.command(name='공지채널')
    async def set_noti_channel(self, ctx):
        path = f'servers/{ctx.message.channel.id}.json'
        path.replace('<', '')
        path.replace('>', '')
        path.replace('#', '')


        if not os.path.isfile(path):
            with open(path, 'w') as new_file:
                new_file.write('{}')

        with open(path, 'r') as json_file:
            data = json.load(json_file)

        data['noti_channel'] = ctx.message.channel.id

        with open(path, 'w') as json_file:
            json.dump(data, json_file)

        await ctx.send(f'<#{ctx.message.channel.id}> 채널이 공지 채널로 저장되었습니다.')

def setup(bot: commands.Bot):
    bot.add_cog(noti(bot))