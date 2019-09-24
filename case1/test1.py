from case1 import RAII

with RAII("example.txt", "r") as file:
    assert file.read() == "foobar\n"


assert file.closed
