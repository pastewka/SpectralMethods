---
layout: default
title: "Tutorial 2"
parent: Project
date: 2024-04-19
categories: project
author: Lars Pastewka
nav_order: 3
---

# Tutorial 2: Fourier interpolation

In this tutorial, we will be exploring the notion put forth in the lecture that a Fourier analysis is actually an interpolation scheme. This is often called _trigonometric interpolation_ or _Fourier interpolation_. In particular, we will discuss an important implication of this: The phenomenom of Gibbs ringing, and what it means for computing a Fourier derivative.

## Discrete Fourier transform

We will be using the discrete Fourier transform (DFT) here as an approximation for the Fourier analysis that works on digital computers. The discrete Fourier transform maps a discrete function in real-space onto a discrete function in reciprocal space. It is the only of the set of transforms that we can use on a computer that works intrinsically with a set of discrete numbers.

Remember the Fourier series,

$$f(x) = \frac{1}{L}\sum_{k=-\infty}^{\infty} (c_k\Delta x) e^{i q_k x}$$

that gives a continuous function $f(x)$. The coefficients are obtained by projecting the function $f(x)$ on the basis vectors $\varphi_k(x)=e^{-i q_k x}$,

$$c_k \Delta x = \int_0^L \text{d}x \, f(x) e^{-i q_k x}.$$

We now evaluate this continuous function at a discrete set of $N$ equally-spaced points, $x_l=l \Delta x$ with $\Delta x=L/N$, indicated by the red crosses in the figure below. Note that here the Fourier series is defined such that the $c_k$ are the proper coefficients of the discrete Fourier transform, hence the factor $\Delta x/L=1/N$.


```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
L = 1
N = 1000
dx = L/N
x = np.arange(N)*dx
sample_points = x[::100] # Sample every 100th point
f = lambda x: np.sin(np.pi*x)**4
plt.plot(x, f(x), 'k-')
plt.plot(sample_points, f(sample_points), 'rx', ms=20)
plt.title('A discretely sampled continuous function');
```


    
![png](tutorial02_files/tutorial02_2_0.png)
    


The discrete Fourier transforms expresses a discrete function as

$$f(x_l) = \frac{1}{N}\sum_{k=-\lfloor (N-1)/2 \rfloor}^{\lfloor N/2 \rfloor} c_k e^{i q_k x_l}$$

where $x_l = l \Delta x$ is now discretized on a grid with spacing $\Delta x$ (see red data points in the above figure) and $q_k = k \Delta q$ is "discretized" as in the normal Fourier series with $\Delta q = 2\pi/L$. Note that the overall length of the periodic domain if $L=\Delta x N$ and sum in Eq. (1) now runs from $0$ to $N-1$. The coefficient are obtained by

$$c_k = \sum_{l=0}^{N-1} f(x_l) e^{-i q_k x_l}.$$

It is important to realize that in this formulation, the length $L$ drops out. We have $q_k x_l=kl \Delta x \Delta q = 2\pi k l / N$. We then obtain

$$f(x_l) =\frac{1}{N} \sum_{k=-\lfloor (N-1)/2 \rfloor}^{\lfloor N/2 \rfloor} c_k e^{i 2\pi k l/N}$$

and

$$c_k = \sum_{l=0}^{N-1} f(x_l) e^{-i 2\pi k l/N}.$$

This is the formulation that can be for example found in the documentation of [numpy's FFT module](https://docs.scipy.org/doc/numpy/reference/routines.fft.html). (This module computes these function for you, but it may make sense if you implement them yourselves for this exercise.) We can think of the discrete Fourier transforms as if the length of our domain is given by the number of grid points, $L=N$. In general, care must be taken that units are converted correctly when solving physical problems.

## Fourier interpolation

The function $f(x_l)$ in Eq. (1) is defined at discrete grid points but we can evaluate Eq. (1) for any value $x$ (since it is a continuous function). E.g. in the above figure, the points $(x_l, f(x_l))$ are given by the red crosses, but the full function $f(x)$ is the black line. Obtaining $f(x)$ from the (truncated) Fourier representation is called Fourier interpolation. This exercise is intended to give you a feeling of what Fourier interpolation means and what a Fourier interpolated function (and its derivatives) look like.

We suggest to explore Fourier interpolation for four types of functions:
* A sine that is periodic on the domain $L$
* A polynomial function of the form $f(x)=(x-x_0)^2$ where $x_0=L/2$ is the center of your interval.
* A step function
* A sawtooth function

Of course, feel free to evaluate other functions as well.

### Task 1: Plot the function and its Fourier interpolation

In order to say something about interpolation, we need to turn the function into a discrete description. Discretize the function above into $N$ grid points (a parameter that you can play with) and then plot the discrete variant in combination with its Fourier interpolated variant, i.e. the discrete Fourier series of that function evaluated at a much finer grid.

## Fourier derivative

We can compute the derivative of a Fourier representation of a function simply by taking the derivatives of the exponential basis function. For example, given Eq. (1) we can compute the derivative

$$f'(x_l) = \frac{1}{N} \sum_{k=-\lfloor (N-1)/2 \rfloor}^{\lfloor N/2 \rfloor} i q_k c_k e^{i q_k x_l}.$$

Note that this is the _derivative of the Fourier interpolated function_. The Fourier transform of the derivative of a function is therefore $i q_k c_k$, given the Fourier transform (coefficients) $c_k$ of the function itself. The _gradient operation_ in reciprocal space is hence a multiplication with the (complex) number $D_k = iq_k$. We have transformed a differential operator into an algrebraic expression (that our computer can work with).

### Task 2: Plot the derivative of the functions above

Plot the full (Fourier interpolated) derivative of the functions above. What do you see?

### Task 3: Finite differences

Compare the Fourier derivative to the derivative obtained from a difference quotient (also called a finite-differences approximation),

$$f'(x_l) = \frac{f(x_{l+1})-f(x_l)}{\Delta x}.$$

What do you see?


