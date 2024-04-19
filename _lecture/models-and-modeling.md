---
layout: default
title: "Introduction"
parent: Lecture
date: 2024-04-19
categories: lecture
author: Lars Pastewka
nav_order: 0
---


<h2 class='chapterHead' id='introduction'><span class='titlemark'>Chapter 1</span><br /><a id='x1-10001'></a>Introduction</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 6 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> The term <span class='cmti-12'>simulation </span>refers to the numerical (computer-aided) solution
of <span class='cmti-12'>models</span>. In this introductory chapter, we discuss how models of physical reality
are build and present different classes of models. These models are usually
described mathematically by means of <span class='cmti-12'>differential equations</span>, i.e. “simulation” is
often (but not always) the numerical solution of a set of ordinary or partial
differential equations. </p></div>
<h3 class='sectionHead' id='models'><span class='titlemark'>1.1 </span> <a id='x1-20001.1'></a>Models</h3>
<!-- l. 12 --><p class='noindent'>Models are approximations for the behavior of the physical world at certain length
scales. For example, a model that explicitly describes atoms “lives” on length
scales on the order of \(\text {nm}\) and may be appropriate to describe the growth of thin
films in semiconductor manufacturing. We would not want to describe a
macroscopic system or phenomenon that lives on scales of \(\sim \text {mm}\) or beyond, such
as how water flows out of a tap or how an airplane wing bends during
takeoff, with such a model. Key to carrying out simulations is therefore
the ability to match the physical phenomenon we want to describe with
the appropriate model and the mathematical method required for its
solution.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 14 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> While we <span class='cmti-12'>could </span>describe even macroscopic systems with atomic-scale
models, this is typically prohibited by the computer resources available to us.
Macroscopic systems consist of more than \(10^{23}\) (Avogadro’s number) atoms,
whose positions we would not be able to fit into present day computers. In
addition, the gist of the question we want to answer may be hidden in such a
fine-grained atomic-scale model like the legendary needle in a haystack.
</p></div>
<!-- l. 18 --><p class='indent'> Figure <a href='#-the-vertical-arrangement-of-the-boxes-corresponds-to-a-length-scale-with-the-shortest-scales-shown-on-the-bottom-the-boxes-themselves-show-categories-of-models-or-simulation-methods-that-are-used-on-these-scales-in-this-class-we-deal-with-the-discretization-of-fields-and-choose-a-specific-use-case-that-falls-into-the-local-balance-category-'>1.1<!-- tex4ht:ref: fig:Scheme --></a> shows on the vertical axis <span class='cmti-12'>length scales </span>and classes of models that
live on these scales. On the shortest length scale, a quantum mechanical
description is usually necessary. This means that if we want to resolve the world
with Å resolution, we find ourselves at the level of quantum mechanics and
all underlying models are of a quantum mechanical nature. Underlying
quantum mechanics is the <span class='cmti-12'>Schrödinger equation</span>, whose (approximate)
solution is implemented in various methods, such as <span class='cmti-12'>density functional
theory</span> (<a href='#XMartin2004-zf'>Martin</a>, <a href='#XMartin2004-zf'>2004</a>), a many-body description of the quantum mechanical
electronic system. If we get rid of modeling the electron explicitly, we arrive at a
class of simulation methods often referred to as <span class='cmti-12'>molecular dynamics</span> (<a href='#XAllen1989-nt'>Allen and
Tildesley</a>, <a href='#XAllen1989-nt'>1989</a>). The key mathematical object in molecular dynamics is the set of



positions and velocities of all atoms, which means we have to introduce
three position and three velocity variables for each of the \(n\) interacting
particles. In contrast, in a quantum mechanical many-body description we are
dealing with a field with three \(n\) position variables each, namely \(\Psi (\v {r}_1,\v {r}_2,\dots ,\v {r}_n;t)\). This
illustrates that formulating models on larger length scales requires some
form of <span class='cmti-12'>coarse-graining</span>, i.e. removing information from a smaller scale
model.
</p>
<figure class='figure'>







