---
layout: default
title: "Differential equations"
parent: Lecture
date: 2024-04-19
categories: lecture
author: Lars Pastewka
nav_order: 7
---


<h2 class='chapterHead' id='differential-equations'><span class='titlemark'>Chapter 7</span><br /><a id='x1-10007'></a>Differential equations</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 7 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> Most of the phenomena we encounter in engineering are very well
described by differential equations. We remember the discrete network models
from electrical engineering and systems theory. They are described by a system of
linear ordinary differential equations with time as an independent variable.
described. We also remember the diffusion process, such as the heat transport in a
component on a heat sink that is exposed to a heat source. This phenomenon is
best described using a partial differential equation (partial differential equation).
In this chapter, we deal with an abstract classification of differential equations.
The diffusion process will be repeated in more detail in the next chapter.
</p></div>
<h3 class='sectionHead' id='ordinary-differential-equations'><span class='titlemark'>7.1 </span> <a id='x1-20007.1'></a>Ordinary differential equations</h3>
<!-- l. 18 --><p class='noindent'>We recall the classification (properties) of <span class='cmti-12'>ordinary </span>differential equations (ODEs)
and recognize the different types of differential equations. For all these differential
equations, we are always interested in a solution for a certain initial value (or
boundary value), e.g. \(x(t=0)=x_0\) etc. This initial value is always part of the definition of the
differential equation.
</p><!-- l. 20 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='linearity'><span class='titlemark'>7.1.1 </span> <a id='x1-30007.1.1'></a>Linearity</h4>
<!-- l. 22 --><p class='noindent'>A linear differential equation is, for example \begin {equation} m\ddot {x}(t)+c\dot {x}(t)+kx=f(t) \label {eq:linear} \end {equation}<a id='x1-3001r1'></a> which describes the damped and
driven harmonic oscillator, while \begin {equation} \frac {\dif ^2x}{\dif t^2}+\mu (x^2-1)\frac {\dif x}{\dif t}+x= 0 \label {eq:nonlinear} \end {equation}<a id='x1-3002r2'></a> is a non-linear equation of motion for \(x\). It
describes the so-called van der Pol oscillator. The non-linearity can be recognized
here by the fact that \(x^2\) multiplies the derivative \(\dif x/\dif t\).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 35 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The first or higher order derivative is a linear operation, since \begin {equation} \frac {\dif ^n}{\dif x^n} \lambda f(x) = \lambda \frac {\dif ^n}{\dif x^n} f(x) \end {equation}<a id='x1-3003r3'></a> for a
constant \(\lambda \) and \begin {equation} \frac {\dif ^n}{\dif x^n} \left [f(x) + g(x)\right ] = \frac {\dif ^n}{\dif x^n} f(x) + \frac {\dif ^n}{\dif x^n} g(x). \end {equation}<a id='x1-3004r4'></a> Time derivatives are displayed with a dot, \begin {equation} \dot {x}(t)=\frac {\dif }{\dif t} x(t). \end {equation}<a id='x1-3005r5'></a> For functions of a
variable, the derivative is often displayed with a dash, \begin {equation} f'(x)=\frac {\dif }{\dif x} f(x). \end {equation}<a id='x1-3006r6'></a> This is no longer possible
for functions with several variables. We will therefore always explicitly use the
differential operator here. </p></div>
<!-- l. 55 --><p class='noindent'>
</p>



