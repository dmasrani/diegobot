'''
NOTE: This is just an example of Discord.py rewrite bot. As the discord.py library is not supported in Code Playground, the code will not work. SO I SAID ONCE AGAIN, THIS IS JUST AN EXAMPLE!

This bot has 2 commands in, say and ping. You can type !ping and the bot will reply with Pong! You can use say command (!say <something>) to say something. Replace 'something' with any message you'd like. If you type for example !say Hello, the following will result in an output: "@Full Gamer said: Hello!"

The ctx.message.author.mention result in mention of author of the message. If you just type !say command, the bot will handle this error and will ask you to say something.

Join this server if you'd like to learn bot development: https://discord.gg/GWdhBSp
'''

import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='!', description='bruh.')
#Defines a bot's prefix and description. There is one predefined command in the bot, the help command. This command shows you the full list of commands you have created.

@bot.event
async def on_ready():
    print("I\'m here!")

#The @bot.event defines a bot event. The on_ready event occurs when the bot is ready / is logged in to the Client. In this example, the "I'm here!" message will be printed to the console.

@bot.command()
async def say(ctx, *, something):
    """Say something!"""
    if something is None:
        await ctx.send("What do you want to say?")
        return

    await ctx.send(f"{ctx.message.author.mention} said: **{something}**")

@bot.command()
async def ping(ctx):
    """Pong!"""
    await ctx.send("Pong!")

bot.run("NDgzMTU5NDU2MzI3NDAxNDgy.D3vzZg.jHfWovXQFv6ouH_HasnjQU1gMjM")
#Replace bot_token with your actual bot token. Do not post it publically, your bot token will be stealed.
