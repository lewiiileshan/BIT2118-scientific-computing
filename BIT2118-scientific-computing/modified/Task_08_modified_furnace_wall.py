"""Task 8 (modified): Jacobi and Gauss-Seidel - temperature through a furnace wall.

Part A: change boundary temperatures and the tolerance of the original 5-point model.
Part B: new case - 20 interior points, furnace face 150 C, outside 25 C; effect of grid size.
"""
import numpy as np
import matplotlib.pyplot as plt


def tridiag(n):
    return 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)


def jacobi(A, b, tol=1e-8, max_iter=20000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errs = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        e = np.linalg.norm(x_new - x, ord=np.inf)
        errs.append(e)
        x = x_new
        if e < tol:
            break
    return x, errs


def gauss_seidel(A, b, tol=1e-8, max_iter=20000):
    x = np.zeros_like(b)
    errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        e = np.linalg.norm(x - old, ord=np.inf)
        errs.append(e)
        if e < tol:
            break
    return x, errs


def solve_case(n, left, right, tol):
    A = tridiag(n)
    b = np.zeros(n)
    b[0], b[-1] = left, right
    xj, ej = jacobi(A, b, tol)
    xg, eg = gauss_seidel(A, b, tol)
    return A, b, xj, ej, xg, eg


# ---------- Part A: parameter change ----------
print("PART A - original 5-point grid, changed boundaries/tolerance")
for left, right, tol in [(100, 20, 1e-8), (80, 30, 1e-8), (100, 20, 1e-3)]:
    A, b, xj, ej, xg, eg = solve_case(5, left, right, tol)
    print(f"left={left}, right={right}, tol={tol:.0e}: Jacobi {len(ej)} its, Gauss-Seidel {len(eg)} its, "
          f"max error vs exact {np.max(np.abs(xg - np.linalg.solve(A, b))):.2e}")

# ---------- Part B: new case ----------
print("\nPART B - furnace wall (150 C inside, 25 C outside)")
for n in (10, 20, 40):
    A, b, xj, ej, xg, eg = solve_case(n, 150.0, 25.0, 1e-6)
    print(f"n={n:>2} interior points: Jacobi {len(ej):>5} its, Gauss-Seidel {len(eg):>5} its")

A, b, xj, ej, xg, eg = solve_case(20, 150.0, 25.0, 1e-8)
exact = np.linalg.solve(A, b)
print(f"n=20 maximum difference Gauss-Seidel vs direct: {np.max(np.abs(xg-exact)):.2e} C")
print("Temperature at first, middle and last interior points:", np.round(xg[[0, 9, 19]], 2))

plt.figure()
plt.plot(range(1, 21), xg, marker="o", label="Gauss-Seidel")
plt.plot(range(1, 21), exact, linestyle="--", label="Direct")
plt.xlabel("Grid point through the wall")
plt.ylabel("Temperature (C)")
plt.title("Temperature profile through furnace wall")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence, 20 interior points")
plt.legend()
plt.grid(True)
plt.show()
