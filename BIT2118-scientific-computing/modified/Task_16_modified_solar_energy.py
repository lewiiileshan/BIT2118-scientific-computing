"""Task 16 (modified): numerical integration - daily energy from a solar panel.

Part A: change the number of sample points on a function with a known integral (sin over 0..pi = 2).
Part B: new case - hourly irradiance converted to panel energy output.
"""
import numpy as np
from scipy.integrate import simpson

# ---------- Part A: parameter change ----------
print("PART A - accuracy versus number of points, integral of sin(x) on [0, pi] (exact = 2)")
for n in (3, 5, 9, 17):
    x = np.linspace(0, np.pi, n)
    y = np.sin(x)
    trap = np.trapezoid(y, x)
    simp = simpson(y, x=x)
    print(f"n={n:>2}: trapezoid error {abs(trap-2):.2e}, Simpson error {abs(simp-2):.2e}")

# ---------- Part B: new case ----------
# Assumptions: panel area 10 m^2, efficiency 18%, irradiance (W/m^2) from 06:00 to 18:00.
hours = np.arange(6, 19, dtype=float)   # 13 readings -> 12 equal intervals (ideal for Simpson)
irradiance = np.array([20, 120, 320, 520, 700, 840, 910, 880, 760, 580, 380, 190, 70], dtype=float)
area, eff = 10.0, 0.18

power_kw = irradiance * area * eff / 1000.0

e_trap = np.trapezoid(power_kw, hours)
e_simp = simpson(power_kw, x=hours)

print("\nPART B - solar energy")
print(f"Peak power: {power_kw.max():.3f} kW at {hours[power_kw.argmax()]:.0f}:00")
print(f"Energy (trapezoid): {e_trap:.4f} kWh")
print(f"Energy (Simpson)  : {e_simp:.4f} kWh")
print(f"Difference        : {abs(e_simp - e_trap):.4f} kWh")
tariff = 25.0  # KES per kWh assumed
print(f"Value at {tariff:.0f} KES/kWh: {e_simp*tariff:.0f} KES per day")
print(f"Daily yield per m^2 of panel: {e_simp/area:.3f} kWh/m^2")
