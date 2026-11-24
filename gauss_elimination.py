import numpy as np

def gauss_elimination(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    M = np.column_stack((A, b))

    # Forward elimination with partial pivoting
    for k in range(n):
        pivot = k + np.argmax(np.abs(M[k:, k]))
        if abs(M[pivot, k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular.")
        M[[k, pivot]] = M[[pivot, k]]

        for i in range(k + 1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i + 1:n], x[i + 1:n])) / M[i, i]
    return x

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    print("Solution [x, y, z]:", gauss_elimination(A, b))
