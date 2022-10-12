from turtle import end_fill
import discord
import os
import json
import random
import ast
import inspect
import re
import discord, datetime, time

from discord.utils import get
from discord.ui import Select
from discord.ui import Button, View
from discord.ext import commands
from discord.ext.commands import Bot

token = "MTAxMDg0NjA5NTQzNTM4Mjg2NQ.GzzEd-.4qzuuO1c3YwcMImvGmhR6iWIkUA8yjg6MFUJA8"
prefix = ';'

bot = commands.AutoShardedBot(command_prefix=";", intents=discord.Intents.all(), help_command=None, owner_ids=[371224177186963460, 990633882644791318])

# ------------------------------------------------------
# bot on / status
@bot.event
async def on_ready():  
    # await bot.load_extension("jishaku")  
    await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} servers"))
    print("smekeria e on")
    
# -------------------------------------------------------


# help
@bot.command()
async def help(ctx):
    embed = discord.Embed(description=f"**info commands**\n`mc`, `invite`, `ping`", color=0x2f3136)
    embed.set_thumbnail(url="https://i.imgur.com/dZxrSZg.png")
    embed.set_author(name=bot.user.name, icon_url="https://i.imgur.com/dZxrSZg.png")
    embed.set_footer(text="© ricobot 2022 - 2023")
    
    await ctx.reply(embed=embed, mention_author=False)

# mc
@bot.command()
async def mc(ctx):
    embed = discord.Embed(description=f"**{ctx.guild.member_count}** members", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)

# invite 
@bot.command()
async def invite(ctx):
    embed = discord.Embed(description="Rico is a multifunctional bot with commands to enhance your discord server by adding emojis", color=0x2f3136)
    button = Button(label="invite", style=discord.ButtonStyle.grey, url="https://discord.com/api/oauth2/authorize?client_id=1010846095435382865&permissions=8&scope=applications.commands%20bot")
    button = Button(label="support", style=discord.ButtonStyle.grey, url="https://ricobot.cf")

    view = View()
    view.add_item(button)
    #view.add_item(button2)
    await ctx.reply(embed=embed, view=view, mention_author=False)

# ping
@bot.command()
async def ping(ctx):
     await ctx.reply(f'....pong 🏓 `{round(bot.latency * 1000)}ms`')
# mt
@bot.command()
async def uptime(self, ctx):
    uptime = str(
        datetime.timedelta(seconds=int(round(time.time() - start))))
    e = discord.Embed(color=0x2f3136,description=f"**{self.bot.user.name}'s** uptime: **{uptime}**")
    await ctx.reply(embed=e, mention_author=False)

bot.run(token)