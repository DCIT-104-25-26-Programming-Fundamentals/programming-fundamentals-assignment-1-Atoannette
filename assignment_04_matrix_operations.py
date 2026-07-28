# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols, label=""):
    print(f"Enter matrix {label} ({rows}x{cols}):")
    matrix = []
    for r in range(rows):
        while True:
            row_values = input(f"Enter row {r + 1}: ").split()
            if len(row_values) != cols:
                print(f"Error: Please enter exactly {cols} numbers.")
                continue
            matrix.append([float(v) for v in row_values])
            break
    return matrix


def display_matrix(matrix):
    for row in matrix:
        formatted = "  ".join(
            str(int(v)) if v == int(v) else str(v) for v in row
        )
        print(formatted)


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def part_a_transpose():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))


def part_b_add():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows, cols, "A")
    matrix_b = read_matrix(rows, cols, "B")
    print("\nSum of Matrices:")
    display_matrix(add_matrices(matrix_a, matrix_b))


def part_c_multiply():
    rows_a = int(input("Enter rows of Matrix A: "))
    cols_a = int(input("Enter columns of Matrix A: "))
    matrix_a = read_matrix(rows_a, cols_a, "A")

    rows_b = cols_a
    print(f"Matrix B must have {rows_b} rows.")
    cols_b = int(input("Enter columns of Matrix B: "))
    matrix_b = read_matrix(rows_b, cols_b, "B")

    print("\nProduct Matrix (A x B):")
    display_matrix(multiply_matrices(matrix_a, matrix_b))


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = input("Select an operation (1-3): ")

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()

