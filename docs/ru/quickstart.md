# Быстрый старт

**На этой странице дается краткое введение в библиотеку. Предполагается, что у вас установлена 
библиотека, если нет - посетите раздел [«Начало»](./start.md)**

## Базовый код

```python
import sqlite3
import requesto as rq

dataBase: rq.dataBase = rq.sqliteConnection(dbname="database.db")
userData: rq.Table = rq.Table("userData", dataBase.cursor)

userData.insert("name, ifPresent", "age", "'John', true, 21")
dataBase.connection.autocommit(False)
print(userData.returnAll("name", "age > 20"))
dataBase.connection.close()
```
Пройдемся шаг за шагом по коду:
* 1-2. Просто импортируем библиотеки sqlite3 и requesto
* 3\. Задаем переменной dataBase тип базы данных и используем функцию [`sqliteConnection()`](./manuals.md/#sqliteConnection()).  Для того чтобы запустить базу данных в режиме временной памяти:
```python
import requesto.requesto as rq
rq.sqliteConnection(ifMemory=True)
```
* 4-12. Пытаемся создать объект таблицы. В случае, если таблицы нет - создаём её.
* 1З. Вставляем в таблицу строку по значениям функцией [`Database.Table.insert()`](./manuals.md/#Table.insert)
* 14\. Выключаем autocommit функцией [`DataBase.Connection.autocommit(False)`](./manuals.md/#DataBase.Connection.autocommit())
* 15\. Выводим все строки, где возраст больше 20 функцией [`Database.Table.returnAll`](./manuals.md/#Table.returnAll)
* 16\. Закрываем connection функцией [`Database.Connection.close()`](./manuals.md/#Database.Connection.close())
