import math
def euclidean_distance(p1, p2):
    dist = math.sqrt((p1[0] - p2[0])*2 + (p1[1] - p2[1])*2) 
    print(f"Distance between {p1} and {p2}: {dist:.4f}")
    return dist
def brute_force(points):
    print(f"Brute force called with {len(points)} points: {points}")
    min_dist = float('inf') 
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            min_dist = min(min_dist, distance)
    print(f"Brute force result: {min_dist:.4f}\n")
    return min_dist
def check_strip(strip, min_dist):
    print(f"Check strip called with {len(strip)} points and min_dist={min_dist:.4f}")
    print(f"Strip points (sorted by y): {strip}")
    min_strip_dist = min_dist
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_strip_dist:
            distance = euclidean_distance(strip[i], strip[j])
            min_strip_dist = min(min_strip_dist, distance)
            j += 1
    print(f"Check strip result: {min_strip_dist:.4f}\n")
    return min_strip_dist
def closest_pair(points_sorted_by_x, depth=0):
    indent = "  " * depth
    n = len(points_sorted_by_x)
    print(f"{indent}closest pair called with {n} points: {points_sorted_by_x}")
    if n <= 3:
        return brute_force(points_sorted_by_x)
    mid = n // 2
    midpoint = points_sorted_by_x[mid]
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]
    print(f"{indent}Dividing at index {mid}, midpoint: {midpoint}")
    print(f"{indent}Left half: {left_half}")
    print(f"{indent}Right half: {right_half}\n")
    print(f"{indent}Processing left half:")
    left_min_dist = closest_pair(left_half, depth + 1)
    print(f"{indent}Processing right half:")
    right_min_dist = closest_pair(right_half, depth + 1)
    min_dist = min(left_min_dist, right_min_dist)
    print(f"{indent}Min distance from halves: {min_dist:.4f} (left={left_min_dist:.4f}, right={right_min_dist:.4f})\n")
    strip = []
    for point in points_sorted_by_x:
        if abs(point[0] - midpoint[0]) < min_dist:
            strip.append(point)
    print(f"{indent}Strip contains {len(strip)} points within {min_dist:.4f} of x={midpoint[0]}")
    strip.sort(key=lambda p: p[1])
    strip_min_dist = check_strip(strip, min_dist)
    result = min(min_dist, strip_min_dist)
    print(f"{indent}closest pair returning: {result:.4f}\n")
    return result
if __name__ == "_main_":
    points = [(1,2), (12,7), (3,7), (7,6), (12,1), (13,14)]
    print("Closest pair")
    print(f"Input points: {points}\n")
    points_sorted = sorted(points, key=lambda p: p[0])
    print(f"Points sorted by x-coordinate: {points_sorted}\n")
    print("Starting algorithm\n")
    min_distance = closest_pair(points_sorted)
    print(f"Minimum distance = {min_distance:.4f}")