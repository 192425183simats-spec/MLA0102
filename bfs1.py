def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Input
n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbors = list(map(str, input(f"Enter neighbors of {node}: ").split()))
    graph[node] = neighbors

start_node = input("Enter starting node: ")

print("DFS Traversal:", end=" ")
dfs(graph, start_node, set())