<div class='center'>
<!-- l. 32 --><p class='noindent'>
</p><!-- l. 36 --><p class='noindent' id='-the-vertical-arrangement-of-the-boxes-corresponds-to-a-length-scale-with-the-shortest-scales-shown-on-the-bottom-the-boxes-themselves-show-categories-of-models-or-simulation-methods-that-are-used-on-these-scales-in-this-class-we-deal-with-the-discretization-of-fields-and-choose-a-specific-use-case-that-falls-into-the-local-balance-category-'> <img alt='PIC' height='585' src='Figures/ExtendedScheme-.png' width='774' /> <a id='x1-2001r1'></a>
</p>
<figcaption class='caption'><span class='id'>Figure 1.1: </span><span class='content'>The vertical arrangement of the boxes corresponds to a length
scale, with the shortest scales shown on the bottom. The boxes themselves
show categories of models or simulation methods that are used on these
scales. In this class we deal with the discretization of fields and choose a
specific use case that falls into the <span class='cmti-12'>local balance </span>category. </span></figcaption><!-- tex4ht:label?: x1-2001r1 -->
</div>



</figure>
<div class='framedenv' id='shaded*-1'>
<!-- l. 42 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> </p>
<ul class='itemize1'>
<li class='itemize'>\(1\,\r {A}=10^{-10}\,\text {m}\)
</li>
<li class='itemize'>The atoms that constitute our physical world are held together by
quantum mechanics. Models based on quantum mechanical principles
are also called <span class='cmti-12'>ab-initio </span>(“from the beginning”) or <span class='cmti-12'>first principles</span>
models. The fundamental equation that describes quantum mechanical
objects is the <span class='cmti-12'>Schrödinger equation</span>. It is itself is in fact already an
approximation, despite the fact that models derived from it are called
<span class='cmti-12'>first principles </span>models!
</li>
<li class='itemize'>The single-particle Schrödinger equation is \(i\hbar \frac {\partial }{\partial t} \Psi (\v {r},t) = \hat {H} \Psi (\v {r},t)\). This is a partial
differential equation for the location- and time-dependent scalar matter
field \(\Psi (\v {r},t)\), with Planck’s constant \(\hbar \) and the Hamilton operator \(\hat {H}\), which
contains the details of the model. The solution of an equation of motion
for many interacting particles, as described by a wavefunction with
mathematical structure \(\Psi (\v {r}_1,\v {r}_2,\dots ,\v {r}_n;t)\), is incomparably more complicated.
</li>
<li class='itemize'>“Semiclassical“ means that the motion of the particles is calculated
according to classical mechanics, but the interactions between the
particles are derived from quantum mechanical laws. This is of course
an approximation that needs to be justified.
</li>
<li class='itemize'>“Mesoscopic” means that the model has an internal length scale and/or
thermal fluctuations are important. These models usually operate on
length scales above the atomic scale (\(\sim \) nm) but below the scales of our
perception of the environment (\(\sim \) mm).



