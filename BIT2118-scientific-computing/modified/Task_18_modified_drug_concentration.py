"""Task 18 (modified): solve_ivp - drug concentration after an oral dose.

Part A: change R and C in the RC circuit (time constant tau = R*C).
Part B: new case - one-compartment model with absorption: gut -> blood -> elimination.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
Vs = 5.0
print("PART A - RC circuit, voltage after 1 second")
for R, C in [(1000.0, 0.001), (2000.0, 0.001), (1000.0, 0.0002)]:
    sol = solve_ivp(lambda t, V: [(Vs - V[0])/(R*C)], (0, 5), [0.0],
                    t_eval=np.linspace(0, 5, 501), rtol=1e-9, atol=1e-11)
    v1 = np.interp(1.0, sol.t, sol.y[0])
    print(f"R={R:.0f}, C={C}: tau={R*C:.4f} s, V(1 s)={v1:.4f} V, V(5 s)={sol.y[0,-1]:.4f} V")

# ---------- Part B: new case ----------
# Assumptions: dose 500 mg, volume of distribution 40 L,
# absorption rate ka = 1.2 /h, elimination rate ke = 0.2 /h. A = amount in gut (mg), C = blood conc (mg/L).
dose, Vd, ka, ke = 500.0, 40.0, 1.2, 0.2

def model(t, y):
    A, C = y
    return [-ka*A, ka*A/Vd - ke*C]

t_eval = np.linspace(0, 24, 481)
sol = solve_ivp(model, (0, 24), [dose, 0.0], t_eval=t_eval, rtol=1e-9, atol=1e-12)
C = sol.y[1]

# Analytical solution for validation
C_exact = (dose*ka/(Vd*(ka - ke))) * (np.exp(-ke*t_eval) - np.exp(-ka*t_eval))
t_peak = np.log(ka/ke)/(ka - ke)

print("\nPART B - drug concentration")
print(f"Peak concentration: {C.max():.3f} mg/L at {t_eval[C.argmax()]:.2f} h (analytic tmax = {t_peak:.2f} h)")
print(f"Concentration at 12 h: {np.interp(12, t_eval, C):.3f} mg/L; at 24 h: {C[-1]:.3f} mg/L")
print(f"Maximum difference from analytical solution: {np.max(np.abs(C - C_exact)):.2e} mg/L")
print(f"Elimination half-life: {np.log(2)/ke:.2f} h")

plt.plot(t_eval, C, label="solve_ivp")
plt.plot(t_eval, C_exact, linestyle="--", label="Analytical")
plt.xlabel("Time (h)")
plt.ylabel("Blood concentration (mg/L)")
plt.title("Oral drug concentration over 24 hours")
plt.legend()
plt.grid(True)
plt.show()
