# Practice Python with Numerical Methods

Benjamin Rose

`brose3@nd.edu`

16 June 2017

!

# Goals

Practice

1. Be able to code your own function integrator
2. Be able to code up a working root finder

!

# Review 

Sunspots moving average example

!

## "Main" Topics in Computational Methods

1. Integration
1. Linear Algebra
1. Root Finding
1. Differential Equations

Explore these on your own too, since we won't be able to cover everything...

!

## "Main" Topics in Computational Methods

1. **Integration**
1. Linear Algebra
1. **Root Finding** (we've done this before)
1. Differential Equations

Explore these on your own too, since we won't be able to cover everything...

!

# Integration

!

## Trapezoid method

1. Divide your interval into some number of sub-intervals

1. Each sub interval is a trapezoid, connecting the two points on the graph

```python
trap = dx * (f(x + dx) + f(x)) / 2
```

!

## Simpson's 3/8 rule

```python
h = (b - a) / 3
factor = (f(a) +
          3*f((2*a + b) / 3) +
          3*f((a + 2*b) / 3) +
          f(b))
integral = (3 * h / 8) * factor
```

!

## Simpson's 3/8 rule (for n intervals)

```python
h = (b - a) / n
xi = a + i*h
integral = 3*h/8 * (
                f(x0) + 3f(x1) + 
               3f(x2) + 2f(x3) + 3f(x4) +
                ... + f(xn) )
```
This only works if `n` is a multiple of 3

!

# Root Finding

We already looked at bisection

!

## Alternatives to bisection

- Newton's method (if we know the functional form of the derivative)

```python
x1 = x0 - f(x0)/df(x0)
```

- Secant method (if we don't)

```python
x2 = x1 - f(x1) *
     (x1 - x0)/(f(x1) - f(x0))
```

!

# Practice

* Handout
* One more week of classes
* Office hours Tuesday 3pm in NSH 186