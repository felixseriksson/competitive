r, c = [int(x) for x in input().split()]
top = [char for char in input()]
left = [char for char in input()]
bottom = [char for char in input()]
right = [char for char in input()]
tb = {"rr":0, "bb": 0, "gg": 0, "rg": 0, "rb": 0, "bg": 0}
lr = {"rr":0, "bb": 0, "gg": 0, "rg": 0, "rb": 0, "bg": 0}
for i in range(c):
    if top[i] == "R" and bottom[i] == "R":
        tb["rr"] += 1
    elif top[i] == "B" and bottom[i] == "B":
        tb["bb"] += 1
    elif top[i] == "G" and bottom[i] == "G":
        tb["gg"] += 1
    elif (top[i] == "R" and bottom[i] == "G") or (top[i] == "G" and bottom[i] == "R"):
        tb["rg"] += 1
    elif (top[i] == "R" and bottom[i] == "B") or (top[i] == "B" and bottom[i] == "R"):
        tb["rb"] += 1
    else:
        tb["bg"] += 1
for i in range(r):
    if left[i] == "R" and right[i] == "R":
        lr["rr"] += 1
    elif left[i] == "B" and right[i] == "B":
        lr["bb"] += 1
    elif left[i] == "G" and right[i] == "G":
        lr["gg"] += 1
    elif (left[i] == "R" and right[i] == "G") or (left[i] == "G" and right[i] == "R"):
        lr["rg"] += 1
    elif (left[i] == "R" and right[i] == "B") or (left[i] == "B" and right[i] == "R"):
        lr["rb"] += 1
    else:
        lr["bg"] += 1
# for key, val in tb.items():
#     print(key, val)
# print()
# for key, val in lr.items():
#     print(key, val)
s = 0
s += tb["rr"]*lr["bg"]
s += tb["gg"]*lr["rb"]
s += tb["bb"]*lr["rg"]
s += tb["rg"]*(lr["rb"] + lr["bb"] + lr["bg"])
s += tb["bg"]*(lr["rr"] + lr["rb"] + lr["rg"])
s += tb["rb"]*(lr["gg"] + lr["bg"] + lr["rg"])
print(s)