def get_matrix(name):
    r = int(input(f"Enter number of rows for {name}: "))
    c = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row by row:")
    mat = []
    for i in range(r):
        row = []
        print(f"Row {i+1}:")
        for j in range(c):
            val = int(input(f"  Element [{i+1}][{j+1}]: "))
            row.append(val)
        mat.append(row)
    return mat, r, c

def multiply(mat1, mat2, r1, c1, r2, c2):
    if c1 != r2:
        print("Matrix multiplication not possible.")
        return None
    res = []
    for i in range(r1):
        row = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += mat1[i][k] * mat2[k][j]
            row.append(s)
        res.append(row)
    return res

m1, r1, c1 = get_matrix("Matrix 1")
m2, r2, c2 = get_matrix("Matrix 2")
prod = multiply(m1, m2, r1, c1, r2, c2)

if prod:
    print("\nResultant Matrix:")
    for r in prod:
        for val in r:
            print(val, end=" ")
        print()
