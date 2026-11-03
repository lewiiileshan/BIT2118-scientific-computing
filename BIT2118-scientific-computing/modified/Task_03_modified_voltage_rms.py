"""Task 3 (modified): vectorization - RMS voltage of an ADC sensor stream.

Part A: change N (the number of values) and see how the speed-up changes.
Part B: new case - convert 12-bit ADC counts to volts and compute RMS and power.
"""
import timeit
import numpy as np

rng = np.random.default_rng(42)

# ---------- Part A: change the data size ----------
print("PART A - speed-up versus data size")
for n in (10_000, 100_000, 1_000_000):
    data = rng.uniform(5, 250, n)

    def loop_version():
        out = []
        for v in data:
            s = v / 1000.0
            out.append(s ** 2)
        return out

    def vector_version():
        return (data / 1000.0) ** 2

    t_loop = timeit.timeit(loop_version, number=1)
    t_vec = timeit.timeit(vector_version, number=5) / 5
    print(f"N={n:>9,}: loop {t_loop:.4f}s, vectorized {t_vec:.6f}s, speed-up {t_loop/t_vec:.0f}x")

# ---------- Part B: new case ----------
# Assumptions: 12-bit ADC (0-4095 counts) mapped to 0-3.3 V, load resistance 10 ohms,
# 500,000 simulated samples of a 50 Hz sine wave with noise.
N = 500_000
t = np.linspace(0, 1, N)
counts = np.clip(np.round(2048 + 1500*np.sin(2*np.pi*50*t) + rng.normal(0, 20, N)), 0, 4095)

volts = counts / 4095 * 3.3          # vectorized unit conversion
centered = volts - volts.mean()      # remove DC offset
rms = np.sqrt(np.mean(centered**2))  # RMS value
power_w = centered**2 / 10.0         # instantaneous power in a 10 ohm load

print("\nPART B - ADC voltage stream")
print(f"Samples: {N:,}")
print(f"DC offset: {volts.mean():.4f} V")
print(f"RMS voltage: {rms:.4f} V  (ideal sine amplitude/sqrt2 = {1500/4095*3.3/np.sqrt(2):.4f} V)")
print(f"Average power in 10 ohm load: {power_w.mean():.5f} W")
