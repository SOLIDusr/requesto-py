import psycopg2 as pg
import sqlite3 as sqlt


class DataBase:
    def __init__(self, connection):
        self.connection: DataBase.Connection = DataBase.Connection(connection)
        self.cursor: pg.cursor | sqlt.Cursor = self.connection.getCursor()

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
        def __init__(self, name: str, databaseObject: DataBase):
            self.__databaseObject = databaseObject
            self.__name = name

        def test(self):
            return self.__databaseObject.cursor.execute(f"SELECT * FROM {self.__name}").fetchall()

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

    db = DataBase(connection)
    return db


def sqliteConnection(ifMemory: bool = False, filename: str = None) -> DataBase:
    if filename is not None:
        connection = sqlt.connect(f"{filename}")
        db = DataBase(connection)
        return db

    elif ifMemory:
        connection = sqlt.connect(":memory:")
        db = DataBase(connection)
        return db

    else:
        raise DataBase.WrongParamError
