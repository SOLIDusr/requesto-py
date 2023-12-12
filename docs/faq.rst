Frequently asked questions
==========================

Contents
--------

-  `Basics <./#Basics>`__

   -  `Initialization <./#Initialization>`__

   -  `Database object <./#Database%20object>`__

   -  `Table object <./#Table%20object>`__

Basics
======

Initialization
--------------

In older (pre-release) versions you could initialize database object by creating Database object,
but now you can use one of


.. code-block:: python

    rq.sqliteConnect()

or

.. code-block:: python

    rq.postgresqlConnect()


Table object
------------

You can create Table object through
`db.Table(name) <manuals.md/#>`__ or
`rq.postgresqlConnection() <manuals.md/#postgresqlConnection>`__

Table object used for controlling data in the table through methods
``fetchAll`` , ``fetchMany``, ``fetchOne`` , ``insert``, ``update``