</li>
<li class='itemize'>“Balance” means that the core of the description is a <span class='cmti-12'>conserved
quantity</span>. Conserved are e.g. particle numbers or mass (that is typically
automatically conserved in models that have particles as the core
mathematical object). The <span class='cmti-12'>balance equation </span>or balancing then simply
counts the particles that flow into or out of a volume element over a
certain time interval. Other conserved variables that can be balanced
are momentum and energy. The balance equation is also called the
<span class='cmti-12'>continuity equation</span>.</li></ul>
</div>
<!-- l. 60 --><p class='indent'> At the level of semiclassical and classical mechanics, also referred to as the
kinetic level, models are either described by molecular dynamics or by
the equation of motion of the single-particle probability density in phase
space \(f(\v {r},\v {p})\) - with location \(\v {r}\) and momentum \(\v {p}\) as independent variables. In the
second case, we have a function \(f(\v {r}(t),\v {p}(t),t)\) which depends on time both explicitly
and implicitly via \(\v {r}(t)\) and \(\v {p}(t)\). Let us assume that we need to discretize \(f(\v {r}(t),\v {p}(t),t)\) on
regular grid of discrete sampling points. At a low resolution of \(10\) points per
variable, this corresponds to already \(10,000,000\) interpolation points. This may be
manageable, but the resolution of such a model would not particularly good.
This undertaking is therefore rather useless. We do not want to conceal
the fact that there are methods for the numerical solution to the two
problems described above, but these will not be discussed in detail in this
class.
</p>
<h3 class='sectionHead' id='particles'><span class='titlemark'>1.2 </span> <a id='x1-30001.2'></a>Particles</h3>
<!-- l. 75 --><p class='noindent'>We can therefore roughly distinguish between two types of models: Models that
have individual discrete elements, for example particles (atoms, molecules, grains,
etc.), as their central mathematical objects and models that have continuous fields
(electrostatic potential, ion concentrations, mechanical stresses and strains) as the
central objects. In the first type of model, evolution equations are formulated for
discrete properties defined on the particles, such as their positions \(\v {r}_i\) and velocities
\(\v {v}_i\).
</p><!-- l. 77 --><p class='indent'> For example, to describe the kinetics of these particles, we could solve
Newton’s equations of motion. This means that for each of the \(n\) particles we have
to formulate \(6\) <span class='cmti-12'>ordinary differential equations (ODEs)</span>, which are coupled to each
other, namely: \begin {equation} \dot {\v {r}}_i(t)=\v {v}_i(t)=\frac {\v {p}_i(t)}{m_i} \label {eq:posupdate} \end {equation}<a id='x1-3001r1'></a> This is the equation for the trajectory of the particle \(i\) in space.



Since \(\v {r}_i\) is a vector, Eq. \eqref{eq:posupdate} is a system of \(3\) ordinary
differential equations. differential equations. The velocity \(\v {v}_i\) of the particle \(i\) at
time \(t\) is also subject to a system of differential equations, expressed most
simply using the momentum \(\v {p}_i\), \begin {equation} \dot {\v {p}}_i(t)=\v {F}_{i}(t), \label {eq:velupdate} \end {equation}<a id='x1-3002r2'></a> where \(\v {F}_{i}(t)\) is the force acting of particle \(i\) at
time \(t\). Equation \eqref{eq:velupdate} describes the temporal evolution
of the momentum of the particle \(i\). Equation \eqref{eq:posupdate} and
\eqref{eq:velupdate} are each \(3\times n\) coupled ordinary differential equations. If, for
example, we want to describe the movement of all molecules in a liter
of water by a simulation, this is impossible due to the large number of
equations and we must switch to a description using balance equations and
fields.
</p><!-- l. 100 --><p class='indent'> Newton’s equations of motion \eqref{eq:posupdate} and \eqref{eq:velupdate}
are by their nature <span class='cmti-12'>basic physical principles</span>. They apply to atoms or planets. The
nature of the force itself, \(\v {F}_{ij}\) in the equations above, depends on the nature of the
physical system that we study. It is not necessarily a fundamental interaction,
such as gravity, but may emerge from a complex interplay of multiple physical
mechanisms. A simple example is the Lennard-Jones interaction with interaction
energy \begin {equation} V_{ij} = 4\varepsilon \left [ \left (\frac {\sigma }{r_{ij}}\right )^{12} - \left (\frac {\sigma }{r_{ij}}\right )^{6}\right ] \label {eq:lj_potential} \end {equation}<a id='x1-3003r3'></a> and force \begin {equation} \v {F}_{ij} = -4\varepsilon \left [ 12\left (\frac {\sigma ^{12}}{r_{ij}^{13}}\right ) - 6\left (\frac {\sigma ^{6}}{r_{ij}^{7}}\right )\right ]\hat {r}_{ij}. \label {eq:lj} \end {equation}<a id='x1-3004r4'></a> We have written this in terms of a pair interaction and assumes
that forces are pair-wise additive, meaning the total force on particle \(i\) is given by \(\v {F}_i=\sum _j \v {F}_{ij}\).
The quantity \(r_{ij}\) is the distance between the particles (here atoms or molecules) \(i\) and
\(j\), and \(\hat {r}_{ij}\) is the normal vector pointing from one to the other. The term \(\propto r^{-13}\)
describes the repulsion of the atoms due to the Pauli exclusion principle
and the term \(\propto r^{-7}\) describes the attraction of the atoms due to the London
dispersion interaction (<a href='#XMuser2023-zb'>Müser et al.</a>, <a href='#XMuser2023-zb'>2023</a>). Both interactions are based on
fundamental physical principles, but the formulation Eq. \eqref{eq:lj}
reduces these complex phenomena to a simple constituating law. Such laws
are often called <span class='cmti-12'>constitutive laws</span>. The numerical solution of Newton’s
equations of motion for atoms or molecules is called <span class='cmti-12'>molecular dynamics
simulation</span>.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 113 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The term constitutive law often appears in the context of field theories. For
the Lennard-Jones potential, this term is rather unusual, but this law is
nevertheless of a constitutive nature. </p></div>
<!-- l. 117 --><p class='indent'> Another example of models with discrete elements are network models for
electrical circuits. Here, an element links an electrostatic potential difference
(energy difference) with a current, for example \begin {equation} i = u / R \label {eq:resistor} \end {equation}<a id='x1-3005r5'></a> describes the current \(i\) that flows
through a resistor \(R\) across which the voltage drops by \(u\). Such models are often
referred to as “lumped-element models”. Equation \eqref{eq:resistor} naturally
also has the quality of a <span class='cmti-12'>constitutive law</span>, as complex electronic processes are
behind the individual parameter \(R\). For a fully formulated model of an electric



