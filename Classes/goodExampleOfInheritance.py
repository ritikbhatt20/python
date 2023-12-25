class InvalidInputError(Exception):   #created custon exception
    pass

class Stream:
    def __init__(self):
        self.opened = True

    def open(self):
        if self.opened:
            raise InvalidInputError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidInputError("Stream is already closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


f = FileStream()
f.read()