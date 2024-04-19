---
layout: default
title: "Approximation and interpolation"
parent: Lecture
date: 2024-04-19
categories: lecture
author: Lars Pastewka
nav_order: 4
---


<h2 class='chapterHead' id='approximation-and-interpolation'><span class='titlemark'>Chapter 5</span><br /><a id='x1-10005'></a>Approximation and interpolation</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 6 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> We now apply the idea of basis functions to approximate functions. To
do this, we return to the concept of the residual. The goal of function
approximation is that the approximated function minimizes the residual. Building
on these ideas, we will then discuss the approximation of differential equations in
the next chapter. </p></div>
<h3 class='sectionHead' id='residual'><span class='titlemark'>5.1 </span> <a id='x1-20005.1'></a>Residual</h3>
<!-- l. 12 --><p class='noindent'>In the previous section, we described how a series expansion can be constructed
using basis functions. A typical series expansion contains a finite number of
elements \(N+1\) and has the form \begin {equation} f_N(x) = \sum _{n=0}^N a_n \varphi _n(x), \end {equation}<a id='x1-2001r1'></a> where \(\varphi _n(x)\) are the basis functions introduced in the
previous chapter.
</p><!-- l. 18 --><p class='indent'> We now want to approach the question of how we can approximate an
arbitrary function \(f(x)\) via such a basis function development. To do this, we define
the residual \begin {equation} R(x) = f_N(x) - f(x), \end {equation}<a id='x1-2002r2'></a> which vanishes at every point \(x\) if \(f_N(x)\equiv f(x)\). For an approximation we want to
“minimize” this residual. (By minimize here we mean to bring it as close
to zero as possible.) So we are looking for the coefficients \(a_n\) of the series
expansion, which approximates the function \(f(x)\) in the sense of minimizing the
residual.
</p><!-- l. 24 --><p class='indent'> At this point, it should be noted that the basis functions must be defined in
the same space for the target function \(f(x)\). For the approximation of a periodic
function \(f(x)\), a periodic basis set should also be used.
</p><!-- l. 26 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='collocation'><span class='titlemark'>5.2 </span> <a id='x1-30005.2'></a>Collocation</h3>
<!-- l. 28 --><p class='noindent'>The first minimization strategy introduced here is <span class='cmti-12'>collocation</span>. This method
requires that the residual disappears at selected collocation points \(y_n\), \begin {equation} R(y_n) = 0 \quad \text {or}\quad f_N(y_n) = f(y_n). \end {equation}<a id='x1-3001r3'></a> The number
of collocation points must correspond to the number of coefficients in the series
expansion. The choice of ideal collocation points \(y_n\) itself is non-trivial, and we will
only discuss specific cases here.
</p><!-- l. 34 --><p class='indent'> As a first example, we discuss here an evolution with \(N\) finite elements. As
collocation points we choose the interpolation points of the base, \(y_n=x_n\). At these
sampling points, only one of the basis functions is non-zero, \(\varphi _n(y_n)=1\) and \(\varphi _n(y_k)=0\) if \(n\not =k\). This means
that the condition \begin {equation} R(y_n) = 0 \end {equation}<a id='x1-3002r4'></a> trivially leads to \begin {equation} a_n = f(y_n). \end {equation}<a id='x1-3003r5'></a> The coefficients \(a_n\) are therefore given by the
function value of the function to be approximated at the collocation point. The
approximation is therefore a piecewise linear function between the function values



