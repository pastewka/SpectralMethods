---
layout: default
title: "Function spaces"
parent: Lecture
date: 2024-07-11
categories: lecture
author: Lars Pastewka
nav_order: 4
---


<h2 class='chapterHead' id='function-spaces'><span class='titlemark'>Chapter 5</span><br /><a id='x1-10005'></a>Function spaces</h2>
<div class='framedenv' id='shaded_-1'>
<!-- l. 6 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Context:</span></span> Before we dive deeper into the numerical solution of partial differential
equations, we need to introduce a mathematical concept: <span class='cmti-12'>Function spaces</span>, or more
concretely <span class='cmti-12'>Hilbert spaces</span>. Function spaces are useful because they formalize the
series expansion and provide easy access to the coefficients of a series expansion
through the concept of basis functions. </p></div>
<h3 class='sectionHead' id='vectors'><span class='titlemark'>5.1 </span> <a id='x1-20005.1'></a>Vectors</h3>
<!-- l. 12 --><p class='noindent'>As an introduction, let us recall the usual Cartesian vectors. We can represent a
vector \(\v {a}=(a_1, a_2, a_3)\) as a linear combination of basis vectors \(\hat {e}_1\), \(\hat {e}_2\) and \(\hat {e}_3\), \begin {equation} \v {a} = a_1 \hat {e}_1 + a_2 \hat {e}_2 + a_3 \hat {e}_3. \label {eq:Cartesian-decomposition} \end {equation}<a id='x1-2001r1'></a> The unit vectors \(\hat {e}_1\), \(\hat {e}_2\) and \(\hat {e}_3\)
are of course the vectors that span the Cartesian coordinate system. (In previous
chapters, we also use the notation \(\hat {x}\equiv \hat {e}_1\), \(\hat {y}\equiv \hat {e}_2\) and \(\hat {z}\equiv \hat {e}_3\).) The numbers \(a_1\), \(a_2\) and \(a_3\) are the
components or <span class='cmti-12'>coordinates </span>of the vector, but also the coefficients multiplying the
unit vectors in Eq. \eqref{eq:Cartesian-decomposition}. In this sense,
they are identical to the coefficients of the series expansion, with the
difference that the \(\hat {e}_i\)s are orthogonal, i.e. \begin {equation} \hat {e}_i\cdot \hat {e}_j = \delta _{ij} \end {equation}<a id='x1-2002r2'></a> where \(\delta _{ij}\) is the Kronecker-\(\delta \). Two
Cartesian vectors \(\v {a}\) and \(\v {b}\) are orthogonal if the scalar product between them
vanishes: \begin {equation} \v {a}\cdot \v {b} = \sum _i a_i^* b_i = 0 \label {eq:vecscalar} \end {equation}<a id='x1-2003r3'></a> Using the scalar product, we can obtain the components as
\(a_i = \v {a}\cdot \hat {e}_i\). This is a direct consequence of the orthogonality of the basis vectors
\(\hat {e}_i\).
</p><!-- l. 28 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='functions'><span class='titlemark'>5.2 </span> <a id='x1-30005.2'></a>Functions</h3>
<!-- l. 30 --><p class='noindent'>In the previous section, we claimed that the basis functions from Chapter 5 are
not orthogonal. For this we need an idea for orthogonality of functions. With a
definition of a scalar product between two <span class='cmti-12'>functions</span>, we can then define
orthogonality as the vanishing of this scalar product.
</p><!-- l. 32 --><p class='indent'> We now introduce a scalar product on functions (pr function spaces). Given
two functions \(g(x)\) and \(f(x)\) on the interval \(x\in [a,b]\), <span class='cmti-12'>define </span>the scalar product as \begin {equation} (f,g) = \int _a^b \dif x\, f^*(x) g(x), \label {eq:funcscalar} \end {equation}<a id='x1-3001r4'></a> where \(f^*(x)\) is the
complex conjugate of \(f(x)\). This scalar product or <span class='cmti-12'>inner </span>product is a map to a real
number with the properties </p>
<ul class='itemize1'>
<li class='itemize'>Positive definite: \((f,f)\ge 0\) and \((f,f)=0\Leftrightarrow f=0\)
</li>



