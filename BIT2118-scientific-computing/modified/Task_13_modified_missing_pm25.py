"""Task 13 (modified): interpolation - filling missing air-quality readings.

Part A: change the query time and compare interpolation types on the original data.
Part B: new case - PM2.5 sensor loses three readings; test methods by hiding known values.
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear = interp1d(hours, temp)
cubic = CubicSpline(hours, temp)

print("PART A - original temperature data, different query times")
for t in (8.5, 10.5, 12.5, 13.75):
    print(f"t={t}: linear {float(linear(t)):.3f} C, cubic {float(cubic(t)):.3f} C, difference {abs(float(linear(t))-float(cubic(t))):.3f}")
try:
    linear(15.0)
except ValueError:
    print("t=15.0 (outside 8-14): ValueError - interpolation does not extrapolate by default")

# ---------- Part B: new case ----------
# Assumption: hourly PM2.5 (ug/m3) from 06:00 to 18:00 (illustrative values).
h = np.arange(6, 19, dtype=float)
pm = np.array([22, 30, 48, 65, 58, 44, 36, 31, 29, 33, 45, 62, 54], dtype=float)

hidden_idx = np.array([3, 6, 10])       # pretend 09:00, 12:00, 16:00 are missing
keep = np.ones(len(h), bool)
keep[hidden_idx] = False

methods = {
    "Linear": interp1d(h[keep], pm[keep]),
    "Cubic spline": CubicSpline(h[keep], pm[keep]),
    "PCHIP": PchipInterpolator(h[keep], pm[keep]),
}

print("\nPART B - recovering hidden PM2.5 values")
print("True hidden values:", pm[hidden_idx])
for name, fn in methods.items():
    est = fn(h[hidden_idx])
    rmse = np.sqrt(np.mean((est - pm[hidden_idx])**2))
    print(f"{name:<13}: estimates {np.round(est, 1)}, RMSE {rmse:.2f}")

fine = np.linspace(6, 18, 300)
plt.scatter(h[keep], pm[keep], label="Recorded")
plt.scatter(h[hidden_idx], pm[hidden_idx], marker="x", color="red", label="Hidden true values")
for name, fn in methods.items():
    plt.plot(fine, fn(fine), label=name)
plt.xlabel("Hour of day")
plt.ylabel("PM2.5 (ug/m3)")
plt.title("Filling missing air-quality readings")
plt.legend()
plt.grid(True)
plt.show()
