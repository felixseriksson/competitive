n = int(input())
p = [int(x) for x in input().split()]
c = 0
for i in range(1, n+1):
    for j in range(1, i):
        if p[i-1] < p[j-1]:
            c += 1
            c %= 2

for _ in range(int(input())):
    q = [int(x) for x in input().split()]
    l = q[1]-q[0]
    c += l*(l+1)/2
    c %= 2
    if c:
        print("odd")
    else:
        print("even")