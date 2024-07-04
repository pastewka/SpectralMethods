---
layout: default
title: "Fourier spectral methods"
parent: Lecture
date: 2024-07-04
categories: lecture
author: Lars Pastewka
nav_order: 5
---


<h2 class='chapterHead' id='fourier-spectral-methods'><span class='titlemark'>Chapter 6</span><br /><a id='x1-10006'></a>Fourier spectral methods</h2>
<div class='framedenv' id='shaded_-1'>
<!-- l. 6 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> We now develop the ideas for solving partial differential equations
outlined in the previous chapters. In this chapter, we specifically describe solution
strategies using the Fourier basis. This leads to a solution method that belongs to
the class of <span class='cmti-12'>spectral methods</span>. The chapter also describes how to extend the
solution approaches to multidimensional spaces and how to treat nonlinear terms.
</p></div>
<h3 class='sectionHead' id='differential-operators'><span class='titlemark'>6.1 </span> <a id='x1-20006.1'></a>Differential operators</h3>
<!-- l. 12 --><p class='noindent'>To solve differential equations, we now use exactly the same methods that we
developed in the previous chapter: Minimizing the residual using the Galerkin
method. Our residual now has the general form \begin {equation} R(x,y,z,\ldots ; a_0, a_1, \ldots , a_N) = \mathcal {L} u_N(x,y,z,\ldots ) - f(x,y,z,\ldots ), \end {equation}<a id='x1-2001r1'></a> where the unknown function \(u_N\) is
represented here as a series expansion into a certain basis \(\varphi _n(x,y,z)\). The Galerkin method
requires \begin {equation} (\varphi _n, R) = 0 \end {equation}<a id='x1-2002r2'></a> for each \(n\).
</p><!-- l. 24 --><p class='indent'> We now discuss the Fourier basis for periodic functions on \(x\in [0,L]\) in one dimension, \begin {equation} \varphi _n(x) = \exp (i q_n x) \label {eq:fourierbasis2} \end {equation}<a id='x1-2003r3'></a>
with \(q_n = 2\pi n/L\). The operator \(\mathcal {L}\) can contain any differential operations that act on the basis
functions, for example \begin {align} \frac {d}{dx} \varphi _n(x) &amp;= iq_n \varphi _n(x) \\ \frac {d^2}{dx^2} \varphi _n(x) &amp;= -q_n^2 \varphi _n(x). \end {align}
</p><!-- l. 34 --><p class='indent'> The derivatives of the (Fourier) basis functions result in the <span class='cmti-12'>same </span>basis
function and an algebraic factor. It is also said that the basis functions <span class='cmti-12'>diagonalize</span>
the differential operator. (This will be different for the finite elements discussed in
the next chapter).
</p><!-- l. 36 --><p class='indent'> This property is particularly useful because, at least for linear differential
equations, the residual becomes a trivial series expansion again and we can easily
determine the coefficients using the orthogonality of the basis.
</p><!-- l. 38 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='poisson-equation-in-one-dimension'><span class='titlemark'>6.2 </span> <a id='x1-30006.2'></a>Poisson equation in one dimension</h3>
<!-- l. 41 --><p class='noindent'>We use the (one-dimensional) Poisson equation, \begin {equation} \nabla ^2 \Phi \equiv \frac {\dif ^2 \Phi }{\dif x^2} = - \frac {\rho }{\varepsilon }, \label {eq:poisson-1d} \end {equation}<a id='x1-3001r4'></a> as a demonstrator. Here \(\rho \) is a
charge density and \(\Phi \) is the electrostatic potential. The residual is therefore \begin {equation} R(x)=\frac {\dif ^2 \Phi }{\dif x^2} + \frac {\rho }{\varepsilon }, \label {eq:poisson-1d-res} \end {equation}<a id='x1-3002r5'></a> and
the solution of Eq. \eqref{eq:poisson-1d} is given by \(R(x)=0\).
</p><!-- l. 59 --><p class='indent'> Formally, we now write the potential as the series expansion \begin {equation} \Phi (x) \approx \Phi _N(x) = \sum _{n=-(N-1)/2}^{(N-1)/2} a_n \varphi _n(x), \end {equation}<a id='x1-3003r6'></a> whereby we will
not explicitly specify the summation limits in the following. We also expand
the right-hand side of Eq. \eqref{eq:poisson-1d} into a series with the
same basis functions, \begin {equation} \rho _N(x) = \sum _{n=-(N-1)/2}^{(N-1)/2} b_n \varphi _n(x). \label {eq:seriesphi} \end {equation}<a id='x1-3004r7'></a> Substituting this into Eq. \eqref{eq:poisson-1d-res}
we obtain \begin {equation} R_N(x) = - \sum _n a_n q_n^2 \varphi _n(x) + \frac {1}{\varepsilon } \sum _n b_n \varphi _n(x). \end {equation}<a id='x1-3005r8'></a> We now multiply this from the left by the basis functions, \((\varphi _k, R_N)\)
(Galerkin method) and, due to the orthogonality of the basis functions, we



