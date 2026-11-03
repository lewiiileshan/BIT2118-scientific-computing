"""Task 9 (modified): eigenvectors - PageRank for a small website.

Part A: change the network (add/remove links) and see how importance shifts.
Part B: new case - directed page links with damping 0.85, solved by eig and power iteration.
"""
import numpy as np


def centrality(adj):
    vals, vecs = np.linalg.eig(adj)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum()


# ---------- Part A: parameter change ----------
base = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]], dtype=float)
more = base.copy()
more[0, 3] = more[3, 0] = 1       # add link A-D
less = base.copy()
less[1, 2] = less[2, 1] = 0       # remove link B-C

print("PART A - eigenvector centrality of nodes A,B,C,D")
for name, M in [("original", base), ("add A-D", more), ("remove B-C", less)]:
    lam, c = centrality(M)
    print(f"{name:<11}: lambda={lam:.4f}, scores={np.round(c, 4)}")

# ---------- Part B: new case ----------
# Assumption: 5 pages. links[i] = pages that page i links TO.
pages = ["Home", "News", "Shop", "Blog", "Contact"]
links = {0: [1, 2, 3], 1: [0, 3], 2: [0, 4], 3: [0, 1, 4], 4: [0]}
n = len(pages)
d = 0.85

H = np.zeros((n, n))                  # column-stochastic link matrix
for j, outs in links.items():
    for i in outs:
        H[i, j] = 1.0 / len(outs)

G = d * H + (1 - d) / n * np.ones((n, n))     # Google matrix

vals, vecs = np.linalg.eig(G)
k = np.argmax(np.real(vals))
pr = np.abs(np.real(vecs[:, k]))
pr /= pr.sum()

r = np.ones(n) / n                     # power iteration
for it in range(1, 200):
    r_new = G @ r
    if np.linalg.norm(r_new - r, 1) < 1e-12:
        break
    r = r_new

print("\nPART B - PageRank")
print(f"Dominant eigenvalue of G: {np.real(vals[k]):.6f} (should be 1)")
for p, a, b in sorted(zip(pages, pr, r), key=lambda t: -t[1]):
    print(f"{p:<8}: eig={a:.4f}  power-iteration={b:.4f}")
print(f"Power iteration converged in {it} iterations; difference from eig: {np.max(np.abs(pr - r)):.2e}")
