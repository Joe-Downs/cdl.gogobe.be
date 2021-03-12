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
import database.sqlpyte3.connectDB as connectDB
import database.sqlpyte3.readDB as readDB
import database.sqlpyte3.writeDB as writeDB
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

conn = connectDB.createConnection("database/cdl.db")
cursor = connectDB.createCursor(conn)

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

@bot.command()
async def event(ctx, *args):
    if args[0] == "add":
        message = botCommands.eventAdd(cursor, args)
    elif args[0] == "list":
        message = botCommands.eventsList(cursor, args)
    elif args[0] == "signup":
        try:
            message = botCommands.eventSignup(cursor, args)
        except ValueError as error:
            message = error
    await ctx.send(message)

@bot.command()
async def reminder(ctx, *args):
    if args[0] == "add":
        message = botCommands.reminderCreate(cursor, ctx, args)
    await ctx.send(message)
        

@bot.command()
async def signup(ctx, arg = None):
    authorName = str(ctx.message.author.name)
    if (arg == None):
        authorID = int(ctx.message.author.id)
    else:
        authorID = int(re.findall("[0-9]+", arg))
    authorStatus = str(ctx.message.author.status)
    writeDB.insertRow(cursor, "users",
                      discordID = authorID,
                      username = authorName,
                      status = authorStatus)
    await ctx.send("Signed " + authorName + " up for the CDL!")

@bot.command()
async def status(ctx, arg = None):
    name = str(ctx.message.author.name)
    if (arg == None):
        discordID = int(ctx.message.author.id)
    else:
        discordID = int((re.findall("[0-9]+", arg))[0])
        user = bot.get_user(discordID)
        name = user.name
    try:
        status = readDB.getValue(cursor, "users",
                                 desiredColumn = "status",
                                 searchColumn = "discordID",
                                 searchValue = discordID,
                                 getMultiple = True)
        message = f"{name} was {status} at signup"
    except sqlite3.ProgrammingError as error:
        message = f"{name} has not signed up yet"
    await ctx.send(message)

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
        connectDB.commitChanges(conn)
        connectDB.closeConnection(conn)
        await ctx.send("Sleep mode activated...")
        print("Stopping Bot...")
        sys.exit()
    if (arg == "commit"):
        connectDB.commitChanges(conn)
        await ctx.send("Committing changes...")

bot.run(bot_token)