<h4 class='subsectionHead' id='order'><span class='titlemark'>7.1.2 </span> <a id='x1-40007.1.2'></a>Order</h4>
<!-- l. 57 --><p class='noindent'>The order of a differential equation is given by the highest derivative that appears
in the equation. Eq. \eqref{eq:linear} and Eq. \eqref{eq:nonlinear} are examples
of second-order differential equations.
</p><!-- l. 59 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='systems'><span class='titlemark'>7.1.3 </span> <a id='x1-50007.1.3'></a>Systems</h4>
<!-- l. 61 --><p class='noindent'>A system of first-order differential equations is formed, for example, by the
equations \begin {align} \frac {\dif x}{\dif t} =&amp; x(m - n y), \label {eq:sys1} \\ \frac {\dif y}{\dif t} =&amp; - y(\gamma - \delta x), \label {eq:sys2} \end {align}
</p><!-- l. 66 --><p class='indent'> the well-known Räuber-Beute equations or Lotka-Volterra equations.
Equations \eqref{eq:sys1} and \eqref{eq:sys2} are still non-linear.
</p><!-- l. 68 --><p class='indent'> Differential equations of higher order can be rewritten into a system of 1st
order equations. In the example of the damped harmonic oscillator, \begin {equation} m\ddot {x}(t)+c\dot {x}(t)+kx=f(t), \end {equation}<a id='x1-5001r7'></a> we replace \(\dot {x} = y\)
and thus obtain two first-order equations instead of the original second-order
equation, namely \begin {align} \dot {x} =&amp; y \\ m\dot {y} =&amp; -cy-kx+f(t) \end {align}
</p><!-- l. 79 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='partial-differential-equations'><span class='titlemark'>7.2 </span> <a id='x1-60007.2'></a>Partial differential equations</h3>
<!-- l. 82 --><p class='noindent'>Partial differential equations (PDEs) are differential equations with more than one
independent variable. As an example, we imagine a time-dependent heat transport
problem in one dimension. This is represented by a diffusion equation
for the local temperature of the system. The temperature is therefore
represented as a function of two independent variables, the time \(t\) and the spatial
position \(x\), \(T(x, t)\). The time evolution of the temperature is given by \begin {equation} \frac {\partial T(x,t)}{\partial t}=\kappa \frac {\partial ^2 T(x,t)}{\partial x^2}, \label {eq:heateq} \end {equation}<a id='x1-6001r8'></a> where \(\kappa \)
denotes the heat conduction coefficient. This equation was developed by
Joseph Fourier (*1768, \(\dagger \)1830), whom we will encounter again during this
course.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 91 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> In Eq. \eqref{eq:heateq}\(\partial /\partial t\) denotes the <span class='cmti-12'>partial derivative</span>. This is the
derivative with respect to one of the arguments (here \(t\)), i.e. the variation of
the function if all other arguments are kept constant. With ODEs, in
contrast to PDEs, only derivatives with respect to one variable (usually
the time \(t\)) occur, which are then denoted by the differential operator \(\dif /\dif t\).
</p></div>



