def rk4_shoot(s_guess, h=0.05):
    x = 0.0
    y = 0.0
    v = s_guess  # v = y'
    steps = int(round(1.0 / h))
    xs, ys = [x], [y]

    for _ in range(steps):
        k1_y = h * v
        k1_v = h * y

        k2_y = h * (v + 0.5 * k1_v)
        k2_v = h * (y + 0.5 * k1_y)

        k3_y = h * (v + 0.5 * k2_v)
        k3_v = h * (y + 0.5 * k2_y)

        k4_y = h * (v + k3_v)
        k4_v = h * (y + k3_y)

        y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        v += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        x = round(x + h, 10)
        xs.append(x)
        ys.append(y)

    return xs, ys

s1, s2 = 0.5, 1.5
_, ys1 = rk4_shoot(s1)
_, ys2 = rk4_shoot(s2)

yb1, yb2 = ys1[-1], ys2[-1]
target = 1.17

# Linear interpolation of initial slope y'(0)
s_opt = s1 + (s2 - s1) * (target - yb1) / (yb2 - yb1)
print(f"Optimal initial slope y'(0) = {s_opt:.6f}\n")

xs, ys = rk4_shoot(s_opt, h=0.1)
for x_val, y_val in zip(xs, ys):
    print(f"x = {x_val:.1f} : y(x) = {y_val:.6f}")