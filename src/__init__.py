import time
from urllib import request, error
import os


def connectionTest():
    try:
        request.urlopen('http://google.com', timeout=1)
    except Exception:
        import warnings

        warnings.warn(
            "Seems like there's no internet connection."
            " 'http://google.com' cannot be pinged."
            " App will continue to run without connection, but some functions may be missing.",
        )


def configTest() -> None:
    if not (os.path.isfile("dbCfg.py")):
        import warnings

        warnings.warn(
            "Seems like there's no database config file. "
            "Close the app and create 'dbCfg.py' or do it right below. "
            "Type 'None' in host to proceed without cfg file.(Exception expected)",
            DeprecationWarning,
            stacklevel=2,
        )
        with open("dbCfg.py", "w") as databaseFile:
            time.sleep(2)
            host = input("Database host:\n")
            if host.lower() == "none":
                return None
            port = input("Database port:\n")
            dbName = input("Database name:\n")
            userName = input("Database user name:\n")
            content = f'host = "{host}"\nport = "{port}"\ndbName = "{dbName}"\nuserName = "{userName}"'
            databaseFile.write(content)
            databaseFile.close()
            return None
    return None


connectionTest()
configTest()
