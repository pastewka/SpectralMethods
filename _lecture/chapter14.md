---
layout: default
title: "Kapitel 14"
parent: Vorlesung
date: 2021-09-28
categories: lecture
author: Lars Pastewka
nav_order: 14
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 14</span><br /><a id='x1-100014'></a>Unstrukturierte Gitter</h2>
<div id='shaded*-1' class='framedenv'>
<!-- l. 5 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> Wir zeigen hier wir die Methode der finiten Elemente für
zweidimensionale unstrukturierte Gitter umgesetzt wird. Hierzu bauen wir
auf den Ergebnissen der vorhergehenden Kapiteln auf und führen die
Koordinatentransformation mit Hilfe der Jacobi-Matrix ein. </p></div>
<h3 class='sectionHead'><span class='titlemark'>14.1 </span> <a id='x1-200014.1'></a>Koordinatentransformation</h3>
<!-- l. 11 --><p class='noindent'>Wir betrachten nun den Fall, in dem unser Gitter nicht mehr strukturiert
ist. Wir brauchen in diesem Fall explizit die Positionen der Knoten \(\v{r}_i\) als
zusätzliche Information. Die Elemente sind dann durch drei Knotenindices
beschrieben. Beim Aufbau der entsprechenden Datenstrukturen ist natürlich zu
beachten, dass Elemente beispielsweise nicht überlappen und das gesamte
Simulationsgebiet trianguliert ist. Wir werden im folgenden den Elementindex \((n)\)
nicht explizit an alle Gleichungen schreiben, die Ausdrücke gelten aber pro
Element.
</p><!-- l. 13 --><p class='indent'> Ein Element wird nun mit drei Knotenposition \(\v{r}_0\), \(\v{r}_1\) und \(\v{r}_2\) beschrieben, wobei die
Indices hier die lokalen Knotenindices beschreiben. Die normierten Koordinaten \(\xi \)
und \(\eta \) beschreiben nun die Position in inneren dieses Elements. Insbesondere ist
Knoten \(0\) durch \((\xi , \eta )=(0,0)\), Knoten \(1\) durch \((\xi , \eta )=(1,0)\) und Knoten \(2\) durch \((\xi , \eta )=(0,1)\) in normierten Koordinaten
gegeben. Wir bilden nun die normierten Koordinaten auf reale Koordinaten durch
eine affine Abbildung ab, \begin{equation} \v{r} = \v{r}_0 + \xi (\v{r}_1-\v{r}_0) + \eta (\v{r}_1-\v{r}_0), \end{equation}
wobei das Dreieck durch die Vektoren \(\v{R}_1=\v{r}_1-\v{r}_0\) und \(\v{R}_2=\v{r}_2-\v{r}_0\) aufgespannt wird (siehe Abb. <a href='#x1-2001r1'>14.1<!-- tex4ht:ref: fig:coordinate-transformation --></a>).
</p>
<figure class='figure'>







<!-- l. 23 --><p class='noindent'><img height='240' width='312' src='Figures/coordinate_transformation.svg' alt='PIC' /> <a id='x1-2001r1'></a>
<a id='x1-2002'></a>
</p>
<figcaption class='caption'><span class='id'>Abbildung 14.1:: </span><span class='content'>Illustration eines Dreiecks mit den normierten Koordinaten
\(\xi \) und \(\eta \). Die Ecken des Dreiecks sind durch die Vektoren \(\v{r}_0\), \(\v{r}_1\) und \(\v{r}_2\) gegeben.
</span></figcaption><!-- tex4ht:label?: x1-2001r14.1 -->



