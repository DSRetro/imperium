class Error(Exception):
    pass

class ArgumentError(Error):
    def __init__(self, message):
        self.message = message
