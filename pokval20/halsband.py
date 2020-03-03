halsband, startval, maxval = input(), 0, 0
for num in range(int(len(halsband)/2)):
    if halsband[num] == "B": startval +=1
for n in range(len(halsband)):
    if halsband[n] == "B": startval -= 1
    if halsband[(n + int(len(halsband)/2))%len(halsband)] == "B": startval += 1
    maxval = max(maxval, startval)
print(maxval)