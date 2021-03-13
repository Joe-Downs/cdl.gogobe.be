# Any and all functions related to events
import database.sqlpyte3.readDB as readDB
import database.sqlpyte3.writeDB as writeDB
import math

# Event class for storing data about each event. Class instances can be used
# to return bundled info about events.
class Event:
    def __init__(self, sqlID, eventNumber, eventName, date):
        self.sqlID = sqlID
        self.eventNumber = eventNumber
        self.eventName = eventName
        self.date = date
    # Converts the info about the event into a nicely formatted string for output
    def __str__(self):
        return f"{self.eventName} {self.eventNumber}\nDate: {self.date}\nSQL ID: {self.sqlID}"

# Create event given title and number (e.g., CDL 203), season, and date
def createEvent(cursor, title, number, seasonID, date):
    writeDB.insertRow(cursor, "events",
                      title = title,
                      number = number,
                      seasonID = seasonID,
                      date = date)

# Get the appropiate season given an event number
# 1-10 is Season 1, 11-20 is Season 2, and so on...
def getSeason(eventNumber):
    season = int(math.floor(eventNumber / 10))
    return season

# Get a list of the {numOfEvents} most recent events of a given title
# (e.g., the 10 most recent CDL or RPG events) and return a list of Event class
# objects containing the SQL ID, title and number, and date.
def getEvents(cursor, eventName, numOfEvents):
    # List of ALL the event numbers of the given title
    eventNumbers = readDB.getValue(cursor, "events", "number", "title", eventName, getMultiple = True,
                                   sortedResults = True, sortBy = "number", descending = True)
    # List of the Event class objects
    eventsList = []
    # Get the other info pertaining to the events, create an Event class object for
    # the event and add it to the eventsList list.
    for i in range(0, numOfEvents):
        sqlID = int(readDB.getValue(cursor, "events", "ROWID", "number", int(eventNumbers[i])))
        eventNumber = int(eventNumbers[i])
        eventDate = readDB.getValue(cursor, "events", "date", "number", eventNumber)
        tempEvent = Event(sqlID, eventNumber, eventName, eventDate)
        eventsList.append(tempEvent)
    return eventsList
