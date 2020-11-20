# import re
# for _ in range(int(input())):
#     pattern = "".join([k + "+" for k in input()])
#     tosearch = input()
#     try:
#         assert re.match(pattern, tosearch).group() == tosearch
#         print("YES")
#     except:
#         print("NO")
from itertools import groupby
for _ in range(int(input())):
    first = ["".join(g) for k, g in groupby(input())]
    second = ["".join(g) for k, g in groupby(input())]
    if len(first) != len(second):
        print("NO")
        continue
    for f,s in zip(first, second):
        if f[0] != s[0] or len(f) > len(s):
            print("NO")
            break
    else:
        print("YES")