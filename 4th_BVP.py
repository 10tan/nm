import numpy as np

N = 3
h = 1.0 / N             # h = 1/3
c = 81.0 * (h**4)       # c = 1.0
phi = np.array([81.0, 162.0, 243.0])
rhs = (h**4) * phi      # [1.0, 2.0, 3.0]

# Stencil with clamped left (y0=0, y_{-1}=y1) and free right (y''(1)=0, y'''(1)=0)
A = np.array([
    [7 + c, -4,     1],
    [-4,     5 + c, -2],
    [2,     -4,     2 + c]
], dtype=float)

y_pivots = np.linalg.solve(A, rhs)
x_pivots = [1/3, 2/3, 1.0]

for x_val, y_val in zip(x_pivots, y_pivots):
    print(f"x = {x_val:.4f} : y = {y_val:.6f}")