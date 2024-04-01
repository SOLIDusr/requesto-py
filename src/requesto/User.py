class User:
    def __init__(self, host, port, username, dbName):
        self.host = host
        self.port = port
        self.username = username
        self.dbName = dbName
        self.password: str = input(f"Input Database password {username}@{host}({dbName})$ ")
