# Code for submitting soundcloud links.
# Written by insxne with help from toxic <33

import discord 
import time
from random import randint
from discord.ext import commands

bot = commands.Bot(command_prefix='z') 
bot.remove_command("help")

tracks = ['']

@bot.command(pass_context=True) 
@commands.cooldown(1, 3600, commands.BucketType.user)
async def submit(ctx, arg):
    channel = bot.get_channel(707329253422661682)
    track = arg
    track_id = len(tracks)
    if "https://soundcloud.com" in track:

        tracks.append(str(track_id) + "|" + arg)
        await ctx.send('Submitted your link!')
    else:
        await channel.send("Invalid URL, must be soundcloud")

@bot.command()
@commands.has_permissions(ban_members=True)
async def lottery(ctx):
    channel = bot.get_channel(707311172587749417)
    selection = randint(1, len(tracks) - 1)
    await channel.send('@everyone THE WINNER IS ' + tracks[selection])
    del tracks[:]

@bot.command()
@commands.has_permissions(ban_members=True)
async def clearlist(ctx):
    del tracks[:]

@bot.command()
async def linklist(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send('```' + '\n'.join(map(str, tracks)) + '```') 

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def removelink(ctx, arg):
    channel = bot.get_channel(707329253422661682)
    tracks.pop(int(arg))
    await channel.send("Link " + str(arg) + " removed.")

@bot.command()
async def insxne(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send("https://soundcloud.com/insxnebeats")

@bot.command()
async def ping(ctx):
    await ctx.send('> Pong! {0}'.format(round(bot.latency, 1)))

@bot.command(pass_context=True)
async def help(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send("""
    > submit      |    for submitting a track or soundcloud prfile
    > linklist       |   for viewing all links in the lottery
    > ping           |   get the bots latency
    > insxne       |   developers soundcloud <3
    """)


@bot.event 
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="Prefix: >>"))

bot.run('NzA3Mjk2NDg0NzY0Mjg3MDQ4.XrGwNQ.gTXZvdlyVmQaMmoA_X78myEh1jE')
