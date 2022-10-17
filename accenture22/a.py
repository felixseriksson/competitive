d = dict()
d["C"] = 0
d["C#"] = 1
d["D"] = 2
d["D#"] = 3
d["E"] = 4
d["F"] = 5
d["F#"] = 6
d["G"] = 7
d["G#"] = 8
d["A"] = 9
d["A#"] = 10
d["B"] = 11

def isChord(a, b, c):
    vals = sorted([a, b, c], key = lambda x: d[x])
    l = sorted([d[a], d[b], d[c]])
    if ((l[1] - l[0]) % 12 == 4) and ((l[2] - l[1]) % 12 == 3):
        print(f"{vals[0]} major")
    elif ((l[2] - l[1]) % 12 == 4) and ((l[0] - l[2]) % 12 == 3):
        print(f"{vals[1]} major")
    elif ((l[0] - l[2]) % 12 == 4) and ((l[1] - l[0]) % 12 == 3):
        print(f"{vals[2]} major")
    else:
        print("not a chord")

isChord(*[input() for _ in range(3)])
