import metaDB
import sqlpyte3.connectDB as connectDB

conn = connectDB.createConnection("cdl.db")
cursor = connectDB.createCursor(conn)


metaDB.createGamemodesTable(cursor)
metaDB.createEventTable(cursor)
metaDB.createReminderTable(cursor)
metaDB.createResultsTable(cursor)
metaDB.createRSVPTable(cursor)
metaDB.createSeasonTable(cursor)
metaDB.createUserTable(cursor)
metaDB.createVehicleTable(cursor)

connectDB.commitChanges(conn)
connectDB.closeConnection(conn)
