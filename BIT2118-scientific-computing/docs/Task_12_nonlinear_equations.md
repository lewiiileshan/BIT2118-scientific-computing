# Task 12: Polynomial and Nonlinear Equation Solving

**Concept:** Nonlinear systems are solved numerically by driving all residuals to zero from an initial guess. Different guesses can lead to different solutions.

**Files:** `code/Task_12_nonlinear_equations.py` (original) and `modified/Task_12_modified_trilateration.py` (modified cases)

## 1. Original program

**Input values:** The circle x squared + y squared = 4 and parabola y = x squared - 1, with initial guesses (1, 1) and (-1, 1).

**Mathematical operations:** scipy.optimize.root on the two residual equations, then printing residuals and the convergence flag.

**Output**

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

**Meaning of the output:** The two intersections are (1.5175, 1.3028) and (-1.5175, 1.3028), reached from the two different starting guesses. Residuals are about 1e-13 and Converged is True. Algebra confirms this: substituting gives y squared + y - 3 = 0, whose only usable root is y = 1.3028.

## 2. Parameter change

**What was changed:** Changed the circle radius to 3 and moved the parabola down to y = x squared - 5.

**How the result changes and why:** With radius 3 the intersections move to (+/-1.8364, 2.3723). With the parabola at y = x squared - 5 and radius 2 there are no real intersections and the solver reports failure, so the success flag must always be checked. np.roots([1, -5, 6]) also confirms the roots 2 and 3 for the polynomial example.

## 3. New real-world case: Locating a phone from cell-tower distances

**Assumptions:** Towers at (0,0), (6,0) and (0,8) km. The phone is truly at (3.75, 3.3072) km and distances are measured exactly (5.0000, 4.0000 and 6.0071 km). Real distances would contain noise.

**Input data:** Tower coordinates and distances; guesses (3, 3) and (3, -3).

**Output of `modified/Task_12_modified_trilateration.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - circle x^2+y^2=r^2 and parabola y=x^2-s
r=2.0, s=1.0: 2 intersection(s): [(1.5175, 1.3028), (-1.5175, 1.3028)]
r=3.0, s=1.0: 2 intersection(s): [(1.8364, 2.3723), (-1.8364, 2.3723)]
r=2.0, s=5.0: 0 intersection(s): []
Polynomial check x^2 - 5x + 6 = 0 -> roots [3. 2.]

PART B - positioning
Distances to towers (km): [5.     4.     6.0071]
Two towers, guess [3.0, 3.0]: position [3.75   3.3072], residual 1.1e-11
Two towers, guess [3.0, -3.0]: position [ 3.75   -3.3072], residual 1.1e-11
Three towers, guess [3.0, 3.0]: position [3.75   3.3072], max residual 1.8e-12
Three towers, guess [3.0, -3.0]: position [3.75   3.3072], max residual 9.8e-10
```

**Interpretation:** Two towers give two mirror-image answers, (3.75, +3.3072) or (3.75, -3.3072), depending on the starting guess, so the position is ambiguous. Adding the third tower removes the ambiguity: both guesses now converge to (3.75, 3.3072). Because there are three equations and two unknowns, least_squares is used instead of root.
