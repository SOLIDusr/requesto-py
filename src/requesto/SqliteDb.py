from .requesto import _DataBase, User
import sqlite3 as sqlt


class SqliteDb(_DataBase):
    def __init__(self,ifMemory: bool = False, filename = None,
                 schemaName="main", autoParce: bool = False):
        if filename is not None:
            connect = sqlt.connect(f"{filename}")
        elif ifMemory:
            connect = sqlt.connect(":memory:")
        else:
            raise _DataBase.WrongParamError
        self.connect = connect
        super().__init__(schemaName=schemaName, connect=self.connect)
        self.tables = []
        self.__schemaName = schemaName
        if autoParce is True:
            self.tables = [_DataBase.Table(table.name, cursor=self.cursor, schemaName=schemaName) for
                           table in self.__getTables()]

    def __str__(self):
        return f"{self.__schemaName}@database"

    def __getTables(self) -> list:
        self.cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table'""")
        listOfTables = [self.Table(tableName[0], self.cursor, self.__schemaName) for tableName in self.cursor.fetchall()
                        if tableName != ""]
        return listOfTables

    class Table(_DataBase.Table):
        def __init__(self, name, cursor, schemaName: str = "main"):
            super().__init__(name, cursor, schemaName)
            self.name = name
            self.__cursor = cursor
            self.__schemaName = schemaName
            self.columns = self.__getColumns()

        def __getColumns(self):
            self.__cursor.execute(f"""Select * FROM {self.name} LIMIT 0""")
            columnNames = [desc[0] for desc in self.__cursor.description]
            return columnNames
