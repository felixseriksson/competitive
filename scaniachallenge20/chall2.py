import itertools
operators = itertools.product("+-", repeat=9)
summ=0
for comb in operators:
    if eval("1{}2{}3{}4{}5{}6{}7{}8{}9{}10".format(*comb)) == 11:
        summ+=1
print(summ)