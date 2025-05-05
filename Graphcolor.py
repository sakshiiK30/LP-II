import matplotlib.pyplot as plt
import networkx as nx

def add_edge(graph, edge1, edge2):
    graph[edge1][edge2] = 1
    graph[edge2][edge1] = 1

def safe_to_assign(i, color_to_assign, graph, v, color):
    for k in range(v):
        if graph[i][k] == 1 and color[k] == color_to_assign:
            return False
    return True

def graph_coloring_util(graph, m, v, i, color):
    if i == v:
        return True
    for j in range(m):
        if safe_to_assign(i, j, graph, v, color):
            color[i] = j
            if graph_coloring_util(graph, m, v, i + 1, color):
                return True
            color[i] = -1
    return False

def graph_coloring(graph, m, v):
    color = [-1] * v
    if graph_coloring_util(graph, m, v, 0, color):
        return color
    else:
        return None

# Initialize graph
v = 6  # number of vertices
graph = [[0]*v for _ in range(v)]

# Add edges
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 0, 3)
add_edge(graph, 2, 4)
add_edge(graph, 2, 5)
add_edge(graph, 3, 5)

# Run graph coloring
m = 3  # number of colors
colors = graph_coloring(graph, m, v)

# Create graph visual
G = nx.Graph()
edges = []
for i in range(v):
    for j in range(i+1, v):
        if graph[i][j] == 1:
            edges.append((i, j))
G.add_edges_from(edges)

# Assign colors
color_map = []
color_palette = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
if colors:
    for c in colors:
        color_map.append(color_palette[c])
else:
    color_map = ['gray'] * v

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color=color_map, node_size=800, font_weight='bold')
plt.title("Graph Coloring Result")
plt.show()
