# Shorthand string used in every table to create the sqlID column, which gives
# each row a unique ID that autoincrements whenever a row is inserted into the
# table. (To autoincrement it, NULL must be inserted into its column)
sqlID = "sqlID INTEGER PRIMARY KEY AUTOINCREMENT"

# Creates table linking gamemode and the event they are used in
def createGamemodesTable(curs):
    gamemodesCommand = f"""
CREATE TABLE gamemodes ({sqlID}, eventID INTEGER, gameModeID INTEGER)
    """
    curs.execute(gamemodesCommand)

# Creates table of events containing info about the event (title, time, etc.)
def createEventTable(curs):
    eventCommand = f"""
CREATE TABLE events
({sqlID}, title TEXT, number INTEGER, seasonID INTEGER, date TEXT)
"""
    curs.execute(eventCommand)

# Creates table of reminders linked to users and events; stores the reminder as
# an absolute time (not an offset from the event)
def createReminderTable(curs):
    reminderCommand = f"""
CREATE TABLE reminders ({sqlID}, eventID INTEGER, time TEXT, userID INTEGER)
"""
    curs.execute(reminderCommand)

# Creates table of results for each event and user
def createResultsTable(curs):
    resultsCommand = f"""
CREATE TABLE results ({sqlID}, eventID INTEGER, gamemodeID INTEGER,
userID INTEGER, place INTEGER, groupNumber INTEGER)
"""
    curs.execute(resultsCommand)

# Creates table of users' registrations for each event containing info about the
# registration (who registered, which event, which vehicle, etc.)
def createRSVPTable(curs):
    rsvpCommand = f"""
CREATE TABLE rsvp ({sqlID}, eventID INTEGER, userID INTEGER, vehicleID, INTEGER)
"""
    curs.execute(rsvpCommand)

# Creates table of seasons to be referenced in the events table
def createSeasonTable(curs):
    seasonCommand = f"""
CREATE TABLE seasons ({sqlID}, number INTEGER)
"""
    curs.execute(seasonCommand)

# Creates table of users containing general info about the user (Discord ID,
# username, etc.)
def createUserTable(curs):
    userCommand = f"""
CREATE TABLE users ({sqlID}, discordID INTEGER, username TEXT, status TEXT)
"""
    curs.execute(userCommand)

# Creates table of vehicles to be referenced by the RSVP table
def createVehicleTable(curs):
    vehicleCommand = f"""
CREATE TABLE vehicles ({sqlID}, name TEXT)
"""
    curs.execute(vehicleCommand)
