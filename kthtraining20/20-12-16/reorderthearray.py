from collections import Counter
length = int(input())
ls = [int(k) for k in input().split()]
mx = max(Counter(ls).values())
print(length - mx)