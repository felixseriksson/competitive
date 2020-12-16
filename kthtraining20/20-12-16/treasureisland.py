rows, cols = [int(k) for k in input().split()]
grid = [[char for char in input()] for _ in range(rows)]
# for row in grid:
    # print(row)

accessiblefromsourcedist = [set() for _ in range(rows+cols-1)]
accessiblefromgoaldist = [set() for _ in range(rows+cols-1)]

found = False

def traverse(graph, start):
    ls = [start]
    while(len(ls) != 0):
        s = ls.pop()
        if start == (0, 0):
            if s not in accessiblefromsourcedist[sum(s)]:
                accessiblefromsourcedist[sum(s)].add(s)
                for nb in [(s[0]+1, s[1]), (s[0], s[1]+1)]:
                    if nb[0] == rows-1 and nb[1] == cols-1:
                        global found
                        found = True
                    if nb[0] >= 0 and nb[0] < rows and nb[1] >= 0 and nb[1] < cols and not (nb[0] == 0 and nb[1] == 0) and not (nb[0] == rows-1 and nb[1] == cols-1):
                        if graph[nb[0]][nb[1]] != "#":
                            ls.append(nb)
        elif start == (rows-1, cols-1):
            if s not in accessiblefromgoaldist[sum(s)]:
                accessiblefromgoaldist[sum(s)].add(s)
                for nb in [(s[0]-1, s[1]), (s[0], s[1]-1)]:
                    
                    if nb[0] >= 0 and nb[0] < rows and nb[1] >= 0 and nb[1] < cols and not (nb[0] == 0 and nb[1] == 0) and not (nb[0] == rows-1 and nb[1] == cols-1):
                        if graph[nb[0]][nb[1]] != "#":
                            ls.append(nb)
        else:
            print("idk")
            exit(0)

traverse(grid, (0,0))
traverse(grid, (rows-1,cols-1))
# print(accessiblefromsourcedist)
# print(accessiblefromgoaldist)
if not found:
    print(0)
    exit(0)
for i in range(len(accessiblefromgoaldist)):
    intersect = accessiblefromsourcedist[i].intersection(accessiblefromgoaldist[i])
    if len(intersect) == 1:
        print(1)
        exit(0)
print(2)