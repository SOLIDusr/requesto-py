Перед установкой убедитесь, что у вас установлены зависимости! Версия с предустановленными зависимостями в разработке. [\*click\*](https://github.com/SOLIDusr/requesto-py/tree/no-dependencies)

Зависимости:
* OS Windows(8.1?/10/11) / OS Linux (Mint 22 / Mint 23 / Ubuntu 23)
* python 3.10
* pip 23.3.1
* psycopg2
* sqlite3
<br>

1. Клонируйте репозиторий

```shell
git clone https://github.com/SOLIDusr/requesto-py.git
```

2. pip/pip3 installer (В процессе разработки)
```shell
pip3 install requesto-py
```

## Базовый концепт работы

---

<p> <b>requesto-py </b> основан на классах и основных принципах ООП.</p>
<p>Пример использования библиотеки с sqlite3:</p>

```python
import requesto as rq

#  declaring database object with sqliteConnection function
dataBase: rq.dataBase = rq.sqliteConnection(dbname="database.db")
#  declaring table object
userData: rq.Table =  rq.Table("userData", dataBase.cursor)
#inserting something
userData.insert(
    "name, ifPresent, age",
    "'John', true, 21")
#printing every id from every row in database
print(userData.returnAll("id"))
#  Output is a tuple of every id from database
#  Same as cursor.fetchall()
```

А как же это бы выглядело в sqlite3?
```python
import sqlite3
connection = sqlite3.connect("database")
cursor = connection.cursor()
cursor.execute("""INSERT INTO userdata (name, ifPresent, age) VALUES ('Weak', false, 38)""")
connection.commit()
print(cursor.execute("""SELECT * FROM userData""").fetchall())
```
Слишком много SQL для простенького запроса.