of \(f(x)\).
</p><!-- l. 44 --><p class='indent'> As a second example, we discuss a Fourier series with corresponding \(2N+1\) Fourier
basis functions, \begin {equation} \varphi _n(x) = \exp \left ( i q_n x \right ). \end {equation}<a id='x1-3004r6'></a> In the context of a collocation method, we require that the
residual vanishes on \(2N+1\) equidistant points, \(R(y_n)=0\) with \begin {equation} y_n = n L / (2N+1). \end {equation}<a id='x1-3005r7'></a> The condition for this is then \begin {equation} \sum _{k=-N}^{N} a_k \exp \left (i q_k y_n\right ) = \sum _{k=-N}^{N} a_k \exp \left (i 2\pi \frac {k n}{2N+1}\right ) = f(y_n). \label {eq:fourier-collocation} \end {equation}<a id='x1-3006r8'></a>
Equations \eqref{eq:fourier-collocation} can now be solved for \(a_k\). We use the fact
that for equidistant collocation points the Fourier matrix \(W_{kn}=\exp (i2\pi kn/(2N+1))\) is unitary (except for
one factor), i.e. its inverse is given by the adjoint: \(\sum _n W_{kn} W_{nl}^* = (2N+1)\delta _{kl}\). We can therefore multiply
Eq. \eqref{eq:fourier-collocation} by \(W_{nl}^*\) and sum over \(n\). This results in \begin {equation} \sum _{n=-N}^{N} \sum _{k=-N}^{N} a_k \exp \left [i 2\pi \frac {(k - l) n}{2N+1}\right ] = \sum _{k=-N}^{N} N a_k \delta _{kl} = N a_l \end {equation}<a id='x1-3007r9'></a> where \begin {equation} \sum _{n=-N}^{N} \exp \left [i 2\pi \frac {(k - l) n}{2N+1}\right ] = (2N+1)\delta _{kl} \end {equation}<a id='x1-3008r10'></a> was
used. This means that the coefficients can be expressed as \begin {equation} a_l = \frac {1}{2N+1} \sum _{n=-N}^{N} f\left (\frac {nL}{2N+1}\right ) \exp \left (-i 2\pi \frac {l n}{2N+1}\right ), \end {equation}<a id='x1-3009r11'></a> can be determined.
This is the <span class='cmti-12'>discrete Fourier transform </span>of the function \(f(y_n)\) discretized on the
collocation points.
</p><!-- l. 97 --><p class='indent'> As a simple example, we show the approximation of the example function \(f(x)=\sin (2\pi x)^3 + \cos (6\pi (x^2-1/2))\)
using the Fourier basis and finite elements. Figure <a href='#-approximation-of-the-periodic-function-fx-x-x-on-the-interval-with-a-fourier-basis-and-finite-elements-in-each-case-top-and-bottom-basis-functions-were-used-the-coefficients-were-determined-using-the-galerkin-method-the-approximation-with-basis-functions-cannot-map-the-two-right-oscillations-of-the-target-function-fx-in-both-cases-'>5.2<!-- tex4ht:ref: fig:example-collocation --></a> shows this approximation
for \(2N+1=5\) and \(2N+1=11\) basis functions with equidistant collocation points.
</p>
<figure class='figure' id='-approximation-of-the-periodic-function-fx-x-x-on-the-interval-with-a-fourier-basis-and-finite-elements-in-each-case-top-and-bottom-basis-functions-were-used-the-coefficients-were-determined-using-the-collocation-method-the-round-dots-show-the-collocation-points-both-approximations-run-exactly-through-these-collocation-points-the-right-collocation-point-is-identical-to-the-left-one-due-to-the-periodicity-the-approximation-with-n-basis-functions-cannot-map-the-two-right-oscillations-of-the-target-function-fx-in-both-cases-'>







<div class='subfigure'>
<!-- l. 108 --><p class='noindent'></p><!-- l. 109 --><p class='noindent'><img alt='PIC' height='249' src='Figures/coll5.svg' width='585' /> </p></div>
<div class='subfigure'>
<!-- l. 111 --><p class='noindent'></p><!-- l. 112 --><p class='noindent'><img alt='PIC' height='256' src='Figures/coll11.svg' width='585' /> </p></div>
<a id='x1-3010r1'></a>
<div class='caption'><span class='id'>Figure 5.1: </span><span class='content'>Approximation of the periodic function \(f(x)=\sin (2\pi x)^3 + \cos (6\pi (x^2-1/2))\) on the interval \([0,1]\) with a
Fourier basis and finite elements. In each case \(5\) (top) and \(11\) (bottom) basis
functions were used. The coefficients were determined using the collocation
method. The round dots show the collocation points. Both approximations
run exactly through these collocation points. (The right collocation point is
identical to the left one due to the periodicity). The approximation with \(N=5\)
basis functions cannot map the two right oscillations of the target function \(f(x)\)
in both cases
</span></div>
.



