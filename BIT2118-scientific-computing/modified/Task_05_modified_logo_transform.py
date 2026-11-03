"""Task 5 (modified): matrix transformations - rotating and shrinking a triangular logo.

Part A: change the angle and scale factors of the original square transformation.
Part B: new case - rotate a logo about ITS OWN CENTRE using 3x3 homogeneous matrices.
"""
import numpy as np


def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])


# ---------- Part A: parameter change ----------
square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
for deg, sx, sy in [(45, 2.0, 1.5), (90, 1.0, 1.0), (45, 2.0, -1.5)]:
    T = rot(deg) @ np.diag([sx, sy])
    out = square @ T.T
    print(f"angle={deg:>3}, scale=({sx},{sy}) -> det={np.linalg.det(T):+.3f}, area of square becomes {abs(np.linalg.det(T)):.3f}")
    print(np.round(out, 3))

# ---------- Part B: new case ----------
# Assumption: logo is a triangle with vertices in pixels. Rotate 30 degrees, scale by 0.5
# about the centroid (translate to origin -> transform -> translate back).
triangle = np.array([[100., 100.], [200., 100.], [150., 187.]])
centroid = triangle.mean(axis=0)

def translate(tx, ty):
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1.0]])

R = np.eye(3); R[:2, :2] = rot(30)
S = np.diag([0.5, 0.5, 1.0])
M = translate(*centroid) @ R @ S @ translate(*(-centroid))

homog = np.hstack([triangle, np.ones((3, 1))])
new_tri = (M @ homog.T).T[:, :2]

def area(p):
    # shoelace formula for a triangle
    (x1, y1), (x2, y2), (x3, y3) = p
    return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

print("\nPART B - logo about its centroid")
print("Centroid before:", np.round(centroid, 2))
print("New vertices:\n", np.round(new_tri, 2))
print("Centroid after :", np.round(new_tri.mean(axis=0), 2), "(unchanged -> pivot works)")
print(f"Area before {area(triangle):.1f}, after {area(new_tri):.1f}, ratio {area(new_tri)/area(triangle):.3f} (expected 0.25 = det of scale)")
