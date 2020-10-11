import discord
import sys
import database.connectDB as connectDB
import database.readDB as readDB
import database.writeDB as writeDB
import events
import reminders
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
async def hug(ctx):
    berryhug = await ctx.guild.fetch_emoji(737506993937318002)
    await ctx.send(berryhug)

@bot.command()
async def event(ctx, *args):
    if args[0] == "add":
        title = args[1]
        number = args[2]
        date = args[3]
        events.createEvent(cursor, title, number, 1, date)
        message = f"Added event \"{title} {number}\" scheduled for {date}."
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
    status = readDB.getValue(cursor, "users",
                                   desiredColumn = "status",
                                   searchColumn = "discordID",
                                   searchValue = discordID)
    if (status != None):
        messageString = name + " was " + status + " at signup"
    else:
        messageString = name + " has not signed up yet"
    await ctx.send(messageString)

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

bot.run(bot_token)
