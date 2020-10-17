# Functions used by the bot for its commands

import discord
import events

# Computes the season (if needed) and adds the event to the database
def eventAdd(cursor, ctx, *args):
    title = upper(args[1])
    eventNumber = args[2]
    date = args[3]
    if title == "CDL":
        season = events.getSeason(eventNumber)
    else:
        # Only CDL events are split into seasons, and there is no season 0
        season = 0
    events.createEvent(cursor, title, eventNumber, season, date)
    return f"Added event \"{title} {eventNumber}\" scheduled for {date}"
