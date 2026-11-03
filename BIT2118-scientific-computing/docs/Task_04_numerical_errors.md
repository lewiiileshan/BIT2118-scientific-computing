# Task 4: Floating-Point Arithmetic and Numerical Errors

**Concept:** Computers store most decimals approximately in binary, so small round-off errors appear and can accumulate. Good code compares with tolerances and avoids unstable formulas.

**Files:** `code/Task_04_numerical_errors.py` (original) and `modified/Task_04_modified_banking_errors.py` (modified cases)

## 1. Original program

**Input values:** The numbers 0.1, 0.2 and 0.3, the approximation 1.414 of the square root of 2, and small values of x (1e-4, 1e-8, 1e-12).

**Mathematical operations:** Exact versus np.isclose comparison, absolute and relative error, and comparison of an unstable formula with its algebraically equivalent stable form.

**Output**

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

**Meaning of the output:** 0.1 + 0.2 equals 0.30000000000000004, so exact comparison is False but np.isclose gives True. The approximation 1.414 has an absolute error of 0.00021356 and a relative error of 0.0151%. For x = 1e-12 the direct formula gives 0.500044450291 while the stable one gives exactly 0.5, so subtracting nearly equal numbers destroyed several digits.

## 2. Parameter change

**What was changed:** Replaced 1.414 with better approximations (1.4142 and 1.41421356) and tried very small tolerances in np.isclose.

**How the result changes and why:** The relative error falls from 0.0151% to 0.0010% and then to about 2e-9 as digits are added. With rtol = 1e-17, np.isclose returns False even for 0.1 + 0.2 versus 0.3, because that tolerance is smaller than the machine precision (about 2.2e-16), so a tolerance must be larger than round-off.

## 3. New real-world case: Accumulated error in a banking ledger and cancellation

**Assumptions:** A ledger adds 0.10 KES one million times (true total 100,000 KES). A second test evaluates (1 - cos x) / x squared for tiny x, whose true limit is 0.5.

**Input data:** One million additions of 0.10, and x = 1e-2, 1e-5, 1e-8.

**Output of `modified/Task_04_modified_banking_errors.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - better approximations give smaller errors
approx=1.414     : absolute=2.14e-04, relative=0.0151%
approx=1.4142    : absolute=1.36e-05, relative=0.0010%
approx=1.41421356: absolute=2.37e-09, relative=0.0000%
np.isclose(0.1+0.2, 0.3) with tolerances:
  rtol=1e-05, atol=0 -> True
  rtol=1e-12, atol=0 -> True
  rtol=1e-17, atol=0 -> False

PART B - accumulated error in a ledger
Naive loop sum      : 100000.000001  (error 1.332883e-06)
math.fsum (exact)   : 100000.000000
np.sum (pairwise)   : 100000.000000
Integer cents total : 100000.00 KES

Cancellation: (1 - cos x)/x^2 should approach 0.5
x=1e-02: direct=0.4999958333, stable=0.4999958333
x=1e-05: direct=0.5000000414, stable=0.5000000000
x=1e-08: direct=0.0000000000, stable=0.5000000000
```

**Interpretation:** The naive loop gives 100000.000001, an error of 1.33e-6 KES from round-off alone. math.fsum, np.sum (pairwise summation) and integer cents all give exactly 100,000.00. This is why financial software stores money as integers or decimals. For x = 1e-8 the direct cancellation formula returns 0.0 (completely wrong) while the half-angle form 2 sin squared (x/2) / x squared gives 0.5.
