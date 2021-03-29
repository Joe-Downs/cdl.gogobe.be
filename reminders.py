# Any and all functions related to reminders
import datetime

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
    readTimeCommand = "SELECT date FROM events WHERE sqlID = ?"
    # Fetch the result and get the first (and only) one which will be the string
    # representation of the date.
    cursor.execute(readTimeCommand, (eventID,))
    eventDatetimeString = cursor.fetchone()[0]
    # Time strings will ALWAYS be stored in the ISO 8601 format with NO offset:
    # YYYY-MM-DDTHH:MM:SS (milliseconds will not be included)
    eventDatetimeObject = datetime.datetime.fromisoformat(eventDatetimeString)
    reminderTimeDelta = datetime.timedelta(seconds = secTimeOffset)
    reminderTime = eventDatetimeObject - reminderTimeDelta
    # Column order: [sqlID, eventID, time, userID]
    # NULL is inserted into the sqlID column because it auto-increments
    createCommand = "INSERT INTO reminders VALUES (NULL, ?, ?, ?)"
    cursor.execute(createCommand, (eventID, reminderTime, userID,))

# Returns a list of the reminder(s) a user has created for themselves
def getReminders(cursor, userID):
    # SQL command to be executed with a placeholder for the userID given
    sqlCommand = "SELECT * FROM reminders WHERE userID=?"
    cursor.execute(sqlCommand, (userID,))
    # Return the list of SQLite3 Row instances
    return cursor.fetchall()
    
