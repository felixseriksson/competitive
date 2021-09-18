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


# if __name__ == "__main__":
#     print("Beginning tests.")
#     sets = DisjointSet()
#     for i in range(4):
#         sets.make_set(i)
#     sets.union(sets.get(0), sets.get(1))
#     sets.union(sets.get(2), sets.get(3))
#     print(sets.members.items())
#     for m in sets.members.values():
#         print("VALUE")
#         print(m.data)
#         print("PARENT")
#         print(sets.find(m).data)
n = int(input())
u = DisjointSet()
nodes = []
for i in range(n):
    x, y = [int(c) for c in input().split()]
    u.make_set(i)
    nodes.append((x,y))
for i in range(n):
    for j in range(n):
        if (nodes[i][0] == nodes[j][0] or nodes[i][1] == nodes[j][1]) and u.find(u.get(i)) != u.find(u.get(j)):
            u.union(u.get(i), u.get(j))

parents = set()
for num in range(n):
    parents.add(u.find(u.get(num)))
print(len(parents)-1)