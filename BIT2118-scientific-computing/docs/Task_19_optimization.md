# Task 19: Numerical Optimization

**Concept:** Optimisation finds inputs that minimise (or maximise) an objective subject to constraints and bounds.

**Files:** `code/Task_19_optimization.py` (original) and `modified/Task_19_modified_production_plan.py` (modified cases)

## 1. Original program

**Input values:** Cost per unit A = 12 and B = 18; capacity per unit A = 100 and B = 170; at least 1000 capacity.

**Mathematical operations:** scipy.optimize.minimize with SLSQP, plus an integer search for whole servers.

**Output**

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution (cost, A, B, capacity): (108, 0, 6, 1020)
```

**Meaning of the output:** The cheapest plan uses only Type B: 5.882 units, total capacity 1000, cost 105.88. B is cheaper per unit of capacity (18/170 = 0.106 versus 12/100 = 0.120). If whole servers are needed, 6 Type B servers cost 108 and give capacity 1020.

## 2. Parameter change

**What was changed:** Raised the capacity requirement to 1500, and separately cut the Type A cost to 9.

**How the result changes and why:** With 1500 capacity the plan scales to 8.82 Type B units (cost 158.82; 9 whole servers cost 162). With cost A = 9 the cost per capacity unit of A (0.090) is now below B (0.106), so the optimum jumps entirely to 10 units of A at cost 90. The optimal solution can switch abruptly when the cost ratio crosses a threshold.

## 3. New real-world case: Production plan for a furniture workshop

**Assumptions:** Profit is 70 per table and 50 per chair (currency units). A table needs 4 wood units and 2 labour hours; a chair needs 3 wood units and 1 labour hour. Available: 240 wood units and 100 labour hours. We maximise profit, so the objective is negated for minimize.

**Input data:** Two constraints and non-negative bounds; the answer is checked with scipy.optimize.linprog.

**Output of `modified/Task_19_modified_production_plan.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - cloud allocation
original      : continuous A=0.00, B=5.88, cost 105.88 | best integer (cost,A,B) = (108, 0, 6)
need 1500     : continuous A=0.00, B=8.82, cost 158.82 | best integer (cost,A,B) = (162, 0, 9)
A cheaper (9) : continuous A=10.00, B=0.00, cost 90.00 | best integer (cost,A,B) = (90, 10, 0)

PART B - production plan
SLSQP : tables=30.000, chairs=40.000, profit=4100.00
linprog: tables=30.000, chairs=40.000, profit=4100.00
Wood used: 240.0/240, labour used: 100.0/100 (both constraints are binding)
Compare only tables: profit 3500
Compare only chairs: profit 4000
```

**Interpretation:** The best plan is 30 tables and 40 chairs for a profit of 4100, found identically by SLSQP and linprog. Both resources are completely used (wood 240/240, labour 100/100), so they are the bottlenecks. Making only tables gives 3500 and only chairs gives 4000, so a mixed plan is better.
