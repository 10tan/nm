def f(x):
    return -0.1 * x**4 - 0.15 * x**3 - 0.5 * x**2 - 0.25 * x + 1.2

def df_exact(x):
    return -0.4 * x**3 - 0.45 * x**2 - 1.0 * x - 0.25

x0 = 0.5
true_val = df_exact(x0)
print(f"True f'(0.5) = {true_val:.6f}\n")

for h in [0.5, 0.25]:
    fwd = (f(x0 + h) - f(x0)) / h
    bwd = (f(x0) - f(x0 - h)) / h
    cent = (f(x0 + h) - f(x0 - h)) / (2 * h)

    err_fwd = abs((true_val - fwd) / true_val) * 100
    err_bwd = abs((true_val - bwd) / true_val) * 100
    err_cent = abs((true_val - cent) / true_val) * 100

    print(f"=== Step Size h = {h:.2f} ===")
    print(f"Forward  O(h)  : {fwd:.7f} | True Rel. Error = {err_fwd:.2f}%")
    print(f"Backward O(h)  : {bwd:.7f} | True Rel. Error = {err_bwd:.2f}%")
    print(f"Centered O(h^2): {cent:.7f} | True Rel. Error = {err_cent:.2f}%\n")