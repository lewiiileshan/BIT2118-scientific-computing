# Task 16: Numerical Integration

**Concept:** Numerical integration approximates an area under a curve. The trapezoidal rule uses straight segments, Simpson's rule uses parabolas.

**Files:** `code/Task_16_numerical_integration.py` (original) and `modified/Task_16_modified_solar_energy.py` (modified cases)

## 1. Original program

**Input values:** Smart-meter power readings every two hours (0.8 to 1.8 kW) over 12 hours.

**Mathematical operations:** np.trapezoid and scipy.integrate.simpson on the power-versus-time data.

**Output**

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

**Meaning of the output:** Estimated energy use is 15.700 kWh (trapezoid) and 15.800 kWh (Simpson), a 0.100 kWh difference. The integral of power over time is energy, so the area under the power curve is the electricity consumed in those 12 hours.

## 2. Parameter change

**What was changed:** Changed the number of sample points on sin(x) over 0 to pi, whose exact integral is 2.

**How the result changes and why:** With 5 points the trapezoid error is 0.104 and Simpson's 0.0046. Doubling the intervals divides the trapezoid error by about 4 (0.0258 at 9 points, 0.0064 at 17) but Simpson's by about 16 (0.00027, 0.000017). More data improves both, and Simpson's improves much faster for smooth data.

## 3. New real-world case: Daily energy from a solar panel

**Assumptions:** Panel area 10 square metres, efficiency 18%, hourly irradiance in W per square metre from 06:00 to 18:00 (20 to 910 W per square metre, illustrative). Power in kW = irradiance x area x efficiency / 1000. A tariff of 25 KES per kWh is assumed.

**Input data:** 13 hourly irradiance readings (12 equal intervals, ideal for Simpson).

**Output of `modified/Task_16_modified_solar_energy.py`** (Part A is the parameter change, Part B is the new case)

```text
PART A - accuracy versus number of points, integral of sin(x) on [0, pi] (exact = 2)
n= 3: trapezoid error 4.29e-01, Simpson error 9.44e-02
n= 5: trapezoid error 1.04e-01, Simpson error 4.56e-03
n= 9: trapezoid error 2.58e-02, Simpson error 2.69e-04
n=17: trapezoid error 6.43e-03, Simpson error 1.66e-05

PART B - solar energy
Peak power: 1.638 kW at 12:00
Energy (trapezoid): 11.2410 kWh
Energy (Simpson)  : 11.2500 kWh
Difference        : 0.0090 kWh
Value at 25 KES/kWh: 281 KES per day
Daily yield per m^2 of panel: 1.125 kWh/m^2
```

**Interpretation:** Peak output is 1.638 kW at 12:00. The day's energy is 11.241 kWh (trapezoid) or 11.250 kWh (Simpson), worth about 281 KES, or 1.125 kWh per square metre of panel. The two rules agree to under 0.01 kWh, so the estimate is stable for this smooth daily curve.