</figure>
<!-- l. 29 --><p class='indent'> Für die Jacobi-Matrix brauchen wir nun Ableitungen der Form \(\partial x/\partial \xi \), wobei \((x,y)=\v{r}\) die
Position innerhalb des Elements bezeichnet: \begin{equation} \t{J} = \begin{pmatrix} \partial x/\partial \xi &amp; \partial x/\partial \eta \\ \partial y/\partial \xi &amp; \partial y/\partial \eta \end{pmatrix} = \begin{pmatrix} \v{R}_1 &amp; \v{R}_2 \end{pmatrix} \end{equation}
Das inverse der Jacobi-Matrix können wir schreiben als \begin{equation} \t{J}^{-1} = \begin{pmatrix} \v{G}_1 &amp; \v{G}_2 \end{pmatrix}^T, \end{equation}
wobei \(\v{R}_i\cdot \v{G}_j=\delta _{ij}\). Die \(\v{G}_i\) sind die reziproken Vektoren zu \(\v{R}_i\), \begin{align} \v{G}_1 &amp;= \frac{1}{R_{11}R_{22}-R_{12}^2} \\ \v{G}_2 &amp;= \frac{1}{R_{11}R_{22}-R_{12}^2} \end{align}
</p><!-- l. 55 --><p class='indent'> Mit Hilfe der Jacobi-Matrix können wir nun Gradienten, \begin{equation} \nabla \cdot \t{J} = \hat{\nabla }, \end{equation}
mit Hilfe des normierten Gradientens, \(\hat{\nabla }=(\partial /\partial \xi , \partial /\partial \eta )\), ausdrücken. Die Skalarprodukte werden
zu \begin{equation} \begin{split} (f,g) &amp;= \int \dif x\dif y\, f^*(x,y)g(x,y) \\ &amp;= |\det \t{J}| \int \dif \xi \dif \eta \, f^*(\xi ,\eta )g(\xi ,\eta ) \end{split} \label{eq:coordinate-transform-scalar-product} \end{equation}
Man beachte, dass die letzte Identität in Gl. \eqref{eq:coordinate-transform-scalar-product}
nur gilt, wenn \(\t{J}\) konstant ist. Dies ist aber für die Transformation hier der Fall.
Weiterhin ist die Jacobi-Determinate (engl. “Jacobian”) das doppelte der Fläche \(A\)
des entsprechenden Dreiecks, \(\det \t{J}=2A\).
</p>
<h3 class='sectionHead'><span class='titlemark'>14.2 </span> <a id='x1-300014.2'></a>Elementmatrix</h3>
<!-- l. 74 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>14.2.1 </span> <a id='x1-400014.2.1'></a>Laplace-Operator</h4>
<!-- l. 76 --><p class='noindent'>Wir betrachten nun die Elementmatrix für den Laplace-Operator, \begin{equation} \begin{split} K_{IJ} &amp;= (\nabla N_I, \nabla N_J), \\ &amp;= \det \t{J} \int \dif \xi \dif \eta \, \hat{\nabla }N_I \cdot \t{J}^{-1} \cdot \left [\t{J}^{-1}\right ]^T \cdot \hat{\nabla } N_J, \end{split} \end{equation}
wobei \begin{equation} \t{J}^{-1} \cdot \left [\t{J}^{-1}\right ]^T = \begin{pmatrix} \v{G}_1\cdot \v{G}_1 &amp; \v{G}_1\cdot \v{G}_2 \\ \v{G}_1\cdot \v{G}_2 &amp; \v{G}_2\cdot \v{G}_2 \end{pmatrix} \end{equation}
Skalarprodukte der reziproken Vektoren einhält. Für orthogonale \(\v{R}_i\) sind auch die
reziproken Vektoren orthogonal und \(\t{J}^{-1} \cdot \left [\t{J}^{-1}\right ]^T\) wird eine Diagonalmatrix.
</p><!-- l. 98 --><p class='indent'> und der Gradient im Sinne der normierten Koordinaten ausgeführt wird. Man
erhält für den Laplace-Operator \begin{equation} \hat{\t{K}} = \begin{pmatrix} 1 &amp; -1/2 &amp; -1/2 \\ -1/2 &amp; 1/2 &amp; 0 \\ -1/2 &amp; 0 &amp; 1/2 \end{pmatrix} \label{eq:elmat2d} \end{equation}



</p>
<h2 class='likechapterHead'><a id='x1-500014.2.1'></a>Literaturverzeichnis</h2>

