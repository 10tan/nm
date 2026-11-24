def f(x, y, z):
    return 1.0 + x * z

def g(x, y, z):
    return -x * y

h = 0.1  # 3 steps to reach x = 0.3 (set h = 0.3 for single-step)
x, y, z = 0.0, 0.0, 1.0

for _ in range(3):
    k1 = h * f(x, y, z)
    l1 = h * g(x, y, z)

    k2 = h * f(x + h / 2, y + k1 / 2, z + l1 / 2)
    l2 = h * g(x + h / 2, y + k1 / 2, z + l1 / 2)

    k3 = h * f(x + h / 2, y + k2 / 2, z + l2 / 2)
    l3 = h * g(x + h / 2, y + k2 / 2, z + l2 / 2)

    k4 = h * f(x + h, y + k3, z + l3)
    l4 = h * g(x + h, y + k3, z + l3)

    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z += (l1 + 2 * l2 + 2 * l3 + l4) / 6
    x = round(x + h, 10)

print(f"At x = {x:.1f} : y = {y:.6f}, z = {z:.6f}")