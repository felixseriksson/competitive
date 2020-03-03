N, M, K = [int(x) for x in input().split()]
kanter = []
for n in range(N-1):
    kanter.append([int(x) for x in input().split()])

if K + M -1 <= N:
    string = ""
    for n in range(K, K+M):
        string += str(n) + " "
    string = string[:-1]
    print(string)
elif K - M >= 0:
    #sätt fåglar nedåt
    string = ""
    for n in sorted(list(range(K-M+1, K+1)), reverse=True):
        string += str(n)+ " "
    print(string)
else:
    print(-1)