# -*- encoding: utf-8 -*-
"""
Write a generator class that yields 4 lines (separated by ‘\n’) from a file,
every time it is called. (max 15 lines)
"""


# class NLiner:
#     """Class w/ iterator protocol"""

#     def __init__(self, file):
#         self.file = file

#     def __iter__(self):
#         return self

#     def __next__(self):
#         lines = "\n".join([next(self.file) for i in range(4)])
#         return lines


def nliner_ori(filename, n=4):
    """generator function"""
    with open(filename) as file:
        yield "\n".join([next(file) for i in range(n)])


def nliner(filename, n=4):
    """generator function"""
    with open(filename) as file:
        buf = []
        for i, line in enumerate(file, start=1):
            buf.append(line)
            if i % n == 0:
                yield "\n".join(buf)
                buf = []


class NLinerCallable:
    """Callable instance w/ generator function"""

    def __init__(self, file, n=4):
        self.file = file
        self.n = n

    def __call__(self):
        yield "\n".join([next(self.file) for i in range(self.n)])
