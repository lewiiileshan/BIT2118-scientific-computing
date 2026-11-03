"""Task 12 (modified): nonlinear systems - locating a phone from tower distances.

Part A: change the circle radius and the parabola shift of the original problem.
Part B: new case - two towers give two possible positions; a third tower removes the ambiguity.
"""
import numpy as np
from scipy.optimize import root, least_squares

# ---------- Part A: parameter change ----------
print("PART A - circle x^2+y^2=r^2 and parabola y=x^2-s")
for r, s in [(2.0, 1.0), (3.0, 1.0), (2.0, 5.0)]:
    def eqs(z, r=r, s=s):
        x, y = z
        return [x**2 + y**2 - r**2, y - (x**2 - s)]
    found = []
    for guess in ([1.0, 1.0], [-1.0, 1.0], [0.5, -2.0]):
        sol = root(eqs, guess)
        if sol.success and not any(np.allclose(sol.x, f, atol=1e-6) for f in found):
            found.append(sol.x)
    print(f"r={r}, s={s}: {len(found)} intersection(s): {[tuple(float(v) for v in np.round(f, 4)) for f in found]}")

print("Polynomial check x^2 - 5x + 6 = 0 -> roots", np.roots([1, -5, 6]))

# ---------- Part B: new case ----------
# Assumptions: towers at known coordinates (km); measured distances are exact here.
towers = np.array([[0.0, 0.0], [6.0, 0.0], [0.0, 8.0]])
true_pos = np.array([3.75, np.sqrt(25 - 3.75**2)])
dist = np.linalg.norm(towers - true_pos, axis=1)
print("\nPART B - positioning")
print("Distances to towers (km):", np.round(dist, 4))

def two_tower(z):
    return [np.linalg.norm(z - towers[0]) - dist[0], np.linalg.norm(z - towers[1]) - dist[1]]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    s = root(two_tower, guess)
    print(f"Two towers, guess {guess}: position {np.round(s.x, 4)}, residual {np.max(np.abs(two_tower(s.x))):.1e}")

def three_tower(z):
    return [np.linalg.norm(z - towers[k]) - dist[k] for k in range(3)]

# Three equations, two unknowns: use least squares (root() needs equal counts).
for guess in ([3.0, 3.0], [3.0, -3.0]):
    s = least_squares(three_tower, guess)
    print(f"Three towers, guess {guess}: position {np.round(s.x, 4)}, max residual {np.max(np.abs(three_tower(s.x))):.1e}")
