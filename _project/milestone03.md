---
layout: default
title: "Milestone 3"
parent: Project
date: 2024-06-30
categories: project
author: Lars Pastewka
nav_order: 8
---

# Milestone 3: Turbulence

In the third milestone, you will run your first turbulence simulation. In this milestone, you will...

* ...learn how to initialized and drive turbulent flow and...
* ...write the simulation output to a file.

The Fourier-spectral solver for the Navier-Stokes equation developed in [Milestone 2](milestone02.md) will now be extended for the simulation of turbulent flow. The idea is to start with a random velocity field that is forced to sustain turbulence. This *forcing* is necessary because otherwise the flow field would decay, like observed for the Taylor-Green vortex in [Milestone 2](milestone02.md).

## Energy and dissipation spectrum

When analyzing the simulations, you will look at the energy and dissipation spectrum of the simulation. The kinetic energy density of flow is given by

$$E(q) = \frac{1}{2} u^2(q).$$

The energy spectrum is a plot of $E(q)$. It is typical to plot this on a double-logarithmic scale to visualize a potential power-law dependence of the energy spectrum. The energy spectrum for turbulent flow is typically $E(q)\propto q^{-5/3}$ (see e.g. [Wikipedia](https://en.wikipedia.org/wiki/Energy_cascade)).

Similarly, we can compute the dissipation spectrum. This described how much energy is dissipated per wavevector $q$. The dissipation spectrum is given by

$$D(q) = \nu q^2 u^2(q),$$

which is the viscous contribution to the spectral variant of the Navier-Stokes equation. Note that $D(q) \propto q^2 E(q)$, i.e. both spectra are related.

## Random initial velocity field

Rather than initializing flow with a deterministic velocity profile, we will use a random flow field in this milestone. It is important to make sure the initial velocity field represents incompressible flow, $\nabla\cdot\vec{v}=0$. In general, a randomly initialized velocity field will not fulfill this condition.

When representing $\vec{v}(\vec{r})$ through a Fourier series, the incompressibility condition becomes $\vec{q}\cdot\tilde{\vec{v}}=0$. Given a generic random field $\tilde{\vec{f}}(\vec{q})$, we can construct an incompressible velocity field through

$$\tilde{\vec{v}}(\vec{q})=\left(\underline{1} - \frac{\vec{q}\otimes\vec{q}}{q^2}\right)\cdot \tilde{\vec{f}}(\vec{q}).$$

It is straightforward to show that $\vec{q}\cdot\tilde{\vec{v}}(\vec{q})$ vanishes for all $\vec{q}$, which mean the flow field is incompressible.

Turbulent flow is best initialized with an energy spectrum $\propto q^{-5/3}$. The following code generates a random field with this power-law correlation.

```python
import numpy as np
# Compute wavevectors
wavevector = (2 * np.pi * fft.fftfreq.T / grid_spacing).T
zero_wavevector = (wavevector.T == np.zeros(3, dtype=int)).T.all(axis=0)
wavevector_sq = np.sum(wavevector ** 2, axis=0)
# Fourier space velocity field
random_field = np.zeros((3,) + fft.nb_fourier_grid_pts, dtype=complex)
rng = np.random.default_rng()
random_field.real = rng.standard_normal(random_field.shape)
random_field.imag = rng.standard_normal(random_field.shape)
# Initial velocity field should decay as k^(-5/3) for the Kolmogorov spectrum
fac = np.zeros_like(wavevector_sq)
# Avoid division by zero
fac[np.logical_not(zero_wavevector)] = velocity_amplitude * \
	wavevector_sq[np.logical_not(zero_wavevector)] ** (-5 / 6)
random_field *= fac
```

The code assumes `fft` is a [`muFFT`](https://muspectre.github.io/muFFT/) transform object. The field in `random_field` is not yet incompressible.

## Forcing

In real flow scenarios, *forcing* occurs because the flow is somehow driven, for example because the velocity of a plane is sustained by its engines or flow in a pipe is established by a pump. In our spectral simulation, we are simulating only a small volume element of a macroscopic flow problem. The periodic domain of our flow problem can therefore be regarded as some form of representative volume element, but there are no inlets, outlets, or walls that would be necessary to actively drive the flow.

Multiple forcing schemes have been described in the literature. We here suggest one of the simplest that is described in [Siggia & Patterson, J. Fluid Mech. (1978)](https://doi.org/10.1017/s0022112078001287). In their scheme, the highest wavelength or lowest wavenumber modes are frozen, i.e. no propagated with the time integration. Siggia & Patterson initialize a random flow field with turbulent energy spectrum $E(q)\propto q^{-5/3}$ and freeze the low wavenumbers of that spectrum.

## I/O

Visualize the turbulent flow. The simplest form of visualization is plotting the absolute velocity $v(\vec{r})$ on two-dimensional slices in the three-dimensional box. We recommend to organize your code in a way that splits computation and visualization into separate components. Write the whole velocity field to a file. For a serial code, you can use the [`npy` format](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html) which can be written by [`np.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html). To prepare for parallelization, it may be useful to write into a [`NetCDF` file](https://en.wikipedia.org/wiki/NetCDF) using the [parallel I/O module of µGrid](https://muspectre.github.io/muGrid/Python.html#i-o). For visualization, NetCDF files can be read with the [`scipy.io.netcdf_file`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.netcdf_file.html) or the [`netCDF4`](https://unidata.github.io/netcdf4-python/) Python modules.

## Parameters

Use unit length for the box and a viscosity of $1/1600$. The simulations should be stable at a time step of $0.01$. You should be able to run at least $32\times 32\times 32$ grid points on a current personal computer. This corresponds to the size of early turbulence simulations of [Orszag](https://doi.org/10.1007/3-540-05716-1_8) and others. Plot the energy and dissipation spectrum at 5 different times throughout your simulation.

## Task summary

We ask you to provide the following results in your final report:

* Visualization of the velocity field showing evolution of the turbulent flow
* Plot of the energy and the dissipation spectrum at 5 different times throughout your simulation 
