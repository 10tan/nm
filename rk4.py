def f(x, y):
    return (y**2 - x**2) / (y + x)

h = 0.2
x = 0.0
y = 1.0

for _ in range(2):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)

    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x = round(x + h, 10)
    print(f"x = {x:.1f} : y = {y:.6f}")