def combinations_knapsack(items, r):
    result = []
    def combine(start, current):
        if len(current) == r:
            result.append(current)
            return
        for i in range(start, len(items)):
            combine(i + 1, current + [items[i]])
    combine(0, [])
    return result

def knapsack_combinations(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_set = []

    for r in range(1, n+1):
        for combo in combinations_knapsack(list(range(n)), r):
            total_w = sum(weights[i] for i in combo)
            total_v = sum(values[i] for i in combo)
            if total_w <= capacity and total_v > max_value:
                max_value = total_v
                best_set = combo

    return best_set, max_value

weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 5, 8, 10, 13]
print("Best set (comb):", knapsack_combinations(weights, values, 15))
