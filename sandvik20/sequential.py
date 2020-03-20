# machines, items = [int(x) for x in input().split()]
# times = [int(x) for x in input().split()][::-1]
# mellan = int(input())
# print(sum(times)+(max(times)*(items-1)))


'''
bottleneckindex = times.index(max(times))
tbottleneck = times[bottleneckindex]*items
tinnan = sum(times[:bottleneckindex])
tefter = sum(times[bottleneckindex+1:])
t = tbottleneck + tinnan + tefter
print(t)
'''
'''
timereq = times[-1]*items
pos = machines
while pos != 0:
    totaltime2 = times[pos]*items
    totaltime1 = times[pos-1]*items
    diff = totaltime2-totaltime1
    if diff >= 0:
        timereq += times[pos-1]
        pos -= 1
        continue
    elif -1*(diff) <= mellan:
        timereq += -1*(diff)
        pos -= 1
        continue
    else:
        timereq += -1*(diff)
        pos -= 1
        continue
print(timereq)
'''
'''
currentmax = times[0] * items
for t in range(machines):
    tid1 = times[t]
    tid2 = times[t+1]
    if tid1 <= tid2:
        platsersombehövs = 0
        currentmax += times[t+1]
        continue
    else: 
        if int(mellan/(tid1-tid2))+1 <= mellan:
            currentmax += times[t+1]
            currentmax += times[t]*(int(mellan/(tid1-tid2))+1)
            #finns tillräckligt med space, behöver bara lägga ut den
        else:
            currentmax += times[t+1]
            currentmax += mellan*times[t]
            currentmax += ((int(mellan/(tid1-tid2))+1)-mellan)*(times[t+1]-times[t])
            pass
            #behöver vänta
print(currentmax)
'''

l1 = [int(x) for x in input().split()]
N = l1[0]
P = l1[1]
T = [int(x) for x in input().split()]
inputarea = int(input())
tottid = 0
maxt = 0
for n in T:
    tottid += n
    maxt = max(maxt, n)
tottid += ((maxt*P)-maxt)
print(tottid)