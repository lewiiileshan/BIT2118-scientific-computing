"""Task 19 (modified): optimisation - production planning for a furniture workshop.

Part A: change the capacity requirement and unit costs in the cloud-server problem.
Part B: new case - maximise profit from tables and chairs subject to wood and labour limits.
"""
import numpy as np
from scipy.optimize import minimize, linprog

# ---------- Part A: parameter change ----------
def cloud(cost_a, cost_b, cap_a, cap_b, need):
    res = minimize(lambda z: cost_a*z[0] + cost_b*z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: cap_a*z[0] + cap_b*z[1] - need})
    best = min(((cost_a*a + cost_b*b, a, b) for a in range(40) for b in range(40) if cap_a*a + cap_b*b >= need))
    return res, best

print("PART A - cloud allocation")
for label, args in [("original", (12, 18, 100, 170, 1000)),
                    ("need 1500", (12, 18, 100, 170, 1500)),
                    ("A cheaper (9)", (9, 18, 100, 170, 1000))]:
    res, best = cloud(*args)
    print(f"{label:<14}: continuous A={res.x[0]:.2f}, B={res.x[1]:.2f}, cost {res.fun:.2f} | best integer (cost,A,B) = {best}")

# ---------- Part B: new case ----------
# Assumptions: profit per table 70, per chair 50 (hundreds of KES).
# Wood: 4 units per table, 3 per chair, 240 available. Labour: 2 h per table, 1 h per chair, 100 h available.
def neg_profit(z):
    return -(70*z[0] + 50*z[1])

cons = [
    {"type": "ineq", "fun": lambda z: 240 - (4*z[0] + 3*z[1])},
    {"type": "ineq", "fun": lambda z: 100 - (2*z[0] + 1*z[1])},
]
res = minimize(neg_profit, x0=[10, 10], method="SLSQP", bounds=[(0, None), (0, None)], constraints=cons)

lp = linprog(c=[-70, -50], A_ub=[[4, 3], [2, 1]], b_ub=[240, 100], bounds=[(0, None), (0, None)])

print("\nPART B - production plan")
print(f"SLSQP : tables={res.x[0]:.3f}, chairs={res.x[1]:.3f}, profit={-res.fun:.2f}")
print(f"linprog: tables={lp.x[0]:.3f}, chairs={lp.x[1]:.3f}, profit={-lp.fun:.2f}")
print(f"Wood used: {4*lp.x[0] + 3*lp.x[1]:.1f}/240, labour used: {2*lp.x[0] + lp.x[1]:.1f}/100 (both constraints are binding)")
for name, tb, ch in [("only tables", 50, 0), ("only chairs", 0, 80)]:
    print(f"Compare {name}: profit {70*tb + 50*ch}")