</figure>
<!-- l. 119 --><p class='indent'> The figure shows that all approximations run exactly through the collocation
points, as required by the collocation condition. The two approaches interpolate
differently between the collocation points <span class='cmti-12'>interpolate</span>. The finite elements lead
to a linear interpolation between the points. The Fourier basis is more
complicated. The curve between the collocation points is called <span class='cmti-12'>Fourier
interpolation</span>.
</p>
<h3 class='sectionHead' id='weighted-residuals'><span class='titlemark'>5.3 </span> <a id='x1-40005.3'></a>Weighted residuals</h3>
<!-- l. 124 --><p class='noindent'>We would now like to generalize the collocation method. To do this, we introduce
the concept of <span class='cmti-12'>test function</span>. Instead of requiring that the residual vanishes at
individual points, we require that the scalar product \begin {equation} (v, R) = 0 \label {eq:test-function} \end {equation}<a id='x1-4001r12'></a> with a function \(v(x)\) disappears.
If Eq. \eqref{eq:test-function} vanishes for any test function \(v(x)\), then the “weak”
formulation Eq. \eqref{eq:test-function} is identical to the strong formulation \(R(x)=0\).
Equation \eqref{eq:test-function} is called a “weak” formulation because
the condition is only fulfilled in the integral sense. In particular, it is
shown in Chapter 9 that this weak formulation leads to a weak <span class='cmti-12'>solution</span>,
which cannot satisfy the original (strong) PDGL at every point. The
condition \eqref{eq:test-function} is often subsumed under the term <span class='cmti-12'>weighted
residuals</span>.
</p><!-- l. 131 --><p class='indent'> A special set of test functions leads directly to the collocation method. We
choose the set of \(N\) test functions \begin {equation} v_n(x) = \delta (x-y_n) \label {eq:colloctest} \end {equation}<a id='x1-4002r13'></a> where \(\delta (x)\) is the Dirac \(\delta \) function and \(y_n\) the collocation
points. The condition \((v_n,R)=0\) for all \(n\in [0,N-1]\) leads directly to the collocation condition
\(R(y_x)=0\).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 138 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The Dirac \(\delta \) function should be familiar from lectures on signal
processing. The most important property of this function is the filter
property, \begin {equation} \int _{-\infty }^{\infty } \dif x\, f(x) \delta (x-x_0) = f(x_0), \end {equation}<a id='x1-4003r14'></a> i.e. the integral over the product of the \(\delta \) function gives the
function value at which the argument of the \(\delta \) function disappears. All other
properties follow from this, e.g. \begin {equation} \int \dif x\, \delta (x) = \Theta (x), \end {equation}<a id='x1-4004r15'></a> where \(\theta (x)\) is the (Heaviside) step function.
</p></div>
<!-- l. 150 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='galerkin-method'><span class='titlemark'>5.4 </span> <a id='x1-50005.4'></a>Galerkin method</h3>



<!-- l. 152 --><p class='noindent'>The Galerkin method is based on the idea of using the basis functions \(\varphi _n\) of the
series expansion as test functions. This leads to the \(N\) conditions \begin {equation} (\varphi _n, R) = 0, \label {eq:galerkinortho} \end {equation}<a id='x1-5001r16'></a> resp.
\begin {equation} (\varphi _n, f_N) = (\varphi _n, f). \end {equation}<a id='x1-5002r17'></a>
</p><!-- l. 162 --><p class='indent'> For an orthogonal set of basis functions, you directly obtain \begin {equation} a_n = \frac {(\varphi _n, f)}{(\varphi _n, \varphi _n)}. \end {equation}<a id='x1-5003r18'></a> This approach
has already been discussed in section <span class='cmbx-12'>??</span>.
</p><!-- l. 168 --><p class='indent'> For a non-orthogonal basis set, e.g. the basis of the finite elements, a linear
system of equations is obtained, \begin {equation} \sum _{m=0}^N (\varphi _n,\varphi _m) a_m = (\varphi _n, f), \label {eq:galerkin-coefficients} \end {equation}<a id='x1-5004r19'></a> where the matrix \(A_{nm}=(\varphi _n,\varphi _m)\) is sparse for the finite
elements.
</p><!-- l. 175 --><p class='indent'> Let us now return to our example function \(f(x)=\sin (2\pi x)^3 + \cos (6\pi (x^2-1/2))\). Figure <a href='#-approximation-of-the-periodic-function-fx-x-x-on-the-interval-with-a-fourier-basis-and-finite-elements-in-each-case-top-and-bottom-basis-functions-were-used-the-coefficients-were-determined-using-the-galerkin-method-the-approximation-with-basis-functions-cannot-map-the-two-right-oscillations-of-the-target-function-fx-in-both-cases-'>5.2<!-- tex4ht:ref: fig:example-collocation --></a> shows the
approximation of this function with Fourier and finite element basis sets and the
Galerkin method. There are no collocation points and the approximation using
finite elements does not exactly match the function to be approximated at the
interpolation points. The function is only approximated in the integral
sense.
</p>
<figure class='figure' id='-approximation-of-the-periodic-function-fx-x-x-on-the-interval-with-a-fourier-basis-and-finite-elements-in-each-case-top-and-bottom-basis-functions-were-used-the-coefficients-were-determined-using-the-galerkin-method-the-approximation-with-basis-functions-cannot-map-the-two-right-oscillations-of-the-target-function-fx-in-both-cases-'>







