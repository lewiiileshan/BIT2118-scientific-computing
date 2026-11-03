# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Concept:** Newton-Raphson uses the derivative to jump toward a root; the secant method estimates the slope from two earlier points. Both converge quickly from a good start.

**Files:** `code/Task_11_newton_secant.py` (original) and `modified/Task_11_modified_loan_rate.py` (modified cases)

## 1. Original program

**Input values:** Cash flows [-10000, 3000, 3500, 4000, 2500], starting guess 0.10 for Newton and 0.05 and 0.20 for secant.

**Mathematical operations:** Find the rate that makes the net present value zero (the internal rate of return).

**Output**

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
Newton iterations: 4, Secant iterations: 7
NPV at Newton solution: 0.000000
```

**Meaning of the output:** Both methods give an IRR of 11.542461%, and the NPV there is zero. Newton needed 4 iterations and secant 7. The project is worthwhile if the required return is below about 11.5%.

## 2. Parameter change

**What was changed:** Changed the cash inflows to larger values and started Newton from a far-away guess of 0.90.

**How the result changes and why:** Larger inflows raise the IRR to 25.4137%. Starting Newton at 0.90 converged to -154.411%, a mathematically valid root but financially meaningless (below -100%), while the secant method still found 11.5425%. Newton depends on its starting point, so results must be checked for sense.

## 3. New real-world case: True interest rate of a loan

**Assumptions:** A loan of 200,000 KES is repaid in 24 equal monthly payments of 10,500 KES. The monthly rate r satisfies P = pmt (1 - (1+r)^-n) / r.

**Input data:** P = 200000, pmt = 10500, n = 24; starting guess 0.02 (Newton) and 0.005, 0.04 (secant).

**Output of `modified/Task_11_modified_loan_rate.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - IRR with different inputs
original           : Newton 11.5425% (4 its), secant 11.5425% (7 its)
larger inflows     : Newton 25.4137% (6 its), secant 25.4137% (7 its)
far starting guess : Newton -154.4110% (12 its), secant 11.5425% (7 its)

PART B - loan rate
Total repaid: 252,000 KES; interest paid: 52,000 KES
Monthly rate - Newton: 1.937918% (4 its), secant: 1.937918% (7 its), bisection: 1.937918% (45 its)
Nominal annual rate (x12): 23.255%
Effective annual rate: 25.901%
Check: payment from rate = 10500.00 KES
```

**Interpretation:** The monthly rate is 1.937918%, giving a nominal annual rate of 23.255% and an effective annual rate of 25.901%. Total repayment is 252,000 KES, so 52,000 KES is interest. Newton needed 4 iterations, secant 7, and bisection 45. Substituting r back gives a payment of exactly 10,500.00 KES.
