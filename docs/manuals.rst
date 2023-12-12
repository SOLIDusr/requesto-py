Справочник по модулю
====================

Справка по версии модуля
------------------------

--------------

Есть два способа вывести версию библиотеки. `Здесь <./versions>`__
описан принцип изменения версий

.. code:: python

   requesto.version_info

“Named tuple” аналогичный ``sys.version_info``.

Как и в случае с ``sys.version_info``, допустимыми значениями уровня
выпуска являются «alpha», «beta», «candidate» и «final».

.. code:: python

   requesto.__version__

Строковое представление версии. Например ‘1.0.0rc1’. Это основано на PEP
440.

requesto
--------

--------------

Методы:

-  `def postgresqlConnect <#postgresqlConnect>`__
-  `def sqliteConnect <#sqliteConnect>`__

DataBase
--------

--------------

``class requesto.DataBase(connection)``

-  class `Connection <#Connection>`__
-  class `Table <#Table>`__
-  class `WrongParamError <#WrongParamError>`__
-  Attribute `connection: DataBase.Connection <#connection>`__
-  Attribute `cursor: psycopg2.cursor | sqlite3.Cursor <#cursor>`__

Connection
----------

--------------

-  def `autocommit <#autocommit>`__
-  def `close <#close>`__
-  def `commit <#commit>`__
-  def `reset <#reset>`__
-  def `isClosed <#isClosed>`__
-  def `__getCursor__ <#getCursor>`__
-  def `getAutocommit <#getAutocommit>`__
-  def `cancel <#cancel>`__
-  def `getTransactionStatus <#getTransactionStatus>`__

Table
-----

--------------

-  def `fetchAll <#fetchAll>`__
-  def `fetchMany <#fetchMany>`__
-  def `fetchOne <#fetchOne>`__
-  def `insert <#insert>`__
-  def `update <#update>`__


``def postgresqlConnect(host, port, dbName, userName) -> DataBase``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Возвращает объект базы данных ``requesto.DataBase``

Параметры:

* host( str ) ( Обязательно ) - Хост сервера базы данных
* port( str ) ( Обязательно ) - Порт сервера базы данных
* dbName( str ) ( Обязательно ) - Название базы данных
* userName( str ) ( Обязательно) - Имя пользователя базы данных

``def sqliteConnect(ifMemory = False, filename = None) -> DataBase | DataBase.WrongParamError``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Возвращает объект базы данных ``requesto.DataBase``

``class WrongParamError``
~~~~~~~~~~~~~~~~~~~~~~~~~

``class DataBase``
~~~~~~~~~~~~~~~~~~

``Attribute connection``
~~~~~~~~~~~~~~~~~~~~~~~~

``Attribute cursor``
~~~~~~~~~~~~~~~~~~~~

``def autocommit(state = True) -> bool``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def close() -> bool``
~~~~~~~~~~~~~~~~~~~~~~~

``def commit() -> bool``
~~~~~~~~~~~~~~~~~~~~~~~~

``def reset()``
~~~~~~~~~~~~~~~

``def isClosed() -> int``
~~~~~~~~~~~~~~~~~~~~~~~~~

``def __getCursor__() -> pg.cursor | sqlt.Cursor``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def getAutocommit()``
~~~~~~~~~~~~~~~~~~~~~~~

``def cancel() -> None``
~~~~~~~~~~~~~~~~~~~~~~~~

``def getTransactionStatus()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``class Table``
~~~~~~~~~~~~~~~

``def fetchAll(param = None, where = None) -> list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def fetchMany(param = None, where = None) -> list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def fetchOne(param = None, where = None) -> tuple``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def insert() -> DataBase``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``def update() -> DataBase``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
