# Frequently asked questions

---

## Contents

* [Basics](./#Basics)
* * [Initialization](./#Initialization)
* * [Database object](./#Database object)
* * [Table object](./#Table object)


# Basics

---
## Initialization

In older (pre-release) versions you could initialize database object by creating Database object,
but now you can use one of these methods [`rq.sqliteConnection()`](manuals.md/#sqliteConnection)
OR [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)
```python
import requesto.requesto as rq
database = rq.postgresqlConnect(host="host",
                       port="port",
                       dbName="dbname",
                       userName="username")
```
OR 
```python
import requesto.requesto as rq
database = rq.sqliteConnection(filename="database.db")
```
---
## Database Object

By calling [`rq.sqliteConnection()`](manuals.md/#sqliteConnection) or [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)
you'll get db object ```requesto.Database```
Database object used to make table oobjects and is like a center of database. `Connection` is a subsidiary object. It controls whole db and `cursor` object.

---

## Table object

You can create Table object through [`db.Table(name)`](manuals.md/#) or [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)

<br>

Table object used for controlling data in the table through methods `fetchAll` , `fetchMany`, `fetchOne`
, `insert`, `update`

---
