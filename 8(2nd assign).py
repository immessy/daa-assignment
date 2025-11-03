def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Error: Matrix dimensions are not compatible for multiplication.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result


print("Enter size of first matrix (rows cols): ", end="")
r1, c1 = map(int, input().split())
print("Enter elements of first matrix row by row:")
A = [list(map(int, input().split())) for _ in range(r1)]

print("\nEnter size of second matrix (rows cols): ", end="")
r2, c2 = map(int, input().split())
print("Enter elements of second matrix row by row:")
B = [list(map(int, input().split())) for _ in range(r2)]

result = multiply_matrices(A, B)

if result:
    print("\nResultant Matrix:")
    for row in result:
        print(*row)
