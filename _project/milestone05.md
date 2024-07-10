---
layout: default
title: "Milestone 5"
parent: Project
date: 2024-07-10
categories: project
author: Lars Pastewka
nav_order: 10
---

# Milestone 5 (optional): Parallelization

In the third milestone, you will run your third turbulence simulation. In this milestone, you will...

* ...learn how to parallelize your code using the [Message Passing Interface (MPI)](https://www.mpi-forum.org/).

Make sure you have read and understood the notes on [bwUniCluster](../_notes/bwUniCluster.md).
We recommend [µFFT](https://github.com/muSpectre/muFFT) for parallel FFT transforms. The documentation has a [section on parallelization](https://muspectre.github.io/muFFT/Python.html#parallelization).

## Parallelization

Parallelize your code. µFFT (and µGrid) will take of most (all?) communication. Your code may therefore already run in parallel.

## Parameters

Run simulations with the same parameters as your simulations of [milestone 4](milestone04.md), but for larger system sizes. You should be able to reach at least $256^3$ on [bwUniCluster](../_notes/bwUniCluster.md). Plot the energy and dissipation spectrum for different grid sizes.

## Task summary

We ask you to provide the following results in your final report:

* Plot of the energy and the dissipation spectrum for 3 different grid sizes.
