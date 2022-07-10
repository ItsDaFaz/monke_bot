#!/usr/bin/python
# bot.py
import os
from quote_test import randomQuote
import random
from discord import message
from dotenv import load_dotenv
import discord
from discord_slash import SlashCommand,SlashContext
from discord.ext import commands
from discord import guild
from discord_slash.utils.manage_commands import create_choice, create_option
from random import randint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
import giphy_client as gc
from giphy_client.rest import ApiException
import requests





load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
api_instance = gc.DefaultApi()
api_key = os.getenv('GIPHY_KEY')
query = 'monkey'
fmt = 'gif'




bot = commands.Bot(command_prefix='!')
slash= SlashCommand(bot,sync_commands=True)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@slash.slash(
    name='where',
    description='Enter a name or tag a user!',
    guild_ids=[int(os.getenv('DISCORD_GUILD'))],
    options=[
        create_option(
        name="user",
        description="Select a user",
        required=True,
        option_type=6,
        )

    ]
)
async def where(ctx:SlashContext,user:str):

    print(user)
    print(user.id)

    username = user.name
    print(user.name)
    #font = ImageFont.load_default()
    font =ImageFont.truetype("arial.ttf", 27)
    img = Image.open('where.png')
    send=True


    draw = ImageDraw.Draw(img)
    draw.text((520, 300),"where "+username,(255,255,255),font=font,stroke_width=2, stroke_fill="#000")
    mention_id='<@!'+str(user.id)+'>'
    print(mention_id)
    #await ctx.send(mention_id)


    if(send==True):
        with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(mention_id,file=discord.File(fp=image_binary, filename='temp.png'))
    else:

        img.save('temp.png')
        await ctx.send("IMAGE SHARING DISABLED FOR DEBUGGING")
        #await channel.send(file=discord.File('temp.png'))




@slash.slash(
    name='where_any',
    description='Write anything!',
    guild_ids=[int(os.getenv('DISCORD_GUILD'))],
    options=[
        create_option(
        name="string",
        description="Write anything",
        required=True,
        option_type=3,
        )

    ]
)

async def where_any(ctx:SlashContext,string:str):



    #string=str(string)

    #font = ImageFont.load_default()
    font =ImageFont.truetype("arial.ttf", 27)
    img = Image.open('where.png')
    send=True


    draw = ImageDraw.Draw(img)
    draw.text((520, 300),"where "+string,(255,255,255),font=font,stroke_width=2, stroke_fill="#000")



    if(send==True):
        with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(file=discord.File(fp=image_binary, filename='temp.png'))
    else:

        img.save('temp.png')
        await ctx.send("IMAGE SHARING DISABLED FOR DEBUGGING")
        #await channel.send(file=discord.File('temp.png'))

@slash.slash(
    name='where_role',
    description='Tag a role!',
    guild_ids=[int(os.getenv('DISCORD_GUILD'))],
    options=[
        create_option(
        name="role",
        description="Select a role",
        required=True,
        option_type=8,
        )

    ]
)
async def where_role(ctx:SlashContext,role:str):


    print(str(role.id))
    username = role.name
    print(role.name)
    #font = ImageFont.load_default()
    font =ImageFont.truetype("arial.ttf", 27)
    img = Image.open('where.png')
    send=True


    draw = ImageDraw.Draw(img)
    draw.text((520, 300),"where "+role.name,(255,255,255),font=font,stroke_width=2, stroke_fill="#000")
    mention_id='<@&'+str(role.id)+'>'
    print(mention_id)
    #await ctx.send(mention_id)


    if(send==True):
        with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(mention_id,file=discord.File(fp=image_binary, filename='temp.png'))
    else:

        img.save('temp.png')
        await ctx.send("IMAGE SHARING DISABLED FOR DEBUGGING")
        #await channel.send(file=discord.File('temp.png'))



def randomQuoteGenerator():
    quote_url="https://api.quotable.io/random"
    querystring = {"tags":"inspirational"}
    

   #quote_response=requests.request("GET", quote_url, headers=headers, params=querystring)
    quote_response=requests.request("GET", quote_url, params=querystring)
    quote_dict=quote_response.json()
    print(quote_dict['content'],quote_dict['author'])
    return quote_dict['content'],quote_dict['author']



@slash.slash(
    name='inspire',
    description='Get inspired by monkey',
    guild_ids=[int(os.getenv('DISCORD_GUILD'))]
    

)
async def inspire(ctx:SlashContext):
    
    try:
        randQuote=randomQuoteGenerator()

        embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Inspired by monke",
        description=randQuote[0]+" - "+randQuote[1]
        
        )

        response = api_instance.gifs_search_get(api_key,query,limit=1,rating='g',offset=randint(1,10),fmt=fmt)
        gif_id = response.data[0]
        gif_url=gif_id.images.downsized.url
        embed.set_image(url=gif_url)
        #print(gif_id)
        await ctx.send(embed=embed)
    except ApiException:
       #print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
        await ctx.send("API ERROR")


    

    



bot.run(TOKEN)
