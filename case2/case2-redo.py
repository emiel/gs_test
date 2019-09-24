# -*- encoding: utf-8 -*-
"""
Write a generator class that yields 4 lines (separated by ‘\n’) from a file,
every time it is called. (max 15 lines)
"""


class ReadN:
    def __init__(self, file, n=4):
        self.file = file
        self.n = 4

    def __iter__(self):
        while True:
            yield "\n".join([next(self.file) for _ in range(self.n)])


if __name__ == "__main__":

    with open("example.txt") as file:
        for buf in ReadN(file):
            print("--")
            print(buf)
