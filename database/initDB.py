import sqlite3
import writeDB

# Creates table of events containing info about
# the event (title, time, etc.)
def createEventTable(cursor):
    writeDB.createTable(cursor, "events",
                        title = "TEXT",
                        number = "INTEGER",
                        seasonID = "INTEGER",
                        date = "TEXT")

# Creates table of results for each event and user
def createResultsTable(cursor):
    writeDB.createTable(cursor, "results",
                        eventID =  "INTEGER",
                        gamemodeID = "INTEGER",
                        userID = "INTEGER",
                        place = "INTEGER",
                        groupNumber = "INTEGER")
    
# Creates table of users' registgrations for each
# event containing info about the registration
# (who registered, which event, which vehicle, etc.)
def createRSVPTable(cursor):
    writeDB.createTable(cursor, "rsvp",
                        eventID = "INTEGER",
                        userID = "INTEGER",
                        vehicleID = "INTEGER")

# Creates table of seasons to be referenced
# in the events table
def createSeasonTable(cursor):
    writeDB.createTable(cursor, "seasons",
                        number = "INTEGER")

# Creates table of users containing general info
# about the user (Discord ID, username, etc.)
def createUserTable(cursor):
    writeDB.createTable(cursor, "users",
                        DiscordID = "INTEGER",
                        username = "TEXT",
                        status = "TEXT")

# Creates table of vehicles to be referenced
# by the RSVP table
def createVehicleTable(cursor):
    writeDB.createTable(cursor, "vehicles",
                        name = "TEXT")
