"""Task 20 (modified): Monte Carlo - probability that a software project finishes on time.

Part A: change N, the standard deviation and the seed in the server-overload simulation.
Part B: new case - three tasks with uncertain durations; probability total <= 32 days.
"""
import numpy as np
import matplotlib.pyplot as plt

# ---------- Part A: parameter change ----------
print("PART A - overload probability (capacity 1000, mean 850)")
print("Exact value for std=120 from the normal distribution: 10.57%")
for N, std, seed in [(1_000, 120, 42), (100_000, 120, 42), (100_000, 120, 7), (100_000, 180, 42)]:
    rng = np.random.default_rng(seed)
    p = (rng.normal(850, std, N) > 1000).mean()
    se = np.sqrt(p*(1-p)/N)
    print(f"N={N:>7,}, std={std}, seed={seed}: p={p:.4%}  (standard error {se:.3%})")

rng = np.random.default_rng(1)
pts = rng.random((200_000, 2))
print(f"Bonus - pi estimate from 200,000 points: {4*np.mean(np.sum(pts**2, axis=1) <= 1):.4f}")

# ---------- Part B: new case ----------
# Assumptions: durations in days follow triangular(min, most likely, max) distributions.
rng = np.random.default_rng(42)
N = 200_000
design = rng.triangular(5, 8, 14, N)
build = rng.triangular(10, 15, 25, N)
test = rng.triangular(4, 6, 12, N)
total = design + build + test

deadline = 32
p_on_time = (total <= deadline).mean()
se = np.sqrt(p_on_time*(1 - p_on_time)/N)

print("\nPART B - project schedule risk")
print(f"Most-likely plan (sum of modes): {8 + 15 + 6} days")
print(f"Mean total: {total.mean():.2f} days, std: {total.std():.2f} days")
print(f"P(finish within {deadline} days) = {p_on_time:.2%} +/- {1.96*se:.2%} (95% interval)")
print(f"80th percentile: {np.percentile(total, 80):.1f} days, 95th percentile: {np.percentile(total, 95):.1f} days")

plt.hist(total, bins=60, alpha=0.8)
plt.axvline(deadline, color="red", linestyle="--", label=f"Deadline {deadline} days")
plt.xlabel("Total project duration (days)")
plt.ylabel("Number of simulations")
plt.title("Monte Carlo project-duration distribution")
plt.legend()
plt.grid(True)
plt.show()
