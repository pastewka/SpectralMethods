---
layout: default
title: "Tutorial 4"
parent: Project
date: 2024-06-02
categories: project
author: Lars Pastewka
nav_order: 5
---
# Tutorial 4: Parallel solution of the heat transport equation

In this exercise, we will parallelize the three-dimensional solution of the heat transport equation from tutorial 3. The goals are to

* ...understand how to work with MPI-parallel programs.
* ...understand how domain decomposition work with FFTs.

## Three-dimensional steady-state problem

We will in this tutorial look back at the 3D variant of the implicit (steady-state) heat transport problem. The steady-state equation for which $\partial T/\partial t=0$, i.e. the solution where the temperature field does not change anymore, is given by
$$R \equiv  \alpha \nabla^2 T + \dot{q}_S=0.$$
Note that $R$ is called the _residual_ and the objective of a numerical solution of these equations is to minimize the residual given an approximation to the function $T(x)$.

## muGrid and muFFT

We now need to switch to a library that support MPI-parallelization. We will use muGrid and muFFT, which provide an abstraction layer to a variety of FFT implementation. You can find the relevant information here:

* [muGrid repository](https://github.com/muSpectre/muGrid), [muGrid documentation](https://muspectre.github.io/muGrid/)
* [muFFT repository](https://github.com/muSpectre/muFFT), [muFFT documentation](https://muspectre.github.io/muFFT/)

### Task 1: Read the manual

Look at the documentation of muGrid and muFFT and familarize yourself with these libraries.

### Task 2: Serial solver with muFFT

Convert your serial solver to use muFFT.

### Task 3: Parallel solver with muFFT

Parallelize your solver.
