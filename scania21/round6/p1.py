# ctr = 0
# for x in range(1, 100):
#     for y in range(1, 100):
#         for a in range(1, 100):
#             for b in range(1, 100):
#                 if x*a + y*b == 93 and a < b:
#                     ctr += 1
# print(ctr)
# ctr = 0
# for i in range()

ctr = 0
for a in range(1,100):
    for b in range(a+1, 100):
        i = 1
        while True:
            if 93 <= a*i:
                break
            if (93 - a*i) % b == 0:
                ctr += 1
                print(a, b, i, (93 - a*i)/b)
                break
            i += 1
print(ctr)