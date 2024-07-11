---
layout: default
title: "Fluid mechanics"
parent: Lecture
date: 2024-07-11
categories: lecture
author: Lars Pastewka
nav_order: 2
---


<h2 class='chapterHead' id='fluid-mechanics'><span class='titlemark'>Chapter 3</span><br /><a id='x1-10003'></a>Fluid mechanics</h2>
<div class='framedenv' id='shaded_-1'>
<!-- l. 3 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> This chapter introduces a specific form of the transport problem: The
Navier-Stokes equations, that describe how fluids flow. </p></div>
<h3 class='sectionHead' id='streaming-velocity'><span class='titlemark'>3.1 </span> <a id='x1-20003.1'></a>Streaming velocity</h3>
<!-- l. 9 --><p class='noindent'>The central quantity in fluid mechanics is the streaming velocity \(\v {v}(\v {r})\). It is a vector
field that describes the average velocity of molecules in the (infinitesimal) volume
element at position \(\v {r}\). Mass is transported along the streaming velocity field, which
can be described by the mass flux \begin {equation} \v {j}_\rho (\v {r})=\rho (\v {r})\v {v}(\v {r}). \label {eq:mass-density} \end {equation}<a id='x1-2001r1'></a> Mass conservation is captured by the
continuity equation \begin {equation} \frac {\partial \rho }{\partial t} + \nabla \cdot \left (\rho \v {v}\right ) = \frac {\partial \rho }{\partial t} + \v {v}\cdot \nabla \rho + \rho \nabla \cdot \v {v} = 0. \label {eq:mass-conservation-navier-stokes} \end {equation}<a id='x1-2002r2'></a> A common approximation is to assume incompressibility, i.e.
fluids where \(\rho \) is constant. From Eq. \eqref{eq:mass-conservation-navier-stokes} we
immediately see, that this means \begin {equation} \nabla \cdot \v {v} = 0. \end {equation}<a id='x1-2003r3'></a> The divergence of the streaming velocity
vanishes in incompressible fluids.
</p><!-- l. 47 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='momentum-conservation'><span class='titlemark'>3.2 </span> <a id='x1-30003.2'></a>Momentum conservation</h3>
<!-- l. 49 --><p class='noindent'>The foundation of fluid dynamics is momentum conservation. Given
fluid density \(\rho (\v {r})\), the momentum density is the vector field \(\v {j}_\rho (\v {r})\) introduced in
Eq. \eqref{eq:mass-density}. The total momentum \begin {equation} \v {p}_\text {tot} = \int \dif ^3 r\, j_\rho (\v {r}) \end {equation}<a id='x1-3001r4'></a> is conserved. Similar to mass
conservation, Eq. \eqref{eq:ntot}, this leads to a continuity equation, \begin {equation} \frac {\partial \v {j}_\rho }{\partial t} + \nabla \cdot \t {\Pi }^T = 0 \label {eq:momentum-continuity} \end {equation}<a id='x1-3002r5'></a> where \(\t {\Pi }\) is a
tensor containing the <span class='cmti-12'>momentum flux </span>in the \(x\)-, \(y\)- and \(z\)-directions. We can integrate
Eq. \eqref{eq:momentum-continuity} over a finite volume \(V\) and use the divergence
theorem to obtain \begin {equation} \frac {\partial \v {p}_V}{\partial t} + \int _{\partial V}\dif ^2 r\,\t {\Pi }\cdot \hat {n} = 0 \label {eq:momentum-continuity-integral} \end {equation}<a id='x1-3003r6'></a> Identifying \(\t {\Pi }\cdot \hat {n}\) as the force per unit area acting normal to the
surface of the volume \(V\), we see that Eq. \eqref{eq:momentum-continuity-integral}
is nothing else than Newton’s second law. The key question that remains is that
the forces that act on each volume element, \(\t {\Pi }\), look like.
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 90 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> When writing an expression like \(\nabla \cdot \t {\Pi }\equiv \text {div}\,\t {\Pi }\) we follow the convention that the
\(\nabla \)-operator acts on the left. In other words, the \(i\)-th component of the divergence of \(\t {\Pi }\)
is given by \begin {equation} \left [\nabla \cdot \t {\Pi }\right ]_i = \partial _\alpha \Pi _{\alpha i}, \end {equation}<a id='x1-3004r7'></a> with summation over repeated indices (Einstein notation).
</p></div>
<!-- l. 98 --><p class='noindent'>
</p>



