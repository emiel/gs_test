"""
Write a Python class that opens a file and automatically closes it after
use, just like in thewith open(filename, ‘r’): statement.(max 15 lines)
"""


class RAII:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()
