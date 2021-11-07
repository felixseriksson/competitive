d = int(input())
total = 100
prevprice = 100000
for _ in range(d):
    newprice = int(input())
    if newprice > prevprice:
        gain = min(total//prevprice, 100000)*(newprice - prevprice)
        total += gain
    prevprice = newprice
print(total)