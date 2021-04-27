# Python Modules
import csv
import sqlite3
# Third-Party Modules
# Custom Modules

# This module will hold functions which (most likely) will only be used a few
# times in initially creating the database. These functions will populate the
# database with data from various CSV files.

# ========================== Populate Database Tables ==========================

# populateAliases() populates the aliases of users given by aliases.csv into the
# aliases table of the database of the given cursor. aliases.csv is strictly
# formatted to simplify the import process. This strict format is: headers which
# read: "discordID,alias" (this allows the CSV to be mapped to a
# dictionary). DiscordIDs are not used because this file is created by a human
# and it's faster to copy the ID from Discord rather than look it up in the
# database. (Python can do that for us!)
def populateAliases(curs):
    with open("aliases.csv", newline = '') as csvAliases:
        aliasReader = csv.DictReader(csvAliases)
        for row in aliasReader:
            aliasCommand = """INSERT INTO aliases
(sqlID, userID, alias) VALUES (NULL, ?, ?)
"""
            discordID = int(row["discordID"])
            discordIDCommand = "SELECT sqlID FROM users WHERE discordID = ?"
            curs.execute(discordIDCommand, (discordID,))
            userID = curs.fetchone()[0]
            print(userID)
            alias = row["alias"]
            curs.execute(aliasCommand, (userID, alias))
        csvAliases.close()

# populateUsers() populates the users given by users.csv into the users table of
# the database of the given cursor. users.csv is strictly formatted to simplify
# the import process. This strict format is: headers which read:
# "discordID,username,status" (this allows the CSV to be mapped to a dictionary)
def populateUsers(curs):
    with open("users.csv", newline = '') as csvUsers:
        userReader = csv.DictReader(csvUsers)
        for row in userReader:
            userCommand = """INSERT INTO users
(sqlID, discordID, username, status) VALUES (NULL, ?, ?, ?)
"""
            discordID = int(row["discordID"])
            username = row["username"]
            status = row["status"]
            curs.execute(userCommand, (discordID, username, status,))
    csvUsers.close()
