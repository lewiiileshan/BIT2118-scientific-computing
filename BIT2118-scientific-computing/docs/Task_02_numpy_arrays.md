# Task 2: NumPy Arrays and Numerical Computation

**Concept:** An array stores many numbers in one object, and NumPy applies an operation to every element without a Python loop.

**Files:** `code/Task_02_numpy_arrays.py` (original) and `modified/Task_02_modified_greenhouse.py` (modified cases)

## 1. Original program

**Input values:** A 24-element array of hourly temperatures in degrees Celsius (17.5 C to 29.4 C).

**Mathematical operations:** np.mean, np.min and np.max summarise the day. The vectorized formula F = 1.8C + 32 converts all 24 values in one expression.

**Output**

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

**Meaning of the output:** The day averages 23.12 C, with a low of 17.50 C in the early morning and a peak of 29.40 C around midday. The first six Fahrenheit values (65.3 F down to 63.5 F and back up to 66.2 F) show the same overnight dip, only on a different scale.

## 2. Parameter change

**What was changed:** Added a constant offset of +3 C to every reading to simulate a heatwave.

**How the result changes and why:** The mean rises from 23.12 C to 26.12 C and the maximum from 29.40 C to 32.40 C, exactly the 3 C added. The standard deviation stays at 4.1742 C because shifting every value by the same amount moves the data but not its spread. In Fahrenheit the mean moves from 73.62 F to 79.02 F, a rise of 5.4 F, because 3 C equals 3 x 1.8 F.

## 3. New real-world case: Greenhouse soil-moisture monitoring

**Assumptions:** A sensor reports volumetric soil moisture (%) once per hour. The 24 values are illustrative, not measured. Crops need irrigation when moisture falls below 30%.

**Input data:** 24 hourly moisture values from 24% to 42%, and a threshold of 30%.

**Output of `modified/Task_02_modified_greenhouse.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - effect of a +3 C offset
Original mean: 23.12 C | Heatwave mean: 26.12 C
Original max : 29.40 C | Heatwave max : 32.40 C
Std deviation unchanged: 4.1742 vs 4.1742
Mean in Fahrenheit: 73.62 F -> 79.02 F

PART B - greenhouse soil moisture
Mean: 34.58 %  Min: 24 % (hour 13)  Max: 42 %
Hours below 30% threshold: 7 -> hours [9, 10, 11, 12, 13, 14, 15]
Fraction of day needing irrigation: 29.2%
Most unusual hour (largest |z|): hour 13 with z = -1.63
```

**Interpretation:** Mean moisture is 34.58%. The driest hour is hour 13 (24%). Seven hours (9 to 15) fall below the threshold, which is 29.2% of the day, so irrigation should be scheduled in the late morning. The z-score of -1.63 at hour 13 confirms that is the most unusual reading. Boolean masks (moisture < 30) and vectorized z-scores replace what would otherwise be several loops.
