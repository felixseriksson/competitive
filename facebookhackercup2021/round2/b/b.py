from collections import defaultdict
class Node:
    '''
    A simple node class which stores rank and parent, for use in Disjoint Sets.
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, rnk, d):
        self.rank = rnk
        self.parent = self
        self.data = d
        self.size = 1


class DisjointSet:
    '''
    A disjoint set datastructure, for implementing union find operations.
    '''

    def __init__(self):
        # The members dictionary hashes the value to the corresponding node
        self.members = dict()

    '''
    Input: Value to be retrieved from sets.
    Output: Node corresponding to the value if it is present, None otherwise.
    '''
    def get(self, val):
        if val in self.members:
            return self.members[val]
        else:
            return None

    def make_set(self, val):
        if val not in self.members:
            # The rank is initially 0 since it is a new set
            self.members[val] = Node(0, val)

    '''
    Takes input of a given node in the members dictionary.
    Returns the root of its set.
    '''
    def find(self, n):
        if n.parent != n:
            self.members[n.data].parent = self.find(n.parent)
        return n.parent

    def union(self, n1, n2):
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)

        if root_n1 == root_n2:
            return True
        else:
            if root_n1.rank > root_n2.rank:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
            elif root_n1.rank < root_n2.rank:
                self.members[root_n2.data].size += self.members[root_n1.data].size
                self.members[root_n1.data].parent = self.members[root_n2.data]
            else:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
                self.members[root_n1.data].rank = root_n1.rank+1

with open("b/test.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]
cases = int(inp[0])
i = 1
out = []

for case in range(1, cases+1):
    n = int(inp[i])
    i += 1
    edges = []
    u = DisjointSet()
    fset = dict()
    freq = dict()
    for _ in range(n-1):
        x, y = [int(a) for a in inp[i].split()]
        edges.append([x, y])
        i += 1
    for node, f in enumerate([int(a) for a in inp[i].split()], start=1):
        u.make_set(node)
        fset[node] = set([f])
        freq[node] = f
    i += 1
    for x, y in edges:
        if u.find(u.get(x)) != u.find(u.get(y)):
            xroot, yroot = u.find(u.get(x)), u.find(u.get(y))
            if freq[x] in fset[yroot.data]:
                oldset = fset[yroot.data]
                oldset.add(freq[x])
                u.union(u.get(x), u.get(y))
                newxroot, newyroot = u.find(u.get(x)), u.find(u.get(y))
                assert newxroot.data == newyroot.data
                fset[newxroot.data] = oldset
            elif freq[y] in fset[xroot.data]:
                oldset = fset[xroot.data]
                oldset.add(freq[y])
                u.union(u.get(x), u.get(y))
                newxroot, newyroot = u.find(u.get(x)), u.find(u.get(y))
                assert newxroot.data == newyroot.data
                fset[newxroot.data] = oldset
            else:
                pass

    parents = set()
    for num in range(1, n+1):
        parents.add(u.find(u.get(num)))
    print(len(parents)-1)

# with open("b/main-out.txt", "w") as outfile:
#     for line in out:
#         outfile.write(line + "\n")