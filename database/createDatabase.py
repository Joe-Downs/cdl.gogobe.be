# Python Modules
# Third-Party Modules
import sqlite3
# Custom Modules
import metaDB

conn = sqlite3.connect("cdl.db")
cursor = conn.cursor()


metaDB.createGamemodesTable(cursor)
metaDB.createEventTable(cursor)
metaDB.createReminderTable(cursor)
metaDB.createResultsTable(cursor)
metaDB.createRSVPTable(cursor)
metaDB.createSeasonTable(cursor)
metaDB.createUserTable(cursor)
metaDB.createVehicleTable(cursor)

# Commit the changes and close the connection
conn.commit()
conn.close()
