"""Task 15 (modified): numerical differentiation - step size and train acceleration.

Part A: change the step size h for a known derivative (d/dx sin x = cos x at x=1).
Part B: new case - estimate acceleration of a train from velocity, with and without noise.
"""
import numpy as np
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
x0 = 1.0
exact = np.cos(x0)
print("PART A - error versus step size h")
print(f"{'h':>8} | {'forward error':>14} | {'central error':>14}")
for h in (1e-1, 1e-2, 1e-3, 1e-5, 1e-8, 1e-12):
    fwd = (np.sin(x0 + h) - np.sin(x0)) / h
    cen = (np.sin(x0 + h) - np.sin(x0 - h)) / (2*h)
    print(f"{h:>8.0e} | {abs(fwd-exact):>14.3e} | {abs(cen-exact):>14.3e}")
print("Error falls with h (truncation) until h is so small that round-off dominates.")

# ---------- Part B: new case ----------
# Assumption: train speed (m/s) measured every 5 s while accelerating then cruising.
t = np.arange(0, 61, 5, dtype=float)
v = 30*(1 - np.exp(-t/20))                 # smooth underlying speed
rng = np.random.default_rng(3)
v_noisy = v + rng.normal(0, 0.3, len(t))   # sensor noise of 0.3 m/s

a_true = (30/20)*np.exp(-t/20)
a_clean = np.gradient(v, t)
a_noisy = np.gradient(v_noisy, t)

print("\nPART B - acceleration from speed")
print(f"Mean absolute error, clean data : {np.mean(np.abs(a_clean - a_true)):.4f} m/s^2")
print(f"Mean absolute error, noisy data : {np.mean(np.abs(a_noisy - a_true)):.4f} m/s^2")
print(f"Acceleration at t=0: true {a_true[0]:.3f}, estimated (clean) {a_clean[0]:.3f}, (noisy) {a_noisy[0]:.3f} m/s^2")

plt.plot(t, a_true, label="True acceleration")
plt.plot(t, a_clean, marker="o", label="From clean speed")
plt.plot(t, a_noisy, marker="s", label="From noisy speed")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Train acceleration from speed data")
plt.legend()
plt.grid(True)
plt.show()
