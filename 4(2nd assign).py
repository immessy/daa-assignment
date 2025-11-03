def generate_permutations(elements):
    permutations_list = []

    def backtrack(index):
        if index == len(elements):
            permutations_list.append(elements[:])
            return
        for j in range(index, len(elements)):
            elements[index], elements[j] = elements[j], elements[index]
            backtrack(index + 1)
            elements[index], elements[j] = elements[j], elements[index]

    backtrack(0)
    return permutations_list


def tsp_brute_force(distance_matrix, start_city=0):
    total_cities = len(distance_matrix)
    other_cities = [i for i in range(total_cities) if i != start_city]

    all_possible_routes = generate_permutations(other_cities)
    shortest_distance = float('inf')
    optimal_route = []

    for route in all_possible_routes:
        current_path = [start_city] + route + [start_city]
        current_distance = 0

        for k in range(len(current_path) - 1):
            current_distance += distance_matrix[current_path[k]][current_path[k + 1]]

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            optimal_route = current_path

    return shortest_distance, optimal_route

distance_matrix = [
    [0, 10, 20, 32, 25],
    [10, 0, 33, 25, 31],
    [15, 34, 35, 0, 21],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

minimum_distance, best_route = tsp_brute_force(distance_matrix)

print("Minimum Distance:", minimum_distance)
print("Optimal Route:", best_route)
