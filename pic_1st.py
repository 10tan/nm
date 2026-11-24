import sympy as sp

x, s = sp.symbols('x s')
y_prev = sp.Integer(2)
z_prev = sp.Integer(1)

for k in range(1, 4):
    y_curr = sp.expand(2 + sp.integrate(s + z_prev.subs(x, s), (s, 0, x)))
    z_curr = sp.expand(1 + sp.integrate(s - y_prev.subs(x, s)**2, (s, 0, x)))

    y_val = float(y_curr.subs(x, 0.1))
    z_val = float(z_curr.subs(x, 0.1))
    print(f"Iteration {k} at x = 0.1: y = {y_val:.8f}, z = {z_val:.8f}")

    y_prev, z_prev = y_curr, z_curr