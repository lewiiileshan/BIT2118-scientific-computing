"""Task 14 (modified): curve fitting - growth of mobile-app users (logistic curve).

Part A: change the model used on the original server data (linear vs quadratic vs cubic).
Part B: new case - fit a logistic growth curve to yearly users and forecast the limit.
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

print("PART A - polynomial degree on server data")
for deg in (1, 2, 3):
    coeffs = np.polyfit(users, resp, deg)
    pred = np.polyval(coeffs, users)
    rmse = np.sqrt(np.mean((resp - pred)**2))
    print(f"degree {deg}: RMSE {rmse:.2f} ms, prediction at 400 users {np.polyval(coeffs, 400):.1f} ms")
print("A higher degree always lowers training error, but extrapolation can become unreliable.")

# ---------- Part B: new case ----------
# Assumption: synthetic data generated from a logistic curve with noise (seed fixed).
# True parameters: L=2.0 million users, k=0.9 per year, midpoint t0=5 years.
rng = np.random.default_rng(7)
years = np.arange(0, 11, dtype=float)
true_users = 2.0 / (1 + np.exp(-0.9*(years - 5)))
observed = true_users + rng.normal(0, 0.05, len(years))

def logistic(t, L, k, t0):
    return L / (1 + np.exp(-k*(t - t0)))

def exponential(t, a, b):
    return a*np.exp(b*t)

p_log, cov = curve_fit(logistic, years, observed, p0=[1.5, 0.5, 4.0])
p_exp, _ = curve_fit(exponential, years, observed, p0=[0.1, 0.3], maxfev=10000)

rmse_log = np.sqrt(np.mean((observed - logistic(years, *p_log))**2))
rmse_exp = np.sqrt(np.mean((observed - exponential(years, *p_exp))**2))
err = np.sqrt(np.diag(cov))

print("\nPART B - logistic growth")
print(f"Logistic fit: L={p_log[0]:.3f} (+/-{err[0]:.3f}) million, k={p_log[1]:.3f}, midpoint={p_log[2]:.2f} years")
print(f"RMSE logistic {rmse_log:.3f} vs exponential {rmse_exp:.3f} (million users)")
print(f"Forecast year 15: logistic {logistic(15, *p_log):.2f} M, exponential {exponential(15, *p_exp):.1f} M")

t = np.linspace(0, 15, 300)
plt.scatter(years, observed, label="Observed")
plt.plot(t, logistic(t, *p_log), label="Logistic fit")
plt.plot(t, exponential(t, *p_exp), linestyle="--", label="Exponential fit")
plt.ylim(0, 3)
plt.xlabel("Years since launch")
plt.ylabel("Users (millions)")
plt.title("Growth curve fitting")
plt.legend()
plt.grid(True)
plt.show()