obtain the equations \begin {equation} (\varphi _k, R_N) = - L q_k^2 a_k + L b_k/\varepsilon . \end {equation}<a id='x1-3006r9'></a> The factor \(L\) appears because the basis functions are
not normalized. The condition \((\varphi _k, R_N)=0\) leads to \(a_k = b_k/(q_k^2 \varepsilon )\). The approximate solution of
the Poisson equation is thus given by \begin {equation} \Phi _N(x) = \sum _n \frac {b_n}{q_n^2 \varepsilon } \varphi _n(x). \label {eq:discrpoissonfouriersol} \end {equation}<a id='x1-3007r10'></a> This is the Fourier series of the
solution.
</p><!-- l. 84 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='transition-to-the-fourier-transform'><span class='titlemark'>6.3 </span> <a id='x1-40006.3'></a>Transition to the Fourier transform</h3>
<!-- l. 86 --><p class='noindent'>The Fourier basis Eq. \eqref{eq:fourierbasis2} is periodic on a finite domain of
length \(L\). If we let the length \(L\) go to infinity, we get a formulation for non-periodic
functions. This leads directly to the <span class='cmti-12'>Fourier transform</span>.
</p><!-- l. 88 --><p class='indent'> We write the series expansion as \begin {equation} \Phi _N(x) = \sum _{n=-N}^N a_n \varphi _n(x) = \sum _{n=-N}^N a_n \exp \left ( i q_n x \right ) = \sum _{n=-N}^N \frac {\Delta q}{2\pi }\,\tilde {\Phi }(q_n) \exp \left ( i q_n x \right ) \label {eq:fouriertrafo1} \end {equation}<a id='x1-4001r11'></a> with \(\Delta q = q_{n+1}-q_n = 2\pi /L\) and rescaled coefficients \(\tilde {\Phi }(q_n)=L a_n\). Here, only
the factor \(1=L \Delta q/2\pi \) was inserted on the right-hand side of Eq. \eqref{eq:fouriertrafo1}.
This now helps to form the limits \(L\to \infty \) and \(N\to \infty \). In this case, \(\Delta q \to dq\) and the sum becomes the
integral. This yields \begin {equation} \Phi (x) = \int _{-\infty }^\infty \frac {\dif q}{2\pi }\,\tilde {\Phi }(q) \exp \left ( i q x \right ), \label {eq:fouriertrafo2} \end {equation}<a id='x1-4002r12'></a> the <span class='cmti-12'>inverse Fourier transform</span>.
</p><!-- l. 100 --><p class='indent'> The (forward) transform is obtained via a similar argument. We now know
that \begin {equation} \tilde {\Phi }(q_n) = L a_n = L \frac {(\varphi _n, \Phi _N)}{(\varphi _n, \varphi _n)} = (\varphi _n, \Phi _N) = \int _0^L \dif x \, \Phi _N(x) \exp \left ( -i q_n x \right ). \end {equation}<a id='x1-4003r13'></a> In the limiting case \(L\to \infty \) and \(N\to \infty \) this becomes \begin {equation} \tilde {\Phi }(q) = \int _{-\infty }^\infty \dif x \, \Phi (x) \exp \left ( -i q x \right ), \label {eq:fouriertrafo3} \end {equation}<a id='x1-4004r14'></a> of the Fourier transform. The
Fourier transform is useful to obtain analytical solutions for partial differential
equations on infinite domains.
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 121 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> A tilde \(\tilde {f}(q)\) denotes the Fourier transform of a function \(f(x)\). The Fourier
transform is a function of the wave vector \(q\). In contrast, from the Fourier series we
obtain countable coefficients \(a_n\). The reason for this is the periodicity of the
function. </p></div>
<!-- l. 125 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='poisson-equation-in-multiple-dimensions'><span class='titlemark'>6.4 </span> <a id='x1-50006.4'></a>Poisson equation in multiple dimensions</h3>
<!-- l. 127 --><p class='noindent'>Similar to how we constructed an approximate solution for a differential equation
using a series expansion, we can use the approach Eq. \eqref{eq:fouriertrafo2} to
obtain analytical solutions. In this section, this is demonstrated using the Poisson
equation in three dimensions.
</p><!-- l. 129 --><p class='indent'> In three dimensions, the Poisson equation is \begin {equation} \nabla ^2 \Phi \equiv \frac {\partial ^2 \Phi }{\partial x^2} + \frac {\partial ^2 \Phi }{\partial y^2} + \frac {\partial ^2 \Phi }{\partial z^2} = - \frac {\rho }{\varepsilon }. \label {eq:poisson-3d} \end {equation}<a id='x1-5001r15'></a> In contrast to
Eq. \eqref{eq:poisson-1d}, the partial derivative \(\partial \) now appears here because \(\Phi (x,y,z)\)
depends on three variables (the Cartesian coordinates).
</p><!-- l. 140 --><p class='indent'> The generalization of the Fourier basis and thus also of the Fourier



