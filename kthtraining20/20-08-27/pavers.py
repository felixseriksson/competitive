n = int(input())
ways = [None]*(n + 1)
tiles = [None]*(n + 1)
ways[0] = 1
ways[1] = 2
tiles[0] = [0, 0, 0]
tiles[1] = [2, 1, 0]
for i in range(2, n+1):
    ways[i] = 7*ways[i-2] + 2*ways[i-1]
    tiles[i] = [(tiles[i-2][0]+8)*ways[i-2] + (tiles[i-1][0]+2)*ways[i-1], (tiles[i-1][1]+1)*ways[i-1], (tiles[i-1][2]+0)*ways[i-1]]

numways = ways[n]
tilesfin  = tiles[n]
tup = [numways, tilesfin[0], tilesfin[1], tilesfin[2]]
string = ""
for k in tup:
    string += str(k) + " "

print(string)