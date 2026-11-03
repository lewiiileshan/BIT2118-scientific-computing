"""Task 11 (modified): Newton-Raphson and secant - finding the true interest rate of a loan.

Part A: change the cash flows and the starting guess of the original IRR problem.
Part B: new case - a 200,000 KES loan repaid with 24 monthly payments of 10,500 KES.
"""
import numpy as np
from scipy.optimize import root_scalar


def make_npv(cash_flows):
    def npv(r):
        return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))
    def d_npv(r):
        return sum(-t*cf / (1 + r)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv


# ---------- Part A: parameter change ----------
print("PART A - IRR with different inputs")
for label, cfs, x0 in [
    ("original", [-10000, 3000, 3500, 4000, 2500], 0.10),
    ("larger inflows", [-10000, 4000, 4500, 5000, 3500], 0.10),
    ("far starting guess", [-10000, 3000, 3500, 4000, 2500], 0.90),
]:
    npv, d = make_npv(cfs)
    nw = root_scalar(npv, fprime=d, x0=x0, method="newton", xtol=1e-12)
    sc = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
    print(f"{label:<19}: Newton {nw.root:.4%} ({nw.iterations} its), secant {sc.root:.4%} ({sc.iterations} its)")

# ---------- Part B: new case ----------
# Assumptions: loan principal P, n equal monthly payments; find monthly rate r with
# P = pmt * (1 - (1+r)^-n) / r
P, pmt, n = 200_000.0, 10_500.0, 24

def f(r):
    return pmt * (1 - (1 + r)**(-n)) / r - P

def df(r):  # analytical derivative
    a = (1 + r)**(-n)
    return pmt * ((n * (1 + r)**(-n - 1)) * r - (1 - a)) / r**2

nw = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-14)
sc = root_scalar(f, x0=0.005, x1=0.04, method="secant", xtol=1e-14)
bs = root_scalar(f, bracket=[1e-4, 0.2], method="bisect", xtol=1e-14)

r = nw.root
print("\nPART B - loan rate")
print(f"Total repaid: {pmt*n:,.0f} KES; interest paid: {pmt*n - P:,.0f} KES")
print(f"Monthly rate - Newton: {r:.6%} ({nw.iterations} its), secant: {sc.root:.6%} ({sc.iterations} its), bisection: {bs.root:.6%} ({bs.iterations} its)")
print(f"Nominal annual rate (x12): {12*r:.3%}")
print(f"Effective annual rate: {(1+r)**12 - 1:.3%}")
print(f"Check: payment from rate = {P*r/(1-(1+r)**(-n)):.2f} KES")
