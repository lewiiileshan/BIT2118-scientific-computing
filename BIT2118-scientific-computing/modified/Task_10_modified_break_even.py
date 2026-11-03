"""Task 10 (modified): bisection and fixed point - break-even of a product.

Part A: change the heat-balance coefficient and the fixed-point starting value.
Part B: new case - find break-even quantities where profit(q) = 0.
"""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
print("PART A - heat balance f(T) = T - 25 - c*exp(-T/20)")
for c, T0 in [(10, 30.0), (15, 30.0), (10, 38.0)]:
    f = lambda T, c=c: T - 25 - c*np.exp(-T/20)
    g = lambda T, c=c: 25 + c*np.exp(-T/20)
    sol = root_scalar(f, bracket=[20, 45], method="bisect", xtol=1e-10)
    T, n = T0, 0
    while n < 200:
        T_new = g(T); n += 1
        if abs(T_new - T) < 1e-10:
            T = T_new
            break
        T = T_new
    print(f"c={c}, start={T0}: bisection {sol.root:.6f} C ({sol.iterations} its), fixed-point {T:.6f} C ({n} its)")

# ---------- Part B: new case ----------
# Assumptions: price falls as quantity rises (market saturation),
# price(q) = 150*exp(-q/1000) KES; fixed cost 8000 KES; variable cost 40 KES per unit.
def profit(q):
    return q * 150*np.exp(-q/1000) - (8000 + 40*q)

low = root_scalar(profit, bracket=[10, 150], method="bisect", xtol=1e-8)
high = root_scalar(profit, bracket=[500, 3000], method="bisect", xtol=1e-8)

# Fixed-point form for the lower root: q = (8000 + 40q) / (150*exp(-q/1000))
g = lambda q: (8000 + 40*q) / (150*np.exp(-q/1000))
q, its = 200.0, 0
for its in range(1, 500):
    q_new = g(q)
    if abs(q_new - q) < 1e-8:
        q = q_new
        break
    q = q_new

q_best = root_scalar(lambda x: (150*np.exp(-x/1000)*(1 - x/1000)) - 40, bracket=[100, 2000], method="bisect").root

print("\nPART B - break-even analysis")
print(f"Lower break-even quantity (bisection): {low.root:.2f} units ({low.iterations} its)")
print(f"Lower break-even quantity (fixed point from 200): {q:.2f} units ({its} its)")
print(f"Upper break-even quantity (bisection): {high.root:.2f} units")
print(f"Profitable range: {low.root:.0f} to {high.root:.0f} units")
print(f"Quantity that maximises profit (marginal revenue = marginal cost): {q_best:.1f} units, profit {profit(q_best):.0f} KES")

qs = np.linspace(1, 3500, 500)
plt.plot(qs, profit(qs))
plt.axhline(0, linewidth=0.8)
plt.axvline(low.root, linestyle="--")
plt.axvline(high.root, linestyle="--")
plt.xlabel("Quantity sold")
plt.ylabel("Profit (KES)")
plt.title("Profit and break-even points")
plt.grid(True)
plt.show()
