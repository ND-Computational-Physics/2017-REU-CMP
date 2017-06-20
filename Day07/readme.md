# Numerical Methods with SciPy

Ben Rose

20 June 2017

!

# Review

1. Trapezoid rule
2. Simpson's rule
3. Newton's Method
4. secant method

!

# Main Topics in Computational Methods

1. Integration
1. Linear Algebra
1. Root Finding
1. Differential Equations

!

## Don't reinvent the wheel!

This runs counter to what we just did last class...

`scipy` has *everything* implemented already

You will often import a submodule via `from scipy import <something_else>`

!

## What we did previously...

Integration:

- `scipy.integrate` has the methods we need
- Also works for ODE solving

Root finding:

- `scipy.optimize` has this (and a whole lot more!)

!

## What we can do now...

Curve fitting:

- still in `scipy.optimize`...

Linear Algebra (won't talk about today):

- `scipy.linalg` (use arrays for matrices)

And more!

!

## Lets Practice

- Example fitting code
- Fit the double Gaussian with `fitting.py`
- You can bring some research data on Thursday if you want.
