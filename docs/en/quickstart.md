# Quickstart

**This page gives a brief introduction to the library. It is assumed that you have installed
library, if not, visit the section [«Getting Started»](./start.md)**

## A minimal code

```python
import sqlite3
import requesto as rq


dataBase: rq.dataBase = rq.sqliteConnect(dbname="database.db")
try:
    userData: rq.Table = rq.Table("userData", dataBase.cursor)
except sqlite3.OperationalError:
    # raise exampleError
    pass

userData.insert("name, ifPresent", "age", "'John', true, 21")
#  Autocommit is on by default. Let's fix it
dataBase.connection.autocommit(False)
#  I will print in console names of people whose age is over 20 

print(userData.fetchAll("name", "age > 20"))
dataBase.connection.close()
```
Let's go through the code step by step:
* 1-2. Simply imported sqlite3 and requesto libraries
* 3\. Set the variable database type dataBase and use the [`sqliteConnection()`](./manuals.md/#sqliteConnection()) function. To launch database object in temporary memory mode:
`
sqliteConnection(ifMemory = True)
`
* 4-11. We are trying to create a Table object. If there is no table - we are sad.
* 12\. We insert a row into the table by values using the function [`Database.Table.insert()`](./manuals.md/#Table.insert)
* 14\. Turn off autocommit with the function [`DataBase.Connection.autocommit(False)`](./manuals.md/#DataBase.Connection.autocommit())
* 17\. We display all rows where the age is greater than 20 using the function [`Database.Table.fetchAll`](./manuals.md/#Table.returnAll)
* 18\. Close the connection with the function [`Database.Connection.close()`](./manuals.md/#Database.Connection.close())


Moreover, in update 1.2 you can now check if table in the database:
```python
...
import requesto as rq
database = rq.DataBase(user=user)
tableName = "userdata"
if tableName not in database.tables:
    raise Exception
try:
    table = database.Table(tableName, cursor=database.cursor)
except:
    raise Exception
...
```