<li class='itemize'>Sesquilinear: \((\alpha f+\beta g,h)=\alpha ^*(f,h)+\beta ^*(g,h)\) and \((f,\alpha g+\beta h)=\alpha (f,g)+\beta (f,h)\)
</li>
<li class='itemize'>Hermitian: \((f,g)=(g,f)^*\)</li></ul>
<!-- l. 48 --><p class='noindent'>The scalar products Eq. \eqref{eq:vecscalar} and \eqref{eq:funcscalar} both fulfill
these properties.
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 50 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> The scalar product between two functions can be defined more generally
with a weight function \(w(x)\), \begin {equation} (f,g) = \int _a^b \dif x\, f^*(x) g(x) w(x). \end {equation}<a id='x1-3002r5'></a> The question of orthogonality between functions can
thus only be answered with respect to a certain definition of the scalar product.
For example, <span class='cmti-12'>Chebyshev polynomials </span>are othogonal with respect to a scale
product with weight function \(w(x)=(1-x^2)^{-1/2}\). Within these notes, we will only use the case
\(w(x)=1\).
</p><!-- l. 57 --><p class='indent'> Other ways of writing the scalar product that are often found in the literature
are \(\langle f,g \rangle \) or \(\langle f|g \rangle \). The latter is particularly common in the physics literature, in particular
in quantum mechanics. </p></div>
<!-- l. 60 --><p class='noindent'>
</p>
<h3 class='sectionHead' id='basis-functions'><span class='titlemark'>5.3 </span> <a id='x1-40005.3'></a>Basis functions</h3>
<!-- l. 63 --><p class='noindent'>Let us now return to the series expansion, \begin {equation} f_N(x) = \sum _{n=1}^N a_n \varphi _n(x). \label {eq:series2} \end {equation}<a id='x1-4001r6'></a> The functions \(\varphi _n(x)\) are called <span class='cmti-12'>basis
functions</span>. A necessary property of the basis functions is their linear independence.
The functions are linearly independent if none of the basis functions themselves
can be written as a linear combination, i.e. in the form of the series expansion
Eq. \eqref{eq:series2}, of the other basis functions. This means that it must be
fulfilled that \begin {equation} \sum _{n=1}^{N}a_n \varphi _n(x) = 0 \end {equation}<a id='x1-4002r7'></a> if and only if all \(a_n=0\). Linearly independent elements form a
basis.
</p><!-- l. 76 --><p class='indent'> This basis is called complete if all relevant functions (= elements of the underlying
vector space) can be represented by the series expansion \eqref{eq:series2}.
(Proofs of the completeness of basis functions are complex and outside the focus
of these notes.) The coefficients \(a_n\) are called coordinates or coefficients. The number
of basis functions or coordinates \(N\) is called the <span class='cmti-12'>dimension </span>of the vector
space.
</p>
<div class='framedenv' id='shaded_-1'>



