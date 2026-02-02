# Graph definition
graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for nbr in graph[start]:
        if nbr not in visited:
            dfs(graph, nbr, visited)

# Run DFS
print("DFS:")
dfs(graph, 1)
