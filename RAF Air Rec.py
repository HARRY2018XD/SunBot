import discord
from discord.ext import commands
import time
import random

bot = commands.Bot(command_prefix = "r!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is online and working.")
    await bot.change_presence(game=discord.Game(name='drill'))

@bot.command(pass_context=True)
async def spitfire(ctx): 
    spitfire = ['https://vsrldassets.redletterdays.co.uk/images/img435/productlarge/SRMSP_1.jpg', 'https://www.virginexperiencedays.co.uk/content/img/product/large/PSPF20.jpg', 'https://acesflyinghigh.files.wordpress.com/2012/02/fhc-spitfire-2011-3.jpg?w=960&h=400&crop=1']
    embed = discord.Embed(
        colour=0x1f32af
    )
    embed.set_author(name='Here are some facts on Spitfires: \nEngine - Rolls Royce Merlin, V12. \nAmount Built - 20,351 \nFirst Flight - March 5th, 1936 \nProduction - 1938 - 1948')
    embed.set_image(url=random.choice(spitfire))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def f16(ctx): 
    f16 = ['https://i.kinja-img.com/gawker-media/image/upload/s--UUTmniNC--/c_fill,f_auto,fl_progressive,g_center,h_675,q_80,w_1200/bsizh55wtlyv4v6ck7ul.jpg', 'https://i.kinja-img.com/gawker-media/image/upload/s--BGeJFlNx--/c_fit,f_auto,fl_progressive,q_80,w_320/qlmdipmtazqs98n69odr.jpg', 'https://nationalinterest.org/sites/default/files/main_images/22940430165_61ddb21e18_o.jpg']
    embed = discord.Embed(
        colour=0x1f32af
    )
    embed.set_author(name='Here are some facts on F16 Super Vipers: \nEngine - GE F110 - 132A Engine \nAmount Built - 4,500+ \nFirst Flight - January 20th, 1974 \nProduction - 1978 - Present')
    embed.set_image(url=random.choice(f16))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def typhoon(ctx): 
    typhoon = ['https://www.southforward.com/wp-content/uploads/2018/05/Eurofighter-Typhoon.jpg', 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iQpC88q6i2ME/v0/-1x-1.jpg', 'https://i.ytimg.com/vi/N38IMzZkRdY/maxresdefault.jpg', 'http://aviationweek.com/site-files/aviationweek.com/files/imagecache/large_img/uploads/2017/06/leonardoeurofighters.jpg']
    embed = discord.Embed(
        colour=0x1f32af
    )
    embed.set_author(name='Here are some facts on Typhoon: \nEngine - Rolls Royce XG-40 \nAmount Built - 623 \nFirst Flight - March 27, 1994 \nProduction - 1994 - Present')
    embed.set_image(url=random.choice(typhoon))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def chinook(ctx): 
    chinook = ['https://www.defencetalk.com/wp-content/uploads/2011/01/RAF-chinook-helicopter.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Chinook_hc2_za682_arp.jpg/1200px-Chinook_hc2_za682_arp.jpg', 'https://www.raf.mod.uk/raf-beta/assets/File/Chinook.png']
    embed = discord.Embed(
        colour=0x1f32af
    )
    embed.set_author(name='Here are some facts on Chinook: \nEngine - Lycoming T55 \nAmount Built - 1,200+ \nFirst Flight - September 21, 1961 \nProduction - 1962 - Present')
    embed.set_image(url=random.choice(chinook))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.kick_members:
        await bot.kick(userName)
        embed = discord.Embed(title="User kicked:", description=f"User {userName} has successfully been kicked.", color=0x1f32af)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ban(ctx, userName: discord.Member, *, reason: str):
    if ctx.message.author.server_permissions.ban_members:
        await bot.ban(userName)
        embed = discord.Embed(title="User banned:", description=f"User {userName} has successfully been banned.", color=0x1f32af)
        await bot.say(embed=embed)





bot.run("NDg0MzgyMjEzMDA2Mjk1MDcw.DmhLsw.MAxXhFR6qzIY5iGI5L2zHKlMyRc")