<!-- l. 95 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='first-order'><span class='titlemark'>7.2.1 </span> <a id='x1-70007.2.1'></a>First order</h4>
<!-- l. 96 --><p class='noindent'>Quasilinear PDEs of the first order, i.e. equations of the form \begin {equation} P(x,t;u)\frac {\partial u(x,t)}{\partial x}+ Q(x,t;u)\frac {\partial u(x,t)}{\partial t}= R(x,t;u), \label {eq:PDE1Oquasi} \end {equation}<a id='x1-7001r9'></a> for an (unknown)
function \(u(x,t)\) and the initial condition \(u(x,t=0)=u_0(x)\) can be systematically traced back to a system
of coupled first-order ODEs. We want to investigate this important property.
</p><div class='framedenv' id='shaded*-1'>
<!-- l. 103 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> In Eq. \eqref{eq:PDE1Oquasi} a representation with two variables \(x\) and \(t\)
was chosen for illustration. In general, we can write \begin {equation} \sum \limits _i P_i(\{x_i\};u)\frac {\partial u(\{x_i\})}{\partial x_i}= R(\{x_i\};u) \end {equation}<a id='x1-7002r10'></a> The notation used here is \(u(\{x_i\})=u(x_0, x_1, x_2, \ldots )\),
i.e. the curly brackets denote all degrees of freedom \(x_i\). </p></div>
<!-- l. 112 --><p class='indent'> Equation \eqref{eq:PDE1Oquasi} can be transformed to a system of ODEs.
This is called the method of characteristics. We can then apply the formalisms
(analytical or numerical) for solving systems of ODEs that we learned about in
the lecture “Differential Equations”.
</p><!-- l. 114 --><p class='indent'> We proceed as follows:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-7004x1'>First, we parameterize the independent
variables in Eq. \eqref{eq:PDE1Oquasi} with a parameter \(s\) according
to \(x(s)\) and \(t(s)\).
</li>
<li class='enumerate' id='x1-7006x2'>We then form the <span class='cmti-12'>total derivative </span>of \(u(x(s),t(s))\) to \(s\) \begin {equation} \frac {\dif u(x(s),t(s))}{\dif s}= \frac {\partial u(x(s),t(s))}{\partial x}\frac {\dif x(s)}{\dif s}+ \frac {\partial u(x(s),t(s))}{\partial t}\frac {\dif t(s)}{\dif s}. \label {eq:totalderiv} \end {equation}<a id='x1-7007r11'></a>
</li>
<li class='enumerate' id='x1-7009x3'>
<!-- l. 124 --><p class='noindent'>By comparing the coefficients of the total derivative \eqref{eq:totalderiv}
with the PDE \eqref{eq:PDE1Oquasi}, you can see that this DGL is solved
exactly when \begin {align} \frac {dx(s)}{ds}&amp;=P(x,t,u),\label {eq:transode1}\\\
\frac {dt(s)}{ds}&amp;=Q(x,t,u)\quad \text {und}\\ \frac {du(s)}{ds} &amp;= R(u(s)).\label {eq:transode3} \end {align}
</p><!-- l. 130 --><p class='noindent'>is fulfilled. This describes the solution along certain curves in the
\((x,t)\)-plane.</p></li></ol>
<!-- l. 132 --><p class='noindent'>We have thus converted the PDE into a set of coupled first-order ODEs,
Eq. \eqref{eq:transex1}-\eqref{eq:transex3}.



</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 134 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Example:</span></span> The transport equation \begin {equation} \frac {\partial u(x,t)}{\partial t}+c\frac {\partial u(x,t)}{\partial x}=0 \label {eq:transportexample} \end {equation}<a id='x1-7010r12'></a> with the initial condition \(u(x,t=0)=u_0(x)\) is to be solved. We
proceed according to the recipe above:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-7012x1'>We parameterize the variables \(x\) and \(t\) with the help of a new variable
\(s\), i.e. \(x(s)\) and \(t(s)\). We are now looking for an expression with which we can
determine \(x(s)\) and \(t(s)\).
</li>
<li class='enumerate' id='x1-7014x2'>We now ask how the function \(u(x(s),t(s))\) behaves. This function describes the change
in an initial value \(u(x(0),t(0))\) with the variable \(s\). The total derivative becomes
\begin {equation} \frac {\dif u(x(s),t(s))}{\dif s}=\frac {\partial u}{\partial t}\frac {\dif t(s)}{\dif s}+\frac {\partial u}{\partial x}\frac {\dif x(s)}{\dif s}. \end {equation}<a id='x1-7015r13'></a>
</li>
<li class='enumerate' id='x1-7017x3'>
<!-- l. 147 --><p class='noindent'>The total derivative is identical to the partial differential equation that we
want to solve if \begin {align} \frac {\dif x(s)}{\dif s} &amp;=c\quad \text {and} \label {eq:transex1}\\ \frac {\dif t(s)}{\dif s} &amp;=1. \end {align}
</p><!-- l. 152 --><p class='noindent'>In this case, the following applies \begin {equation} \frac {\dif u(s)}{\dif s} = 0.\label {eq:transex3} \end {equation}<a id='x1-7018r14'></a>
</p></li>
<li class='enumerate' id='x1-7020x4'>The general solutions for the three ordinary differential
equations \eqref{eq:transex1}-\eqref{eq:transex3} are given by
\begin {align} x(s) &amp;= cs + \text {const.},\\ t(s) &amp;= s + \text {const.}\quad \text {and}\\ u(s) &amp;= \text {const.} \end {align}
</li>
<li class='enumerate' id='x1-7022x5'>With the initial conditions \(t(0)=0\), \(x(0)=\xi \) and \(u(x,t=0)=f(\xi )\) you get \(t=s\), \(x=ct+\xi \) and \(u=f(\xi )=f(x-ct)\),</li></ol>
<!-- l. 164 --><p class='noindent'>The initial condition \(f(\xi )\) is transported with the speed \(c\) in the positive x-direction. The
solution for \(u\) remains constant, as the derivative of \(u\) is zero, so \(u\) retains the value
given by the initial condition. The field \(u(x,0)\) is therefore shifted at a constant speed \(c\): \(u(x,t)=u(x-ct,0)\).
</p></div>



