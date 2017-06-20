#!/usr/bin/env python3
"""fitting.py -- fits a two overlapping Gaussian peaks

Starting Code:
Mike Moran
mmoran0032@gmail.com
2016-06-28
Benjamin Rose
benjamin.rose@me.com
2017-06-20
"""

import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit


def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.

    Parameters
    ----------
    x : numpy.array
        The input values for the Gaussian function. Similar to the x values 
        used in a plotting command.

    A : float
        Maximum value of the Gaussian.

    mu : float
        Location (along x-axis) for the center of the Gaussian. Maybe outside 
        the range of `x`.

    sigma : float
        Width of the Gaussian.

    Return
    ------
    numpy.array
        A y-value (in a Gaussian shape) for each `x` given.
    """
    return A * numpy.exp(-(x - mu)**2/(2 * sigma**2))


def fitter(x, A0, mu0, sig0, A1, mu1, sig1):
    """
    Function to fit to the data. Two Gaussians that 
    """
    return


bins, counts = numpy.loadtxt('two_peaks.txt', unpack=True)
= curve_fit()