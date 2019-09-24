from case2 import NLiner, nliner, NLinerCallable


with open("example.txt") as file:
    for line in NLiner("example.txt"):
        print(line)

gen = nliner("example.txt")
print(gen.next())
print(gen.next())

# with open("example.txt") as file:
#     f = NLinerCallable(file)

#     for line in f():
#         print(line)
