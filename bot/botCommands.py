# Functions used by the bot for its commands

import events

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
    
    
