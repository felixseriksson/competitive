# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:56:54 2020

@author: felix
"""
from math import floor

rads = int(input())
lista = [int(x) for x in input().split()]
inrangelist = []
summa = 0

def gethousesinrange(radius):
    points = 0
    for h in range(radius):
        points += floor(((radius**2)-(h**2))**0.5)
    return 4*points + 1

    # number = 0
    # width = radius
    # height = 0
    # while width != 0:
    #     number += width
    #     if ((width**2)+(height**2))**0.5 <= radius:
    #         height += 1
    #         continue
    #     else:
    #         height += 1
    #         width -= 1
    #         continue
    # return (number*4)-4*radius + 1

minrest5 = float("inf")
minrest1 = []

for n in lista:
    temp = gethousesinrange(n)
    inrangelist.append(temp)
    summa += temp
    temprest = temp % 8
    if temprest == 1:
        if len(minrest1) == 7:
            for index in range(len(minrest1)):
                if temp < minrest1[index]:
                    minrest1[index] = temp
                    break
        elif len(minrest1) < 7:
            minrest1.append(temp)
        minrest1.sort()
    else:
        minrest5 = min(minrest5, temp)

rest = summa % 8

restlist = []
for n in inrangelist:
    restlist.append(n % 8)

for n in range(7-len(minrest1)):
    minrest1.append(float("inf"))

toremove = 0
if rest == 0:
    toremove = 0
elif rest < 5:
    toremove = sum(minrest1[:rest])
else:
    toremove = min(sum(minrest1[:rest]), minrest5 + sum(minrest1[:(rest-5)]))

print(toremove)

# print(lista)
# print(inrangelist)
# print(summa)
# print(rest)
# print(minrest1)
# print(minrest5)
# print(restlist)
# print("needs to remove at least", toremove)