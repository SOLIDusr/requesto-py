# Быстрый старт

**На этой странице дается краткое введение в библиотеку. Предполагается, что у вас установлена 
библиотека, если нет - посетите раздел [«Начало»](./start.md)**

## Базовый код

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
Пройдемся шаг за шагом по коду:
* 1-2. Просто импортируем библиотеки sqlite3 и requesto
* 3\. Задаем переменной dataBase тип базы данных и используем функцию [`sqliteConnection()`](./manuals.md/#sqliteConnection()).  Для того чтобы запустить базу данных в режиме временной памяти:
```python
sqliteConnection(ifMemory=True)
```
* 4-12. Пытаемся создать объект таблицы. В случае, если таблицы нет - создаём её.
* 1З. Вставляем в таблицу строку по значениям функцией [`Table.insert()`](./manuals.md/#Table.insert)
* 14\. Выключаем autocommit функцией [`DataBase.Connection.autocommit(False)`](./manuals.md/#DataBase.Connection.autocommit())
* 15\. Выводим все строки, где возраст больше 20 функцией [`Table.returnAll`](./manuals.md/#Table.returnAll)
* 16\. Закрываем connection функцией [`Database.Connection.close()`](./manuals.md/#Database.Connection.close())
