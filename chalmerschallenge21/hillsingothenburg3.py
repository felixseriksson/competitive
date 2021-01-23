def all_vertices(graph):
    """Return a set of all vertices in a graph.
    
    graph -- a weighted, directed graph.
    """
    vertices = set()
    for v in graph.keys():
        vertices.add(v)
        for u in graph[v].keys():
            vertices.add(u)
    return vertices

def is_edge(graph, tail, head):
    """Return if the edge (tail)->(head) is present
    in a graph.
    
    graph -- a weighted, directed graph.
    tail -- a vertex.
    head -- a vertex.
    """
    return (tail in graph) and (head in graph[tail])

class NoShortestPathError(Exception):
    pass

class NegativeCycleError(NoShortestPathError):
    def __init__(self, weight, cycle):
        self.weight = weight
        self.cycle = cycle

    def __str__(self):
        return f"Weight {self.weight}: {self.cycle}"

def shortest_path_bellman_ford(*, graph, start, end):
    """Find the shortest path from start to end in graph,
    using the Bellman-Ford algorithm.
    
    If a negative cycle exists, raise NegativeCycleError.
    If no shortest path exists, raise NoShortestPathError.
    """
    n = len(all_vertices(graph))

    dist = {}
    pred = {}

    def is_dist_infinite(v):
        return v not in dist

    def walk_pred(start, end):
        path = [start]
        v = start
        while v != end:
            v = pred[v]
            path.append(v)
        path.reverse()
        return path

    def find_cycle(start):
        nodes = []
        node = start
        while True:
            if node in nodes:
                cycle = [
                    node,
                    *reversed(nodes[nodes.index(node) :]),
                ]
                print(nodes)
                print(cycle)
                return cycle
            nodes.append(node)
            if node not in pred:
                break
            node = pred[node]

    dist[start] = 0

    # Relax approximations (n-1) times.

    for _ in range(n - 1):
        for tail in graph.keys():
            if is_dist_infinite(tail):
                continue
            for head, weight in graph[tail].items():
                alt = dist[tail] + weight
                if is_dist_infinite(head) or (
                    alt < dist[head]
                ):
                    dist[head] = alt
                    pred[head] = tail

    # Check for negative cycles.

    for tail in graph.keys():
        for head, weight in graph[tail].items():
            if (dist[tail] + weight) < dist[head]:
                cycle = find_cycle(tail)
                cycle_weight = sum(
                    graph[c_tail][c_head]
                    for (c_tail, c_head) in zip(
                        cycle, cycle[1:]
                    )
                )
                raise NegativeCycleError(
                    cycle_weight, cycle
                )

    # Build shortest path.

    if is_dist_infinite(end):
        raise NoShortestPathError

    best_weight = dist[end]
    best_path = walk_pred(end, start)

    return best_weight, best_path

nodes, edges = [int(x) for x in input().split()]
to, fr = input().split()
heights = [int(x) for x in input().split()]
g = dict()
for _ in range(edges):
    n1, n2 = input().split()
    if heights[int(n1)-1] == heights[int(n2)-1]:
        try:
            g[n1][n2] = 0
        except:
            g[n1] = dict()
            g[n1][n2] = 0
        try:
            g[n2][n1] = 0
        except:
            g[n2] = dict()
            g[n2][n1] = 0
    elif heights[int(n1)-1] < heights[int(n2)-1]:
        try:
            g[n1][n2] = heights[int(n2)-1] - heights[int(n1)-1]
        except:
            g[n1] = dict()
            g[n1][n2] = heights[int(n2)-1] - heights[int(n1)-1]
        try:
            g[n2][n1] = 0
        except:
            g[n2] = dict()
            g[n2][n1] = 0
    else:
        try:
            g[n1][n2] = 0
        except:
            g[n1] = dict()
            g[n1][n2] = 0
        try:
            g[n2][n1] = heights[int(n1)-1] - heights[int(n2)-1]
        except:
            g[n2] = dict()
            g[n2][n1] = heights[int(n1)-1] - heights[int(n2)-1]

print(shortest_path_bellman_ford(graph=g, start=to, end=fr)[0])