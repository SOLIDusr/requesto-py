Make sure you installed all dependencies before installation!

Dependencies:
* OS Windows (8.1?/10/11) / OS Linux (Mint 22 / Mint 23 / Ubuntu 23 / Kali / Fedora)
* python 3.10 or higher
* pip 23.3.1 or higher
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


<p> <b>requesto-py </b> revolves around basic OOP concepts, classes and objects.</p>
<p>Example of usage of the library with sqlite3 and postgres</p>

```python
import requesto as rq

#  declaring database object with SqliteDb class
dataBase = rq.SqliteDb(filename="database.db")
#  declaring table object
userData = rq.Table("userData", dataBase.cursor, schemaName="main")
```

```python
import requesto as rq

dataBase = rq.PostgresDb(host="localhost", port="5432", username="NaroMori", dbName="MainDb")
userData = rq.Table("userData", dataBase.cursor, schemaName="public")
```

All info about functions and classes can be found [here](./manuals.md) or in the docstring.

Every subsequent interaction will be done using `database` and `userData` objects.
