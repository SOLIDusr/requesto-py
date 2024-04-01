# Быстрый старт

**На этой странице дается краткое введение в библиотеку. Предполагается, что у вас установлена 
библиотека, если нет - посетите раздел [«Начало»](./start.md)**

## Базовый код

```python
import requesto as rq


dataBase: rq.dataBase = rq.sqliteConnect(dbname="database.db")
try:
    userData: rq.Table = rq.Table("userData", dataBase.cursor)
except sqlite3.OperationalError:
    # raise exampleError
    pass

#  Autocommit is off by default. Let's fix it
dataBase.connection.autocommit(True)

userData.insert("name, ifPresent", "age", "'John', true, 21")

#  Let's print in console names of people whose age is over 20 

print(userData.fetchAll("name", "age > 20"))

dataBase.connection.close()
```
Давайте рассмотрим код шаг за шагом:
* 1-2. Просто импортируем библиотеки sqlite3 и requesto.
* 3\. Задаем переменной базы данных тип dataBase и используем функцию [`sqliteConnection()`](./manuals.md/#sqliteConnection()). Чтобы запустить объект базы данных в режиме временной памяти:
`
sqliteConnection(ifMemory = True)
`
* 4-11. Мы пытаемся создать объект Table. Если таблицы нет - мы в печали.
* 12\. Включите автокоммит с помощью функции [`DataBase.Connection.autocommit(False)`](./manuals.md/#DataBase.Connection.autocommit())
* 14\.  Вставляем строку в таблицу по значениям с помощью функции [`Database.Table.insert()`](./manuals.md/#Table.insert)
* 18\. Выводим все строки, в которых возраст больше 20, с помощью функции [`Database.Table.fetchAll`](./manuals.md/#Table.returnAll)
* 19\. Закрываем соединение с помощью функции [`Database.Connection.close()`](./manuals.md/#Database.Connection.close())
