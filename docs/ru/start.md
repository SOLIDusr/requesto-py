Перед установкой убедитесь, что у вас установлены зависимости! Версия с предустановленными зависимостями в разработке. [\*click\*](https://github.com/SOLIDusr/requesto-py/tree/no-dependencies)

Зависимости:
* OS Windows(8.1?/10/11) / OS Linux (Mint 22 / Mint 23 / Ubuntu 23)
* python 3.10
* pip 23.3.1
* psycopg2
* sqlite3
<br>

# Установка

**Как клонировать репозиторий**

<details>
<summary>GitHub</summary>

```shell
git clone https://github.com/SOLIDusr/requesto-py.git
```

</details>

<details>
<summary>pip3</summary>

```shell
pip3 install requesto-py
```

</details>

## Базовый концепт работы

---

<p> <b>requesto-py </b> основан на классах и основных принципах ООП.</p>
<p>Пример использования библиотеки с sqlite3:</p>

```python
import requesto as rq

#  Обозначаем объект базы данных с помощью класса SqliteDb
dataBase = rq.SqliteDb(filename="database.db")
#  Обозначаем объект таблицы
userData = rq.Table("userData", dataBase.cursor, schemaName="main")
```

```python
import requesto as rq

dataBase = rq.PostgresDb(host="localhost", port="5432", username="NaroMori", dbName="MainDb")
userData = rq.Table("userData", dataBase.cursor, schemaName="public")
```

Вся информация о функциях и классах может быть найдена [тут](./manuals.md) или в док строке в самом коде.

Все дальнейшие манипуляции будут производится с помощью объектов `database` и `userData`.
