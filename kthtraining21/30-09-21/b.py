n = int(input())
inp = input().split()
makessense = True
for i, val in enumerate(inp, start=1):
    try:
        a = int(val)
        if i != a:
            makessense = False
            break
    except:
        pass
if makessense:
    print("makes sense")
else:
    print("something is fishy")