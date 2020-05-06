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
        print('')
        print("-User has submitted " + str(arg))
    else:
        await channel.send("Invalid URL, must be soundcloud")  
    

@bot.command()
@commands.has_permissions(ban_members=True)
async def lottery(ctx):
    channel = bot.get_channel(707311172587749417)
    selection = randint(1, len(tracks) - 1)
    await channel.send('@everyone THE WINNER IS ' + tracks[selection])
    print('')
    print('-Winner for lottery selected')
    del tracks[:]


@bot.command()
@commands.has_permissions(ban_members=True)
async def clearlist(ctx):
    print('')
    print('-Admin has cleared the list')
    del tracks[:]

@bot.command()
async def linklist(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send('```' + '\n'.join(map(str, tracks)) + '```') 
    print('')
    print('-User has used linklist')

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def removelink(ctx, arg):
    channel = bot.get_channel(707329253422661682)
    tracks.pop(int(arg))
    await channel.send("Link " + str(arg) + " removed.")
    print('')
    print('-Admin has removed link ' + str(arg))

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def resetcooldown(ctx):
    submit.reset_cooldown(ctx)
    print('')
    print('-Admin has reset his cooldown')

@bot.command()
async def insxne(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send("https://soundcloud.com/insxnebeats")
    print('')
    print('-User has used command insxne')

@bot.command()
async def ping(ctx):
    await ctx.send('> Pong! {0}'.format(round(bot.latency, 1)))
    print('')
    print('-User has pinged the bot')

@bot.command(pass_context=True)
async def help(ctx):
    channel = bot.get_channel(707329253422661682)
    await channel.send("""
    > submit      |    for submitting a track or soundcloud prfile
    > linklist       |   for viewing all links in the lottery
    > ping           |   get the bots latency
    > insxne       |   developers soundcloud <3
    """)
    print('')
    print('-User has used help')


@bot.event 
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="Prefix: z"))

bot.run('')
