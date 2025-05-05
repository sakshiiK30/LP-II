class Node:
    def __init__(self):
        self.parent = -1
        self.rank = 0

class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def find(dsuf, v):
    if dsuf[v].parent == -1:
        return v
    dsuf[v].parent = find(dsuf, dsuf[v].parent)
    return dsuf[v].parent

def union(dsuf, fromP, toP):
    if dsuf[fromP].rank > dsuf[toP].rank:
        dsuf[toP].parent = fromP
    elif dsuf[fromP].rank < dsuf[toP].rank:
        dsuf[fromP].parent = toP
    else:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1

def kruskal(edge_list, V):
    dsuf = [Node() for _ in range(V)]
    edge_list.sort(key=lambda edge: edge.wt)
    mst = []

    i = 0  # index for edge_list
    e = 0  # count of edges in MST

    while e < V - 1 and i < len(edge_list):
        curr_edge = edge_list[i]
        fromP = find(dsuf, curr_edge.src)
        toP = find(dsuf, curr_edge.dest)

        if fromP != toP:
            union(dsuf, fromP, toP)
            mst.append(curr_edge)
            e += 1
        i += 1

    return mst

def print_mst(mst):
    total_weight = sum(edge.wt for edge in mst)
    print("\nMinimum Spanning Tree:")
    for edge in mst:
        print(f"src : {edge.src}\ndest : {edge.dest}\nwt : {edge.wt}\n")
    print(f"Minimum weight of MST: {total_weight}")

# Input and Execution
if __name__ == "__main__":
    E = int(input("Enter the number of edges: "))
    V = int(input("Enter the number of vertices: "))
    
    edge_list = []
    for i in range(E):
        s, d, w = map(int, input(f"Enter edge {i + 1} (src dest wt): ").split())
        edge_list.append(Edge(s, d, w))
    
    mst = kruskal(edge_list, V)
    print_mst(mst)

OUTPUT:
Enter the number of edges: 4
Enter the number of vertices: 5
Enter edge 1 (src dest wt): 0 1 1
Enter edge 2 (src dest wt): 0 2 1
Enter edge 3 (src dest wt): 1 3 2
Enter edge 4 (src dest wt): 2 4 4

Minimum Spanning Tree:
src : 0
dest : 1
wt : 1

src : 0
dest : 2
wt : 1

src : 1
dest : 3
wt : 2

src : 2
dest : 4
wt : 4

Minimum weight of MST: 8
