# Any and all functions related to reminders
import database.writeDB as writeDB
import database.readDB as readDB
import datetime

# Create a reminder given a cursor, event, time offset (in seconds), and the user
def createReminder(cursor, eventID, secTimeOffset, userID):
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
