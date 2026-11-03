"""Task 7 (modified): LU decomposition - implicit heat diffusion in a metal rod.

Part A: change the diagonal of A and the measurement vector.
Part B: new case - same matrix reused for 400 time steps (LU factor once vs solve each time).
"""
import timeit
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# ---------- Part A: parameter change ----------
for diag in (4.0, 2.5, 2.05):
    A = np.array([[diag, -1, 0], [-1, diag, -1], [0, -1, diag - 1]])
    b = np.array([15.0, 10.0, 10.0])
    x = np.linalg.solve(A, b)
    print(f"diag={diag}: solution={np.round(x, 4)}, cond(A)={np.linalg.cond(A):.2f}")
print("Smaller diagonal -> larger condition number -> solution more sensitive to errors.\n")

# ---------- Part B: new case ----------
# Assumptions: rod discretised into n=300 points, r = alpha*dt/dx^2 = 0.4, ends held at 0 C,
# initial temperature 100 C in the middle third, 0 C elsewhere.
n, r, steps = 300, 0.4, 400
A = np.diag((1 + 2*r)*np.ones(n)) + np.diag(-r*np.ones(n-1), 1) + np.diag(-r*np.ones(n-1), -1)

u0 = np.zeros(n)
u0[n//3: 2*n//3] = 100.0

lu, piv = lu_factor(A)

def with_lu():
    u = u0.copy()
    for _ in range(steps):
        u = lu_solve((lu, piv), u)
    return u

def with_solve():
    u = u0.copy()
    for _ in range(steps):
        u = np.linalg.solve(A, u)
    return u

u_lu, u_solve = with_lu(), with_solve()
t_lu = timeit.timeit(with_lu, number=3) / 3
t_solve = timeit.timeit(with_solve, number=3) / 3

print("PART B - heat diffusion with implicit stepping")
print(f"Max temperature: start {u0.max():.1f} C -> after {steps} steps {u_lu.max():.2f} C")
print(f"Max difference between LU and np.linalg.solve results: {np.max(np.abs(u_lu - u_solve)):.2e}")
print(f"Time with LU reuse (factor once): {t_lu:.4f} s (plus one factorisation)")
print(f"Time re-solving every step     : {t_solve:.4f} s")
print(f"Approximate saving: {t_solve/t_lu:.1f}x")
