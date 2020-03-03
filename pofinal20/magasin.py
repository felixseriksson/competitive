björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
vaken = []
for n in range(björnar):
    d, m = [int(x) for x in input().split("/")]
    indexdag = dagarmånad[m-1]+d
    if n == 0:
        offset = 0#(indexdag+dagaride)
        vaken.append([indexdag + dagaride, indexdag + 364])
        continue
    #(första dag i tjänst, sista dag i tjänst)
    start = (indexdag+dagaride)
    end = indexdag + 365 
    vaken.append([start - offset-1, end - offset-1])
    # if start < end:
    #     vaken.append([(start-offset)%365, (end-offset)%365])
    # elif start > end:
    #     vaken.append([(start-offset)%365, (end-offset)%365+365])
    
#print(vaken)
starttuple = vaken.pop(0)
vaken = sorted(vaken, key= lambda x: x[0])
# for elementindex in range(len(vaken)):
#     if vaken[elementindex][0] < starttuple[0]:
#         temp = vaken[elementindex].copy()
#         temp[0] += 365
#         temp[1] += 365
#         vaken.append(temp)
#     elif vaken[elementindex][0] >= starttuple[0]:
#         del vaken[:elementindex]
#         break
#print(vaken)

def findsubintervalls(intervalls, currenttuple): #lista av tuples
    current = currenttuple[0]
    goal = current + 365
    counter = 0
    while True:
        endpoint = currenttuple[1]
        potential = [0,0]
        for subintervall in intervalls:
            if subintervall[0] <= endpoint:
                if subintervall[1] > potential[1]:
                    potential = subintervall
                else:
                    pass
            else:
                break
        counter += 1
        if potential[1] >= goal:
            break
        try:
            del intervalls[:intervalls.index(potential)+1]
        except:
            return -1
        currenttuple = potential
    return counter

print(findsubintervalls(vaken, starttuple))