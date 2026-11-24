
import numpy as np

def romberg(f, a, b, max_level=5, tol=1e-10):
    R = np.zeros((max_level, max_level))

    # First trapezoidal approximation
    h = b - a
    R[0, 0] = (h / 2) * (f(a) + f(b))

    for k in range(1, max_level):

        h = (b - a) / (2 ** k)

        # Calculate new function values at midpoints
        new_sum = sum(
            f(a + (2 * i - 1) * h)
            for i in range(1, 2 ** (k - 1) + 1)
        )

        # Trapezoidal refinement
        R[k, 0] = 0.5 * R[k-1, 0] + h * new_sum

        # Richardson extrapolation
        for j in range(1, k + 1):
            R[k, j] = (
                (4 ** j * R[k, j-1] - R[k-1, j-1])
                / (4 ** j - 1)
            )

        # Check convergence
        if abs(R[k, k] - R[k-1, k-1]) < tol:
            return R[:k+1, :k+1], R[k, k]

    return R, R[max_level-1, max_level-1]


if __name__ == "__main__":

    # Example: Integrate 1/(1+x^2) from 0 to 1
    def f(x):
        return 1 / (1 + x**2)

    a = 0
    b = 1

    table, result = romberg(f, a, b)

    print("Romberg Integration Table:\n")
    print(table)

    print("\nFinal Integral =", result)
    print("Exact Value    =", np.pi / 4)

