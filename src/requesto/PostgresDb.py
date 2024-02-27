from .requesto import _DataBase, User
import psycopg2 as pg


class PostgresDb(_DataBase):
    def __init__(self, user: User = None, host=None, port=None, dbName=None, userName=None,
                 schemaName=None, autoParce: bool = False):
        if user is not None:
            self.connect = pg.connect(
                    host=user.host,
                    user=user.username,
                    password=user.password,
                    database=user.dbName,
                    port=user.port)
        else:
            userPass: str = input(f"Input Database password\n"
                                    f"{userName}@{host}({dbName})$ ")
            self.connect = pg.connect(
                        host=host,
                        user=userName,
                        password=userPass,
                        database=dbName,
                        port=port)
        super().__init__(schemaName, self.connect)
        self.__schemaName = schemaName

        self.tables = []
        if autoParce is True:
            self.tables: list[PostgresDb.Table] = [
                _DataBase.Table(table.name, cursor=self.cursor, schemaName=schemaName) for
                table in self.__getTables()]
        else:
            self.tables = []

    def __str__(self):
        return f"{self.__schemaName}@database"

    def __getTables(self) -> list:
        self.cursor.execute(f"""SELECT table_name FROM information_schema.tables
                WHERE table_schema = '{self.__schemaName}'""")

        listOfTables = [self.Table(tableName[0], self.cursor, self.__schemaName) for tableName in self.cursor.fetchall()
                        if tableName != ""]
        return listOfTables

    class Table(_DataBase.Table):

        def __init__(self, name, cursor, schemaName: str = "public"):
            super().__init__(name, cursor, schemaName)
            self.name = name
            self.__cursor = cursor
            self.__schemaName = schemaName
            self.columns = self.__getColumns()

        def __getColumns(self):
            self.__cursor.execute(f"""Select * FROM {self.name} LIMIT 0""")
            columnNames = [desc[0] for desc in self.__cursor.description]
            return columnNames
