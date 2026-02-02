def minimax(depth, node_index, is_max, values):
    if depth == 2:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values),
            minimax(depth + 1, node_index * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values),
            minimax(depth + 1, node_index * 2 + 1, True, values)
        )

values = [3, 5, 2, 9]
result = minimax(0, 0, True, values)
print(result)
