# for case in range(1, int(input())+1):
#     x, y, l = input().split()
#     x, y = int(x), int(y)
#     cost = sum([x if (l[i] == "C" and l[i+1] == "J") else y if (l[i] == "J" and l[i+1] == "C") else 0 for i in range(len(l) - 1)])
#     l = l.lstrip("?").rstrip("?")
#     changes = []
#     for i in range(len(l)-1):
#         if (l[i] == "C" or l[i] == "J") and (l[i+1] == "?"):
#             changes.append(l[i])
#         elif (l[i] == "?") and (l[i+1] == "C" or l[i+1] == "J"):
#             changes.append(l[i+1])
#     for i in range(len(changes)-1):
#         cost += x if (changes[i] == "C" and changes[i+1] == "J") else y if (changes[i] == "J" and changes[i+1] == "C") else 0
#     print("Case #{}: {}".format(case, cost))

# for case in range(1, int(input())+1):
#     x, y, l = input().split()
#     x, y, l = int(x), int(y), l.lstrip("?").rstrip("?")
#     cost = 0
#     last = l[0]
#     for i in range(1, len(l)):
#         if l[i] == "C":
#             if last == "C":
#                 continue
#             elif last == "J":
#                 cost += y
#                 last = "C"
#             else:
#                 print("ERROR!")
#         elif l[i] == "J":
#             if last == "C":
#                 cost += x
#                 last = "J"
#             elif last == "J":
#                 continue
#             else:
#                 print("ERROR")
#         else:
#             continue
#     print("Case #{}: {}".format(case, cost))

for case in range(1, int(input())+1):
    x, y, l = input().split()
    x, y = int(x), int(y)
    l = [k for k in l if k != "?"]
    cost = 0
    if len(l) == 1:
        print("Case #{}: {}".format(case, cost))
        continue
    for i in range(len(l)-1):
        if l[i] == "C" and l[i+1] == "J":
            cost += x
        elif l[i] == "J" and l[i+1] == "C":
            cost += y
        else:
            continue
    print("Case #{}: {}".format(case, cost))