# Task 9: Eigenvalues and Eigenvectors

**Concept:** An eigenvector keeps its direction under the matrix and is only scaled by its eigenvalue (Av = lambda v). The dominant eigenvector measures influence in a network.

**Files:** `code/Task_09_eigenvalues.py` (original) and `modified/Task_09_modified_pagerank.py` (modified cases)

## 1. Original program

**Input values:** A 4x4 adjacency matrix for nodes A, B, C, D (A and D link to B and C; B and C link to all others).

**Mathematical operations:** np.linalg.eig, selection of the dominant eigenvalue, normalisation of its eigenvector, and verification of Av = lambda v.

**Output**

```text
All eigenvalues: [ 2.5616 -0.     -1.5616 -1.    ]
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

**Meaning of the output:** The dominant eigenvalue is 2.5616. Nodes B and C score 0.2808 and nodes A and D score 0.2192, because B and C have three connections while A and D have two. The verification error is 1.5e-15, so the eigenpair is correct.

## 2. Parameter change

**What was changed:** Added a link between A and D, then separately removed the link between B and C.

**How the result changes and why:** Adding A-D makes every node connected to every other, so the dominant eigenvalue becomes 3 and all scores equal 0.25. Removing B-C leaves a four-node ring with eigenvalue 2 and equal scores. Symmetry gives equal importance, and for a regular network the dominant eigenvalue equals the number of links per node.

## 3. New real-world case: PageRank for a five-page website

**Assumptions:** Pages Home, News, Shop, Blog and Contact. Links: Home to News, Shop and Blog; News to Home and Blog; Shop to Home and Contact; Blog to Home, News and Contact; Contact to Home. Damping factor 0.85 (the surfer follows a link 85% of the time and jumps randomly otherwise).

**Input data:** A column-stochastic link matrix H and Google matrix G = 0.85 H + 0.15/5 (all ones).

**Output of `modified/Task_09_modified_pagerank.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - eigenvector centrality of nodes A,B,C,D
original   : lambda=2.5616, scores=[0.2192 0.2808 0.2808 0.2192]
add A-D    : lambda=3.0000, scores=[0.25 0.25 0.25 0.25]
remove B-C : lambda=2.0000, scores=[0.25 0.25 0.25 0.25]

PART B - PageRank
Dominant eigenvalue of G: 1.000000 (should be 1)
Home    : eig=0.3412  power-iteration=0.3412
Blog    : eig=0.2052  power-iteration=0.2052
News    : eig=0.1848  power-iteration=0.1848
Contact : eig=0.1420  power-iteration=0.1420
Shop    : eig=0.1267  power-iteration=0.1267
Power iteration converged in 37 iterations; difference from eig: 2.09e-13
```

**Interpretation:** Home ranks first (0.3412) because every other page links to it, followed by Blog (0.2052), News (0.1848), Contact (0.1420) and Shop (0.1267). The dominant eigenvalue of G is exactly 1, as theory requires for a probability matrix. Power iteration reaches the same ranking in 37 iterations, matching np.linalg.eig to 2e-13, and is the method used for very large networks.
