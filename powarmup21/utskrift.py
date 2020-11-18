width = int(input())
numwords = int(input())
words = []
for _ in range(numwords):
    words.append(input())

def solveprint(p, n): 
    k = 0
    if p[n] == 1: 
        k = 1
    else: 
        k = solveprint(p, p[n] - 1) + 1
    print(*words[p[n]-1:n])
    return k 

offby = [[0 for _ in range(numwords + 1)] for _ in range(numwords + 1)]
linecost = [[0 for _ in range(numwords + 1)] for _ in range(numwords + 1)]
cost = [float("inf") for _ in range(numwords + 1)]
p = [0 for _ in range(numwords + 1)]
lengthofwordi = [len(k) for k in words]
# print(lengthofwordi)

for i in range(numwords + 1):
    offby[i][i] = width - lengthofwordi[i-1]
    linecost[i][i] = abs(width - lengthofwordi[i-1])
    for j in range(i + 1, numwords + 1):
        offby[i][j] = offby[i][j-1] - lengthofwordi[j-1] - 1
        linecost[i][j] = abs(offby[i][j])

# for line in linecost:
#     print(line)

cost[0] = 0
for j in range(1, numwords+1):
    for i in range(1, j+1):
        if cost[i-1] != float("inf") and linecost[i][j] != float("inf") and cost[i-1] + linecost[i][j] < cost[j]:
            cost[j] = cost[i-1] + linecost[i][j]
            p[j] = i
# print()
# print(cost)
# print(p)

solveprint(p, numwords)

# for j in range(numwords, 1, -1):
#     for i in range(numwords, j, -1):
#         if i == j:
#             cost[j] = linecost[i][j]
#             p[j] = i
#         else:
#             cost[j] = linecost[i][j]
#             p[j] = i
# print(cost)
# # for line in linecost:
# #     print(linecost)
# for row in range(numwords, 0, -1):
#     for col in range(row, numwords+1):
#         print(linecost[row][col])

# Tushar   
# Roy likes
# to code  
#
# cost[i] = lincost[i][j] + cost[i-1]
# alts:
# tushar + nåt eqiv 3 + nåt (roy och framåt)
# tushar roy + nåt equiv 1 + nåt (likes och framåt)
# tushar roy likes + nåt equiv 7 + nåt (to och framåt)
# tushar roy likes to + nåt equiv 10 + nåt (code och framåt)
# tushar roy likes to code + nåt equiv 15 + nåt (inget)
#---
# roy + nåt equiv 6 + nåt (likes och framåt)
# roy likes + nåt equiv 0 + nåt (to och framåt)
# roy likes to + nåt equiv 3 + nåt (code och framåt)
# roy likes to code + nåt equiv 8 + nåt (inget)
#---
# likes + nåt equiv 4 + nåt (to och framåt)
# likes to + nåt equiv 1 + nåt (code och framåt)
# likes to code + nåt equiv 4 + nåt (inget)
#---
# to + nåt equiv 7 + nåt (code och framåt)
# to code + nåt equiv 2 + nåt (inget)
#---
# code + nåt equiv 5 + nåt (inget)