def distance(tup1, tup2):
    return sum(((tup1[i]-tup2[i])**2 for i in range(len(tup1))))**0.5

def solution(masses, locations):
    for _ in range(len(locations)-1):
        mindex = masses.index(min(masses))
        minloc = locations[mindex]
        minmass = masses[mindex]
        leastdist = float("inf")
        otherindex = None
        for loc in locations:
            d = distance(minloc, loc)
            if d > leastdist:
                pass
            elif d == 0:
                pass
            elif d <= leastdist:
                leastdist = d
                otherindex = locations.index(loc)
                otherloc = loc
                othermass = masses[otherindex]
        newloc = tuple([sum(x)//2 for x in zip(minloc, otherloc)])
        newmass = minmass + othermass
        del masses[mindex]
        del masses[otherindex if otherindex < mindex else otherindex-1]
        del locations[mindex]
        del locations[otherindex if otherindex < mindex else otherindex-1]
        masses.insert(0, newmass)
        locations.insert(0, newloc)
    
    return sum(locations[0])

#print(solution([2, 5, 4], [(1, 4), (3, 1), (2, 6)]))