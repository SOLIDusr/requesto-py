import psycopg2 as pg
import sqlite3 as sqlt


class DataBase:
    def __init__(self, connection, dbtype: str = None):
        self.connection: DataBase.Connection = DataBase.Connection(connection)
        self.cursor: pg.cursor | sqlt.Cursor = self.connection.getCursor()
        self.dbtype = dbtype

    def createTable(self, name: str | None = None, columns: dict | None = None):
        __cursor = self.cursor
        __row = ""

        def parceType(type: str = None) -> str:
            if self.dbtype == "sqlite3":
                match type:
                    case "str":
                        return "TEXT"
                    case "int":
                        return "INTEGER"
                    case "float":
                        return "REAL"
                    case "date":
                        return "NUMERIC"
            else:
                match type:
                    case ""
        for column in columns:
            __row += "\n     "
            __row += column
            __row += " "
            __row += columns.get(column)
            __row += ","
        __row = __row[:-1]

        __cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {name} ({__row}
        );
        """)
        return self.Table(name, self)

    class Connection:

        def __init__(self, connection):
            self.connection: pg.connection | sqlt.Connection = connection

        def autocommit(self, state: bool = True) -> bool:
            self.connection.autocommit = state
            return state

        def close(self) -> bool:
            try:
                self.connection.close()
                return True
            except AttributeError:
                return False

        def commit(self) -> bool:
            try:
                self.connection.commit()
                return True
            except AttributeError:
                return False

        def reset(self) -> bool:
            self.connection.reset()
            return True

        def isClosed(self) -> int:
            return self.connection.closed

        def getCursor(self):
            return self.connection.cursor()

        def getAutocommit(self):
            return self.connection.autocommit

        def cancel(self):
            return self.connection.cancel()

        def GetTrStatus(self):
            return self.connection.get_transaction_status()

    class Table:

        def __init__(self, name: str, databaseObject):
            self.__databaseObject: DataBase = databaseObject
            self.__name = name

        def fetchAll(self, param: str = None, params: str = None) -> list:
            if param is None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name}""").fetchall()
            elif param is not None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name}""").fetchall()
            elif param is None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                        .fetchall())
            elif param is not None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE""" + params)
                        .fetchall())
            else:
                raise DataBase.WrongParamError

        def fetchMany(self, param: str | None = None, params: str | None = None, size: int | None = 0) -> list:
            if param is None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name}""").fetchmany(size)
            elif param is not None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name}""").fetchmany(size)
            elif param is None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                        .fetchmany(size))
            elif param is not None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE""" + params)
                        .fetchmany(size))
            else:
                raise DataBase.WrongParamError

        def fetchOne(self, param: str | None = None, params: str | None = None) -> tuple:
            if param is None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name}""").fetchone()
            elif param is not None and params is None:
                return self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name}""").fetchone()
            elif param is None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                        .fetchone())
            elif param is not None and params is not None:
                return (self.__databaseObject.cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE""" + params)
                        .fetchone())
            else:
                raise DataBase.WrongParamError

        def insert(self, params: str | None = None, values: str | None = None):
            assert params is not None
            assert values is not None
            return self.__databaseObject.cursor.execute(f"""INSERT INTO {self.__name} ({params}) VALUES {values}""")

    class WrongParamError(Exception):
        pass


def postgresqlConnect(host, port, dbName, userName) -> DataBase:
    userPass: str = input("Enter database password\n>")
    connection = pg.connect(
        host=host,
        user=userName,
        password=userPass,
        database=dbName,
        port=port)

    db = DataBase(connection, "psql")
    return db


def sqliteConnection(ifMemory: bool = False, filename: str = None) -> DataBase:
    if filename is not None:
        connection = sqlt.connect(f"{filename}")
        db = DataBase(connection, "sqlite3")
        return db

    elif ifMemory:
        connection = sqlt.connect(":memory:")
        db = DataBase(connection, "sqlite3")
        return db

    else:
        raise DataBase.WrongParamError
