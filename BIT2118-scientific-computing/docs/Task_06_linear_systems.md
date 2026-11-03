# Task 6: Solution of Systems of Linear Equations

**Concept:** A system Ax = b is solved for the unknown vector x. np.linalg.solve uses LU factorisation internally and is preferred to computing the inverse.

**Files:** `code/Task_06_linear_systems.py` (original) and `modified/Task_06_modified_circuit.py` (modified cases)

## 1. Original program

**Input values:** A = [[4,2],[8,12]] (CPU and memory per server type) and b = [20, 72] (observed CPU and memory totals).

**Mathematical operations:** np.linalg.solve(A, b), then verification with A @ x and the residual b - A @ x.

**Output**

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

**Meaning of the output:** The solution is 3 servers of Type A and 4 of Type B. Check: 4(3) + 2(4) = 20 CPU and 8(3) + 12(4) = 72 GB. The residual is zero, confirming the answer.

## 2. Parameter change

**What was changed:** Changed the observed totals b to (26, 76) and (20, 80).

**How the result changes and why:** With (26, 76) the solution becomes 5 servers of A and 3 of B. With (20, 80) it becomes 2.5 and 5, which cannot be whole servers, so that pair of measurements is inconsistent with the physical situation (a measurement or modelling error). The solution is linear in b, so small changes in the totals change the answer proportionally.

## 3. New real-world case: Mesh-current analysis of a three-loop resistor circuit

**Assumptions:** R1 = 10, R2 = 20, R3 = 15, R4 = 25 and R5 = 30 ohms; source V1 = 12 V drives loop 1 and V2 = 5 V opposes in loop 3. R2 is shared by loops 1 and 2, and R4 by loops 2 and 3. Kirchhoff's voltage law gives three equations.

**Input data:** A 3x3 resistance matrix [[30,-20,0],[-20,60,-25],[0,-25,55]] and voltage vector [12, 0, -5].

**Output of `modified/Task_06_modified_circuit.py`** (Part A is the parameter change, Part B is the new case)

```text
Totals CPU=20, MEM=72 -> Type A=3.000, Type B=4.000
Totals CPU=26, MEM=76 -> Type A=5.000, Type B=3.000
Totals CPU=20, MEM=80 -> Type A=2.500, Type B=5.000
Note: (20, 80) gives non-integer servers, so that observation is inconsistent with whole machines.

PART B - mesh currents
I1 = 508.155 mA
I2 = 162.232 mA
I3 = -17.167 mA
Residual norm: 2.0196621902627922e-15
Condition number of coefficient matrix: 5.48
Current through R2 (I1-I2): 345.923 mA, power 2393.251 mW
Current through R4 (I2-I3): 179.399 mA, power 804.601 mW
```

**Interpretation:** The mesh currents are I1 = 508.155 mA, I2 = 162.232 mA and I3 = -17.167 mA; the negative sign means loop 3 current flows opposite to the assumed direction. The residual is about 2e-15 and the condition number is only 5.48, so the answer is reliable. The current through shared R2 is 345.923 mA (2393 mW) and through R4 is 179.399 mA (805 mW).
