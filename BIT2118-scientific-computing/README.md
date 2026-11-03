# BIT 2118 Scientific Computing - Group Work Tasks 2 to 20

Name: ____________________  Registration number: ____________________

This repository holds the programs, outputs and documentation for the BIT 2118 group work. For every task the documentation identifies the inputs and operations, changes a parameter and explains the effect, interprets the output and graphs, and adapts the program to a different real-world case.

## Structure

| Folder | Contents |
|---|---|
| `code/` | The original programs from the brief (Task_02 to Task_20) |
| `modified/` | One modified program per task: Part A changes a parameter, Part B solves a new real-world case |
| `outputs/` | Captured text output of every program (`original/`, `modified/`) |
| `figures/` | Plots saved from the programs that draw graphs |
| `docs/` | One documentation file per task |
| `run_all.py` | Runs every program in a folder without a display and saves outputs and plots |

## Run

```bash
pip install numpy scipy matplotlib
python code/Task_02_numpy_arrays.py          # run a single program
python run_all.py code outputs/original      # run all original programs
python run_all.py modified outputs/modified  # run all modified programs
```

Requires NumPy 2.x (the programs use `np.trapezoid`). Timing results in Tasks 3 and 7 depend on the computer.

## Tasks

| Task | Topic | Original program | Modified case | Documentation |
|---|---|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | `code/Task_02_numpy_arrays.py` | Greenhouse soil-moisture monitoring | [docs/Task_02_numpy_arrays.md](docs/Task_02_numpy_arrays.md) |
| 3 | Mathematical Functions and Vectorization | `code/Task_03_vectorization.py` | RMS voltage of an ADC sensor stream | [docs/Task_03_vectorization.md](docs/Task_03_vectorization.md) |
| 4 | Floating-Point Arithmetic and Numerical Errors | `code/Task_04_numerical_errors.py` | Accumulated error in a banking ledger and cancellation | [docs/Task_04_numerical_errors.md](docs/Task_04_numerical_errors.md) |
| 5 | Matrix Algebra and Matrix Operations | `code/Task_05_matrix_algebra.py` | Rotating and shrinking a triangular logo about its own centre | [docs/Task_05_matrix_algebra.md](docs/Task_05_matrix_algebra.md) |
| 6 | Solution of Systems of Linear Equations | `code/Task_06_linear_systems.py` | Mesh-current analysis of a three-loop resistor circuit | [docs/Task_06_linear_systems.md](docs/Task_06_linear_systems.md) |
| 7 | Gaussian Elimination and LU Decomposition | `code/Task_07_gaussian_lu.py` | Implicit time-stepping of heat diffusion in a metal rod | [docs/Task_07_gaussian_lu.md](docs/Task_07_gaussian_lu.md) |
| 8 | Iterative Methods for Linear Systems | `code/Task_08_iterative_linear.py` | Temperature profile through a furnace wall | [docs/Task_08_iterative_linear.md](docs/Task_08_iterative_linear.md) |
| 9 | Eigenvalues and Eigenvectors | `code/Task_09_eigenvalues.py` | PageRank for a five-page website | [docs/Task_09_eigenvalues.md](docs/Task_09_eigenvalues.md) |
| 10 | Root Finding: Bisection and Fixed-Point Methods | `code/Task_10_bisection_fixed_point.py` | Break-even quantities with a falling price | [docs/Task_10_bisection_fixed_point.md](docs/Task_10_bisection_fixed_point.md) |
| 11 | Root Finding: Newton-Raphson and Secant Methods | `code/Task_11_newton_secant.py` | True interest rate of a loan | [docs/Task_11_newton_secant.md](docs/Task_11_newton_secant.md) |
| 12 | Polynomial and Nonlinear Equation Solving | `code/Task_12_nonlinear_equations.py` | Locating a phone from cell-tower distances | [docs/Task_12_nonlinear_equations.md](docs/Task_12_nonlinear_equations.md) |
| 13 | Interpolation | `code/Task_13_interpolation.py` | Recovering missing PM2.5 air-quality readings | [docs/Task_13_interpolation.md](docs/Task_13_interpolation.md) |
| 14 | Curve Fitting and Approximation | `code/Task_14_curve_fitting.py` | Logistic growth of a mobile app's user base | [docs/Task_14_curve_fitting.md](docs/Task_14_curve_fitting.md) |
| 15 | Numerical Differentiation | `code/Task_15_numerical_differentiation.py` | Train acceleration from speed measurements | [docs/Task_15_numerical_differentiation.md](docs/Task_15_numerical_differentiation.md) |
| 16 | Numerical Integration | `code/Task_16_numerical_integration.py` | Daily energy from a solar panel | [docs/Task_16_numerical_integration.md](docs/Task_16_numerical_integration.md) |
| 17 | Ordinary Differential Equations - Euler Method | `code/Task_17_euler_ode.py` | SIR epidemic in a school of 1,000 students | [docs/Task_17_euler_ode.md](docs/Task_17_euler_ode.md) |
| 18 | Numerical Solution of ODEs Using SciPy | `code/Task_18_scipy_ode.py` | Drug concentration after an oral dose | [docs/Task_18_scipy_ode.md](docs/Task_18_scipy_ode.md) |
| 19 | Numerical Optimization | `code/Task_19_optimization.py` | Production plan for a furniture workshop | [docs/Task_19_optimization.md](docs/Task_19_optimization.md) |
| 20 | Random Numbers and Monte Carlo Methods | `code/Task_20_monte_carlo.py` | Probability that a software project finishes on time | [docs/Task_20_monte_carlo.md](docs/Task_20_monte_carlo.md) |

## Notes

- Data in the new real-world cases are illustrative or synthetic (generated with fixed random seeds) unless stated otherwise. They show the method, not measured facts.
- Task 1 in the brief is the self-paced prerequisite course and has no program.