<!-- l. 78 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> A <span class='cmti-12'>vector space </span>is a set on which the operations of addition and scalar
multiplication are defined with the usual properties, such as the existence of
neutral and inverse elements and associative, commutative and distributive laws.
If this space is defined on functions, it is also referred to as a <span class='cmti-12'>function space</span>. If
there is also an inner product such as Eq. \eqref{eq:funcscalar}, then we speak of
a <span class='cmti-12'>Hilbert space</span>. </p></div>
<!-- l. 82 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='orthogonality'><span class='titlemark'>5.3.1 </span> <a id='x1-50005.3.1'></a>Orthogonality</h4>
<!-- l. 84 --><p class='noindent'>Particularly useful basis functions are orthogonal. Using the scalar product, we
can now define orthogonality for these functions. Two functions \(f\) and \(g\) are
orthogonal if the scalar product vanishes, \((f, g) = 0\). A set of mutually orthogonal
basis functions satisfies \begin {equation} (\varphi _n, \varphi _m) = \nu _{n} \delta _{nm}, \end {equation}<a id='x1-5001r8'></a> where \(\delta _{nm}\) is the Kronecker-\(\delta \). For \(\nu _n\equiv (\varphi _n, \varphi _n)=1\) the basis is called
<span class='cmti-12'>orthonormal</span>.
</p><!-- l. 90 --><p class='indent'> Orthogonality is useful because it shows a way to obtain the coefficients of the
series expansion \eqref{eq:series2}: \begin {equation} (\varphi _n, f_N) = \sum _{i=1}^N a_i (\varphi _n, \varphi _i) = \sum _{i=1}^N a_i \nu _i \delta _{ni} = a_n \nu _n \end {equation}<a id='x1-5002r9'></a> which yields the coefficients as \begin {equation} a_n = \frac {(\varphi _n, f_N)}{(\varphi _n, \varphi _n)}. \label {eq:coordinates} \end {equation}<a id='x1-5003r10'></a> The
coefficients are given by the projection (the scalar product) of the function onto
the basis vectors. Remember that the following also applies to Cartesian vectors: \(a_n = \v {a}\cdot \hat {e}_n\).
(The normalization factor can be omitted here because \(\hat {e}_n\cdot \hat {e}_n=1\), i.e. the Cartesian basis
vectors are orthonormal!) The coefficient given by Eq. \eqref{eq:coordinates} can
be thought of as coordinates of the function, similar to the coordinates in
Cartesian space.
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 107 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> A useful identity for an expansion into orthogonal bases is <span class='cmti-12'>Parseval’s
theorem</span>. Because scalar products between different basis functions vanish, the
square (or power) of a series expansion is given by \begin {equation} (f_N, f_N) = \sum _{n=1}^N |a_n|^2 \nu _n, \end {equation}<a id='x1-5004r11'></a> or for orthonormal basis
functions \begin {equation} (f_N, f_N) = \sum _{n=1}^N |a_n|^2. \end {equation}<a id='x1-5005r12'></a> </p></div>
<!-- l. 118 --><p class='noindent'>
</p>
<h4 class='subsectionHead' id='fourier-basis'><span class='titlemark'>5.3.2 </span> <a id='x1-60005.3.2'></a>Fourier basis</h4>
<!-- l. 121 --><p class='noindent'>An important set of basis functions is the <span class='cmti-12'>Fourier basis</span>, \begin {equation} \varphi _n(x) = \exp \left ( i q_n x \right ), \label {eq:fourier-basis} \end {equation}<a id='x1-6001r13'></a> on the interval \(x\in [0,L]\) with \(q_n = 2\pi n/L\)
and \(n\in \mathbb {Z}\). The Fourier basis is periodic on this interval and is shown in Fig. <a href='#real-part-of-the-fourier-basis-functions-eq-tht-x-thteqrefeqfourierbasis-tht-for-n-the-higher-order-basis-functions-oscillate-with-a-smaller-period-and-represent-higher-frequencies'>5.1<!-- tex4ht:ref: fig:fourier-basis --></a>. It can
easily be shown that \begin {equation} (\varphi _n, \varphi _m) = L \delta _{nm}, \end {equation}<a id='x1-6002r14'></a> so that the Fourier basis is orthogonal. The coefficients \(a_n\) of
the Fourier series, \begin {equation} f_\infty (x) = \sum _{n=-\infty }^\infty a_n \varphi _n(x), \label {eq:fourierseries} \end {equation}<a id='x1-6003r15'></a> can thus be obtained as \begin {equation} a_n=\frac {1}{L}(\varphi _n, f_\infty )=\frac {1}{L}\int _0^L \dif x\, f_\infty (x) \exp \left (-i q_n x\right ). \end {equation}<a id='x1-6004r16'></a> This is the well-known formula for the
coefficients of the Fourier series.



</p>
<figure class='figure'>







