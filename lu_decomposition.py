import numpy as np

def lu_solve(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    # Doolittle LU decomposition: A = L @ U, with diagonal(L) = 1
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        if abs(U[i, i]) < 1e-12:
            raise ValueError("Zero pivot encountered; this simple LU version needs pivoting.")

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    # Forward substitution: L @ y = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Back substitution: U @ x = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return L, U, x

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    L, U, x = lu_solve(A, b)
    print("L =\n", L)
    print("U =\n", U)
    print("Solution [x, y, z]:", x)
