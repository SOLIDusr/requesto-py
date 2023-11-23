import sqlite3
import requesto


db = requesto.postgresqlConnect(
    host="83.220.170.127",
    port="5432",
    dbName="coredb",
    userName="dolta"
)

userData = requesto.Table(name="userdata", databaseObject=db)

print(userData.test())
