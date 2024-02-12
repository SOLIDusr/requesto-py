Make sure you installed all dependencies before installation! Version with pre-downloaded dependencies in progress. [\*click\*](https://github.com/SOLIDusr/requesto-py/tree/no-dependencies)

Dependencies:
* OS Windows(8.1?/10/11) / OS Linux (Mint 22 / Mint 23 / Ubuntu 23 / Kali / Fedora)
* python 3.10
* pip 23.3.1
* psycopg2
* sqlite3
<br>

**How to clone the repo**

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


## Basic consept of use

---

<p> <b>requesto-py </b> revolves around basic OOP concepts, classes and objects.</p>
<p>Example of usage of the library with sqlite3</p>

```python
import requesto as rq

#  declaring database object with sqliteConnection function
dataBase: rq.dataBase = rq.sqliteConnect(filename="database.db")
#  declaring table object
userData: rq.Table =  rq.Table("userData", dataBase.cursor, schemaName="schema")
#inserting something
userData.insert(
    "name, ifPresent, age",
    "'John', true, 21")
#printing every id from every row in database
print(userData.fetchAll("id"))
#  Output is a tuple of every id from database
#  Same as cursor.fetchall()
```

Same on sqlite3:
```python
import sqlite3
connection = sqlite3.connect("database")
cursor = connection.cursor()
cursor.execute("""INSERT INTO userdata (name, ifPresent, age) VALUES ('Weak', false, 38)""")
connection.commit()
cursor.execute("""SELECT * FROM userData""")
print(cursor.fetchall())
```
Too many SQL for this easy request.
