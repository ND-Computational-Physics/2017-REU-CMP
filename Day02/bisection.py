""" bisection.py -- bisection demo for first class

    Language: Python 3
    Mark A. Caprio
    University of Notre Dame
    Written for Computational Methods in Physics, Spring 2014.
    Last modified January 12, 2015.
"""

# read in external libraries
import math

# define function for rootfinding
def f(x):
    return math.cos(x) - x

# define tolerance on final result (hence number of bisections)
tolerance = 1e-3

# set up initial bracketing interval
#   Note: Sign of function *must* change in this interval for method to work.
xa = 0.
xb = 1.
error = xb - xa
iteration_count = 0

# bisect until tolerance reached
while (error > tolerance):

    # increment iteration count
    iteration_count += 1
    print("iteration", iteration_count)

    # find interval midpoint
    xm = (xa + xb) / 2
    print("  xa =",xa,";","xb =",xb,"->","xm=",xm)

    # evaluate function
    fxa = f(xa)
    fxb = f(xb)
    fxm = f(xm)
    print("  f(xa) =",fxa,";","f(xb) =",fxb,";","f(xm)=",fxm)

    # find which subinterval contains root
    if (fxm == 0):
        # accidentally landed on root (often occurs for "toy" test intervals)
        print("  landed on root")
        xa = xm
        xb = xm
    elif ((fxa * fxm) < 0):
        # sign change is in left half of interval
        print("  left subinterval")
        xb = xm
    else:
        # sign change is in right half of interval
        print("  right subinterval")
        xa = xm

    # find new error to use in tolerance test
    error = xb - xa
    print("  error =",error)

# give result
print("root lies in interval",xa,"<= x <=",xb)
