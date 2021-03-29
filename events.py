# Any and all functions related to events
import math

# Create event given title and number (e.g., CDL 203), season, and date
def createEvent(cursor, title, number, seasonID, date):
    # Column order: [sqlID, title, number, seasonID, date]
    # NULL is inserted into the sqlID column because it auto-increments
    sqlCommand = "INSERT INTO events VALUES (NULL, ?, ?, ?, ?)"
    cursor.execute(sqlCommand, (title, number, seasonID, date,))

# Get the appropiate season given an event number
# 1-10 is Season 1, 11-20 is Season 2, and so on...
def getSeason(eventNumber):
    season = int(math.floor(eventNumber / 10))
    return season

# Get a list of the {numOfEvents} most recent events of a given title
# (e.g., the 10 most recent CDL or RPG events) and return a list of Event class
# objects containing the SQL ID, title and number, and date.
def getEvents(cursor, eventName, numOfEvents):
    # SQL command to be executed with a placeholder for how many events to
    # return.
    sqlCommand = "SELECT * FROM events ORDER BY number DESC LIMIT ?"
    cursor.execute(sqlCommand, (numOfEvents,))
    # Return the list of SQLite3 Row instances
    return cursor.fetchall()

# Get the full name of an event (title and event) and return it as two variables
def getFullEventName(cursor, eventID):
    sqlCommand = "SELECT title, number FROM events WHERE sqlID = ?"
    cursor.execute(sqlCommand, (eventID,))
    row = cursor.fetchone()
    return row["title"], row["number"]
