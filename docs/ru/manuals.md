# Справочник по модулю

## Справка по версии модуля

-----

!WORK IN PROGRESS!

-----


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

- [`class` `DataBase`](####DataBase)
- [`class` `Connection`](####Connection)
- [`class` `PostgresDb`](####postgresdb)
- [`class` `SqliteDb`](####sqlitedb)

#### `class DataBase`

---

`class requesto.DataBase(connection)`

- [`class` `Connection`](#Connection)
- [`class` `Table`](#Table)
- [`class` `WrongParamError`](#WrongParamError)
- [`Attribute` `connection: DataBase.Connection`](#connection)
- [`Attribute` `cursor: psycopg2.cursor | sqlite3.Cursor`](#cursor)


#### `class Connection`

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

#### `class Table`

---

- [`def` `fetchAll`](#fetchAll)
- [`def` `fetchMany`](#fetchMany)
- [`def` `fetchOne`](#fetchOne)
- [`def` `insert`](#insert)
- [`def` `update`](#update)

#### `class PostgresDb`

Возвращает объект базы данных `requesto.DataBase`

Параметры:
* `host( str )` - Хост сервера базы данных
* `port( str )` - Порт сервера базы данных
* `dbName( str )` - Название базы данных
* `userName( str )` - Имя пользователя базы данных

#### `` class SqliteDb``

Возвращает объект базы данных `requesto.DataBase`

Параметры:
* `databaseFile (str) = None` - Имя файла базы данных
* `ifMemory (bool) = False` - Работает ли база данных в оперативной памяти
* `schemaName (str) = "main"` - Имя схемы с которой будет работа

#### `` class ConnectionDetailsMissingException``



#### `` class DataBase``


#### `` Attribute connection``


#### `` Attribute cursor``


#### `` def autocommit(state = True) -> bool``


#### `` def close() -> bool``


#### `` def commit() -> bool``


#### `` def reset()``


#### `` def isClosed() -> int``


#### `` def __getCursor__() -> pg.cursor | sqlt.Cursor``


#### `` def getAutocommit()``


#### `` def cancel() -> None``


#### `` def getTransactionStatus()``


#### `` class Table``


#### `` def fetchAll(param = None, where = None) -> list``


#### `` def fetchMany(param = None, where = None) -> list``


#### `` def fetchOne(param = None, where = None) -> tuple``


#### `` def insert() -> DataBase``


#### `` def update() -> DataBase``
