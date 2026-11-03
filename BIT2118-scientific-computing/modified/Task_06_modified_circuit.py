"""Task 6 (modified): linear systems - mesh-current analysis of a circuit.

Part A: change the observed totals in the server problem.
Part B: new case - three-loop resistor network solved with Kirchhoff's voltage law.
"""
import numpy as np

# ---------- Part A: parameter change ----------
A = np.array([[4.0, 2.0], [8.0, 12.0]])
for cpu, mem in [(20, 72), (26, 76), (20, 80)]:
    x = np.linalg.solve(A, np.array([cpu, mem], dtype=float))
    print(f"Totals CPU={cpu}, MEM={mem} -> Type A={x[0]:.3f}, Type B={x[1]:.3f}")
print("Note: (20, 80) gives non-integer servers, so that observation is inconsistent with whole machines.")

# ---------- Part B: new case ----------
# Assumptions: R1..R5 in ohms; V1 drives loop 1, V2 opposes in loop 3.
R1, R2, R3, R4, R5 = 10.0, 20.0, 15.0, 25.0, 30.0
V1, V2 = 12.0, 5.0

# Mesh currents I1, I2, I3 (A). R2 shared by loops 1-2, R4 shared by loops 2-3.
M = np.array([
    [R1 + R2,   -R2,           0.0],
    [-R2,        R2 + R3 + R4, -R4],
    [0.0,       -R4,            R4 + R5]
])
v = np.array([V1, 0.0, -V2])

I = np.linalg.solve(M, v)
residual = v - M @ I

print("\nPART B - mesh currents")
for k, cur in enumerate(I, start=1):
    print(f"I{k} = {cur*1000:.3f} mA")
print("Residual norm:", np.linalg.norm(residual))
print(f"Condition number of coefficient matrix: {np.linalg.cond(M):.2f}")

# Derived quantity: power dissipated in the shared resistors
print(f"Current through R2 (I1-I2): {(I[0]-I[1])*1000:.3f} mA, power {(I[0]-I[1])**2*R2*1000:.3f} mW")
print(f"Current through R4 (I2-I3): {(I[1]-I[2])*1000:.3f} mA, power {(I[1]-I[2])**2*R4*1000:.3f} mW")
