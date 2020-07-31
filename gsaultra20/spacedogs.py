import bisect

def distance(tup1, tup2):
    return sum(((tup1[i]-tup2[i])**2 for i in range(len(tup1))))**0.5

def solution(masses, locations):
    listlist = sorted(zip(masses,locations))
    #print(listlist)
    for _ in range(len(locations)-1):
        minmass, minloc = listlist.pop(0)
        #mindex = masses.index(min(masses))
        #minloc = locations[mindex]
        #minmass = masses[mindex]
        leastdist = float("inf")
        otherindex = None
        for tup in listlist:
            loc=  tup[1]
            d = distance(minloc, loc)
            if d > leastdist:
                pass
            # elif d == 0:
            #     pass
            elif d <= leastdist:
                leastdist = d
                otherindex = listlist.index(tup)
                otherloc = loc
                #othermass = masses[otherindex]
        newmass = minmass + listlist[otherindex][0]
        newloc = tuple([sum(x)//2 for x in zip(minloc, otherloc)])
        del listlist[otherindex]
        #del masses[mindex]
        #del masses[otherindex if otherindex < mindex else otherindex-1]
        #del locations[mindex]
        #del locations[otherindex if otherindex < mindex else otherindex-1]
        #masses.insert(0, newmass)
        #locations.insert(0, newloc)
        bisect.insort(listlist, (newmass, newloc))
    
    return sum(listlist[0][1])

#print(solution([2, 5, 4], [(1, 4), (3, 1), (2, 6)]))
