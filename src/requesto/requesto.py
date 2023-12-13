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

import psycopg2 as pg
import sqlite3 as sqlt
import traceback
import warnings
import psycopg2.errors as pgerr


class DataBase:
    """
    DataBase class [:class:`.DataBase`]: Represents the database object.
    """
    def __init__(self, connection):
        self.connection: DataBase.Connection = DataBase.Connection(connection)
        self.cursor: pg.cursor | sqlt.Cursor = self.connection.__getCursor__()
        # self.dbtype = dbtype

    class Connection:

        def __init__(self, connection):
            self.connection: pg.connection | sqlt.Connection = connection

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
            resets database. Represents cursor.reset function
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
        def __init__(self, name: str, cursor):
            self.__cursor: pg.cursor | sqlt.Cursor = cursor
            self.__name = name

        def query(self, request: str = None):
            """
            execute custom query
            :param request: :class:`str` - provided request to proceed
            """
            assert request is not None
            self.__cursor.execute(f"""{request}""")

        def fetchAll(self, param: str = None, where: str = None) -> list:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchall() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:('id = 5')
            """
            try:
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
                return self.__cursor.fetchall()
            except AttributeError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

            except DataBase.WrongParamError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchMany(self, param: str | None = None, where: str | None = None, size: int | None = 0) -> list:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchmany() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:('id = 5')
            :param size: :class:`int` - size of a list to return (0 < size < 8**10)
            """
            try:
                assert size is not None and 8**10 > size > 0
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
            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return []

        def fetchOne(self, param: str | None = None, where: str | None = None) -> tuple:
            """
            Fetches information from the table by specific conditions
            Represents cursor.fetchone() function
            :param param: :class:`str` - given variables' names
            :param where: :class:`str` - condition of inserting. Example:('id = 5')
            """
            try:
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
                return self.__cursor.fetchone()
            except AttributeError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()
            except DataBase.WrongParamError:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return ()
            except pgerr.UndefinedTable or pgerr.UndefinedColumn:
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
            except pgerr.UniqueViolation:
                trace = traceback.format_exc()
                warnings.warn(trace)
                return False
            
        def update(self, params: str | None = None, values: str | None = None, where: str | None = None) -> bool:
            """Updates given variables in the table with given values
            :param params: :class:`str` - given variables' names
            :param values: :class:`str` - values
            :param where: :class:`str` - condition of inserting. Example:('id = 5')
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
    """Adds a field to the embed object.
        This function returns the :class:`DataBase`
        Fancy password input included!
         :param host: :class:`str` Database host
         :param port: :class:`str` Port of the database server
         :param dbName: :class:`str` Name of the database
         :param userName: :class:`str` Username of the database user
         :raises TypeError: :class:`TypeError` : if any argument is not stated
        """
    userPass: str = input(f"Input Database password\n"
                          f"{userName}@{host}({dbName})$")
    connection = pg.connect(
        host=host,
        user=userName,
        password=userPass,
        database=dbName,
        port=port)

    db = DataBase(connection)
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
        db = DataBase(connection)
        return db

    elif ifMemory:
        connection = sqlt.connect(":memory:")
        db = DataBase(connection)
        return db

    else:
        raise DataBase.WrongParamError
