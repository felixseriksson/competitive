n = int(input())
l = set([int(x) for x in input().split()])
ll = set([int(x) for x in input().split()])
print(list(l.difference(ll))[0])