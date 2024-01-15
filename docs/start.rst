Make sure you installed all dependencies before installation! Version
with pre-downloaded dependencies in progress.
`\*click\* <https://github.com/SOLIDusr/requesto-py/tree/no-dependencies>`__

Dependencies: \* OS Windows(8.1?/10/11) / OS Linux (Mint 22 / Mint 23 /
Ubuntu 23) \* python 3.10 \* pip 23.3.1 \* psycopg2=2.9.9 \* sqlite3

1. How to clone the repo

.. code:: shell

   git clone https://github.com/SOLIDusr/requesto-py.git

2. pip/pip3 installer (In development)

.. code:: shell

   pip3 install requesto-py

Basic consept of use
--------------------

--------------

.. raw:: html

   <p>

requesto-py revolves around basic OOP concepts, classes and objects.

.. raw:: html

   </p>

.. raw:: html

   <p>

Example of usage of the library with sqlite3

.. raw:: html

   </p>

.. code:: python

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

And how does it look on sqlite3?

.. code:: python

   import sqlite3
   connection = sqlite3.connect("database")
   cursor = connection.cursor()
   cursor.execute("""INSERT INTO userdata (name, ifPresent, age) VALUES ('Weak', false, 38)""")
   connection.commit()
   print(cursor.execute("""SELECT * FROM userData""").fetchall())

Too many SQL for this easy request.
