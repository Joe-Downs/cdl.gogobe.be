# Any and all functions related to reminders
import database.writeDB as writeDB
import database.readDB as readDB
import datetime

# Converts a value in days, hours, or minutes to seconds
def getSeconds(value, unit):
    if unit == "day" or unit == "days":
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
        value = -1
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
