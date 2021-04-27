# Python Modules
import csv
import sqlite3
# Third-Party Modules
# Custom Modules

# This module will hold functions which (most likely) will only be used a few
# times in initially creating the database. These functions will populate the
# database with data from various CSV files.

# ========================== Populate Database Tables ==========================

# populateUsers() populates the users given by users.csv into the users table of
# the database of the given cursor.
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
