"""Task 4 (modified): floating-point errors in banking and cancellation.

Part A: change the approximation of sqrt(2) and the tolerance used for comparison.
Part B: new case - adding 0.10 KES one million times (accumulated round-off) and
        catastrophic cancellation in (1 - cos x) / x^2.
"""
import math
import numpy as np

# ---------- Part A: parameter change ----------
true_value = np.sqrt(2)
print("PART A - better approximations give smaller errors")
for approx in (1.414, 1.4142, 1.41421356):
    abs_err = abs(true_value - approx)
    print(f"approx={approx:<10}: absolute={abs_err:.2e}, relative={abs_err/true_value:.4%}")

print("np.isclose(0.1+0.2, 0.3) with tolerances:")
for rtol in (1e-5, 1e-12, 1e-17):
    print(f"  rtol={rtol:.0e}, atol=0 -> {np.isclose(0.1+0.2, 0.3, rtol=rtol, atol=0)}")

# ---------- Part B: new case ----------
print("\nPART B - accumulated error in a ledger")
n = 1_000_000
naive = 0.0
for _ in range(n):
    naive += 0.10
exact_total = n * 0.10  # 100000.0

print(f"Naive loop sum      : {naive:.6f}  (error {abs(naive-exact_total):.6e})")
print(f"math.fsum (exact)   : {math.fsum([0.10]*n):.6f}")
print(f"np.sum (pairwise)   : {np.sum(np.full(n, 0.10)):.6f}")

# Keeping money in integer cents avoids the issue entirely
cents = sum([10]*n)
print(f"Integer cents total : {cents/100:.2f} KES")

print("\nCancellation: (1 - cos x)/x^2 should approach 0.5")
for x in (1e-2, 1e-5, 1e-8):
    direct = (1 - np.cos(x)) / x**2
    stable = 2*np.sin(x/2)**2 / x**2
    print(f"x={x:.0e}: direct={direct:.10f}, stable={stable:.10f}")
