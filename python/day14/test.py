from collections import defaultdict

foo = defaultdict(int)
foo["hoi"] = "doei"

def lol(dict):
    dict["foo"] = "bar"

print(foo)
lol(foo)
print(foo)