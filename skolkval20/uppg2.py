påsar = int(input()) # läs in antalet tepåsar
personer = int(input()) # läs in antalet personer
räckertill = []
tiotal = []
rester = []
kannor = 0
personerkvar = 0
for n in range(påsar):
    räckertill.append(int(input()))

for val in räckertill:
    tiotal.append(val - (val % 10))
    rester.append(val % 10)

summatiotal  = sum(tiotal)

kannor = summatiotal / 10

if summatiotal > personer:
        print(int(((personer - (personer % 10)) / 10 + 1)))
else:
    personerkvar = personer - summatiotal
    rester.sort(reverse=True)
    for n in rester:
        personerkvar -= n
        kannor += 1
        if personerkvar <= 0:
            break

print(int(kannor))