from abc import ABC, abstractmethod


class InvaildOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvaildOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvaildOperationError("stream is already closed")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data form a Netowork")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")


stream = MemoryStream()
stream.open()
