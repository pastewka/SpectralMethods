---
layout: default
title: "Kapitel 15"
parent: Vorlesung
date: 2021-09-28
categories: lecture
author: Lars Pastewka
nav_order: 15
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 15</span><br /><a id='x1-100015'></a>Festkörpermechanik</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 3 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> Die Methode der finiten Elementen hat ihren Ursprung in der
Festkörpermechanik (auch <span class='cmti-12'>Strukturmechanik</span>). So gut wie alle Simulationen in
diesem Bereich werden weiterhin mit Hilfe diese Methode durchgeführt. In
diesem Kapitel werden wir die Grundgleichungen des elastostatischen
Gleichgewichts diskretisieren, die eine Form haben die dem in den vorherigen
Kapiteln diskutierten Transportproblem ähnlich sind. </p></div>
<h3 class='sectionHead'><span class='titlemark'>15.1 </span> <a id='x1-200015.1'></a>Elastostatisches Gleichgewicht</h3>
<!-- l. 9 --><p class='noindent'>Die Grundgleichung der Festkörpermechanik beschreibt das elastostatische
Gleichgewicht. Gegeben ein Tensorfeld \(\t{\sigma }(\v{r})\), dass die <span class='cmti-12'>mechanische Spannung </span>im
System beschreibt, lauten diese \begin{equation} \nabla \cdot \t{\sigma } = 0 \label{eq:elastostaticeq} \end{equation}
Wir berechnen nun die Divergenz eines <span class='cmti-12'>Tensors zweiter Ordnung </span>(bzw. einen
Tensor<span class='cmti-12'>feldes </span>zweiter Ordnung) und müssen kurz klarstellen, was wir mit der
Operation \(\nabla \cdot =\text{div}\) meinen. In Komponentenschreibweise wird Gl. \eqref{eq:elastostaticeq}
zu \begin{equation} \partial _i \sigma _{ij} = 0, \end{equation}
wobei \(\partial _i\equiv \partial /\partial r_i\) die Ableitung respektive der Komponente der Position \(r_i\) ist und
wir hier die <span class='cmti-12'>Einsteinsche Summenkonvention </span>eingeführt haben. Diese
Gleichgewichtsbedingung hat ihren Ursprung in der Erhaltung des Impulses; \(\t{\sigma }\)
beschreibt drei unabhängige Impulsströme und Gl. \eqref{eq:elastostaticeq} ist
die stationäre Kontinuitätsgleichung, \(\nabla \cdot \v{j}=0\), für diese drei Impulsströme die durch
die Spaltenvektoren des Tensors \(\t{\sigma }\) gegeben sind.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 20 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In der Einsteinschen Summenkonvention lässt man
Summationssymbole weg und impliziert Summation über wiederholte Indices. Im
obigen Beispiel, \begin{equation} \partial _i \sigma _{ij} \equiv \sum _i \partial _i \sigma _{ij}. \end{equation}
Ein Skalarprodukt zwischen den Vektoren \(\v{a}\) und \(\v{b}\) wird in dieser Konvention
geschrieben als \begin{equation} \v{a}\cdot \v{b} = a_i b_i. \end{equation}
Diese Indexschreibweise ist nützlich, weil sie eindeutig ist. In der dyadischen
Notation müssen wir meistens dazu sagen, was wir mit einer Operation
meinen. So ist z.B. bei der Divergenz eines Tensors nicht klar, ob die
Divergenz auf den ersten oder den zweiten Index wirken soll. (Wir nutzen
hier eine Konvention, in der die Divergenz auf den ersten Index wirkt.) </p></div>



