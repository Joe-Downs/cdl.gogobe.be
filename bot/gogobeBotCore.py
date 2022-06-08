import discord
import sys
import pathlib
# Get the CDL git repo and add it to Python's working
# module path. This will only apply to Python while the
# program is running.
# This is the directory the file is in
fileDir = pathlib.Path(__file__).parent.absolute()
# This is the directory above
parentDir = fileDir.parent
sys.path.append(str(parentDir))
import botCommands
import events
import reminders
import sqlite3
import config
import re
from discord.ext import commands


bot_token = config.getDiscordToken()
owner_ID = 174362561385332736
prefix = config.getCommandPrefix()

bot = commands.Bot(command_prefix = prefix)

conn = sqlite3.connect("database/cdl.db")
# The Row instance allows for the row returned by sqlite3 to be mapped by column
# name and index in a dictionary-like format. Additionally, "it
# supports...iteration, representation, equality testing and len()"
# (from https://docs.python.org/3/library/sqlite3.html#sqlite3.Row)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def hi(ctx):
    await ctx.send("hello")

@bot.command()
async def hug(ctx, arg):
    huggedID = int(re.findall("[0-9]+", arg)[0])
    loonaHugGfy = "https://gfycat.com/FreeDarkHairstreakbutterfly"
    await ctx.send(f"<@{huggedID}> {loonaHugGfy}")

# 'sudo' commands can only be run by the bot owner
@bot.command()
async def sudo(ctx, arg):
    # Checks if the message was sent by the bot owner
    # If not, tell the user and exit
    if (ctx.message.author.id != owner_ID):
        await ctx.send(ctx.message.author.name +
                       " is not in the sudoers file." +
                       " This incident will be reported.")
        return

    if (arg == "exit" or arg == "stop"):
        conn.commit()
        conn.close()
        await ctx.send("Sleep mode activated...")
        print("Stopping Bot...")
        sys.exit()
    if (arg == "commit"):
        conn.commit()
        await ctx.send("Committing changes...")

bot.run(bot_token)
