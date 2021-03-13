# Functions used by the bot for its commands

import discord
import events
import reminders

# Computes the season (if needed) and adds the event to the database
# Returns a message to be sent by the bot
def eventAdd(cursor, args):
    title = args[1].upper()
    eventNumber = int(args[2])
    print(eventNumber)
    date = args[3]
    if title == "CDL":
        season = events.getSeason(eventNumber)
    else:
        # Only CDL events are split into seasons, and there is no season 0
        season = 0
    events.createEvent(cursor, title, eventNumber, season, date)
    return f"Added event \"{title} {eventNumber}\" scheduled for {date}"

def eventsList(cursor, args):
    # Event titles are always all uppercase
    eventTitle = args[1].upper()
    # The default is 5 if no number is given
    try:
        numOfEvents = int(args[2])
    except:
        numOfEvents = 5
    # Formatting the bot's response
    # Begin the message wtih three backticks for a code block
    message = "```\n"
    # Add column headers for the table
    message += "  ID  :  Event     :  Date \n"
    message += "------+------------+---------------------\n"
    # Get the list of Event objects of the necessary events and add the info
    # to the bot's response
    eventList = events.getEvents(cursor, eventTitle, numOfEvents)
    # Format the bot's response with data about the events
    for Event in eventList:
        message += f"{Event.sqlID:4d}  :  "
        message += f"{Event.eventName} {Event.eventNumber:4d}  :  "
        message += f"{Event.date}\n"
    # Finish off the message with closing backticks
    message += "```"
    return message

# Signs a user up for a specified event
def eventSignup(cursor, args):
    try:
        eventSQLID = int(args[1])
    except ValueError:
        raise ValueError(f"``{args[1]}`` is not an integer.")
    except IndexError:
        raise ValueError(f"No event ID was given.")

# Creates a reminder at the given time for a given user
def reminderCreate(cursor, ctx, args):
    eventID = args[1]
    timeOffset= int(args[2])
    units = args[3]
    userID = ctx.message.author.id
    try:
        reminders.createReminder(cursor, eventID, timeOffset, units, userID)
        message = f"Created a reminder for you! I will remind you {timeOffset} {units} before the event"
    except ValueError as error:
        message = error
    return message
            
# Returns a nicely formatted table of all the reminders a user has created
def remindersList(cursor, ctx, args):
    userID = ctx.message.author.id
    # Formatting the bot's response
    # Begin the message with three backticks for a code block
    message = "```\n"
    # Add column headers for the table
    message += "  ID  :  Event     :  Reminder Date \n"
    message += "------+------------+---------------------\n"
    # Get a list of Reminder objects
    reminderList = reminders.getReminders(cursor, userID)
    # Format the bot's response with data about the events
    for reminder in reminderList:
        message += f"{reminder.sqlID:4d}  :  "
        message += f"{reminder.eventName} {reminder.eventNumber:4d}  :  "
        message += f"{reminder.date}\n"
    # Finish off the message with closing backticks
    message += "```"
    return message
