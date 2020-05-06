# Code for submitting soundcloud links.
# Written by insxne

import discord 
import time
from random import randint
from discord.ext import commands

bot = commands.Bot(command_prefix='>>') 

tracks = ['']


####################################################################################
@bot.command(pass_context=True) 
@commands.cooldown(1, 3600, commands.BucketType.user)
async def submit(ctx, arg):
    channel = bot.get_channel(707329253422661682)
    track = arg
    if "https://soundcloud.com" in track:

        tracks.append(arg)
        await ctx.send('Submitted your track!')
    else:
        await channel.send("Invalid URL, must be soundcloud")
######################################################################################


#######################################################################################
@bot.command()
@commands.has_permissions(ban_members=True)
async def lottery(ctx):
    channel = bot.get_channel(707311172587749417)
    selection = randint(1, len(tracks) - 1)
    await channel.send('@everyone THE WINNER IS ' + tracks[selection])
    del tracks[:]
#######################################################################################


######################################################################################
@bot.command()
@commands.has_permissions(ban_members=True)
async def clearlist(ctx):
    del tracks[:]
#######################################################################################


########################################################################################
@bot.command()
async def tracklist(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send('```' + '\n'.join(map(str, tracks)) + '```') 
########################################################################################  

@bot.command()
async def insxne(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send("https://soundcloud.com/insxnebeats")

@bot.event 
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)

bot.run('')
