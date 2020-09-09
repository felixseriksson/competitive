'''
sources = int(input())
l = [int(x) for x in input().split()]
while l[-1] >= 0:
    del l[-1]
print(-1*sum(l))
'''
sources = int(input())
l = [int(x) for x in input().split()]
mana = 0
while True:
    try:
        if l[-1] >= 0:
            l.pop(-1)
        else:
            break
    except:
        break
while l:
    mana = max(mana - int(l.pop(-1)), 0)
    # mana = mana - int(l.pop(-1))
print(mana)