circuits we also need Kirchhoff’s rules, that have the quality of <span class='cmti-12'>balance equations</span>.
In Fig. <a href='#-the-vertical-arrangement-of-the-boxes-corresponds-to-a-length-scale-with-the-shortest-scales-shown-on-the-bottom-the-boxes-themselves-show-categories-of-models-or-simulation-methods-that-are-used-on-these-scales-in-this-class-we-deal-with-the-discretization-of-fields-and-choose-a-specific-use-case-that-falls-into-the-local-balance-category-'>1.1<!-- tex4ht:ref: fig:Scheme --></a>, these models are therefore referred to as <span class='cmti-12'>global balance </span>models.
“Lumped-element models” also lead to systems of ordinary differential equations,
which are often solved numerically by explicit time propagation. Well-known
representatives of this type of simulation software are, for example <span class='cmti-12'>SPICE </span>or
<span class='cmti-12'>MATLAB Simulink</span>.
</p><!-- l. 124 --><p class='indent'> Such a global balance description is characterized by a lack of interest in local
resolution. We are not interested in densities, but only in total masses, not
in current densities but only in currents. This is best illustrated by the
above-mentioned resistor whose contacts are at different potentials, which results
in a current flow. We do not ask ourselves how the current is distributed in
the resistor. We do not even ask whether the resistor is homogeneous or
inhomogeneous. The model only requires the overall resistance \(R\), essentially
modeling the resistor as a black box to which we assign the value of a single
parameter. This approach is discussed in detail in electrical engineering and
systems theory.
</p><!-- l. 127 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='fields'><span class='titlemark'>1.3 </span> <a id='x1-40001.3'></a>Fields</h3>
<!-- l. 129 --><p class='noindent'>However, if we now realize that our black box is only insufficiently described with
one parameter, then we need to replace it with a more complex models, for
example and equivalent circuit with details that resolve the internal state of the
component. This in turn can be taken so far, that a continuum is created at the
end - we have arrived at a <span class='cmti-12'>local balance </span>descriptions. Staying with the example of
flow, we need parameters such as conductivity (or for fluids viscosity
or diffusivity), which now describe the resistance to flow locally. These
parameters can be obtained from experiments or <span class='cmti-12'>ab-initio </span>simulations but
are required as input to (or the “parameterization” of) the local balance
description.
</p><!-- l. 136 --><p class='indent'> Local balance means that we can assign density, concentration, temperature or
similar quantity to each point in space. However, this means that the temporal
changes in the local degrees of freedom - i.e. the momentum or velocity - are
constrained by a <span class='cmti-12'>local, thermodynamic-equilibrium </span>condition. (In thermodynamic
equilibrium, the momentum satisfies a Maxwell-Boltzmann distribution.) This
local equilibrium does not mean that we no longer have dynamics: If we think of a
swarm of gas or liquid molecules, then their individual velocities follow an
equilibrium distribution function, but their mean follows the balance equation.
The dynamics are therefore averaged over a huge number of these particles. Local



