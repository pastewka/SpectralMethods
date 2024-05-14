---
layout: default
title: "Tutorial 3"
parent: Project
date: 2024-05-14
categories: project
author: Lars Pastewka
nav_order: 4
---
# Tutorial 3: Solving the heat transport equation

In this exercise, we will be looking at the solution of the Fourier heat transport equation. This is the same Fourier that invented the Fourier analysis. Indeed he invented this mathematical tool precisely to be able to solve the heat transport equation. Like Fourier himself, we will here use Fourier spectral methods to solve the heat transport equation. The learning goals of this exercise are to

* ...understand how to formulate differential equations in the Fourier domain.
* ...understand the difference between explicit and implicit solutions.
* ...understand that differential operators are diagonal and that the implicit solution is simply an algebraic manipulation.




## Fourier heat transport
 
The Fourier heat transport equation are mathematically identical to the diffusion equation discussed in class. A simple underlying picture would be the diffusion of heat packets, or the diffusion of particles carrying a certain amount of heat. Heat is energy, but it is commonly measured in terms of temperature $T$. In order to convert between these two, we need a material property, the heat capacity $c$, then $q=\rho c_p T$ with density $\rho$. $q$ is the energy density, i.e. energy per unit volume. Note that in general, $q(x,y,z,t)$, $T(x,y,z,t)$, $\rho(x,y,z)$ and $c_p(x,y,z)$ are fields that vary with position $x,y,z$ and potentially time $t$.

Since energy is a conserved quantity, the continuity equation holds for $q$. (Remember that we derived the continuity equation in class for particles numbers which are obviously conserved. Energy is similarly conserved in any physical system and hence the same expression holds.) In mathematical terms
$$\frac{\partial q}{\partial t}=\rho c_p\frac{\partial T}{\partial t}=-\nabla\cdot \vec{j}_q+\dot{q}_S$$
where $\vec{j}_Q$ is the heat current and $\dot{q}_S$ are heat sources or sinks. (A lighted candle could for example be a source of heat. $\dot{q}_S$ describes the energy generated per unit volume and time.) Note that we have assumed that $\rho$ and $c_p$ do not vary with time $t$ so that we can pull it out of the derivative.

The _constitutive expression_ for the heat current goes back to Fourier and states that the current is proportional to the temperature gradient,
$$\vec{j}_Q = -k \nabla T$$
where $k$ is called the thermaly conductivity. Putting these two equation together we get
$$\rho c_p\frac{\partial T}{\partial t} = k \nabla^2 T+\dot{q}_S,$$
if we assume that $k$ also does not depend on position. Note that we can rewrite this equation as
$$\frac{\partial T}{\partial t} = \frac{k}{\rho c_p} \nabla^2 T +\dot{q}_S= \alpha \nabla^2 T+\dot{q}_S$$
with $\alpha=k/\rho c_p$. The equation hence only depends on a single paramter $\alpha$ that contains the density $\rho$, the heat capacity $c_p$ and the thermal conductivity $k$ of the sample.

In the _steady-state_ (that is typically achieved for long times $t$) all derivative with respect to $t$ vanish and we obtain $$\alpha \nabla^2 T + \dot{q}_S=0.$$   Use periodic boundary conditions! 





## One-dimensional steady-state problem
We will in this tutorial first discuss the 1D variant of these equations. The dynamic equation in 1D becomes
$$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}+\dot{q}_S$$
and the steady-state equation for which $\partial T/\partial t=0$, i.e. the solution where the temperature field does not change anymore, is given by
$$R \equiv  \alpha \frac{\partial^2 T}{\partial x^2} + \dot{q}_S=0.$$
Note that $R$ is called the _residual_ and the objective of a numerical solution of these equations is to minimize the residual given an approximation to the function $T(x)$.

 Compute the implicit solution using Fourier spectral method. Remember that the starting point is to write the target function, in this case the temperature field $T(x)$, as the approximation
$$T_N(x) = \sum_{k=0}^{N-1} \tilde{T}_k \nu_k(x)$$
where $\nu_k(x)$ is the set of basis functions. Our solution will be obtained in terms of the expansion coefficients $\tilde T_k$.

### Task: Numerical solution

For the one-dimensional problem, find the algebraic equation for the expansion coefficients $\tilde T_k$. You can use either a Galerkin or a collocation formulation, but the Galerkin formulation maybe easier because it directly leads to a set of equations for the expansion coefficents $\tilde T_k$. (Galerkin and collocation schemes are actually identical for this basis set. This is why the method described here is sometimes termed _pseudospectral_.) In the Galerkin formulation, the discrete equations are
$$(\nu_k, R)=0.$$
Note that for $N$ basis function this gives a set of $N$ linear equations.

* What is the nature of these equations? Are these equation coupled our uncoupled?

* Suggest a solution strategy.
* Implement a numerical scheme that solves for the coefficient $\tilde T_k$ given a non-zero field of heat sources $\dot{q}_S$.



## One-dimensional time-dependent problem

We can use an explicit  or implicit solution scheme to propagate the temperature field $T(x,t_0)$ from its initial value. A discrete representation of the time derivative operator is straightforwardly obtained by Taylor series expansion of some function $f(t)$. We simple write time derivative $ \frac{\partial f}{\partial t}  \approx \frac{f(t+\Delta t)-f(t)}{\Delta t} $, or in the case of heat transport equation
$$T(t+\Delta t)=T(t) + \frac{\partial T}{\partial t} \Delta t = T(t) + \left(\alpha \frac{\partial^2 T}{\partial x^2} + \dot{q}_S\right)\Delta t.$$
This type of explicit time stepping is called _Euler integration_. There are more clever ways for solving initial value problems, such as the class of methods called _Runge-Kutta_ integration, but for the sake of simplicity we will here only use Euler integration. Note that this requires a (very) small time step $\Delta t$ to be accurate.

### Task: Time propagation 
* Implement explicit solution of the heat transport equation using Euler integration. 
Propagate the heat transport equation starting from an initial Gaussian temperature profile.

When you run the simulation:
* What do you see? Does it make (physical) sense?
* What is the final condition at $t\to\infty$.

## Three-dimensional solution

Now look at the three-dimension implicit problem using the Fourier spectral method.

### Task: Numerical solution

* Solve the temperature field for a pair of heat source and sink that are both spherical.
* What do the basis functions look like in the three dimensional case?
* What does the gradient operator and Laplacian become in the Fourier representation?
* _Hint:_ The three-dimensional problem is difficult to visualize. You can plot slices through the three-dimensional system using the [`pcolormesh`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pcolormesh.html) command of matplotlib.
