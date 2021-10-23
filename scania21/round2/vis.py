import matplotlib.pyplot as plt
datafile = "data.txt"

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

points = []

with open(datafile, "r") as da:
    for index, line in enumerate(da):
        point = [int(l) for l in line.strip().split()]
        points.append(point)

xs = [p[0] for p in points]
ys = [p[1] for p in points]
plt.scatter(xs, ys)
plt.show()