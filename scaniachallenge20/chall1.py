import itertools
print(max([eval("1{}2{}3{}4{}5".format(*c)) for c in itertools.permutations(["+", "-", "/", "*"], 4)]))