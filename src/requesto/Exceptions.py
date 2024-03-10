class ConnectionDetailsMissingException(Exception):
    def __init__(self):
        super().__init__("No connection details provided!")
