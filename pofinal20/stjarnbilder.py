punkter = int(input())
img1 = []
img2 = []
for n in range(punkter):
    img1.append([int(x) for x in input().split()])
for n in range(punkter):
    img2.append([int(x) for x in input().split()])

for n in range(punkter):
    # om inte raket
    offsets = []
    for m in range(punkter):
        offsets.append([img1[m][0]-img2[m][0], img1[m][1]-img2[m][1]])
    print(offsets)
    potentiellapositioner = []
    for offset in offsets:
        potentiellapositioner.append([img1[m][0]-offset[0], offset[1]-img2[m][1]])
    print(potentiellapositioner)