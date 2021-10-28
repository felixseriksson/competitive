from math import ceil
h, p = [int(x) for x in input().split()]
ki, kl = (60*h*p)/100000, (11*h*p)/100000
i = 1
while True:
    if ki*i + 5*ceil(i*h/1000) <= kl*i + 60*ceil(i*h/8000):
        i+= 1
    else:
        print(i)
        exit()