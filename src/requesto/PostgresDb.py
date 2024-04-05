from .requesto import DataBase
from .User import User

try:
    import psycopg2 as pg
except ImportError:
    raise ImportError("Psycopg2 is not installed. Please install it using pip.")


class PostgresDb(DataBase):
    def __init__(self, user: User = None, host=None, port=None, dbName=None, userName=None,
                 schemaName="public"):
        if user is not None:
            connection = pg.connect(
                host=user.host,
                user=user.username,
                password=user.password,
                database=user.dbName,
                port=user.port)
        elif user is None and host is not None and port is not None and dbName is not None and userName is not None:
            userPass: str = input(f"Input Database password\n"
                                  f"{userName}@{host}({dbName})$ ")
            connection = pg.connect(
                host=host,
                user=userName,
                password=userPass,
                database=dbName,
                port=port)
        else:
            raise ConnectionDetailsMissingException("Database details were not provided!")

        super().__init__(connection, schemaName=schemaName)
        self.__schemaName = schemaName
        self.tables = self.__getTables()


    def __getTables(self):
        self.cursor.execute(f"""SELECT table_name FROM information_schema.tables
                       WHERE table_schema = '{self.__schemaName}'""")

        listOfTables = [DataBase.Table(tableName[0], self.cursor, self.__schemaName)
                        for tableName in self.cursor.fetchall() if tableName != ""]
        return listOfTables

    class Connection(DataBase.Connection):
        def __init__(self, connection):
            super().__init__(connection)

    class Table(DataBase.Table):

        def __init__(self, name: str, cursor, schemaName: str = "public"):
            super().__init__(name=name, cursor=cursor, schemaName=schemaName)
            self.__cursor = cursor
            self.__name = name

        def __getColumns(self):
            self.__cursor.execute(f"""Select * FROM {self.__name} LIMIT 0""")
            columnNames = [desc[0] for desc in self.__cursor.description]
            return columnNames
