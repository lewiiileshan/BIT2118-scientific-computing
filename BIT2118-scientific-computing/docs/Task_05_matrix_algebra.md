# Task 5: Matrix Algebra and Matrix Operations

**Concept:** Matrix multiplication applies a linear transformation (rotation, scaling, reflection) to many points consistently. The determinant gives the area scale factor.

**Files:** `code/Task_05_matrix_algebra.py` (original) and `modified/Task_05_modified_logo_transform.py` (modified cases)

## 1. Original program

**Input values:** Four corners of the unit square, a 45 degree rotation matrix and a scaling matrix (x by 2, y by 1.5).

**Mathematical operations:** Combine the matrices with @ (rotation @ scale), transform all points with a single product with the transpose, and compute the determinant.

**Output**

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

**Meaning of the output:** The point (1, 0) becomes (1.414, 1.414): it is stretched to x = 2 and then turned 45 degrees. The determinant is 3.0 (2 x 1.5), so the transformed shape has three times the area of the unit square. Order matters: rotation @ scale first scales and then rotates.

## 2. Parameter change

**What was changed:** Changed the angle and scale factors: 90 degrees with no scaling, and a negative y scale (-1.5).

**How the result changes and why:** A pure 90 degree rotation has determinant 1, so the area is unchanged. With a y scale of -1.5 the determinant becomes -3.0: the area still triples, but the negative sign means the shape is mirrored (its orientation is reversed).

## 3. New real-world case: Rotating and shrinking a triangular logo about its own centre

**Assumptions:** The logo is a triangle with vertices at (100,100), (200,100) and (150,187) pixels. It is rotated by 30 degrees and scaled by 0.5 about its centroid, which needs a translation. Translation is not a 2x2 matrix, so 3x3 homogeneous coordinates are used.

**Input data:** Three vertex coordinates, a 3x3 matrix M = T(centroid) @ R @ S @ T(-centroid).

**Output of `modified/Task_05_modified_logo_transform.py`** (Part A is the parameter change, Part B is the new case)

```text
angle= 45, scale=(2.0,1.5) -> det=+3.000, area of square becomes 3.000
[[ 0.     0.   ]
 [ 1.414  1.414]
 [ 0.354  2.475]
 [-1.061  1.061]]
angle= 90, scale=(1.0,1.0) -> det=+1.000, area of square becomes 1.000
[[ 0.  0.]
 [ 0.  1.]
 [-1.  1.]
 [-1.  0.]]
angle= 45, scale=(2.0,-1.5) -> det=-3.000, area of square becomes 3.000
[[ 0.     0.   ]
 [ 1.414  1.414]
 [ 2.475  0.354]
 [ 1.061 -1.061]]

PART B - logo about its centroid
Centroid before: [150. 129.]
New vertices:
 [[135.6  103.94]
 [178.9  128.94]
 [135.5  154.11]]
Centroid after : [150. 129.] (unchanged -> pivot works)
Area before 4350.0, after 1087.5, ratio 0.250 (expected 0.25 = det of scale)
```

**Interpretation:** The centroid stays at (150, 129), proving the logo pivots around itself. The area drops from 4350 to 1087.5, a ratio of 0.25 which equals 0.5 squared (the determinant of the scaling part); the rotation contributes a determinant of 1. One combined matrix transforms every vertex, which is how graphics engines apply many transformations efficiently.
