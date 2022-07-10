# bot.py
import os
import random
from dotenv import load_dotenv
import discord
from discord_slash import SlashCommand
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='where')
async def nine_nine(ctx,name=None):

    if name==None:
        await ctx.send("Please enter a name or tag a user")
    else:

        #font = ImageFont.load_default()
        font =ImageFont.truetype("arial.ttf", 27)
        img = Image.open('where.png')

        draw = ImageDraw.Draw(img)
        draw.text((520, 300),"Where monkey",(0,0,0),font=font)

        img.save('temp.png')

bot.run(TOKEN)