balance also does not mean that different temperatures or densities cannot exist
at different locations. The differences in these parameters are then the
driving forces of the dynamics – temperature gradients, density gradients,
etc.
</p><!-- l. 143 --><p class='indent'> Such models fall into the category of <span class='cmti-12'>field theories</span>, and their mathematical
description is based on <span class='cmti-12'>partial </span>differential equations. (This is in contrast to the
ordinary differential equations of discrete models.) A <span class='cmti-12'>transport theory</span>
is a specific class of field theory that is based on the balancing mass,
momentum or energy and requiring constitutive laws for the description of the
material behavior. These constitutive laws contain <span class='cmti-12'>transport parameters </span>such
as the viscosity or diffusion constant. There are also field theories that
have the character of a basic physical principle. This is, for example,
the Schrödinger equation mentioned above or the Maxwell equations of
electrodynamics.
</p><!-- l. 145 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='which-model-is-the-right-one'><span class='titlemark'>1.4 </span> <a id='x1-50001.4'></a>Which model is the right one?</h3>
<!-- l. 147 --><p class='noindent'>Choosing and formulating the right model is a form of art. Just because a theory
is called “quantum mechanics” (and leaves one or the other in awe at
its complexity), it does not necessarily offer the solution to the problem
that we are trying to solve. Too much detail can even be a hindrance
and we must constantly ask ourselves how much detail is necessary in
model and simulation. We always need ask ourselves before we start a
simulation: “Is a simulation of this complexity really necessary, or can I
simplify the problem?” The simulation should be seen as a tool and not
as an end in itself, according to the American mathematician Richard
Wesley Hamming (*1915, \(\dagger \)1998): “<span class='cmti-12'>The purpose of computing is insight, not
numbers</span>”.



</p>
<h2 class='likechapterHead' id='bibliography'><a id='x1-6000'></a>Bibliography</h2>
<div class='thebibliography'>
<p class='bibitem'><span class='biblabel'>
<a id='XAllen1989-nt'></a><span class='bibsp'>   </span></span>M. P. Allen and D. J. Tildesley. <span class='cmti-12'>Computer Simulation of Liquids</span>. Oxford
University Press, 1989.
</p>
<p class='bibitem'><span class='biblabel'>
<a id='XMartin2004-zf'></a><span class='bibsp'>   </span></span>R. M. Martin. <span class='cmti-12'>Electronic Structure</span>. Cambridge University Press, 2004.
</p>
<p class='bibitem'><span class='biblabel'>
<a id='XMuser2023-zb'></a><span class='bibsp'>   </span></span>M. H. Müser, S. V. Sukhomlinov, and L. Pastewka. Interatomic
potentials: achievements and challenges. <span class='cmti-12'>Advances in Physics: X</span>, 8(1):
2093129, Jan. 2023.
</p>
</div>