<!-- l. 167 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='second-order'><span class='titlemark'>7.2.2 </span> <a id='x1-80007.2.2'></a>Second order</h4>
<!-- l. 171 --><p class='noindent'>Examples of second-order PDEs are the... </p>
<ul class='itemize1'>
<li class='itemize'>...wave equation: \begin {equation} \frac {\partial ^2 u}{\partial t^2}-\frac {\partial ^2 u}{\partial x^2}=0 \end {equation}<a id='x1-8001r15'></a>
</li>
<li class='itemize'>...diffusion equation (which we will look at in more detail here):
\begin {equation} \frac {\partial u}{\partial t}-\frac {\partial ^2 u}{\partial x^2}=0 \end {equation}<a id='x1-8002r16'></a>
</li>
<li class='itemize'>...Laplace equation (which we will also get to know better): \begin {equation} \frac {\partial ^2 u}{\partial x^2}+\frac {\partial ^2 u}{\partial y^2}=0 \end {equation}<a id='x1-8003r17'></a></li></ul>
<!-- l. 186 --><p class='noindent'>The second order here refers to the second derivative. These examples are formulated
for two variables, but these differential equations can also be written down for
more degrees of freedom.
</p><!-- l. 188 --><p class='indent'> For two variables, the general form of second-order linear PDEs is \begin {equation} a(x,y) \frac {\partial ^2 u}{\partial x^2}+ b(x,y)\frac {\partial ^2 u}{\partial x\partial y}+ c(x,y)\frac {\partial ^2 u}{\partial y^2}=F\left (x,y;u,\frac {\partial u}{\partial x},\frac {\partial u}{\partial y}\right ), \end {equation}<a id='x1-8004r18'></a> where \(F\)
itself must of course also be linear in the arguments if the entire equation is to be
linear. We now classify 2nd order PDEs, but note that this classification
is not exhaustive and that it only applies pointwise. The latter means
that the PDE can fall into a different classification at different points in
space.
</p><!-- l. 197 --><p class='indent'> We first assume that \(F=0\) and \(a\), \(b\), \(c\) are constant. Then we get: \begin {equation} a\frac {\partial ^2 u}{\partial x^2}+b\frac {\partial ^2 u}{\partial x\partial y}+ c\frac {\partial ^2 u}{\partial y^2}=0. \label {eq:n2ndoconst} \end {equation}<a id='x1-8005r19'></a> We rewrite this
equation as the quadratic form \begin {equation} \begin {pmatrix} \partial /\partial x \\ \partial /\partial y \end {pmatrix} \cdot \begin {pmatrix} a &amp; b/2 \\ b/2 &amp; c \end {pmatrix} \cdot \begin {pmatrix} \partial /\partial x \\ \partial /\partial y \end {pmatrix} u = \nabla \cdot \t {C} \cdot \nabla u =0 \label {eq:quadform} \end {equation}<a id='x1-8006r20'></a> We can now diagonalize the coefficient matrix \(\t {C}\).
This for to \begin {equation} \t {C} = \t {U} \cdot \begin {pmatrix} \lambda _1 &amp; 0 \\ 0 &amp; \lambda _2 \end {pmatrix}\cdot \t {U}^T, \label {eq:diagquadform} \end {equation}<a id='x1-8007r21'></a> where \(\t {U}\) is unitary due to the symmetry of \(\t {C}\), \(\t {U}^T \cdot \t {U}=\t {1}\). The geometric
interpretation of the operation \(\t {U}\) is a rotation. We now introduce transformed
coordinates \(x'\) and \(y'\) so that \begin {equation} \nabla = \t {U} \cdot \nabla ' \end {equation}<a id='x1-8008r22'></a> with \(\nabla '=(\partial /\partial x', \partial /\partial y')\). In other words, the transformation matrix is
given as \begin {equation} \t {U} = \begin {pmatrix} \partial x'/\partial x &amp; \partial y'/\partial x \\ \partial x'/\partial y &amp; \partial y'/\partial y \end {pmatrix}. \end {equation}<a id='x1-8009r23'></a> Equation \eqref{eq:n2ndoconst} becomes \begin {equation} \lambda _1 \frac {\partial ^2 u}{\partial x'^2} + \lambda _2 \frac {\partial ^2 u}{\partial y'^2} = 0. \label {eq:diag2nd} \end {equation}<a id='x1-8010r24'></a> We have diagonalized the
coefficients of the differential equation. For any twice differentiable function \(f(z)\), is \begin {equation} u(x', y') = f\left (\sqrt {\lambda _2} x' + i\sqrt {\lambda _1} y'\right ) \end {equation}<a id='x1-8011r25'></a> a
solution of Eq. \eqref{eq:diag2nd}.
</p><!-- l. 259 --><p class='indent'> The analytical expression for the eigenvalues is:
</p><!-- l. 265 --><p class='indent'> We now distinguish three cases: </p>



