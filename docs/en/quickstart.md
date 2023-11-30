# Quickstart

**This page gives a brief introduction to the library. It is assumed that you have installed
library, if not, visit the section [«Getting Started»](./start.md)**

## A minimal code

```python
import sqlite3
import requesto as rq

dataBase: rq.dataBase = rq.sqliteConnection(dbname="database.db")
try:
    userData: rq.Table = rq.Table("userData", dataBase.cursor)
except sqlite3.OperationalError:
    userData: rq.Table = rq.createTable("userData", {
        "id": "pk",
        "name": "str",
        "ifPresent": "bool",
        "age": "int"
    })

userData.insert("name, ifPresent", "age", "'John', true, 21")
#  Autocommit по умолчанию включен. Исправим это!
dataBase.connection.autocommit(False)
#  Выведем в консоль имена всех, чей возрат больше 20

print(userData.returnAll("name", "age > 20"))
dataBase.connection.close()
```
Let's go through the code step by step:
* 1-2. Simply imported sqlite3 and requesto libraries
* 3\. Set the variable database type dataBase and use the [`sqliteConnection()`](./manuals.md/#sqliteConnection()) function. To launch database object in temporary memory mode:
``` python
sqliteConnection(ifMemory = True)
```
* 4-12. We are trying to create a Table object. If there is no table - creating it.
* 1З. We insert a row into the table by values using the function [`Database.Table.insert()`](./manuals.md/#Table.insert)
* 14\. Turn off autocommit with the function [`DataBase.Connection.autocommit(False)`](./manuals.md/#DataBase.Connection.autocommit())
* 15\. We display all rows where the age is greater than 20 using the function [`Database.Table.returnAll`](./manuals.md/#Table.returnAll)
* 16\. Close the connection with the function [`Database.Connection.close()`](./manuals.md/#Database.Connection.close())
