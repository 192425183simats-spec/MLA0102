from collections import deque

# Graph definition
graph = {
    1: [2, 3],
    2: [5, 6],
    3: [7],
    4: [],
    5: [],
    6: [],
    7: [8],
    8: []
}

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

# Run BFS
print("BFS:")
bfs(graph, 1)
