# Any and all functions related to reminders
import database.sqlpyte3.readDB as readDB
import database.sqlpyte3.writeDB as writeDB
import datetime

# Reminder class for storing data about each reminder. Class instances can be
# used to return bundled info about reminders.
class Reminder:
    def __init__(self, sqlID, eventName, eventNumber, date):
        self.sqlID = sqlID
        self.eventName = eventName
        self.eventNumber = eventNumber
        self.date = date
        
    # Converts the info about the reminder into a nicely formatted string
    def __str__(self):
        toString = f"Reminder for {self.eventName} {self.eventNumber}\n"
        toString += f"Date: {self.date}\n"
        toString += f"SQL ID: {self.sqlID}"
        return toString

# Converts a value in days, hours, or minutes to seconds
def getSeconds(value, unit):
    if value < 0:
        # Don't accept negative values, to simplify things. Plus, no one
        # should be wanting a reminder *after* the event has passed.
        raise ValueError("Values cannot be negative")
    elif unit == "day" or unit == "days":
        value *= 86400
    elif unit == "hour" or unit == "hours":
        value *= 3600
    elif unit == "minute" or unit == "minutes":
        value *= 60
    elif unit == "second" or unit == "seconds":
        # It's already in seconds, no conversion needed
        value *= 1
    else:
        # It's not in days, hours, minutes, or seconds - something went wrong
        raise ValueError("Units are not in days, hours, minutes, or seconds")
    return value

# Create a reminder given a cursor, event, time offset (in seconds), and the user
def createReminder(cursor, eventID, timeOffset, unit, userID):
    # A value and unit is passed into the createReminder() function, and then the
    # getSeconds() function is called, reducing function calls elsewhere
    secTimeOffset = getSeconds(timeOffset, unit)
    # We want an absolute time, so we first need to get the event's
    # time, then subtract the offset
    eventDatetimeString = readDB.getValue(cursor, "events", "date", "ROWID", eventID)
    # Time strings will ALWAYS be stored in the ISO 8601 format with NO offset:
    # YYYY-MM-DDTHH:MM:SS (milliseconds will not be included)
    eventDatetimeObject = datetime.datetime.fromisoformat(eventDatetimeString)
    reminderTimeDelta = datetime.timedelta(seconds = secTimeOffset)
    reminderTime = eventDatetimeObject - reminderTimeDelta
    writeDB.insertRow(cursor, "reminders",
                      eventID = eventID,
                      time = reminderTime,
                      userID = userID)

# Returns a list of the reminder(s) a user has created for themselves
def getReminders(cursor, userID):
    # Get a list of the eventIDs that the user has created reminders for
    reminderIDs = readDB.getValue(cursor, "reminders","ROWID", "userID", userID,
                                  getMultiple = True)
    # List of the Reminder class objects
    reminderList = []
    for reminderID in reminderIDs:
        sqlID = reminderID
        eventID = int(readDB.getValue(cursor, "reminders", "eventID",
                                      "ROWID", sqlID))
        eventName = readDB.getValue(cursor, "events", "title", "ROWID",
                                    eventID)
        eventNumber = int(readDB.getValue(cursor, "events", "number",
                                          "ROWID", eventID))
        date = readDB.getValue(cursor, "reminders", "time", "ROWID", sqlID)
        tempReminder = Reminder(sqlID, eventName, eventNumber, date)
        reminderList.append(tempReminder)
    return reminderList
