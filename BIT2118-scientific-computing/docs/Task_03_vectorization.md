# Task 3: Mathematical Functions and Vectorization

**Concept:** Vectorization evaluates a formula on a whole array at once, which is shorter and much faster than looping element by element.

**Files:** `code/Task_03_vectorization.py` (original) and `modified/Task_03_modified_voltage_rms.py` (modified cases)

## 1. Original program

**Input values:** One million simulated latency values between 5 ms and 250 ms (random generator seed 42).

**Mathematical operations:** Convert milliseconds to seconds (divide by 1000) and square each value, once with a Python loop and once with vectorized NumPy. timeit measures both.

**Output**

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1509 s
Vectorized time: 0.0030 s
Approximate speed-up: 49.8x
```

**Meaning of the output:** Both methods give identical numbers (first value 0.0379 s squared). The loop took 0.1509 s and the vectorized code 0.0030 s, a speed-up of about 50 times. Exact timings depend on the computer and vary between runs, but vectorization is always far faster.

## 2. Parameter change

**What was changed:** Changed N, the number of values, from 1,000,000 to 10,000 and 100,000.

**How the result changes and why:** Vectorization won at every size (83x, 18x and 55x in this run). The ratio is not constant because timings of a few milliseconds are noisy and NumPy has a fixed start-up cost per call. The loop time grows roughly linearly with N (0.0020 s, 0.0181 s, 0.1340 s) while the vectorized time stays tiny.

## 3. New real-world case: RMS voltage of an ADC sensor stream

**Assumptions:** A 12-bit analog-to-digital converter (0 to 4095 counts) maps to 0 to 3.3 V. The signal is a 50 Hz sine wave of amplitude 1500 counts plus noise (standard deviation 20 counts), centred at 2048. The load resistor is 10 ohms. 500,000 samples are simulated.

**Input data:** 500,000 integer counts clipped to 0 to 4095.

**Output of `modified/Task_03_modified_voltage_rms.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - speed-up versus data size
N=   10,000: loop 0.0014s, vectorized 0.000020s, speed-up 69x
N=  100,000: loop 0.0172s, vectorized 0.000684s, speed-up 25x
N=1,000,000: loop 0.1630s, vectorized 0.002608s, speed-up 63x

PART B - ADC voltage stream
Samples: 500,000
DC offset: 1.6504 V
RMS voltage: 0.8549 V  (ideal sine amplitude/sqrt2 = 0.8547 V)
Average power in 10 ohm load: 0.07308 W
```

**Interpretation:** Counts convert to volts with one vectorized line. The DC offset is 1.6504 V, close to the expected 1.65 V (half of 3.3 V). The RMS voltage is 0.8549 V, almost equal to the theoretical amplitude divided by the square root of 2 (0.8547 V), so the simulation behaves as theory predicts. The average power in the 10 ohm load is 0.07308 W.
