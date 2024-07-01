---
layout: default
title: "Milestone 2"
parent: Project
date: 2024-06-30
categories: project
author: Lars Pastewka
nav_order: 7
---

# Milestone 2: Taylor-Green vortex

In the second milestone, you will implement the spectral solution of the Navier-Stokes equation and test it on a Taylor-Green vortex. The goal is to...

* ...learn how work with explicit time stepping schemes and to...
* ...understand that viscosity describes the decay of the velocity field

## Navier-Stokes equation

You will now implement the first solver for the incompressible Navier-Stokes equations. We use the rotational form of the equations, which is given by

$$\frac{\partial\vec{u}}{\partial t}=2\vec{u}\times \vec{\omega}+\nu \nabla^2 \vec{u}-\nabla P$$

where $\nu$ is the (kinematic) viscosity and $P(x,y,z)$ the pressure field. The vorticity $\vec{\omega}=\frac{1}{2}\nabla\times\vec{u}$ was already introduced in the [previous milestone](milestone01.md). This equation is solved subject to the incompressibility condition,

$$\nabla\cdot\vec{u}=0.$$

We can use this incompressibility condition to compute the pressure. Taking the divergence of the Navier-Stokes equations and using incompressibility, we obtain the auxiliary equation

$$\nabla^2 P=2\nabla\cdot\left(\vec{u}\times \vec{\omega}\right).$$

This equation is known as the pressure Poisson equation.

### Task 1: Spectral Navier-Stokes equations

Rewrite the Navier-Stokes equations and the pressure Poisson equation in terms of the Fourier-transformed velocity field $\tilde{\vec{u}}$. Since $\vec{\omega}$ depends on $\vec{u}$ (see [milestone 1](milestone01.md)), the term $\vec{u}\times\vec{\omega}$ is nonlinear in $\vec{u}$. This term is best computed in real (and not Fourier) space and it makes sense to leave the Fourier transform of this term, $\widetilde{\vec{u}\times\vec{\omega}}$, as is in the equations. Because this implies that part of the calculation is carried out in Fourier space and part in real space, the resulting numerical scheme is often denoted as *pseudo spectral*.
Once you have written everything in the Fourier representation, you can use the pressure Poisson equation to eliminate the pressure in the Navier-Stokes equations.

**Hint:** The final equation can be found for example in [Mortensen & Langtangen, Comput. Phys. Comm. (2016)](https://doi.org/10.1016/j.cpc.2016.02.005). The first report of a pseudo-spectral Navier-Stokes solver in the literature is from Orszag & Patterson, see [Statistical Models and Turbulence (1972)](https://doi.org/10.1007/3-540-05716-1_8) and [Physical Review Letters (1972)](https://doi.org/10.1103/PhysRevLett.28.76). Make sure to include the full derivation of the this equation into your report.

## Time stepping

You are now almost ready to solve the Navier-Stokes equations. You are still missing a time stepping algorithm that propagates the velocity field $\vec{u}$ (or rather $\tilde{\vec{u}}$) forward in time. We suggest to use a simple explicit, fourth-order Runge-Kutta integrator for this.
The following code is an implementation of this specific Runge-Kutta method:
```python
def rk4(f, t: float, y: np.ndarray, dt: float) -> np.ndarray:
    """
    Implements the fourth-order Runge-Kutta method for numerical integration
    of multidimensional fields.

    Parameters
    ----------
    f : function
        The function to be integrated. It should take two arguments: time t
        and field y.
    t : float
        The current time.
    y : array_like
        The current value of the field.
    dt : float
        The time step for the integration.

    Returns
    -------
    dy : np.ndarray
        The increment of the field required to obtain the value at t + dt.
    """
    k1 = f(t, y)
    k2 = f(t + dt / 2, y + dt / 2 * k1)
    k3 = f(t + dt / 2, y + dt / 2 * k2)
    k4 = f(t + dt, y + dt * k3)
    return dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
```

### Task 2: Fourth-order Runge-Kutta

Use the code snippet above and implement the main loop that steps the simulation forward in time.

## Taylor-Green vortex

The [Taylor-Green vortex](https://en.wikipedia.org/wiki/Taylor%E2%80%93Green_vortex) is a simple sinosoidal flow field. It is given by the velocity field

$$\begin{aligned}u_x(x,y,z)&=A\cos ax\sin by\sin cz\\u_y(x,y,z)&=B\sin ax\cos by\sin cz\\u_z(x,y,z)&=C\sin ax\sin by\cos cz\end{aligned}.$$

The two-dimensional Taylor-Green vortex

$$\begin{aligned}u_x(x,y,z)&=A\cos ax\sin by\\u_y(x,y,z)&=B\sin ax\cos by\\u_z(x,y,z)&=0\end{aligned}$$

has an analytical solution that can be used to test whether your code works.

### Task 3: Analytical solution

Show that the Taylor-Green vortex represents incompressible flow. The incompressibility condition will link the prefactors $A$, $B$ and $C$ (in the case of the three-dimensional vortex). Then derive the analytical solution for the time evolution of the two-dimensional Taylor-Green vortex. Assume that the prefactor is time-dependent and seek a solution for that time dependence.

### Task 4: Numerical solution

Run a numerical calculation of the two-dimensional Taylor-Green vortex and check whether the results agree with your analytical solution.

**Hint:** You can run the two-dimensional vortex on a system consisting only of a few grid points in one direction to save computational time. 

## Task summary

We ask you to provide the following results in your final report:

* Derivation of the spectral representation of the incompressible Navier-Stokes equations
* Derivation of the analytical solution of the two-dimensional Taylor-Green vortex
* Plot illustrating a numerical test of your code, carried out by comparing analytical and numerical solutions of the Taylor-Green vortex