transform to three dimensions is trivial. A basis is obtained by multiplying
basis functions in the Cartesian directions (\(x\), \(y\) and \(z\)). Usually, you now
need three indices for the coefficients, which denote the basis in \(x\), \(y\) and \(z\)
respectively. The result is a series expansion \begin {equation} \begin {split} \Phi _{NMO}(x,y,z) =&amp; \sum _{n=-(N-1)/2}^{(N-1)/2} \sum _{m=-(M-1)/2}^{(M-1)/2} \sum _{o=-(O-1)/2}^{(O-1)/2} a_{nmo} \varphi _n(x) \varphi _m(y) \varphi _o(z) \\ \equiv &amp; \sum _{n=-(N-1)/2}^{(N-1)/2} \sum _{m=-(M-1)/2}^{(M-1)/2} \sum _{o=-(O-1)/2}^{(O-1)/2} a_{nmo} \varphi _{nmo}(x,y,z) \end {split} \end {equation}<a id='x1-5002r16'></a> with (possibly different)
truncation orders \(N\), \(M\) and \(O\). The basis set is given here by the functions \(\varphi _{nmo}(x,y,z)=\varphi _n(x)\varphi _m(y)\varphi _o(z)\).
Orthogonality of this basis set is trivially derived from the orthogonality of the
one-dimensional basis functions \(\varphi _n(x)\). The generalization of the Fourier transform
follows directly from this. The Fourier inverse transform is written as \begin {equation} \Phi (x,y,z) = \int _{-\infty }^\infty \frac {\dif ^3 q}{(2\pi )^3}\,\tilde {\Phi }(q_x, q_y, q_z) \exp \left ( i q_x x + i q_y y + i q_z z\right ), \label {eq:fouriertrafo3d} \end {equation}<a id='x1-5003r17'></a> where the
Fourier transform \(\tilde {\Phi }\) now naturally depends on three wave vectors \(q_x\), \(q_y\) and \(q_z\).
The differential operator \(\dif ^3 q=\dif q_x \dif q_y \dif q_z\) is a shorthand notation for three-dimensional
integration.
</p><!-- l. 154 --><p class='indent'> We can now insert Eq. \eqref{eq:fouriertrafo3d} into the PDGL
Eq. \eqref{eq:poisson-3d} and obtain \begin {equation} R(\v {r}) = \int _{-\infty }^\infty \frac {\dif ^3 q}{(2\pi )^3}\, \left [ \left (-q_x^2 - q_y^2 - q_z^2\right ) \tilde {\Phi }(\v {q}) + \frac {\tilde {\rho }(\v {q})}{\varepsilon } \right ] \exp \left ( i \v {q}\cdot \v {r} \right ) = 0 \end {equation}<a id='x1-5004r18'></a> with \(\v {r}=(x,y,z)\) and \(\v {q}=(q_x,q_y,q_z)\). This equation must be fulfilled
for every \(x,y,z\) and therefore the argument of the integration must disappear, i.e.
\begin {equation} -q^2 \tilde {\Phi }(\v {q}) + \frac {\tilde {\rho }(\v {q})}{\varepsilon } = 0. \label {eq:fourierpoisson2d} \end {equation}<a id='x1-5005r19'></a>
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 176 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> An alternative argument is obtained by writing the Fourier transform of \(R(x,y,z)\): \begin {equation} R(q_x', q_y', q_z') = \int \dif ^3 r \, R(\v {r}) \exp \left ( -i q_x x - i q_y y - i q_z z \right ). \end {equation}<a id='x1-5006r20'></a>
This contains terms of the form \begin {equation} \int _{-\infty }^\infty \dif x\, \exp \left (i (q_x - q_x') x\right ) = 2\pi \delta (q_x - q_x'), \end {equation}<a id='x1-5007r21'></a> which are expressions of the orthogonality of the
basis functions. Since the basis functions are now “parameterized” with a
continuous \(q_x\) (instead of a discrete \(n\)), a Dirac \(\delta \) function is obtained instead of the
Kronecker \(\delta \) in the orthogonality relation. </p></div>
<!-- l. 190 --><p class='indent'> Equation \eqref{eq:fourierpoisson2d} can easily be solved analytically. This
yields \begin {equation} \tilde {\Phi }(\v {q}) = \frac {\tilde {\rho }(\v {q})}{\varepsilon q^2} \label {eq:fourierpoissonsol} \end {equation}<a id='x1-5008r22'></a> with \(q=|\v {q}|\). This is equivalent to solving Eq. \eqref{eq:discrpoissonfouriersol}
for the Poisson equation on a periodic domain. The difficulty now lies in
evaluating the back and forth transformation for a given \(\rho (x,y,z)\).
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 199 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Example:</span></span> As an example, we now consider the solution for a point charge \(Q\) at the
origin, \begin {equation} \rho (x,y,z) = Q \delta (x) \delta (y) \delta (z). \end {equation}<a id='x1-5009r23'></a> The Fourier transform of the charge density \(\rho \) is obtained from
Eq. \eqref{eq:fouriertrafo3}, \begin {equation} \tilde {\rho }(q_x,q_y,q_z) = Q. \end {equation}<a id='x1-5010r24'></a> I.e. the Fourier transform of the electrostatic
potential is given by (see Eq. \eqref{eq:fourierpoissonsol}) \begin {equation} \tilde {\Phi }(\v {q}) = \frac {Q}{\varepsilon q^2}, \end {equation}<a id='x1-5011r25'></a> and thus the
representation in real space is \begin {equation} \begin {split} \Phi (\v {r}) =&amp; \int _{-\infty }^\infty \frac {\dif ^3 q}{(2\pi )^3}\, \frac {Q}{\varepsilon q^2} \exp \left ( i \v {q}\cdot \v {r} \right ) \\ =&amp; \frac {Q}{(2\pi )^3 \varepsilon } \int _0^\infty \dif q \int _0^{2\pi } \dif \phi \int _{-1}^1 \dif (\cos \theta ) \, \exp \left ( i q r \cos \theta \right ) \end {split} \end {equation}<a id='x1-5012r26'></a> where \(\dif ^3 q = q^2 \dif q \dif \phi \dif (\cos \theta )\) with azimuth angle \(\phi \) and elevation angle \(\theta \),
was used (see also Fig. <a href='#volume-element-for-integration-in-spherical-coordinates'>6.1<!-- tex4ht:ref: fig:volume-spherical --></a>). We require here (without limiting the generality)
that \(\v {r}\) points in the direction of the zenith.
</p><!-- l. 227 --><p class='indent'> One obtains \begin {equation} \begin {split} \Phi (\v {r}) =&amp; \frac {Q}{(2\pi )^2 \varepsilon } \int _0^\infty \dif q \int _{-1}^1 \dif (\cos \theta ) \, \exp \left ( i q r \cos \theta \right ) \\ =&amp; \frac {Q}{(2\pi )^2 \varepsilon } \int _0^\infty \dif q\, \frac {\exp ( i q r ) - \exp (-iqr)}{iqr} \\ =&amp; \frac {Q}{(2\pi )^2 \varepsilon } \int _{-\infty }^\infty \dif q\, \frac {\sin q r}{qr} \\ =&amp; \frac {Q}{4\pi \varepsilon r}, \end {split} \end {equation}<a id='x1-5013r27'></a> where \(\int \dif x\,\sin x/x=\pi \) was used. This is the known solution for the
electrostatic potential of a point charge. It is also called the fundamental
solution or <span class='cmti-12'>Green’s function </span>of the (three-dimensional) Poisson equation.
</p></div>
<figure class='figure'>







<!-- l. 252 --><p class='noindent' id='volume-element-for-integration-in-spherical-coordinates'><img alt='PIC' height='390' src='Figures/illustr_angles_1.svg' width='390' /> <a id='x1-5014r1'></a>
</p>
<figcaption class='caption'><span class='id'>Figure 6.1: </span><span class='content'>Volume element for integration in spherical coordinates.
</span></figcaption><!-- tex4ht:label?: x1-5014r1 -->



</figure>



<h2 class='likechapterHead' id='bibliography'><a id='x1-6000'></a>Bibliography</h2>

