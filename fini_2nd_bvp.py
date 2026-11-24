import numpy as np

N = 4
h = 1.0 / N
x = np.linspace(0, 1, N + 1)
xi = x[1:-1]  # x = 0.25, 0.50, 0.75
n_int = N - 1

A = np.zeros((n_int, n_int))
for i in range(n_int):
    A[i, i] = h**2 - 2
    if i > 0:
        A[i, i - 1] = 1.0
    if i < n_int - 1:
        A[i, i + 1] = 1.0

b = (h**2) * (xi**2)
b[0] -= 0.0   # y(0) = 0
b[-1] -= 2.0  # y(1) = 2

y_int = np.linalg.solve(A, b)

for x_val, y_val in zip(xi, y_int):
    print(f"y({x_val:.2f}) = {y_val:.6f}")