from case5 import Pair, _ndiff

assert _ndiff("AAAAAAAA", "AAAAAAAA") == 0
assert _ndiff("AAAAAAAA", "BAAAAAAA") == 1
assert _ndiff("AAAAAAAA", "BBAAAAAA") == 2
assert _ndiff("AAAAAAAA", "BBBBBBBB") == 8

assert Pair("AAAAAAAA", "BBBBBBBB") == Pair("AAAAAAAA", "BBBBBBBB")
assert Pair("AAAAAAAA", "ABBBBBBB") == Pair("AAAAAAAA", "BBBBBBBB")
assert Pair("BAAAAAAA", "BBBBBBBB") == Pair("AAAAAAAA", "BBBBBBBB")