<h3 class='sectionHead' id='convection'><span class='titlemark'>3.3 </span> <a id='x1-40003.3'></a>Convection</h3>
<!-- l. 100 --><p class='noindent'>Momentum is convected with the flow, which is described by a drift term \begin {equation} \t {\Pi }_\text {Drift} = \v {j}_\rho \otimes \v {v} = \rho \v {v}\otimes \v {v}. \end {equation}<a id='x1-4001r8'></a> What is
still missing is a <span class='cmti-12'>constitutive law </span>that describes the behavior of the fluid,
given by the stress tensor \(\t {\tau }\). The overall momentum flux is the given by
\(\t {\Pi }=\t {\Pi }_\text {Drift}+\t {\tau }\).
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 114 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The symbol \(\otimes \) denotes the outer product. The outer product between two
vectors is a tensor with elements \begin {equation} \left [\v {a}\otimes \v {b}\right ]_{ij} = a_i b_j \end {equation}<a id='x1-4002r9'></a> The quantity \(\v {v}\otimes \v {v}\) is hence the symmetric tensor \begin {equation} \begin {pmatrix} v_x v_x &amp; v_x v_y &amp; v_x v_z \\ v_x v_y &amp; v_y v_y &amp; v_y v_z \\ v_x v_z &amp; v_y v_z &amp; v_z v_z. \end {pmatrix} \end {equation}<a id='x1-4003r10'></a>
Some authors simply omit the symbol \(\otimes \) and write \(\v {a}\otimes \v {b}=\v {a}\v {b}\). Since this is easily confused
with the inner (or scalar) product \(\v {a}\cdot \v {b}\), we will always explicitly write the operation \(\otimes \).
</p></div>
<!-- l. 136 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='newtonian-fluids'><span class='titlemark'>3.4 </span> <a id='x1-50003.4'></a>Newtonian fluids</h3>
<!-- l. 138 --><p class='noindent'>The simplest constitutive law for fluids is given by \begin {equation} \t {\tau } = P\t {1} - \eta \t {\dot \gamma }, \end {equation}<a id='x1-5001r11'></a> where \(P\) is the fluid pressure, \(\eta \)
the viscosity and \begin {equation} \t {\dot \gamma } = \nabla \otimes \t {v} \end {equation}<a id='x1-5002r12'></a> the shear-rate tensor.
</p><!-- l. 152 --><p class='indent'> The overall equation for momentum equation then becomes \begin {equation} \frac {\partial \v {j}_\rho }{\partial t} + \nabla \cdot \left ( \rho \v {v}\otimes \v {v} + P\t {1} - \eta \t {\dot \gamma } \right ) = 0 \end {equation}<a id='x1-5003r13'></a> For
incompressible flow, this can be simplified to \begin {equation} \frac {\partial \v {v}}{\partial t} + \left ( \v {v} \cdot \nabla \right ) \v {v} + \nabla p - \nu \nabla ^2\v {v} = 0. \label {eq:incompressible-navier-stokes} \end {equation}<a id='x1-5004r14'></a> with kinematic viscosity \(\nu =\eta /\rho \)
and specific pressure \(p=P/\rho \). We can further rewrite the convective term to
\begin {equation} \frac {\partial \v {v}}{\partial t} = \v {v} \times \left ( \nabla \times \v {v} \right ) + \nu \nabla ^2\v {v} - \nabla p. \label {eq:rotational-navier-stokes} \end {equation}<a id='x1-5005r15'></a>
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 212 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The triple cross product can be written as two triple dot products, \begin {equation} \v {v}\times \left (\nabla \times \v {v}\right ) = \frac {1}{2} \nabla v^2 - \left (\v {v}\cdot \nabla \right )\v {v}, \end {equation}<a id='x1-5006r16'></a> as can
be easily checked by writing out the equation component-wise. Because of
incompressibility, \(\nabla ^2 v^2=0\) and hence \begin {equation} \v {v}\times \left (\nabla \times \v {v}\right ) = - \left (\v {v}\cdot \nabla \right )\v {v}, \end {equation}<a id='x1-5007r17'></a> which allows to rewrite the Navier-Stokes
equation in the form given by Eq. \eqref{eq:rotational-navier-stokes}.
</p></div>
<!-- l. 239 --><p class='indent'> Note that we can identify the curl of the velocity field as field of angular
velocities, \begin {equation} \v {\omega } = \frac {1}{2} \nabla \times \v {v}, \end {equation}<a id='x1-5008r18'></a> sometimes called the <span class='cmti-12'>vorticity</span>. The incompressible Navier-Stokes
equations become \begin {equation} \frac {\partial \v {v}}{\partial t} = 2 \v {v} \times \v {\omega } + \nu \nabla ^2\v {v} - \nabla p. \label {eq:vorticity-navier-stokes} \end {equation}<a id='x1-5009r19'></a>
</p><!-- l. 264 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='pressure-poisson-equation'><span class='titlemark'>3.5 </span> <a id='x1-60003.5'></a>Pressure Poisson equation</h3>
<!-- l. 266 --><p class='noindent'>For compressible flow, the pressure \(P\) is tied to the density \(\rho \) through an equation of



state, that contains the compressibility of the fluid. For incompressible for, the
compressibility is essentially infinite an we need alternatives routes for obtaining
the pressure. Taking the divergence of Eq. \eqref{eq:rotational-navier-stokes} and
using incompressibility yields \begin {equation} \nabla ^2 p = 2 \nabla \cdot \left ( \v {v} \times \v {\omega } \right ), \end {equation}<a id='x1-6001r20'></a> which is known as the pressure Poisson equation.
This auxiliary equation couples the pressure to the flow field \(\v {v}(\v {r})\) at every instance in
time.



</p>
<h2 class='likechapterHead' id='bibliography'><a id='x1-7000'></a>Bibliography</h2>

