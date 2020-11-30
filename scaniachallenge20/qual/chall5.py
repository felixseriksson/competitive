from matplotlib import pyplot as plt
import scipy.spatial

pts = []
with open("C:\\Users\\felix\\Documents\\GitHub\\competitive\\scaniachallenge20\\points.txt", "r") as file:
    for line in file:
        for word in line.split():
            x, y = word.split(",")
            pts.append(tuple([int(x[1:]), int(y[:-1])]))


convexhull = scipy.spatial.ConvexHull(pts)
print(convexhull.simplices)

# # diagnostics (nästan så att man kan räkna själv lol)
x = [pt[0] for pt in pts]
y = [pt[1] for pt in pts]
plt.plot(x, y, "o")
xcv = [pt[0] for pt in convexhull.simplices]
ycv = [pt[1] for pt in convexhull.simplices]
plt.plot(xcv, ycv, "r.-")
plt.show()