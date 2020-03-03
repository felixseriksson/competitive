nums = int(input())
lista = []
for n in range(nums):
    lista.append(int(input()))
#print(lista)
maxdist = float("inf")
for el in range(nums):
    maxdist = min(maxdist, lista[el]+lista[(el-2)%nums])
print(maxdist)