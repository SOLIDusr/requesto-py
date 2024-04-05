import sqlite3 as sqlt
from .requesto import DataBase
from .User import User
from .Exceptions import *

class SqliteDb(DataBase):
    def __init__(self, connection, schemaName="main"):
        super().__init__(connection, schemaName=schemaName)
        self.__schemaName = schemaName
        self.tables = self.__getTables()

    def __getTables(self) -> list:
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [self.Table(tableName[0], self.cursor, self.__schemaName) for tableName in self.cursor.fetchall()]

    class Connection(DataBase.Connection):
        def __init__(self, connection):
            super().__init__(connection)

    class Table(DataBase.Table):

        def __init__(self, name: str, cursor, schemaName: str = "main"):
            super().__init__(name=name, cursor=cursor, schemaName=schemaName)
            self.__cursor = cursor
            self.__name = name

        def __getColumns(self):
            self.__cursor.execute(f"""Select * FROM {self.__name} LIMIT 0""")
            columnNames = [desc[0] for desc in self.__cursor.description]
            return columnNames
