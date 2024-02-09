# Start
---

## Contents

* [Basics](#Basics)
* * [Initialization](#Initialization)
* * [Database object](#Database object)
* * [Table object](#Table object)


<anchor name="Basics">

</anchor>

# Basics


<anchor name="Initialization">

</anchor>

## Initialization

In older (pre-release) versions you could initialize database object by creating Database object,
but now you can use one of these methods [`rq.sqliteConnection()`](manuals.md#sqliteConnection)
OR [`rq.postgresqlConnection()`](manuals.md#postgresqlConnection)

```Python
import requesto-py as rq


user: rq.User = rq.User(
                host="ip",
                port="port",
                dbName="name",
                userName="username"
            )

db = rq.Postgresq

```




<anchor name="Database object">

</anchor>

## Database Object

By calling [`rq.sqliteConnection()`](manuals.md#sqliteConnection) or [`rq.postgresqlConnection()`](manuals.md#postgresqlConnection)
you'll get db object ```requesto.Database```
Database object used to make table oobjects and is like a center of database. `Connection` is a subsidiary object. It controls whole db and `cursor` object.



## Table object

You can create Table object through [`db.Table(name)`](manuals.md#) or [`rq.postgresqlConnection()`](manuals.md#postgresqlConnection)



Table object used for controlling data in the table through methods `fetchAll` , `fetchMany`, `fetchOne`
, `insert`, `update`

