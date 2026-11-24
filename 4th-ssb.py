import numpy as np

n = 3
h = 1.0 / n
c = 81.0 * (h**4)
x = np.array([1/3, 2/3])
rhs = (h**4) * 81.0 * (x**2)

# Simply supported BCs: y(0)=y(1)=0, y''(0)=y''(1)=0 -> y_{-1}=-y_1, y_4=-y_2
A = np.array([
    [5 + c, -4],
    [-4,     5 + c]
], dtype=float)

y_int = np.linalg.solve(A, rhs)

for x_val, y_val in zip(x, y_int):
    print(f"y({x_val:.4f}) = {y_val:.6f}")