<div class='subfigure'>
<!-- l. 186 --><p class='noindent'></p><!-- l. 187 --><p class='noindent'><img alt='PIC' height='249' src='Figures/gal5.svg' width='585' /> </p></div>
<div class='subfigure'>
<!-- l. 189 --><p class='noindent'></p><!-- l. 190 --><p class='noindent'><img alt='PIC' height='247' src='Figures/gal11.svg' width='585' /> </p></div>
<a id='x1-5005r2'></a>
<div class='caption'><span class='id'>Figure 5.2: </span><span class='content'>Approximation of the periodic function \(f(x)=\sin (2\pi x)^3 + \cos (6\pi (x^2-1/2))\) on the interval \([0,1]\) with a
Fourier basis and finite elements. In each case \(5\) (top) and \(11\) (bottom) basis
functions were used. The coefficients were determined using the Galerkin
method. The approximation with \(5\) basis functions cannot map the two right
oscillations of the target function \(f(x)\) in both cases.
</span></div>



</figure>
<div class='framedenv' id='shaded*-1'>
<!-- l. 197 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The Galerkin condition (see also Eq. \eqref{eq:galerkinortho})
\begin {equation} (\varphi _n, R) = 0, \end {equation}<a id='x1-5006r20'></a> means that the residual is <span class='cmti-12'>orthogonal </span>to all basis functions. In other
words, the residual can only contain contributions to the function that
cannot be mapped with the given basis set. However, this also means that
we can systematically improve our solution by extending the basis set.
</p></div>
<h3 class='sectionHead' id='least-squares'><span class='titlemark'>5.5 </span> <a id='x1-60005.5'></a>Least squares</h3>
<!-- l. 207 --><p class='noindent'>An alternative approach to approximation is to minimize the square of the
residual, \((R, R)\), also knows as a <span class='cmti-12'>least squares </span>approach. For a general series expansion
with \(N\) basis functions, we obtain \begin {equation} \begin {split} (R, R) &amp;= (f, f) + (f_N, f_N) - (f_N, f) - (f, f_N) \\ &amp;= (f, f) + \sum _{n=0}^N \sum _{m=0}^N a_n^* a_m (\varphi _n, \varphi _m) - \sum _{n=0}^N a_n^* (\varphi _n, f) - \sum _{n=0}^N a_n (f, \varphi _n). \end {split} \end {equation}<a id='x1-6001r21'></a> This error square is minimized if \begin {equation} \frac {\partial (R,R)}{\partial a_k} = \sum _{n=0}^N a_n^* (\varphi _n, \varphi _k) - (f, \varphi _k) = 0 \end {equation}<a id='x1-6002r22'></a> and \begin {equation} \frac {\partial (R,R)}{\partial a^*_k} = \sum _{n=0}^N a_n (\varphi _k, \varphi _n) - (\varphi _k, f) = 0. \end {equation}<a id='x1-6003r23'></a> This
expression is identical to Eq. \eqref{eq:galerkin-coefficients} of the Galerkin
method.



</p>
<h2 class='likechapterHead' id='bibliography'><a id='x1-7000'></a>Bibliography</h2>