<!-- l. 32 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>15.2 </span> <a id='x1-300015.2'></a>Hooksche Gesetz</h3>
<!-- l. 34 --><p class='noindent'>Neben dem physikalischen Grundprinzip, dass die Erhaltung des Impulsstromes
und damit das elastostatische Gleichgewicht beschreibt, brauchen wir noch ein
Konstitutivgesetz, dass uns sagt wie der Spannungstensor (also der Impulsstrom)
auszusehen hat. Hierzu führen wir zunächst die Verschiebungen \(\v{u}(\v{r})\) ein, die die
Verformung eines Raumpunktes auf Grund der mechanischen Belastung
beschrieben. Aus diesen Verschieben berechnen wir den Dehnungstensor
\begin{equation} \t{\varepsilon } = \frac{1}{2}\left [ \nabla \v{u} + \left (\nabla \v{u}\right )^T \right ], \label{eq:strain} \end{equation}
bzw. in Komponentenschreibweise \begin{equation} \varepsilon _{ij} = \frac{1}{2} \left ( \partial _i u_j + \partial _j u_i \right ). \end{equation}
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 44 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Der Ausdruck \(\nabla \v{u}\) ist <span class='cmti-12'>nicht </span>die Divergenz von \(\v{u}\). Diese ist gegeben
durch \(\nabla \cdot \v{u}\) – der Punkt ist entscheidend. \(\nabla \v{u}\) ist der Gradient des Vektorfeldes \(\v{u}(\v{r})\) und damit
ein Tensorfeld zweiter Ordnung. Die Komponenten sind gegeben durch
\begin{equation} \left [\nabla \v{u}\right ]_{ij} = \partial _i u_j. \end{equation}
Die Komponenten des transponierten Tensors sind daher \begin{equation} \left [\nabla \v{u}\right ]^T_{ij} = \left [\nabla \v{u}\right ]_{ji} = \partial _j u_i. \end{equation}
</p></div>
<!-- l. 55 --><p class='indent'> Das Hooksche Gesetz beschreibt nun welche Dehnung zu welcher Spannung
führt. Für isotrope Festkörper lautet es \begin{equation} \t{\sigma } = \left (\lambda \, \text{tr}\,\t{\varepsilon }'\right ) \t{1} + 2\mu \t{\varepsilon }' \quad \text{bzw.}\quad \sigma _{ij} = \lambda \delta _{ij} \varepsilon '_{kk} + 2\mu \varepsilon '_{ij}. \label{eq:Hookes-law} \end{equation}
mit \(\varepsilon _{ij}'=\varepsilon _{ij}-\varepsilon _{0,ij}\). Hierbei heißen \(\lambda \) und \(\mu \) <span class='cmti-12'>Lamé-Konstanten</span>. Die Konstante \(\mu \) wird auch das
Schermodul genannt. Der Ausdruck \(\varepsilon _{kk}'\equiv \sum _k\varepsilon _{kk}'=\text{tr}\,\t{\varepsilon }'\) (Einstein-Konvention!) ist die Spur des
Dehnungstensors. Wir haben hier den Dehnungstensor \(\t{\varepsilon }'=\t{\varepsilon }-\t{\varepsilon }_0\) eingeführt, der eine
Eigendehnung \(\v{\varepsilon }_0\) (engl. “eigenstrain”) berücksichtig, die z.B. durch eine thermische
Expansion gegeben sein kann.
</p><!-- l. 79 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>15.3 </span> <a id='x1-400015.3'></a>Schwache Form</h3>
<!-- l. 81 --><p class='noindent'>Wir haben ein gekoppeltes lineares Gleichungssystem zweiter Ordnung, welches
wir nun mit Hilfe der Methode der finiten Elemente diskretisieren werden. Wir
formulieren zunächst die schwache Form von Gl. \eqref{eq:elastostaticeq},



\begin{equation} \int \dif ^3 r\, \v{v}(\v{r})\cdot \left ( \nabla \cdot \t{\sigma } \right ) = 0 \quad \text{bzw.}\quad \int \dif ^3 r\, v_j(\v{r}) \partial _i\sigma _{ij} = 0, \end{equation}
wobei \(\v{v}(\v{r})\) nun ein Testvektor ist. Wir nutzen nun wieder eine Variante der
Produktregel, \begin{equation} \partial _i\left ( \sigma _{ij} v_j \right ) = \left (\partial _i \sigma _{ij}\right ) v_j + \sigma _{ij} \left (\partial _i v_j\right ), \end{equation}
um die Ableitung auf die Testfunktion zu überführen. Man erhält
\begin{equation} \int \dif ^3 r\, \left [\nabla \cdot \left (\t{\sigma }\cdot \v{v}\right ) - \left (\nabla \v{v}\right ):\t{\sigma } \right ] = 0, \label{eq:weakmech1} \end{equation}
wobei der Doppelpunkt ein doppeltes Skalarprodukt (oder <span class='cmti-12'>Kontraktion</span>) bezeichnet, \(\t{A}:\t{B}=A_{ij}B_{ij}\).
Wir können nun wieder den ersten Term in Gl. \eqref{eq:weakmech1} mit Hilfe
des Gaussschen Satzes in ein Oberflächenintegral, \begin{equation} \int \dif ^2 r\, \v{v}\cdot \left (\t{\sigma }\cdot \hat{n}\right ) - \int \dif ^3 r\, \left (\nabla \v{v}\right ):\t{\sigma } = 0, \label{eq:weakmech2} \end{equation}
überführen, wobei die Tatsache genutzt wurde, dass \(\t{\sigma }\) symmetrisch ist. Dies ist
die schwache Form des mechanischen Gleichgewichts. Der Ausdruck \(\t{\sigma }\cdot \hat{n}\) sind die die
Flächenlasten (engl. “tractions”) auf die Oberfläche.
</p><!-- l. 105 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>15.4 </span> <a id='x1-500015.4'></a>Diskretisierung</h3>
<!-- l. 107 --><p class='noindent'>Wir diskretisieren diese Gleichung nun mit Hilfe der Galerkin-Methode und setzen
gleich lineare finite Elemente als Basisfunktionen an. Dies erlaubt es uns,
die Diskretisierung direkt mit Hilfe der Formfunktionen und nicht der
Basisfunktionen zu schreiben. Wir setzen also innerhalb Element \((n)\) an, dass
\begin{equation} u_j(\v{r}) = a_{j,Jn} N_J^{(n)}(\v{r}), \end{equation}
wobei \(Jn\) für den globalen Knotenindex steht, der dem lokalen Index des Knotens \(J\)
auf Element \((n)\) entspricht und Summation über \(J\) auf Grund des wiederholten
Indices impliziert ist.
</p><!-- l. 113 --><p class='indent'> Unsere Testfunktion \(\v{v}(\v{r})\) ist nun vektorwertig. Wir benötigen damit
einen Satz von \(DN\) Testvektoren, wobei \(D\) die Dimension des Raumes und \(N\) die
Anzahl der Elemente bezeichnet. Wir setzen daher innerhalb des Elements \((n)\)
\begin{equation} \v{v}_{i,I}(\v{r}) = N_I^{(n)}(\v{r}) \hat{e}_i \end{equation}
mit \(i\in [1,\ldots ,D]\) als Testvektor an. Hier bezeichnet \(\hat{e}_i\) den Vektor, bei dem die \(i\)-te Komponente \(1\)
und alle anderen Komponenten \(0\) sind, also den kanonischen Einheitsvektor in
Richtung \(i\).
</p><!-- l. 119 --><p class='indent'> Mit diesen Ansatzfunktionen erhält man für die Dehnung auf Element \((n)\)
\begin{equation} \varepsilon ^{(n)}_{ij} = \frac{1}{2} \left (a_{i,Jn} \partial _j N_J^{(n)} + a_{j,Jn} \partial _i N_J^{(n)}\right ). \end{equation}
Das Hooksche Gesetz wird damit zu \begin{equation} \sigma ^{(n)}_{ij}(\v{r}) = \lambda (\v{r}) \delta _{ij} a_{k,Jn} \partial _k N_J^{(n)} + \mu (\v{r}) \left (a_{i,Jn} \partial _j N_J^{(n)} + a_{j,Jn} \partial _i N_J^{(n)}\right ) - \sigma _{0,ij}(\v{r}) \end{equation}
mit \begin{equation} \sigma _{0,ij}(\v{r}) = \lambda (\v{r}) \delta _{ij} \varepsilon _{0,kk}(\v{r}) + 2\mu (\v{r}) \varepsilon _{0,ij}(\v{r}). \end{equation}
Die diskretisierte Form des Volumenterms der Gleichgewichtsbedingung lautet
\begin{equation} \begin{split} \int \dif ^3 r\, \left (\nabla \v{v}\right ):\t{\sigma } =&amp; \int \dif ^3 r\, \left (\nabla N_I^{(n)}\otimes \hat{e}_i\right ):\t{\sigma } \\ =&amp; \int \dif ^3 r\, \left (\partial _j N_I^{(n)}\right )\sigma _{ji} \\ =&amp; \int \dif ^3 r\, \left \{ \lambda (\v{r}) a_{k,Jn} \partial _i N_I^{(n)} \partial _k N_J^{(n)}\right . \\ &amp; + \mu (\v{r}) \left (a_{i,Jn} \partial _j N_I^{(n)}\partial _j N_J^{(n)} + a_{j,Jn} \partial _j N_I^{(n)}\partial _i N_J^{(n)}\right ) \\ &amp;\left . - \sigma _{0,ji}(\v{r}) \partial _j N_I^{(n)} \right \}.\\ \end{split} \label{eq:voleq} \end{equation}
Für lineare Element sind bis auf die Materialkonstanten alle Terme in
dieser Gleichung konstant. Das Integral führt damit effektiv zu einer
Mittelung der Materialkonstanten auf den Element. Wir führen die mittleren



Materialkonstanten \begin{equation} \lambda ^{(n)} = \frac{1}{V^{(n)}} \int \dif ^3 r\, \lambda (\v{r}) \end{equation}
und eine äquivalent Gleichung für \(\mu \) und \(\t{\sigma }_0\) ein. Hierbei ist nun \(V^{(n)}\) das Volumen des
Elements \((n)\). Wir können Gl. \eqref{eq:voleq} schreiben als \begin{equation} \begin{split} \int \dif ^3 r\, \left (\nabla \v{v}\right ):\t{\sigma } =&amp; \lambda ^{(n)} a_{j,Jn}V^{(n)}\partial _i N_I^{(n)} \partial _j N_J^{(n)} + \mu ^{(n)} a_{j,Jn} \delta _{ij} V^{(n)}\partial _k N_I^{(n)}\partial _k N_J^{(n)} \\ &amp; + \mu ^{(n)} a_{j,Jn} V^{(n)}\partial _j N_I^{(n)}\partial _i N_J^{(n)} - V^{(n)}\sigma _{0,ij}^{(n)} \partial _j N_I^{(n)}. \end{split} \end{equation}
Die Elementmatrix hat daher die Komponenten \begin{equation} K^{(n)}_{IiJj} = \lambda ^{(n)} k_{IiJj}^{(n)} + \mu ^{(n)} \delta _{ij} k_{IkJk}^{(n)} + \mu ^{(n)} k_{IjJi}^{(n)} \end{equation}
mit \(k_{IiJj}^{(n)}=V^{(n)}\partial _i N_I^{(n)} \partial _j N_J^{(n)}\) und der Beitrag des Elements zum Lastvektor lautet \(f_{Ii}^{(n)}=V^{(n)}\sigma _{0,ij}^{(n)} \partial _j N_I^{(n)}\).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 203 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Für unser strukturiertes zweidimensionales Gitter erhalten wir \(V^{(n)}=\Delta x\Delta y/2\)
und \begin{equation} \t{k} = \frac{1}{2} \begin{pmatrix} \Delta y/\Delta x &amp; 1 &amp; -\Delta y/\Delta x &amp; \cdot &amp; \cdot &amp; -1 \\ 1 &amp; \Delta x/\Delta y &amp; -1 &amp; \cdot &amp; \cdot &amp; -\Delta x/\Delta y \\ -\Delta y/\Delta x &amp; -1 &amp; \Delta y/\Delta x &amp; \cdot &amp; \cdot &amp; 1 \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ -1 &amp; -\Delta x/\Delta y &amp; 1 &amp; \cdot &amp; \cdot &amp; \Delta x/\Delta y \end{pmatrix} \end{equation}
sowohl für das untere linke als auch das obere rechte Dreieck. Der Lastvektor
wird zu \begin{equation} \v{f} = \frac{1}{2}\begin{pmatrix} -\sigma _{0,xx}\Delta y -\sigma _{0,xy}\Delta x \\ -\sigma _{0,xy}\Delta y -\sigma _{0,yy}\Delta x \\ \sigma _{0,xx}\Delta y \\ \sigma _{0,xy}\Delta y \\ \sigma _{0,xy}\Delta x \\ \sigma _{0,yy}\Delta x \end{pmatrix} \end{equation}
für das untere linke Dreieck. Der Lastvektor für das obere rechte Dreieck ist \(-\v{f}\).
Für \(\Delta x=\Delta y\) wird die Elementsteifigkeitsmatrix zu \begin{equation} \t{k} = \frac{1}{2} \begin{pmatrix} 1 &amp; 1 &amp; -1 &amp; \cdot &amp; \cdot &amp; -1 \\ 1 &amp; 1 &amp; -1 &amp; \cdot &amp; \cdot &amp; -1 \\ -1 &amp; -1 &amp; 1 &amp; \cdot &amp; \cdot &amp; 1 \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ -1 &amp; -1 &amp; 1 &amp; \cdot &amp; \cdot &amp; 1 \end{pmatrix}. \end{equation}
Wenn wir hier die Spur von Untermatrizen der Größe \(2\times 2\) berechnen, erhalten wir
die Matrix des Laplace-Operators, Gl. \eqref{eq:elmat2d}.
</p><!-- l. 240 --><p class='indent'> Die Dehnung auf Element \((n)\) wird zu \begin{align} \varepsilon ^{(n)}_{xx} &amp;= a_{x,Jn} \partial _x N_J^{(n)} = -a_{x,0n}/\Delta x + a_{x,1n}/\Delta x \\ \varepsilon ^{(n)}_{yy} &amp;= a_{y,Jn} \partial _y N_J^{(n)} = -a_{y,0n}/\Delta _y + a_{y,2n}/\Delta y \\ \varepsilon ^{(n)}_{xy} &amp;= \frac{1}{2} \left (a_{x,Jn} \partial _y N_J^{(n)} + a_{y,Jn} \partial _x N_J^{(n)}\right ) \nonumber \\ &amp;= \frac{1}{2}\left (-a_{x,0n}/\Delta y + a_{x,2n}/\Delta y - a_{y,0n}/\Delta x + a_{y,1n}/\Delta x\right )t \end{align}
</p>
</div>



<h2 class='likechapterHead'><a id='x1-600015.4'></a>Literaturverzeichnis</h2>

