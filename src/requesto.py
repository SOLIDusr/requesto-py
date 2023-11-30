import psycopg2 as pg
import sqlite3 as sqlt
import traceback
import warnings
import psycopg2.errors as pgerr


class DataBase:
    def __init__(self, connection, dbtype: str = None):
        self.connection: DataBase.Connection = DataBase.Connection(connection)
        self.cursor: pg.cursor | sqlt.Cursor = self.connection.__getCursor__()
        # self.dbtype = dbtype

    # def createTable(self, name: str | None = None, columns: dict | None = None):
    #     __cursor = self.cursor
    #     __row = ""
    #
    #     def parceType(type: str = None) -> str:
    #         if self.dbtype == "sqlite3":
    #             match type:
    #                 case "str":
    #                     return "TEXT"
    #                 case "int":
    #                     return "INTEGER"
    #                 case "float":
    #                     return "REAL"
    #                 case "date":
    #                     return "NUMERIC"
    #         else:
    #             match type:
    #                 case "str":
    #                     return "VARCHAR(256)"
    #     for column in columns:
    #         __row += "\n     "
    #         __row += column
    #         __row += " "
    #         __row += columns.get(column)
    #         __row += ","
    #     __row = __row[:-1]
    #
    #     __cursor.execute(f"""
    #     CREATE TABLE IF NOT EXISTS {name} ({__row}
    #     );
    #     """)
    #     return self.Table(name, self)

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

        def __getCursor__(self):
            return self.connection.cursor()

        def getAutocommit(self):
            return self.connection.autocommit

        def cancel(self):
            return self.connection.cancel()

        def GetTrStatus(self):
            return self.connection.get_transaction_status()

        def getTransactionStatus(self):
            return self.connection.get_transaction_status()

    class Table:
        def __init__(self, name: str, cursor):
            self.__cursor: pg.cursor | sqlt.Cursor = cursor
            self.__name = name

        def fetchAll(self, param: str = None, params: str = None) -> list:
            try:
                if param is None and params is None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name}""")
                elif param is not None and params is None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name}""")
                elif param is None and params is not None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                elif param is not None and params is not None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE """ + params)
                else:
                    raise DataBase.WrongParamError
                return self.__cursor.fetchall()
            except AttributeError as AE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

            except DataBase.WrongParamError as WPE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchMany(self, param: str | None = None, params: str | None = None, size: int | None = 0) -> list:
            try:
                assert size is not None and size > 0
                if param is None and params is None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name}""")
                elif param is not None and params is None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name}""")
                elif param is None and params is not None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                elif param is not None and params is not None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE """ + params)
                else:
                    raise DataBase.WrongParamError
                return self.__cursor.fetchmany(size)
            except AttributeError as AE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []
            except DataBase.WrongParamError as WPE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []
            except AssertionError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []
            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchOne(self, param: str | None = None, params: str | None = None) -> tuple:
            try:
                if param is None and params is None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name}""")
                elif param is not None and params is None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name}""")
                elif param is None and params is not None:
                    self.__cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + params)
                elif param is not None and params is not None:
                    self.__cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE """ + params)
                else:
                    raise DataBase.WrongParamError
                return self.__cursor.fetchone()
            except AttributeError as AE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()
            except DataBase.WrongParamError as WPE:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()
            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()

        def insert(self, params: str | None = None, values: str | None = None) -> bool:
            try:
                assert params is not None
                assert values is not None
                request = f"""INSERT INTO {self.__name} ({params}) VALUES ({values})"""
                self.__cursor.execute(request)
                return True
            except pgerr.UniqueViolation as UV:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
            
        def update(self, params: str | None = None, values: str | None = None, where: str | None = None) -> bool:
            try:
                assert params is not None and values is not None
                if where is None:
                    request = f"""UPDATE {self.__name} SET ({params}) = ({values})"""
                else:
                    request = f"""UPDATE {self.__name} SET ({params}) = ({values}) WHERE {where}"""
                if params.count(",") == 0:
                    request = request.replace("(", "")
                    request = request.replace(")", "")
                self.__cursor.execute(request)
                return True
            except AssertionError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
            except pgerr.Error:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
            except pgerr.UniqueViolation:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
            except Exception:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
    class WrongParamError(Exception):
        pass


def postgresqlConnect(host, port, dbName, userName) -> DataBase:
    userPass: str = input(f"Input Database password\n"
                          f"{userName}@{host}({dbName})$")
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
