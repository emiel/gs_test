from case4 import cd


assert cd("/foo", "bar") == "/foo/bar"
assert cd("/foo", "./bar") == "/foo/bar"
assert cd("/foo", "../bar") == "/bar"
assert cd("/", "../bar") == "/bar"
assert cd("/foo/bar", "../../qux") == "/qux"
