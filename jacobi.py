import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if np.any(np.abs(np.diag(A)) < 1e-12):
        raise ValueError("Jacobi method requires non-zero diagonal entries.")

    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for iteration in range(1, max_iter + 1):
        x_new = np.zeros(n)
        for i in range(n):
            total = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - total) / A[i, i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration
        x = x_new

    raise RuntimeError("Jacobi method did not converge within max_iter.")

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    solution, iterations = jacobi(A, b)
    print("Solution [x, y, z]:", solution)
    print("Iterations:", iterations)
