# https://en.wikipedia.org/wiki/Resistance_distance
# https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
# https://en.wikipedia.org/wiki/Laplacian_matrix#Example
# https://en.wikipedia.org/wiki/Degree_matrix
# https://mathematica.stackexchange.com/questions/83395/efficient-implementation-of-resistance-distance-for-graphs

nodes, queries, edges = [int(x) for x in input().split()]

laplacianmatrix = [[0 for column in range(nodes)] for row in range(nodes)]
edgectr = edges

while edgectr > 0:
    line = [int(x) for x in input().split()]
    outnode = line.pop(0)
    degofoutnode = line.pop(0)
    laplacianmatrix[outnode-1][outnode-1] += degofoutnode
    for node in line:
        laplacianmatrix[node-1][outnode-1] = -1
        laplacianmatrix[outnode-1][node-1] = -1
        laplacianmatrix[node-1][node-1] += 1
    edgectr -= len(line)

for row in laplacianmatrix:
    print(row)