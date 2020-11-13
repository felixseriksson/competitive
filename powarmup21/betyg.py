maxa, maxc, maxe = [int(x) for x in input().split()]
antala, antalc, antale = [int(x) for x in input().split()]

betyg = "E"
if antalc >= maxc/2:
    betyg = "D"
    if antalc == maxc:
        betyg = "C"
        if antala >= maxa/2:
            betyg = "B"
            if antala == maxa:
                betyg = "A"

print(betyg)