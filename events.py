# Any and all functions related to events
import database.readDB as readDB
import database.writeDB as writeDB
import math

# Create event given title and number (e.g., CDL 203), season, and date
def createEvent(cursor, title, number, seasonID, date):
    writeDB.insertRow(cursor, "events",
                      title = title,
                      number = number,
                      seasonID = seasonID,
                      date = date)

# Get the appropiate season given a event number
# 1-10 is Season 1, 11-20 is Season 2, and so on...
def getSeason(eventNumber):
    season = int(math.floor(eventNumber / 10))
    return season
    
