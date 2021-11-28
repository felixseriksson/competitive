from itertools import product, combinations

def check(a, b, c, d):
    if a[0] == b[0] and a[0] == c[0] and a[0] == d[0]:
        return True
    elif a[1] == b[1] and a[1] == c[1] and a[1] == d[1]:
        return True
    else:
        dyb = b[1] - a[1]
        dxb = b[0] - a[0]
        dyc = c[1] - a[1]
        dxc = c[0] - a[0]
        dyd = d[1] - a[1]
        dxd = d[0] - a[0]
        if dyb*dxc == dyc*dxb and dyb*dxd == dyd*dxb:
            return True
        else:
            return False

points = product(range(9), range(11))
# print(list(points))
# for p1 in product(range(9), range(11)):
#     for p2 in product(range(9), range(11)):
#         for p3 in product(range(9), range(11)):
#             for p4 in product(range(9), range(11)):
#                 p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
#                 if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
#                     print(p1, p2, p3, p4)
#                     continue
#                 else:
#                     print(p1, p2, p3, p4)
#                     print(check(p1, p2, p3, p4))
n = 0
i = 0
for comb in combinations(list(points), 4):
    p1, p2, p3, p4 = comb
    xes = [p1[0], p2[0], p3[0], p4[0]]
    ys = [p1[1], p2[1], p3[1], p4[1]]
    i += 1
    if not i % 100000:
        print(f"{i} of 3.7 million")
    if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
        # print(p1, p2, p3, p4)
        continue
    elif (0 not in xes) and (8 not in xes) and (0 not in ys) and (10 not in ys):
        continue
    else:
        # print(p1, p2, p3, p4)
        # print(check(p1, p2, p3, p4))
        if check(p1, p2, p3, p4):
            # print("found")
            n += 1
print(n)