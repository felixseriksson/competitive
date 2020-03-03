summa = 0
num = 1
stenar = [] # stenar[n] ger antal stenar som behövs för att bygga en index+1 hög pyramid 
            # ex. stenar[3] stenar behövs för en 4 hög pyramid

while summa <= 100000000:
    summa += num**2
    stenar.append(summa)
    num += 2

antalstenar = int(input())
for n in range(len(stenar)):
    if antalstenar >= stenar[n] and antalstenar < stenar[n+1]:
        print(n+1)
'''
#OEIS: A000447 (alternativ)
stenar = []
n = 1
while n*(4*n**2-1)/3 < 100000000:
    stenar.append(n*(4*n**2-1)/3)
    n += 1

antalstenar = int(input())
for n in range(len(stenar)):
    if antalstenar >= stenar[n] and antalstenar < stenar[n+1]:
        print(n+1)
'''