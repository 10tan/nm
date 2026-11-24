import sympy as sp

x = sp.Symbol('x')
y = sp.Function('y')(x)
dy = sp.Derivative(y, x)
d2y = x**3 - y**2 * dy

subs_d2 = {sp.Derivative(y, x, 2): d2y}
d3y = sp.diff(d2y, x).subs(subs_d2)
d4y = sp.diff(d3y, x).subs(subs_d2)
d5y = sp.diff(d4y, x).subs(subs_d2)

init_vals = {x: 1, y: 1, dy: 1}
coeffs = [
    1.0,
    1.0,
    float(d2y.subs(init_vals)),
    float(d3y.subs(init_vals)),
    float(d4y.subs(init_vals)),
    float(d5y.subs(init_vals)),
]

def taylor_eval(h):
    fact = 1
    total = coeffs[0]
    for k in range(1, len(coeffs)):
        fact *= k
        total += coeffs[k] * (h**k) / fact
    return total

print(f"y(1.1) = {taylor_eval(0.1):.8f}")
print(f"y(1.2) = {taylor_eval(0.2):.8f}")