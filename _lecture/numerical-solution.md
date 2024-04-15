---
layout: default
title: "Numerical solution"
parent: Lecture
date: 2024-04-15
categories: lecture
author: Lars Pastewka
nav_order: 3
---


<h2 class='chapterHead' id='numerical-solution'><span class='titlemark'>Chapter 4</span><br /><a id='x1-10004'></a>Numerical solution</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 6 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> We will now put the transportation problem aside for a while and
devote ourselves to the <span class='cmti-12'>numerical </span>solution of differential equations. This chapter
shows the basics of the numerical analysis of differential equations and
introduces a few important concepts, in particular the series expansion and
the residual. The presentation here follows chapter 1 from <a href='#Xboyd_chebyshev_2000'>Boyd</a> (<a href='#Xboyd_chebyshev_2000'>2000</a>).
</p></div>
<h3 class='sectionHead' id='series-expansion'><span class='titlemark'>4.1 </span> <a id='x1-20004.1'></a>Series expansion</h3>
<!-- l. 12 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=2c5c9440-a3de-442a-9d84-ac840105f558'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=2c5c9440-a3de-442a-9d84-ac840105f558</span></a>
</p><!-- l. 14 --><p class='indent'> In abstract notation, we are looking for unknown functions \(u(x,y,z,...)\) that solve a set
of differential equations \begin {equation} \mathcal {L} u(x,y,z,\ldots ) = f(x,y,z,\ldots ) \label {eq:gendgl} \end {equation}<a id='x1-2001r1'></a> must be fulfilled. Here, \(\mathcal {L}\) is a (not necessarily
linear) operator that contains the differential (or integral) operations.
We now introduce an important concept for the (numerical) solution
of the differential equation: We approximate the function \(u\) by a <span class='cmti-12'>series
expansion</span>. We write \begin {equation} u_N(x, y, z, \ldots ) = \sum _{n=0}^N a_n \varphi _n(x,y,z,\ldots ) \label {eq:seriesexpansion} \end {equation}<a id='x1-2002r2'></a> where the \(\varphi _n\) are called “base functions”. We will
discuss the properties of these basis functions in more detail in the next
chapter.
</p><!-- l. 29 --><p class='indent'> We can now write the differential equation as, \begin {equation} \mathcal {L} u_N(x,y,z,\ldots ) = f(x,y,z,\ldots ). \end {equation}<a id='x1-2003r3'></a> This representation means that
we have now replaced the question of the unknown function \(u\) with the
question of the unknown coefficients \(a_n\). We only have to let the differential
operator \(\mathcal {L}\) act on the (known) basis functions \(\varphi _n\) and we can calculate this
analytically.
</p><!-- l. 36 --><p class='indent'> What remains is to determine the coefficients \(a_n\). These coefficients
are numbers, and these numbers can be calculated by a computer.
Equation \eqref{eq:seriesexpansion} is of course an approximation. For certain
basis functions, it can be shown that these are “complete” and can therefore
represent certain classes of functions exactly. However, this is only true under the
condition that the series Eq. \eqref{eq:seriesexpansion} is extended to \(N\to \infty \). For
all practical applications (such as implementations in computer code),
however, this series expansion must be aborted. A “good” series expansion
approximates the exact solution already at low \(N\) with a small error. With this
statement, we would of course have to specify how we want to quantify errors.
Numerically, we then search for the exact coefficients \(a_n\) that minimize the
error.
</p><!-- l. 39 --><p class='indent'> The choice of a good basis function is non-trivial. We will mainly use “finite
elements” as basis functions here and briefly touch on other types. Before we go
deeper into this topic, we need some more concepts to understand numerical
analysis.



