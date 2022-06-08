import sqlite3
import oneOffs

conn = sqlite3.connect("test.db")
curs = conn.cursor()

#oneOffs.populateUsers(curs)
#oneOffs.populateAliases(curs)



oneOffs.populateResults()

lowerNames = []
for name in names:
    lowerNames.append(name.lower().strip())

#print(lowerNames)

registeredNames = []
curs.execute("SELECT username FROM users")
for name in curs:
    registeredNames.append(name[0].lower())

curs.execute("SELECT alias FROM aliases")
for alias in curs:
    registeredNames.append(alias[0].lower())


for name in registeredNames:
    print(name)


users = []
for name in lowerNames:
    if name not in registeredNames:
        print(f"{name} not in list")
    else:
        users.append(name)

for name in lowerNames:
    print(name)

print(users)
conn.commit()
