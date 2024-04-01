# Справочник по модулю

## Справка по версии модуля



Есть два способа вывести версию библиотеки.

```python
requesto.version_info
```
"Named tuple" аналогичный `sys.version_info`.

Как и в случае с `sys.version_info`, допустимыми значениями уровня выпуска являются «alpha», «beta», 
«candidate» и «final».

```python
requesto.__version__
```

Строковое представление версии. Например '1.2.0r'. Это основано на PEP 440.

## requesto

### Основные классы

- [`class` `PostgresDb`](#postgresdb)
- [`def` `SqliteDb`](#sqlitedb)


## DataBase

---

`class requesto.DataBase(connection)`

- [`class` `Connection`](#Connection)
- [`class` `Table`](#Table)
- [`class` `WrongParamError`](#WrongParamError)
- [`Attribute` `connection: DataBase.Connection`](#connection)
- [`Attribute` `cursor: psycopg2.cursor | sqlite3.Cursor`](#cursor)


## Connection

---

- [`def` `autocommit`](#autocommit)
- [`def` `close`](#close)
- [`def` `commit`](#commit)
- [`def` `reset`](#reset)
- [`def` `isClosed`](#isClosed)
- [`def` `__getCursor__`](#__getCursor__)
- [`def` `getAutocommit`](#getAutocommit)
- [`def` `cancel`](#cancel)
- [`def` `getTransactionStatus`](#getTransactionStatus)

## Table

---

- [`def` `fetchAll`](#fetchAll)
- [`def` `fetchMany`](#fetchMany)
- [`def` `fetchOne`](#fetchOne)
- [`def` `insert`](#insert)
- [`def` `update`](#update)


### `` class PostgresDb``

Возвращает объект базы данных `requesto.DataBase`

Параметры:
* host( str ) ( Обязательно ) - Хост сервера базы данных
* port( str ) ( Обязательно ) - Порт сервера базы данных
* dbName( str ) ( Обязательно ) - Название базы данных
* userName( str ) ( Обязательно ) - Имя пользователя базы данных


### `` class SqliteDb``

Возвращает объект базы данных `requesto.DataBase`


### `` class WrongParamError``


### `` class DataBase``


### `` Attribute connection``


### `` Attribute cursor``


### `` def autocommit(state = True) -> bool``


### `` def close() -> bool``


### `` def commit() -> bool``


### `` def reset()``


### `` def isClosed() -> int``


### `` def __getCursor__() -> pg.cursor | sqlt.Cursor``


### `` def getAutocommit()``


### `` def cancel() -> None``


### `` def getTransactionStatus()``


### `` class Table``


### `` def fetchAll(param = None, where = None) -> list``


### `` def fetchMany(param = None, where = None) -> list``


### `` def fetchOne(param = None, where = None) -> tuple``


### `` def insert() -> DataBase``


### `` def update() -> DataBase``
