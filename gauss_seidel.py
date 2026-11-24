import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if np.any(np.abs(np.diag(A)) < 1e-12):
        raise ValueError("Gauss-Seidel method requires non-zero diagonal entries.")

    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for iteration in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            left = np.dot(A[i, :i], x[:i])       # newly updated values
            right = np.dot(A[i, i + 1:], x_old[i + 1:])  # previous values
            x[i] = (b[i] - left - right) / A[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iteration

    raise RuntimeError("Gauss-Seidel method did not converge within max_iter.")

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    solution, iterations = gauss_seidel(A, b)
    print("Solution [x, y, z]:", solution)
    print("Iterations:", iterations)
