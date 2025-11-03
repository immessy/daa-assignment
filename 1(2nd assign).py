def permutations(arr):
    result = []

    def permute(current, remaining):
        if len(remaining) == 0:
            result.append(current)
            return
        for i in range(len(remaining)):
            permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])

    permute([], arr)
    return result


data = [1, 2, 3]
print("Permutations:", permutations(data))
