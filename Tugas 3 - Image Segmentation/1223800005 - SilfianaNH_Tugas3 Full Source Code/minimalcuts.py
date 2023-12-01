import random

def min_cut(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        graph[u].extend(graph[v])
        
        for node in graph[v]:
            graph[node].remove(v)
            graph[node].append(u)
        del graph[v]
    min_cuts = len(list(graph.values())[0])
    return min_cuts
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Contoh pengujian
min_cut_result = min_cut(graph)
print("Minimal cuts:", min_cut_result)
