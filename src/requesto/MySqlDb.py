from requesto import _DataBase
from mysql.connector import connect, Error


class MySqlDb(_DataBase):
    def __init__(self, connection, schemaName: str = "default", autoParce: bool = False):
        super().__init__(connection, schemaName)
        self.tables = []
        self.__schemaName = schemaName
        if autoParce is True:
            self.tables = [_DataBase.Table(table.name, cursor=self.cursor, schemaName=schemaName) for
                           table in self.__getTables()]

    def __str__(self):
        return f"{self.__schemaName}@database"

    def __getTables(self) -> list:
        self.cursor.execute(f"""SELECT name FROM information_schema.tables WHERE table_schema = '{self.__schemaName}'""")
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
