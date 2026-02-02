def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):
    if depth == 0:
        return values[nodeIndex]

    if isMax:
        best = -1000

        for i in range(2):
            val = alphabeta(depth - 1, nodeIndex * 2 + i,
                             False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth - 1, nodeIndex * 2 + i,
                             True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Driver code
values = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3

result = alphabeta(depth, 0, True, values, -1000, 1000)
print("Optimal value:", result)
