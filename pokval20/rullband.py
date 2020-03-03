import heapq

class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, neighbours):
        self.nodes[key] = neighbours
    
    def add_rullband(self, nyttrullband):
        self.nodes[str(nyttrullband[0])][str(nyttrullband[1])] = nyttrullband[2]
        self.nodes[str(nyttrullband[1])][str(nyttrullband[0])] = nyttrullband[2]

    def traceback_path(self, target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        return list(reversed(path))

    def shortest_path(self, start, finish):
        OPEN = [HeapEntry(start, 0.0)]
        CLOSED = set()
        parents = {start: None}
        distance = {start: 0.0}

        while OPEN:
            current = heapq.heappop(OPEN).node

            if str(current) == str(finish):
                return self.traceback_path(finish, parents), int(distance[current]) #list of path, dist. to finish

            if current in CLOSED:
                continue

            CLOSED.add(current)

            for child in self.nodes[current].keys():
                if child in CLOSED:
                    continue
                tentative_cost = distance[current] + self.nodes[current][child]

                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(OPEN, heap_entry)

graph = Graph()

inputline1 = [int(char) for char in input().split()]
N, M, g = inputline1[0], inputline1[1], inputline1[2]
for num in range(M+1):
    temp = {}
    if num != M:
        temp[str(num+1)] = int(g)
    if num != 0:
        temp[str(num-1)] = int(g)
    graph.add_node(str(num), temp)

for num in range(N):
    rullband = [int(char) for char in input().split()]
    graph.add_rullband(rullband)
print(graph.nodes)
print(graph.shortest_path("0", str(M))[1])