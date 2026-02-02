from collections import deque

def water_jug_problem():
    jug1_capacity = 4
    jug2_capacity = 3
    goal = 2

    visited = set()
    queue = deque()
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        if jug1 == goal:
            return path

        states = []

        states.append((jug1_capacity, jug2))
        states.append((jug1, jug2_capacity))
        states.append((0, jug2))
        states.append((jug1, 0))

        transfer = min(jug1, jug2_capacity - jug2)
        states.append((jug1 - transfer, jug2 + transfer))

        transfer = min(jug2, jug1_capacity - jug1)
        states.append((jug1 + transfer, jug2 - transfer))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


solution = water_jug_problem()

print("Steps to get exactly 2 gallons in 4-gallon jug:")
for step in solution:
    print(step)
