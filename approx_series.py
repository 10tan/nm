import sympy as sp

t = sp.Symbol('t')
x = sp.Function('x')(t)
y = sp.Function('y')(t)

dx = x * y + 2 * t
dy = 2 * t * y + x

order = 5
dX = [x, dx]
dY = [y, dy]

subs_deriv = {sp.Derivative(x, t): dx, sp.Derivative(y, t): dy}

for k in range(1, order):
    dX.append(sp.diff(dX[k], t).subs(subs_deriv))
    dY.append(sp.diff(dY[k], t).subs(subs_deriv))

init_vals = {t: 0, x: 1, y: -1}

x_series = sum((dX[k].subs(init_vals) / sp.factorial(k)) * t**k for k in range(order + 1))
y_series = sum((dY[k].subs(init_vals) / sp.factorial(k)) * t**k for k in range(order + 1))

print("Approximate series x(t):", x_series)
print("Approximate series y(t):", y_series)