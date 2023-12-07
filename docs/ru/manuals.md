# Справочник по модулю

## Справка по версии модуля

---

Есть два способа вывести версию библиотеки. [Здесь](./versions) описан принцип изменения версий

```python
requesto.version_info
```
"Named tuple" аналогичный `sys.version_info`.

Как и в случае с `sys.version_info`, допустимыми значениями уровня выпуска являются «alpha», «beta», 
«candidate» и «final».

```python
requesto.__version__
```

Строковое представление версии. Например '1.0.0rc1'. Это основано на PEP 440.

## requesto

---

Методы:

- [`def` `postgresqlConnect`](#postgresqlConnect)
- [`def` `sqliteConnect`](#sqliteConnect)


## DataBase

---

`class requesto.DataBase(connection)`

- [`class` `Connection`](#Connection)
- [`class` `Table`](#Table)
- [`class` `WrongParamError`](#WrongParamError)
- [`Attribute` `connection: DataBase.Connection`](#connection)
- [`Attribute` `cursor: psycopg2.cursor | sqlite3.Cursor`](#cursor)


## Connection

---

- [`def` `autocommit`](#autocommit)
- [`def` `close`](#close)
- [`def` `commit`](#commit)
- [`def` `reset`](#reset)
- [`def` `isClosed`](#isClosed)
- [`def` `__getCursor__`](#__getCursor__)
- [`def` `getAutocommit`](#getAutocommit)
- [`def` `cancel`](#cancel)
- [`def` `getTransactionStatus`](#getTransactionStatus)








