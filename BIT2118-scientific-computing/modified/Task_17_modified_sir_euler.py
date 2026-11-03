"""Task 17 (modified): Euler method - an SIR epidemic model.

Part A: change the step size h and cooling constant k in the original cooling model.
Part B: new case - SIR model for a school of 1,000 students solved with Euler's method.
"""
import numpy as np
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
def cooling_euler(h, k, T0=90.0, Ta=25.0, end=30.0):
    t = np.arange(0, end + h/2, h)
    T = np.zeros_like(t)
    T[0] = T0
    for i in range(len(t) - 1):
        T[i+1] = T[i] + h * (-k * (T[i] - Ta))
    exact = Ta + (T0 - Ta)*np.exp(-k*t)
    return T[-1], exact[-1]

print("PART A - Euler error for cooling")
for h, k in [(1.0, 0.12), (0.5, 0.12), (0.1, 0.12), (1.0, 0.5), (5.0, 0.5)]:
    e, x = cooling_euler(h, k)
    print(f"h={h}, k={k}: Euler {e:.4f} C, exact {x:.4f} C, error {abs(e-x):.4f} C")
print("Note h=5, k=0.5 gives h*k=2.5 (> 2): each step multiplies the error by (1-h*k) = -1.5, so Euler is unstable.")

# ---------- Part B: new case ----------
# Assumptions: N=1000, beta=0.3 contacts/day, gamma=0.1 recovery/day (R0 = 3), 1 initial infected.
N, beta, gamma = 1000.0, 0.3, 0.1

def sir_euler(h, days=120):
    n = int(round(days / h))
    S = np.zeros(n + 1); I = np.zeros(n + 1); R = np.zeros(n + 1)
    S[0], I[0], R[0] = N - 1, 1, 0
    for i in range(n):
        new_inf = beta * S[i] * I[i] / N
        rec = gamma * I[i]
        S[i+1] = S[i] - h*new_inf
        I[i+1] = I[i] + h*(new_inf - rec)
        R[i+1] = R[i] + h*rec
    t = np.linspace(0, days, n + 1)
    return t, S, I, R

print("\nPART B - SIR epidemic")
print(f"Basic reproduction number R0 = beta/gamma = {beta/gamma:.1f}")
for h in (1.0, 0.1, 0.01):
    t, S, I, R = sir_euler(h)
    print(f"h={h}: peak infected {I.max():.1f} on day {t[I.argmax()]:.1f}, total ever infected {R[-1] + I[-1]:.0f} ({(R[-1]+I[-1])/N:.1%})")

t, S, I, R = sir_euler(0.1)
plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.xlabel("Day")
plt.ylabel("Students")
plt.title("SIR model by Euler method (h = 0.1 day)")
plt.legend()
plt.grid(True)
plt.show()
