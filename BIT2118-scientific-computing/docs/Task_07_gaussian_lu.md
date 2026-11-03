# Task 7: Gaussian Elimination and LU Decomposition

**Concept:** LU decomposition factors A once into lower and upper triangular matrices so that many right-hand sides can be solved cheaply.

**Files:** `code/Task_07_gaussian_lu.py` (original) and `modified/Task_07_modified_heat_rod_lu.py` (modified cases)

## 1. Original program

**Input values:** A 3x3 tridiagonal matrix A and three different measurement vectors b.

**Mathematical operations:** lu_factor(A) once, then lu_solve for each b, with a residual check and a comparison to np.linalg.solve.

**Output**

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

**Meaning of the output:** The first set gives x = (5, 5, 5), matching the direct solver. The other two sets give (5.317, 5.268, 4.756) and (4.902, 5.610, 5.537). All residual norms are about 1e-15, so the solutions are accurate to machine precision.

## 2. Parameter change

**What was changed:** Reduced the diagonal value of A from 4.0 to 2.5 and 2.05 (the last diagonal entry is one less) while keeping the same b.

**How the result changes and why:** The condition number rises from 2.39 to 5.37 and 13.29, and the solution grows from (5,5,5) to (28.8, 44.0, 51.4). As the matrix approaches singularity, the same input produces larger, more error-sensitive outputs, which is why condition numbers matter.

## 3. New real-world case: Implicit time-stepping of heat diffusion in a metal rod

**Assumptions:** A rod is split into 300 points; the diffusion number r = alpha dt / dx squared is 0.4; the ends are held at 0 C; initially the middle third is at 100 C. Each time step solves (I + r L) u_new = u_old with the same matrix for 400 steps.

**Input data:** A 300x300 tridiagonal matrix and an initial temperature vector.

**Output of `modified/Task_07_modified_heat_rod_lu.py`** (Part A is the parameter change, Part B is the new case)

```text
diag=4.0: solution=[5. 5. 5.], cond(A)=2.39
diag=2.5: solution=[12.3256 15.814  17.2093], cond(A)=5.37
diag=2.05: solution=[28.7877 44.0149 51.4427], cond(A)=13.29
Smaller diagonal -> larger condition number -> solution more sensitive to errors.

PART B - heat diffusion with implicit stepping
Max temperature: start 100.0 C -> after 400 steps 99.47 C
Max difference between LU and np.linalg.solve results: 0.00e+00
Time with LU reuse (factor once): 0.0120 s (plus one factorisation)
Time re-solving every step     : 0.4523 s
Approximate saving: 37.8x
```

**Interpretation:** The peak temperature falls from 100 C to 99.47 C as heat spreads outwards. Re-using the LU factors gives results identical to calling np.linalg.solve each step (maximum difference 0), yet it took 0.0112 s instead of 0.4150 s, about 37 times faster. Times vary by machine, and the one-time factorisation cost is small compared to 400 solves.
