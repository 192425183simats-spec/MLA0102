import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1), ('E', 1)],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 0
}

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    expansion_order = []

    while open_list:
        _, current = heapq.heappop(open_list)
        expansion_order.append(current)

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost
            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    return expansion_order, path, g_cost[goal]

start_node = 'A'
goal_node = 'F'

expanded, optimal_path, total_cost = a_star(start_node, goal_node)

print("Order of node expansion:", expanded)
print("Optimal path:", optimal_path)
print("Total cost:", total_cost)
