import connectDB
import initDB
import readDB
import writeDB

conn = connectDB.createConnection("cdl.db")
cursor = connectDB.createCursor(conn)


initDB.createEventGamemodesTable(cursor)
initDB.createEventTable(cursor)
initDB.createReminderTable(cursor)
initDB.createResultsTable(cursor)
initDB.createRSVPTable(cursor)
initDB.createSeasonTable(cursor)
initDB.createUserTable(cursor)
initDB.createVehicleTable(cursor)

connectDB.commitChanges(conn)
connectDB.closeConnection(conn)
