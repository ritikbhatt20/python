from abc import ABC, abstractmethod

class InvalidInputError(Exception):   #created custon exception
    pass

class Stream(ABC):     #made this stream class abstract by inheriting it with AbstractBaseClass
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

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class memoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

stream = memoryStream()
# whenever a class has any abstract method or it is abstract, then we cannot instantiate it 