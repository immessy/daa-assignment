def knapsack_binary(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_set = []

    for mask in range(1 << n):
        total_w, total_v = 0, 0
        for i in range(n):
            if mask & (1 << i):
                total_w += weights[i]
                total_v += values[i]
        if total_w <= capacity and total_v > max_value:
            max_value = total_v
            best_set = [i for i in range(n) if mask & (1 << i)]
    return best_set, max_value

weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 5, 8, 10, 13]
print("Best set:", knapsack_binary(weights, values, 15))