</p><!-- l. 41 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='residual'><span class='titlemark'>4.2 </span> <a id='x1-30004.2'></a>Residual</h3>
<!-- l. 43 --><p class='noindent'>An important concept is that of <span class='cmti-12'>residuum</span>. Our goal is to solve Eq. \eqref{eq:gendgl}.
The exact solution would be \(\mathcal {L} u - f\equiv 0\). However, since we can only construct an
approximate solution, this condition will not be fulfilled exactly. We define the
residual as exactly this deviation from the exact solution, namely \begin {equation} R(x,y,z,\ldots ; a_0, a_1, \ldots , a_N) = \mathcal {L} u_N(x,y,z,\ldots ) - f(x,y,z,\ldots ). \label {eq:residual} \end {equation}<a id='x1-3001r4'></a> The residual is
therefore a kind of measure for the error we make. The strategy for numerically
solving the differential equation Eq. \eqref{eq:gendgl} is now to determine the
coefficients \(a_n\) in such a way that the residual Eq. \eqref{eq:residual} is
minimal. We have thus mapped the solution of the differential equation to an
optimization problem. The different numerical methods, which we will discuss in
the next chapters, are mainly determined by the specific optimization
strategy.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 52 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> Numerical methods for <span class='cmti-12'>optimization </span>are a central core of the numerical
solution of differential equations and thus of simulation techniques. There are
countless optimization methods that work better or worse in different
situations. We will first treat such optimizers as “black boxes”. At the end of
the course, we will return to the question of optimization and discuss
some well-known optimization methods. The term <span class='cmti-12'>minimization method </span>is
often used synonymously with optimization methods. A good overview of
optimization methods can be found in the book by <a href='#Xnocedal_numerical_2006'>Nocedal and Wright</a> (<a href='#Xnocedal_numerical_2006'>2006</a>).
</p></div>
<!-- l. 56 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='a-first-example'><span class='titlemark'>4.3 </span> <a id='x1-40004.3'></a>A first example</h3>
<!-- l. 59 --><p class='noindent'>We now want to concretize these abstract ideas using an example and introduce a
few important terms. Let’s look at the one-dimensional boundary value problem, \begin {equation} \frac {\dif ^2 u}{\dif x^2} - (x^6 + 3x^2)u = 0, \label {eq:odeexample} \end {equation}<a id='x1-4001r5'></a>
with the boundary conditions \(u(-1)=u(1)=1\). (I.e. \(x\in [-1,1]\) is the domain on which we are looking for
the solution.) In this case, the abstract differential operator \(\mathcal {L}\) takes the
concrete form \begin {equation} \mathcal {L} = \frac {\dif ^2 }{\dif x^2} - (x^6 + 3x^2) \end {equation}<a id='x1-4002r6'></a> is given. The exact solution to this problem is given by
\begin {equation} u(x) = \exp \left [(x^4-1)/4\right ]. \end {equation}<a id='x1-4003r7'></a>
</p><!-- l. 74 --><p class='indent'> We now guess an approximate solution as a series expansion for this equation.



