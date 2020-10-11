# Any and all functions related to events
import database.readDB as readDB
import database.writeDB as writeDB

# Create event given title and number (e.g., CDL 203), season, and date
def createEvent(cursor, title, number, seasonID, date):
    writeDB.insertRow(cursor, "events",
                      title = title,
                      number = number,
                      seasonID = seasonID,
                      date = date)
