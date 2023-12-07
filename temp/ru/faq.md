# Часто задаваемые вопросы

---

## Содержание

* [Основы](./#Основы)
* * [Инициализация](./#Инициализация)
* * [Объект базы данных](./#Объект базы данных)
* * [Объект таблицы](./#Объект таблицы)


# Основы

---
## Инициализация

В старых (дорелизных) версиях инициализация происходила созданием объекта базы данных,
но сейчас для этого используется одна из функций [`rq.sqliteConnection()`](manuals.md/#sqliteConnection)
или [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)
```python
import requesto as rq
database = rq.postgresqlConnect(host="host",
                       port="port",
                       dbName="dbname",
                       userName="username")
```
Или 
```python
import requesto as rq
database = rq.sqliteConnection(filename="database.db")
```
---
## Объект базы данных

Вызов функции [`rq.sqliteConnection()`](manuals.md/#sqliteConnection) или [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)
возвращает объект ```requesto.Database```
Объект Database используется для назначения таблиц и является некоторым центром БД. Дочерним объектом
Database является объект `Connection`. Он отвечает за управление базой данных и объектом `cursor`.

---

## Объект таблицы

Создание объекта Table через [`db.Table(name)`](manuals.md/#) или [`rq.postgresqlConnection()`](manuals.md/#postgresqlConnection)

<br>

Объект Table используется для управления данными в таблице через функции `fetchAll` , `fetchMany`, `fetchOne`
, `insert`, `update`

---