<ul class='itemize1'>
<li class='itemize'>The case \(\det \t {C}=\lambda _1\lambda _2=ac-b^4/4=0\) with \(b\ne 0\) and \(a\ne 0\) leads to a parabolic PDE. This PDE is called
parabolic because the quadratic form Eq. \eqref{eq:quadform} or
\eqref{eq:diagquadform} describes a parabola. (This is of course an analogy.
You have to replace the differential operators with coordinates for this to
work). Without restriction of generality, let \(\lambda _2=0\). Then we get \begin {equation} \frac {\partial ^2 u}{\partial x'^2}=0. \label {eqnparab} \end {equation}<a id='x1-8012r26'></a> This is the
canonical form of a parabolic PDE.
</li>
<li class='itemize'>The case \(\det \t {C}=\lambda _1 \lambda _2=ac-b^2/4&gt;0\) leads to an elliptic PDE. This PDE is called elliptic because the
quadratic form Eq. \eqref{eq:quadform} or \eqref{eq:diagquadform}
describes an ellipse for a constant right-hand side. (For \(\lambda _1=\lambda _2\) it is a circle). We
now convert the equation for the elliptical case to a standardized form and
introduce the scaled coordinates \(x'=\sqrt {\lambda _1} x''\) and \(y'=\sqrt {\lambda _2} y''\). Eq. \eqref{eq:diag2nd} then
becomes the canonical elliptic PDE \begin {equation} \frac {\partial ^2 u}{\partial x''^2}+\frac {\partial ^2 u}{\partial y''^2}=0. \label {eqnelliptic} \end {equation}<a id='x1-8013r27'></a> The canonical elliptic PDE is
therefore the Laplace equation, Eq. \eqref{eqnelliptic} (here in two
dimensions). Solutions of the Laplace equation are called <span class='cmti-12'>harmonic
functions</span>.
</li>
<li class='itemize'>The case \(\det \t {C}=\lambda _1\lambda _2=ac-b^2/4&lt;0\) results in the so-called hyperbolic PDE. This PDE is called
hyperbolic because the quadratic form Eq. \eqref{eq:quadform} or
\eqref{eq:diagquadform} for a constant right-hand side describes a
hyperbola. Without restricting the generality, we now require \(\lambda _1&gt;0\) and \(\lambda _2&lt;0\). Then
we can again introduce scaled coordinates \(x'=\sqrt {\lambda _1}x''\) and \(y'=\sqrt {-\lambda _2}y''\) so that \begin {equation} \frac {\partial ^2 u}{\partial x''^2} - \frac {\partial ^2 u}{\partial y''^2} = \begin {pmatrix} \partial u/\partial x'' \\ \partial u/\partial y'' \end {pmatrix} \cdot \begin {pmatrix} 1 &amp; 0 \\ 0 &amp; -1 \end {pmatrix} \cdot \begin {pmatrix} \partial u/\partial x'' \\ \partial u/\partial y'' \end {pmatrix} = 0. \label {eq:hyb} \end {equation}<a id='x1-8014r28'></a> We can now use a
further coordinate transformation, namely a rotation by \(45^\circ \), to bring the
coefficient matrix in Eq. \eqref{eq:hyb} to a form in which the diagonal
elements are \(0\) and the secondary diagonal elements are \(1\). This results in the
differential equation \begin {equation} \frac {\partial ^2 u}{\partial x''' \partial y'''}=0, \label {eqnd2udxideta0} \end {equation}<a id='x1-8015r29'></a> where \(x''''\) and \(y''''\) are the corresponding rotated coordinates.
This equation is the canonical form of a hyperbolic PDE and is
equivalent to Eq. \eqref{eq:n2ndoconst} in the new variables \(x'''\) and
\(y'''\).</li></ul>
<!-- l. 313 --><p class='indent'> For higher dimensional problems, we need to look at the eigenvalues of the
coefficient matrix \(\t {C}\). The PDE is called <span class='cmti-12'>parabolic </span>if there is an eigenvalue
that vanishes, but all other eigenvalues are either greater or less than
zero. The PDE is called <span class='cmti-12'>elliptic </span>if all eigenvalues are either greater than
zero or less than zero. The PDE is called <span class='cmti-12'>hyperbolic </span>if there is exactly



one negative eigenvalue and all others are positive or if there is exactly
one positive eigenvalue and all others are negative. It is clear that for
PDEs with more than two variables, these three classes of PDEs are not
exhaustive and there are coefficient matrices that fall outside this classification
scheme. For problems with exactly two variables, this classification leads to
the conditions for the determinants of the coefficient matrix mentioned
above.
</p><!-- l. 315 --><p class='indent'> These three types of 2nd-order linear PDEs can also be solved analytically for
some problems. In the following, we give an example of this.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 319 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Example:</span></span> We solve the one-dimensional wave equation. \begin {equation} \frac {\partial ^2 u}{\partial x^2}-\frac {1}{c^2}\frac {\partial ^2 u}{\partial t^2}=0 \label {eqn1Dwaveeqn} \end {equation}<a id='x1-8016r30'></a> by separating
the variables. To do this, we take the approach \(u(x,t)=X(x)T(t)\), which leads to \begin {equation} \frac {1}{X}\frac {\partial ^2 X}{\partial x^2}=\frac {1}{c^2}\frac {1}{T}\frac {\partial ^2 T}{\partial t^2}. \label {eqnseparate} \end {equation}<a id='x1-8017r31'></a> In
Eq. \eqref{eqnseparate}, the left-hand side depends only on the variable \(x\),
while the right-hand side depends only on \(t\). For any \(x\) and \(t\), this equation
can only be fulfilled if both sides are equal to a constant and we thus
obtain \begin {equation} \frac {1}{X}\frac {\partial ^2 X}{\partial x^2}=-k^2=\frac {1}{c^2}\frac {1}{T}\frac {\partial ^2 T}{\partial t^2}\,\mathrm {.} \end {equation}<a id='x1-8018r32'></a> This results in the following two equations \[\frac {\partial ^2 X}{\partial x^2}+k^2X=0\] with the solution \(X(x)=e^{\pm ikx}\) and \[\frac {\partial ^2 T}{\partial t^2}+\omega ^2T=0\]
with the solution \(T(t)=e^{\pm i\omega t}\), where we have set \(\omega ^2=c^2k^2\). have set. This example needs
initial conditions to be completed so that we can can find a solution.
</p></div>



<h2 class='likechapterHead' id='bibliography'><a id='x1-9000'></a>Bibliography</h2>

