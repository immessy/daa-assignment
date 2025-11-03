def combinations(arr, r):
    result = []

    def combine(start, current):
        if len(current) == r:
            result.append(current)
            return
        for i in range(start, len(arr)):
            combine(i + 1, current + [arr[i]])

    combine(0, [])
    return result


data = [1, 2, 3, 4]
print("Combinations of 2:", combinations(data, 2))