This approximate solution should already fulfill the boundary conditions. The
equation \begin {equation} u_2(x) = 1 + (1-x^2)(a_0 + a_1 x + a_2 x^2) \label {eq:approxexample} \end {equation}<a id='x1-4004r8'></a> is constructed in such a way that the boundary conditions are fulfilled.
We can express these as \begin {equation} u_2(x) = 1 + a_0 (1-x^2) + a_1 x (1-x^2) + a_2 x^2 (1-x^2) \end {equation}<a id='x1-4005r9'></a> to exponentiate the basis functions \(\varphi _i(x)\). Here \(\varphi _0(x)=1-x^2\), \(\varphi _1(x)= x (1-x^2)\) and \(\varphi _2(x) = x^2 (1-x^2)\). Since
these basis functions are non-zero on the entire domain \([-1,1]\), this basis is called a
<span class='cmti-12'>spectral </span>basis. (Mathematically: The carrier of the function corresponds to the
domain.)
</p><!-- l. 85 --><p class='indent'> In the next step, we must find the residual \begin {equation} R(x; a_0, a_1, a_2) = \frac {\dif ^2 u_2}{\dif x^2} - (x^6 + 3x^2)u_2 \end {equation}<a id='x1-4006r10'></a> minimize. For this we choose a
strategy called <span class='cmti-12'>collocation</span>: We require that the residual vanishes exactly at three
selected points: \begin {equation} R(x_i; a_0, a_1, a_2)=0 \quad \text {for}\quad x_0=-1/2, x_1=0\;\text {und}\;x_2=1/2. \end {equation}<a id='x1-4007r11'></a>
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 96 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The disappearance of the residual at \(x_i\) does not mean that \(u_2(x_i)\equiv u(x_i)\), i.e. that at \(x_i\)
our approximate solution corresponds to the exact solution. We are still
restricted to a limited set of functions, namely the functions covered by
Eq. \eqref{eq:approxexample}. </p></div>
<!-- l. 100 --><p class='indent'> From the collocation condition we now get a linear system of equations with
three unknowns: \begin {align} R(x_0; a_0, a_1, a_2) \equiv &amp; -\frac {659}{256} a_0 + \frac {1683}{512} a_1 - \frac {1171}{1024} a_2 - \frac {49}{64} = 0 \\ R(x_1; a_0, a_1, a_2) \equiv &amp; -2(a_0-a_2) = 0 \\ R(x_2; a_0, a_1, a_2) \equiv &amp; -\frac {659}{256} a_0 - \frac {1683}{512} a_1 - \frac {1171}{1024} a_2 - \frac {49}{64} = 0 \\ \end {align}
</p><!-- l. 106 --><p class='indent'> The solution of these equations results in \begin {equation} a_0 = -\frac {784}{3807}, \quad a_1 = 0 \quad \text {and} \quad a_2 = a_0. \end {equation}<a id='x1-4008r12'></a> Figure <a href='#-analytical-solution-ux-and-numerical-approximate-solution-ux-of-the-gdgl-tht-x-thteqrefeqodeexample-tht-'>4.1<!-- tex4ht:ref: fig:first_example --></a> shows the “numerical”
solution \(u_2(x)\) in comparison with the exact solution \(u(x)\).
</p>
<figure class='figure'>







<!-- l. 116 --><p class='noindent' id='-analytical-solution-ux-and-numerical-approximate-solution-ux-of-the-gdgl-tht-x-thteqrefeqodeexample-tht-'> <img alt='PIC' height='250' src='Figures/numerical_example-.png' width='585' /> <a id='x1-4009r1'></a>
</p>
<figcaption class='caption'><span class='id'>Figure 4.1: </span><span class='content'>Analytical solution \(u(x)\) and “numerical” approximate solution \(u_2(x)\) of
the GDGL \eqref{eq:odeexample}.
</span></figcaption><!-- tex4ht:label?: x1-4009r1 -->



</figure>
<!-- l. 122 --><p class='indent'> In the numerical example shown here, both the basis functions and the
strategy for minimizing the residual can be varied. In the course of this lecture, we
will establish the finite elements as basis functions and use the Galerkin method
as minimization strategy. To do this, we must first discuss properties of possible
basis functions.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 124 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The example shown here is a simple case of <span class='cmti-12'>discretization</span>. We have gone
from a continuous function to the discrete coefficients \(a_0\), \(a_1\), \(a_2\). </p></div>



<h2 class='likechapterHead' id='bibliography'><a id='x1-5000'></a>Bibliography</h2>
<div class='thebibliography'>
<p class='bibitem'><span class='biblabel'>
<a id='Xboyd_chebyshev_2000'></a><span class='bibsp'>   </span></span>J. P. Boyd. <span class='cmti-12'>Chebyshev and Fourier Spectral Methods</span>. Dover Publications,
New York, 2000.
</p>
<p class='bibitem'><span class='biblabel'>
<a id='Xnocedal_numerical_2006'></a><span class='bibsp'>   </span></span>J. Nocedal and S. J. Wright. <span class='cmti-12'>Numerical Optimization</span>. Springer, New
York, 2nd ed edition, 2006.
</p>
</div>

