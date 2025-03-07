def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        if len(row) != cols:
            raise ValueError(f"Row {i+1} must have {cols} columns.")
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    rows_A = int(input("Enter the number of rows for matrix A: "))
    cols_A = int(input("Enter the number of columns for matrix A: "))
    rows_B = int(input("Enter the number of rows for matrix B: "))
    cols_B = int(input("Enter the number of columns for matrix B: "))

    if cols_A != rows_B:
        raise ValueError("Number of columns in matrix A must be equal to number of rows in matrix B for multiplication.")

    print("Enter matrix A:")
    A = get_matrix(rows_A, cols_A)
    print("Enter matrix B:")
    B = get_matrix(rows_B, cols_B)

    result = multiply_matrices(A, B)
    print("Resultant matrix after multiplication:")
    print_matrix(result)