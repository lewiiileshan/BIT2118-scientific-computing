"""Task 2 (modified): NumPy arrays - greenhouse soil-moisture sensor.

Part A: change an input of the original program (add a +3 C heatwave offset).
Part B: new real-world case - 24 hourly soil-moisture readings (%) from an IoT sensor.
"""
import numpy as np

# ---------- Part A: parameter change on the original weather-station data ----------
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
HEATWAVE_OFFSET = 3.0  # changed parameter: every hour is 3 C hotter
hot = temperatures_c + HEATWAVE_OFFSET

print("PART A - effect of a +3 C offset")
print(f"Original mean: {temperatures_c.mean():.2f} C | Heatwave mean: {hot.mean():.2f} C")
print(f"Original max : {temperatures_c.max():.2f} C | Heatwave max : {hot.max():.2f} C")
print(f"Std deviation unchanged: {temperatures_c.std():.4f} vs {hot.std():.4f}")
print(f"Mean in Fahrenheit: {1.8*temperatures_c.mean()+32:.2f} F -> {1.8*hot.mean()+32:.2f} F")

# ---------- Part B: new case ----------
# Assumption: sensor reads volumetric soil moisture (%) once per hour. Values are illustrative.
moisture = np.array([
    42, 41, 40, 39, 38, 37,
    35, 33, 31, 29, 27, 26,
    25, 24, 24, 26, 30, 36,
    40, 41, 42, 42, 41, 41
], dtype=float)
THRESHOLD = 30.0  # irrigate when moisture drops below this value

below = moisture < THRESHOLD
z_scores = (moisture - moisture.mean()) / moisture.std()  # vectorized standardisation

print("\nPART B - greenhouse soil moisture")
print(f"Mean: {moisture.mean():.2f} %  Min: {moisture.min():.0f} % (hour {moisture.argmin()})  Max: {moisture.max():.0f} %")
print(f"Hours below {THRESHOLD:.0f}% threshold: {below.sum()} -> hours {np.where(below)[0].tolist()}")
print(f"Fraction of day needing irrigation: {below.mean():.1%}")
print(f"Most unusual hour (largest |z|): hour {np.abs(z_scores).argmax()} with z = {z_scores[np.abs(z_scores).argmax()]:.2f}")
