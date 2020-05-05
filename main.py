# Code for submitting soundcloud links.
# Written by insxne

import discord 
import time
from random import randint
from discord.ext import commands

bot = commands.Bot(command_prefix='>>') 

tracks = ['']

@bot.command(pass_context=True) 
async def submit(ctx, arg):
    channel = bot.get_channel(707329253422661682)
    track = arg
    if "https://soundcloud.com" in track:

        tracks.append(arg)
        await ctx.send('Submitted your track!')

    else:
        await channel.send("Invalid URL, must be soundcloud")



@bot.command()
async def lottery(ctx):
    channel = bot.get_channel(707311172587749417)
    selection = randint(1, len(tracks) - 1)
    await channel.send('@everyone THE WINNER IS ' + tracks[selection])
    del tracks[:]

@bot.event 
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)

bot.run('')