<!-- l. 145 --><p class='noindent' id='real-part-of-the-fourier-basis-functions-eq-tht-x-thteqrefeqfourierbasis-tht-for-n-the-higher-order-basis-functions-oscillate-with-a-smaller-period-and-represent-higher-frequencies'><img alt='PIC' height='229' src='Figures/fourierbasis.svg' width='390' /> <a id='x1-6005r1'></a>
</p>
<figcaption class='caption'><span class='id'>Figure 5.1: </span><span class='content'>Real part of the Fourier basis functions,
Eq. \eqref{eq:fourier-basis}, for \(n=1,2,3,4\). The higher order basis functions oscillate
with a smaller period and represent higher frequencies
</span></figcaption><!-- tex4ht:label?: x1-6005r1 -->
.



</figure>
<div class='framedenv' id='shaded_-1'>
<!-- l. 151 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> Conceptually, the Fourier basis describes different frequency components,
while the basis of the finite elements described in the next section describes
spatial localization. </p></div>
<!-- l. 155 --><p class='indent'> For real-valued function with \(f_\infty (x)\equiv f_\infty ^*(x)\), we get \begin {equation} \sum _{n=-\infty }^\infty a_n \varphi _n(x) \equiv \sum _{n=-\infty }^\infty a_n^* \varphi _{-n}(x) \end {equation}<a id='x1-6006r17'></a> because \(\varphi ^*_n(x)=\varphi _{-n}(x)\). This means \(a_n=a^*_{-n}\) is a necessary
condition to obtain a real-valued \(f(x)\). This has implications for truncating the Fourier
series to a finite number of terms \(N\). In particular, we need to truncate
symmetrically, i.e. \begin {equation} f_N(x) = \sum _{n=-(N-1)/2}^{(N-1)/2} a_n \exp \left (iq_n x\right ) \end {equation}<a id='x1-6007r18'></a> with odd \(N\).
</p>
<h4 class='subsectionHead' id='finite-elements'><span class='titlemark'>5.3.3 </span> <a id='x1-70005.3.3'></a>Finite elements</h4>
<!-- l. 173 --><p class='noindent'>Another basis set that is important for numerical analysis is the finite-element
basis. In contrast to the Fourier basis, which only becomes zero at isolated points
in the entire domain, the finite element basis is localized in space and is zero
for large areas of the domain. It thus divides the domain into spatial
sections.
</p><!-- l. 175 --><p class='indent'> In its simplest form, the basis consists of localized piece-wise linear functions,
the “tent” functions, \begin {equation} \varphi _n(x) = \left \{ \begin {array}{ll} \frac {x-x_{n-1}}{x_n - x_{n-1}} &amp; \text {for}\; x\in [x_{n-1},x_n]\\ \frac {x_{n+1-x}}{x_{n+1} - x_n} &amp; \text {for}\; x\in [x_n,x_{n+1}] \\ 0 &amp; \text {else} \end {array} \right . \label {eq:finite-element-basis} \end {equation}<a id='x1-7001r19'></a> Here, the \(x_n\) are the <span class='cmti-12'>nodes </span>(also known as grid points)
between which the tents are spanned. The functions are constructed in such a way
that the maximum value is \(1\) and \(\int _0^L \dif x\,\varphi _n(x)=(x_{n+1}-x_{n-1})/2\). This basis is the simplest form of the finite
element basis and is shown in Fig. <a href='#the-base-of-the-finite-elements-in-its-simplest-linear-incarnation-each-basis-function-is-a-marquee-that-runs-over-a-certain-interval-between-and-and-back-again-see-also-eq-tht-x-thteqrefeqfiniteelementbasis-tht'>5.2<!-- tex4ht:ref: fig:febasis --></a>. Higher order polynomials can be used for
greater accuracy.
</p>
<figure class='figure'>







<!-- l. 192 --><p class='noindent' id='the-base-of-the-finite-elements-in-its-simplest-linear-incarnation-each-basis-function-is-a-marquee-that-runs-over-a-certain-interval-between-and-and-back-again-see-also-eq-tht-x-thteqrefeqfiniteelementbasis-tht'><img alt='PIC' height='115' src='Figures/febasis.svg' width='390' /> <a id='x1-7002r2'></a>
</p>
<figcaption class='caption'><span class='id'>Figure 5.2: </span><span class='content'>The base of the finite elements in its simplest, linear incarnation.
Each basis function is a “marquee” that runs over a certain interval between
\(0\) and \(1\) and back again, see also Eq. \eqref{eq:finite-element-basis}.
</span></figcaption><!-- tex4ht:label?: x1-7002r2 -->



</figure>
<!-- l. 198 --><p class='indent'> An important note at this point is that the basis of the finite elements <span class='cmti-12'>not </span>is
orthogonal. In our one-dimensional case, the scalar product does not vanish for
the nearest neighbors. This is the case because two neighbors each have an
overlapping rising and falling edge. One obtains \begin {align} M_{nn} \equiv (\varphi _n, \varphi _n) &amp;= \frac {1}{3}(x_{n+1}-x_{n-1}) \\ M_{n,n+1} \equiv (\varphi _n, \varphi _{n+1}) &amp;= \frac {1}{6}(x_{n+1}-x_n) \\ M_{nm} \equiv (\varphi _n, \varphi _m) &amp;= 0 \quad \text {for}\;|n-m|&gt;1 \end {align}
</p><!-- l. 204 --><p class='indent'> for the scalar products.
</p><!-- l. 206 --><p class='indent'> Nevertheless, we can use these relations to determine the coefficients of a series
expansion, \begin {equation} f_N(x) = \sum _{n=0}^{N-1} a_n \varphi _n(x), \end {equation}<a id='x1-7003r20'></a> which yields \begin {equation} \begin {split} (\varphi _n, f_N(x)) &amp;= a_{n-1} (\varphi _n, \varphi _{n-1}) + a_n (\varphi _n, \varphi _n) + a_{n+1} (\varphi _n, \varphi _{n+1}) \\ &amp;= M_{n,n-1} a_{n-1} + M_{nn} a_n + M_{n,n+1} a_{n+1}. \end {split} \end {equation}<a id='x1-7004r21'></a> We can express this as \begin {equation} (\varphi _n, f_N(x)) = \left [ \t {M}\cdot \v {a} \right ]_n \end {equation}<a id='x1-7005r22'></a> where \([\v {v}]_n=v_n\) denotes the \(n\)th
component of the vector enclosed by the two square brackets \([\cdot ]_n\). The matrix \(\t {M}\) is
<span class='cmti-12'>sparse</span>. For an orthogonal basis, such as the Fourier basis of section <a href='#fourier-basis'>5.3.2<!-- tex4ht:ref: sec:fouirer-basis --></a>, this
matrix is diagonal. For a basis with identical distances \(x_{n+1}-x_n=1\) of the grid points \(x_n\), the
matrix has the following form \begin {equation} \t {M} = \begin {pmatrix} 2/3 &amp; 1/6 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots \\ 1/6 &amp; 2/3 &amp; 1/6 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots \\ 0 &amp; 1/6 &amp; 2/3 &amp; 1/6 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots \\ 0 &amp; 0 &amp; 1/6 &amp; 2/3 &amp; 1/6 &amp; 0 &amp; \cdots \\ 0 &amp; 0 &amp; 0 &amp; 1/6 &amp; 2/3 &amp; 1/6 &amp; \cdots \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1/6 &amp; 2/3 &amp; \cdots \\ \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots \end {pmatrix}. \end {equation}<a id='x1-7006r23'></a> To find the coefficients \(a_n\), we must solve a
(sparse) linear system of equations. The matrix \(\t {M}\) is also called the <span class='cmti-12'>mass
matrix</span>.
</p>
<div class='framedenv' id='shaded_-1'>
<!-- l. 234 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Note:</span></span> Basis sets that are different from zero only at individual points are
called <span class='cmti-12'>spectral </span>basis sets. In particular, the Fourier basis is a spectral
basis set for periodic functions. The <span class='cmti-12'>orthogonal polynomials </span>are important
spectral basis sets that are also used in numerical analysis. For example,
Chebyshev polynomials are good basis sets for non-periodic functions
defined on closed intervals. The finite-element basis is not a spectral basis.
</p></div>



<h2 class='likechapterHead' id='bibliography'><a id='x1-8000'></a>Bibliography</h2>

