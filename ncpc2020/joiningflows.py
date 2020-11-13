taps = int(input())
flows = sorted([[int(x) for x in input().split()] for _ in range(taps)], key = lambda x: x[0]) # temp, minflow, maxflow sorted by temp, lo to hi

mintiaisum = sum([k[0]*k[1] for k in flows])
minvol, maxvol = sum([k[1] for k in flows]), sum([k[2] for k in flows])
mintemp, maxtemp = min([k[0] for k in flows]), max([k[0] for k in flows])

# print(minvol, maxvol)
# print(mintemp, maxtemp)

def calculatemintoadd(flowleft, flowlist):
    ret = 0
    for flow in flowlist:
        if flowleft >= flow[2] - flow[1]:
            ret += (flow[2] - flow[1]) * flow[0]
            flowleft -= (flow[2] - flow[1])
        else:
            ret += flow[0]*flowleft
            break
    return ret

def calculatemaxtoadd(flowleft, flowlist):
    ret = 0
    for flow in flowlist:
        if flowleft >= flow[2] - flow[1]:
            ret += (flow[2] - flow[1]) * flow[0]
            flowleft -= (flow[2] - flow[1])
        else:
            ret += flow[0]*flowleft
            break
    return ret

for query in range(int(input())):
    td, vd = [int(x) for x in input().split()]
    if td > maxtemp or td < mintemp or vd > maxvol or vd < minvol:
        print("no")
        continue
    desired = td*vd
    lefttochecktofillvolume = vd - sum([k[1] for k in flows])
    # beräkna minsta möjliga för given volym
    minadd = calculatemintoadd(lefttochecktofillvolume, flows)
    # beräkna mesta möjliga för given volym
    maxadd = calculatemaxtoadd(lefttochecktofillvolume, flows[::-1])
    if desired >= mintiaisum + minadd and desired <= mintiaisum + maxadd:
        print("yes")
    else:
        print("no")