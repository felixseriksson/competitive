def solve_equations(AM, BM):
    for fd in range(len(AM)):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(len(AM)):
            AM[fd][j] *= fdScaler
        BM[fd][0] *= fdScaler
        for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd+1:]:
            crScaler = AM[i][fd]
            for j in range(len(AM)):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
    return BM

n, k, p = input().split()
n, k, p = int(n), int(k), float(p)
a = [[0 for _ in range(2**n)] for _ in range(2**n)]
b = [[0] for _ in range(2**n)]
for i in range(2**n):
    if len([1 for a in str(bin(i)) if a == "1"]) >= k:
        b[i][0] = 0
        a[i][i] = 1
    else:
        otherpart = i%(2**(n-1))
        pval = otherpart*2 + 1
        oneminuspval = otherpart*2
        b[i][0] = -1
        a[i][pval] += p
        a[i][oneminuspval] += 1-p
        a[i][i] += -1

print(solve_equations(a, b)[0][0])