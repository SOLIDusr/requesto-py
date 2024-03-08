from .requesto import DataBase
from .User import User

try:
    import psycopg2 as pg
except ImportError:
    from warnings import warn

    warn("Failed to import psycopg2")
    exit(-1)


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
        else:
            userPass: str = input(f"Input Database password\n"
                                  f"{userName}@{host}({dbName})$ ")
            connection = pg.connect(
                host=host,
                user=userName,
                password=userPass,
                database=dbName,
                port=port)

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

        def createTable(self, tableName, schemaName):
            self.connection.cursor().execute(f"CREATE TABLE IF NOT EXISTS {tableName}("
                                             f""
                                             f")")
