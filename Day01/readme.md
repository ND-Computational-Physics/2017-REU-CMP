# Introduction to Python

Ben Rose

31 May 2017

!

## Course Site

`nd.edu/~brose3/2017reu-cmp`

- includes installation files, data, notes, schedule, etc.
- will be continually updated during the course

!

## Who are you?

!

## Getting Help

- Google/Stackoverflow 
    - `python3 [thing to search]` 
- Python documentation is very helpful: 
    - docs.python.org/3/
- The interpreter itself: `help(print)`
- External Resources section on the class website

!

# Roadmap

1. Introduction to Python
1. Introduction (continued)
1. Loops and File I/O
1. Special Topics in Standard Python
1. Introduction to NumPy/Matplotlib
1. Numerical Methods
1. Numerical Methods in SciPy
1. Final Project

!

# Let's code!

www.continuum.io/downloads

!

## Math Operations

```
+  -  *  **  /  //  %

import math
math.cos(math.pi)
```

!

## Functions

```
print('Hello, world!')
print(5**3)
len('physics')
```

!

## Variables

```
name = 'Ben'
print(name)
full_name = name + ' Rose'
print('My full name is', full_name)
```

!

## Tired of typing?

We can create a program that we can just run, instead of typing everything in
over and over again.

```python
#!/usr/bin/env python3
""" file.py -- description

Ben Rose
2017-05-31
"""
# code goes here
print(5**2)
```

!

## Your own functions

```
def square_it(number):
    """ description of function
    number : description of arguments
    """
    return number**2
```

