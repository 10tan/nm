import numpy as np

def sor(A, b, omega=1.1, x0=None, tol=1e-10, max_iter=1000):
    if not 0 < omega < 2:
        raise ValueError("For standard SOR, choose 0 < omega < 2.")

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if np.any(np.abs(np.diag(A)) < 1e-12):
        raise ValueError("SOR requires non-zero diagonal entries.")

    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for iteration in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            left = np.dot(A[i, :i], x[:i])
            right = np.dot(A[i, i + 1:], x_old[i + 1:])
            x_gauss_seidel = (b[i] - left - right) / A[i, i]
            x[i] = (1 - omega) * x_old[i] + omega * x_gauss_seidel

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iteration

    raise RuntimeError("SOR method did not converge within max_iter.")

if __name__ == "__main__":
    A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    b = [6, 22, -10]
    solution, iterations = sor(A, b, omega=1.1)
    print("Solution [x, y, z]:", solution)
    print("Iterations:", iterations)
