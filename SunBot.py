import discord
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot successfully booted & online.")
    print("My name is " + client.user.name)
    print("My ID is " + client.user.id)
    await client.change_presence(game=discord.Game(type=2,name='SunnyBot (!)'))

@client.command(pass_context=True)
@commands.has_role("Sun")
async def say(ctx, *, args):
    await client.say(args)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def Robux(ctx):
    await client.say("Info page on Robux: We are constantly trying to stock up on robux and sell it to anyone and everyone. We don't go first when selling, however if you're interested. DM ``@SunDance#7568``.")

@client.command(pass_context=True)
async def robux(ctx):
    await client.say("Info page on Robux: We are constantly trying to stock up on robux and sell it to anyone and everyone. We don't go first when selling, however if you're interested. DM ``@SunDance#7568``.")

@client.event
async def on_member_join(member):
    if member.server.id == "475438053750603807":
        channel = client.get_channel("475667894223503361")
        await client.send_message(channel, f"Welcome {member.mention} to Sunny's Services Server (SSS). Head to info to find out more about this server!")
        role = discord.utils.get(member.server.roles, name='Customers')
        await client.add_roles(member, role)

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=100):
    await client.purge_from(ctx.message.channel, limit=int(amount) + 1)
    await client.say ('Messages successfully removed.')

@client.event
async def on_command_error(error: Exception, ctx: commands.Context):
    if isinstance(error, commands.CommandNotFound):
        return
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

client.run("NDc1NjYxOTc0ODk0ODA0OTky.DkiSRw.4eKjL1U9oSTGye9QCZAMmVUHy3U")

