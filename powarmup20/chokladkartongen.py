obs = int(input())
observationer = list(input().split())
observationer = list(map(int, observationer))
#print(observationer)
counter = 0

for n in range(obs-1):
    if observationer[n] < observationer[n+1]:
        counter += 1

print(counter)