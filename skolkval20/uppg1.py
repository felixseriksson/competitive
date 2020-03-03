def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

summa = 0
ö = 0
deltagare = int(input()) #skriv antal deltagare

while summa < deltagare:
    ö += 1
    summa += Fibonacci(ö)

print(ö)