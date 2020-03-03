inputline1 = [int(char) for char in input().split()]
N = inputline1[0]
M = inputline1[1]
temp = [int(char) for char in input().split()]
tider = {}

for n in range(min(M, len(temp))):
    tider[n] = M*(temp.pop(0)-1)+n
if temp != []:
    for n in range(N-M):
        tider[n+M] = M*temp.pop(0)
print(tider)
