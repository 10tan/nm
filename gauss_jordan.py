import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    M = np.column_stack((A, b))

    # Convert the coefficient matrix to the identity matrix
    for k in range(n):
        pivot = k + np.argmax(np.abs(M[k:, k]))
        if abs(M[pivot, k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular.")
        M[[k, pivot]] = M[[pivot, k]]

        M[k] = M[k] / M[k, k]

        for i in range(n):
            if i != k:
                M[i] -= M[i, k] * M[k]

    return M[:, -1]

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    print("Solution [x, y, z]:", gauss_jordan(A, b))
