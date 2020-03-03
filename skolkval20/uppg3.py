from string import ascii_uppercase
from itertools import product
antalburar = int(input())
antaldjurarter = int(input())
antalbråkigagrupper = int(input())
bråkiga = {}
temp = []
burar = []

for num in range(antalbråkigagrupper):
    temp = [character for character in input()]
    bråkiga[num] = temp
    temp = []

if antalbråkigagrupper == 0:
    print(antaldjurarter * (antaldjurarter-1) ** (antalburar-1))

'''
letters = [char for char in ascii_uppercase]
grannar = {}
for n in range(antaldjurarter):
    grannar[letters[n]] = []
for n in range(antaldjurarter):
    temp = []
    for num in range(antaldjurarter):
        if num != letters[num] and num not in bråkiga[n]:
            temp.append(letters[num])
    grannar[letters[n]] = temp

print(grannar)
'''
letters = [char for char in ascii_uppercase[:antaldjurarter]]
possibilities = list(product(letters, repeat=antaldjurarter))

#print(possibilities)

for n in range(antaldjurarter-1):
    for tupl in possibilities:
        if tupl[n] == tupl[n+1]:
            possibilities.remove(tupl)

print(possibilities)