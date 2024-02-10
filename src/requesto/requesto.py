"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
try:
    import psycopg2 as pg
except ImportError:
    # pip.main is going to be deleted probably. Might be a problem
    from pip import main

    main(['install', 'psycopg2==2.9.9'])
    import psycopg2 as pg
import sqlite3 as sqlt
import traceback
import warnings

"""
That is a horrible solution right there! Do not even do that in your code.
"""

_cursor_ = pg._psycopg.cursor
_connection_ = pg._psycopg.connection


class DataBase:
    """
    DataBase class [:class:`.DataBase`]: Represents the database object.
    """

    def __init__(self, connection, schemaName: str = "public", dbType: str | None = None):
        self.dbType = dbType
        self.connection: DataBase.Connection = DataBase.Connection(connection)
        self.cursor: _cursor_ | sqlt.Cursor = self.connection.__getCursor__()
        self.__schemaName: str = schemaName
        if dbType == "postgresql":
            self.tables = self.__getTables()

    def __str__(self):
        return f"{self.__schemaName}@database"

    def __getTables(self) -> list:
        self.cursor.execute(f"""SELECT table_name FROM information_schema.tables
               WHERE table_schema = '{self.__schemaName}'""")
        # for tableName in self.cursor.fetchall()[0]:
        #     if tableName == "":
        #         pass
        #     else:
        #         listOfTables.append(self.Table(tableName, cursor=self.cursor))
        listOfTables = [self.Table(tableName[0], self.cursor, self.__schemaName) for tableName in self.cursor.fetchall()
                        if tableName != ""]
        return listOfTables

    class Connection:

        def __init__(self, connection):
            self.connection: _connection_ | sqlt.Connection = connection

        def autocommit(self, state: bool = True) -> bool:
            """
            Changes state of autocommit.
            :returns: :class:`bool` - State of autocommit in program
            """
            self.connection.autocommit = state
            return state

        def close(self) -> bool:
            """
            Closes database connection if not closed.
            :returns: :class:`bool`
            :raises AttributeError: :class:`AttributeError`
            """
            try:
                self.connection.close()
                return True
            except AttributeError:
                return False

        def commit(self) -> bool:
            """
            Commits changes in database. In case of error or in case of cursor is None raises AttributeError
            :returns: :class:`pg.cursor` || :class:`sqlt.Cursor`
            :raises AttributeError: :class:`AttributeError`
            """
            try:
                self.connection.commit()
                return True
            except AttributeError:
                raise AttributeError

        def reset(self):
            """
            resets database. Represents `cursor.reset` function
            :returns: :class:`None`
            """
            self.connection.reset()

        def isClosed(self) -> int:
            """
            returns cursor object
            :returns: :class:`pg.cursor` || :class:`sqlt.Cursor`
            """
            return self.connection.closed

        def __getCursor__(self):
            """
            returns cursor object.
            :returns: :class:`pg.cursor` || :class:`sqlt.Cursor`
            """
            return self.connection.cursor()

        def getAutocommit(self):
            """
            returns current autocommit state.
            :returns: :class:`bool`
            """
            return self.connection.autocommit

        def cancel(self) -> None:
            """
            returns nothing. Cancel() method from cursor
            :returns: :class:`None`
            """
            return self.connection.cancel()

        def getTransactionStatus(self):
            """
            returns transaction status. Basically **cursor.get_transaction.status()** func
            :returns: [:class:`str`] transaction status
            """
            return self.connection.get_transaction_status()

    class Table:
        def __init__(self, name, cursor, schemaName: str = "public"):
            self.__cursor = cursor
            self.__name = name
            self.__schemaName = schemaName
            self.columns = self.__getColumns()

        def __str__(self):
            return self.__schemaName + "@" + "database" + "@" + self.__name

        def __getColumns(self):
            self.__cursor.execute(f"""Select * FROM {self.__name} LIMIT 0""")
            columnNames = [desc[0] for desc in self.__cursor.description]
            return columnNames

        def query(self, request: str = None):
            """
            execute custom query
            :param request: :class:`str` - provided request to proceed
            """
            assert request is not None
            self.__cursor.execute(f"""{request}""")

        def __paramsCheck(self, param, where):
            if param is None and where is None:
                self.__cursor.execute(f"""SELECT * FROM {self.__name}""")
            elif param is not None and where is None:
                self.__cursor.execute(f"""SELECT {param} FROM {self.__name}""")
            elif param is None and where is not None:
                self.__cursor.execute(f"""SELECT * FROM {self.__name} WHERE """ + where)
            elif param is not None and where is not None:
                self.__cursor.execute(f"""SELECT {param} FROM {self.__name} WHERE """ + where)
            else:
                raise DataBase.WrongParamError

        def fetchAll(self, param: str = None, where: str = None) -> list:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchall() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:`('id = 5')`
            """
            try:
                self.__paramsCheck(param, where)
                return self.__cursor.fetchall()
            except AttributeError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

            except DataBase.WrongParamError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchMany(self, param: str | None = None, where: str | None = None, size: int | None = 0) -> list:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchmany() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:`('id = 5')`
            :param size: :class:`int` - size of a list to return (0 < size < 8**10)
            """
            try:
                assert size is not None and 8 ** 10 > size > 0
                self.__paramsCheck(param, where)
                return self.__cursor.fetchmany(size)
            except AttributeError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []
            except DataBase.WrongParamError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []
            except AssertionError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchOne(self, param: str | None = None, where: str | None = None) -> tuple:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchone() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:`('id = 5')`
            """
            try:
                self.__paramsCheck(param, where)
                return self.__cursor.fetchone()
            except AttributeError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()
            except DataBase.WrongParamError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()

        def insert(self, params: str | None = None, values: str | None = None) -> bool:
            """Inserts given variables in the table with given values
                        :param params: :class:`str` - given variables' names
                        :param values: :class:`str` - values
                        """
            try:
                assert params is not None
                assert values is not None
                request = f"""INSERT INTO {self.__name} ({params}) VALUES ({values})"""
                self.__cursor.execute(request)
                return True
            except Exception as e:  # Some shit happened to pg.errors, so I removed it for good.
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False

        def update(self, params: str | None = None, values: str | None = None, where: str | None = None) -> bool:
            """Updates given variables in the table with given values
            :param params: :class:`str` - given variables' names
            :param values: :class:`str` - values
            :param where: :class:`str` - condition of inserting. Example:`('id = 5')`
            """
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

    class WrongParamError(Exception):
        pass


class User:
    def __init__(self, host, port, username, dbName):
        self.host = host
        self.port = port
        self.username = username
        self.dbName = dbName
        self.password: str = input(f"Input Database password {username}@{host}({dbName})$ ")


def postgresqlConnect(user: User = None, host=None, port=None, dbName=None, userName=None,
                      schemaName=None) -> DataBase:
    """Adds a field to the embed object.
        This function returns the :class:`DataBase`
        Fancy password input included!
         :param user: :class:`user.User` User object with data to connect.
         If not provided - defaults to manual data input
         :param host: :class:`str` Database host
         :param port: :class:`str` Port of the database server
         :param dbName: :class:`str` Name of the database
         :param userName: :class:`str` Username of the database user
         :param schemaName: :class:`str` Name of the schema where the user wants to connect to the database
         :raises TypeError: :class:`TypeError` : if any argument is not stated
        """
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

    db = DataBase(connection, schemaName=schemaName, dbType="postgresql")
    return db


def sqliteConnect(ifMemory: bool = False, filename: str = None) -> DataBase | DataBase.WrongParamError:
    """Initializes database object

    This function returns the :class:`DataBase`
    Do not use **ifMemory** with **filename** stated
     :param filename: :class:`str` Filename of the database file
     :param ifMemory: :class:`bool` Make true to launch in RAM mode
     :raises WrongParamError: :class:`DataBase.WrongParamError` if any of the param is wrong
    """
    if filename is not None:
        connection = sqlt.connect(f"{filename}")

    elif ifMemory:
        connection = sqlt.connect(":memory:")

    else:
        raise DataBase.WrongParamError

    db = DataBase(connection, dbType="sqlite3")
    return db
