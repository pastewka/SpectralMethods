---
layout: default
title: "Kapitel 12 [Jan. 17-Feb. 11]"
parent: Vorlesung
date: 2022-03-10
categories: lecture
author: Lars Pastewka
nav_order: 12
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 12</span><br /><a id='x1-100012'></a>Festkörpermechanik</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 3 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> Die Methode der finiten Elementen hat ihren Ursprung in der
Festkörpermechanik (auch <span class='cmti-12'>Strukturmechanik</span>). So gut wie alle Simulationen in
diesem Bereich werden weiterhin mit Hilfe diese Methode durchgeführt. In
diesem Kapitel werden wir die Grundgleichungen des elastostatischen
Gleichgewichts diskretisieren, die eine Form haben die dem in den vorherigen
Kapiteln diskutierten Transportproblem ähnlich sind. </p></div>
<h3 class='sectionHead'><span class='titlemark'>12.1 </span> <a id='x1-200012.1'></a>Elastostatisches Gleichgewicht</h3>
<!-- l. 9 --><p class='noindent'>Die Grundgleichung der Festkörpermechanik beschreibt das elastostatische
Gleichgewicht. Gegeben ein Tensorfeld \(\t {\sigma }(\v {r})\), dass die <span class='cmti-12'>mechanische Spannung </span>im
System beschreibt, lauten diese \begin {equation} \nabla \cdot \t {\sigma } = \v {0} \label {eq:elastostaticeq} \end {equation}
Wir berechnen nun die Divergenz eines <span class='cmti-12'>Tensors zweiter Ordnung </span>(bzw. einen
Tensor<span class='cmti-12'>feldes </span>zweiter Ordnung) und müssen kurz klarstellen, was wir mit der
Operation \(\nabla \cdot =\text {div}\) meinen. In Komponentenschreibweise wird Gl. \eqref{eq:elastostaticeq}
zu \begin {equation} \partial _\alpha \sigma _{\alpha \beta } = 0, \end {equation}
wobei \(\partial _\alpha \equiv \partial /\partial r_\alpha \) die Ableitung respektive der Komponente der Position \(r_\alpha \) ist und
wir hier die <span class='cmti-12'>Einsteinsche Summenkonvention </span>eingeführt haben. Diese
Gleichgewichtsbedingung hat ihren Ursprung in der Erhaltung des Impulses; \(\t {\sigma }\)
beschreibt drei unabhängige Impulsströme und Gl. \eqref{eq:elastostaticeq} ist
die stationäre Kontinuitätsgleichung, \(\nabla \cdot \v {j}=0\), für diese drei Impulsströme \(\v {j}_\beta \) die
durch die Spaltenvektoren des Tensors \(\t {\sigma }\) gegeben sind, \(\t {\sigma }=(\v {j}_x, \v {j}_y, \v {j}_z)\). Wir werden hier
griechische Indices (\(\alpha \), \(\beta \), etc.) verwenden, um die kartesichen Raumdimensionen
(bzw. Richtungen) anzuzeigen und von den Knoten und Elementindizes zu
unterscheiden.
</p><!-- l. 20 --><p class='indent'> Die mechanische Spannung beschreibt eine Kraft pro Fläche und wird der
SI-Einheit <span class='cmti-12'>Pascal </span>gemessen. Wenn wir Gl. \eqref{eq:elastostaticeq}über eine
(beliebiges) Volumenelement \(\omega \in \Omega \) integrieren, so erhalten wir \begin {equation} \int _\omega \dif ^3 r\, \nabla \cdot \t {\sigma } = \int _{\partial \omega } \dif ^2 r\, \t {\sigma }\cdot \hat {n} = 0 \end {equation}
nach Anwendung des Gaussschen Satzes, wobei \(\partial \omega \) wieder die Oberfläche des
Volumenelements \(\omega \) ist. Der Ausdruck \(\v {t}=\t {\sigma }\cdot \hat {n}\) ist die Projektion der Spannung auf die
Oberflächennormale \(\hat {n}\) – die sogenannten Flächenlasten \(\v {t}\) (engl. “traction” oder
“surface traction”). Der Ausdruck \(\dif \v {F}=\v {t}\dif ^2 r\) ist damit die (infinitesimale) Kraft \(\dif \v {F}\) auf
ein Oberflächenelement und das Integral damit die Summe über alle
Oberflächenkräfte. Diese Summe muss verschwinden; dies ist ein Ausdruck
für das <span class='cmti-12'>Kräftegleichgewicht </span>und damit statisches Gleichgewicht in dem
Volumenelement. Weiterhin gilt noch <span class='cmti-12'>Gleichgewicht der Drehmomente </span>in allen
Volumenelementen \(\omega \). Diese Bedingung führt dazu, dass der Spannungstensor \(\t {\sigma }\)



symmetrisch ist, also \(\t {\sigma }^T=\t {\sigma }\).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 26 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In der Einsteinschen Summenkonvention lässt man
Summationssymbole weg und impliziert Summation über wiederholte Indices. Im
obigen Beispiel, \begin {equation} \partial _\alpha \sigma _{\alpha \beta } \equiv \sum _\alpha \partial _\alpha \sigma _{\alpha \beta }. \end {equation}
Ein Skalarprodukt zwischen den Vektoren \(\v {a}\) und \(\v {b}\) wird in dieser Konvention
geschrieben als \begin {equation} \v {a}\cdot \v {b} = a_\alpha b_\alpha . \end {equation}
Diese Indexschreibweise ist nützlich, weil sie eindeutig ist. In der dyadischen
Notation müssen wir meistens dazu sagen, was wir mit einer Operation
meinen. So ist z.B. bei der Divergenz eines Tensors nicht klar, ob die
Divergenz auf den ersten oder den zweiten Index wirken soll. (Wir nutzen
hier eine Konvention, in der die Divergenz auf den ersten Index wirkt.) </p></div>
<!-- l. 38 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>12.2 </span> <a id='x1-300012.2'></a>Hooksche Gesetz</h3>
<!-- l. 40 --><p class='noindent'>Neben dem physikalischen Grundprinzip, dass die Erhaltung des Impulsstromes
und damit das elastostatische Gleichgewicht beschreibt, brauchen wir noch ein
Konstitutivgesetz, dass uns sagt wie der Spannungstensor (also der Impulsstrom)
auszusehen hat. Hierzu führen wir zunächst die Verschiebungen \(\v {u}(\v {r})\) ein, die die
Verformung eines Raumpunktes auf Grund der mechanischen Belastung
beschrieben. Aus diesen Verschiebungen berechnen wir den Dehnungstensor
\begin {equation} \t {\varepsilon } = \frac {1}{2}\left [ \nabla \v {u} + \left (\nabla \v {u}\right )^T \right ], \label {eq:strain} \end {equation}
bzw. in Komponentenschreibweise \begin {equation} \varepsilon _{\alpha \beta } = \frac {1}{2} \left ( \partial _\alpha u_\beta + \partial _\beta u_\alpha \right ). \end {equation}
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 50 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Der Ausdruck \(\nabla \v {u}\) ist <span class='cmti-12'>nicht </span>die Divergenz von \(\v {u}\). Diese ist gegeben
durch \(\nabla \cdot \v {u}\) – der Punkt ist entscheidend. \(\nabla \v {u}\) ist der Gradient des Vektorfeldes \(\v {u}(\v {r})\) und damit
ein Tensorfeld zweiter Ordnung. Die Komponenten sind gegeben durch
\begin {equation} \left [\nabla \v {u}\right ]_{\alpha \beta } = \partial _\alpha u_\beta . \end {equation}
Die Komponenten des transponierten Tensors sind daher \begin {equation} \left [\nabla \v {u}\right ]^T_{\alpha \beta } = \left [\nabla \v {u}\right ]_{\beta \alpha } = \partial _\beta u_\alpha . \end {equation}
Expliziter könnte man den Gradienten eines Vektorfeldes mit Hilfe des äußeren
Produkts schreiben, es gilt \begin {equation} \nabla \v {u} = \nabla \otimes \v {u} \end {equation}
mit äußerem Produkt \([\v {a}\otimes \v {b}]_{\alpha \beta }=a_\alpha b_\beta \). In der Literatur findet sich allerdings meistens die Form \(\nabla \v {u}\).



</p></div>
<!-- l. 66 --><p class='indent'> Das Hooksche Gesetz beschreibt nun welche Dehnung zu welcher Spannung
führt. Für isotrope Festkörper lautet es \begin {equation} \t {\sigma } = \left (\lambda \, \text {tr}\,\t {\varepsilon }'\right ) \t {1} + 2\mu \t {\varepsilon }' \quad \text {bzw.}\quad \sigma _{\alpha \beta } = \lambda \delta _{\alpha \beta } \varepsilon '_{\gamma \gamma } + 2\mu \varepsilon '_{\alpha \beta }. \label {eq:Hookes-law} \end {equation}
mit \(\varepsilon _{\alpha \beta }'=\varepsilon _{\alpha \beta }-\varepsilon _{0,\alpha \beta }\). Hierbei heißen \(\lambda \) und \(\mu \) <span class='cmti-12'>Lamé-Konstanten</span>. Die Konstante \(\mu \) wird auch das
Schermodul genannt. Der Ausdruck \(\varepsilon _{\gamma \gamma }'\equiv \sum _\gamma \varepsilon _{\gamma \gamma }'=\text {tr}\,\t {\varepsilon }'\) (Einstein-Konvention!) ist die Spur des
Dehnungstensors. Wir haben hier den Dehnungstensor \(\t {\varepsilon }'=\t {\varepsilon }-\t {\varepsilon }_0\) eingeführt, der eine
Eigendehnung \(\t {\varepsilon }_0\) (engl. “eigenstrain”) berücksichtig, die z.B. durch eine thermische
Expansion gegeben sein kann.
</p><!-- l. 90 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>12.3 </span> <a id='x1-400012.3'></a>Schwache Form</h3>
<!-- l. 92 --><p class='noindent'>Wir haben ein gekoppeltes lineares Gleichungssystem zweiter Ordnung, welches
wir nun mit Hilfe der Methode der finiten Elemente diskretisieren werden. Wir
formulieren zunächst die schwache Form von Gl. \eqref{eq:elastostaticeq},
\begin {equation} \int _\Omega \dif ^3 r\, \v {v}(\v {r})\cdot \left ( \nabla \cdot \t {\sigma } \right ) = 0 \quad \text {bzw.}\quad \int _\Omega \dif ^3 r\, v_\beta (\v {r}) \partial _\alpha \sigma _{\alpha \beta } = 0, \end {equation}
wobei \(\v {v}(\v {r})\) nun ein Testvektor ist. Wir nutzen nun wieder eine Variante der
Produktregel, \begin {equation} \partial _\alpha \left ( \sigma _{\alpha \beta } v_\beta \right ) = \left (\partial _\alpha \sigma _{\alpha \beta }\right ) v_\beta + \sigma _{\alpha \beta } \left (\partial _\alpha v_\beta \right ), \end {equation}
um die Ableitung auf die Testfunktion zu überführen. Man erhält
\begin {equation} \int _\Omega \dif ^3 r\, \left [\nabla \cdot \left (\t {\sigma }\cdot \v {v}\right ) - \left (\nabla \v {v}\right ):\t {\sigma } \right ] = 0, \label {eq:weakmech1} \end {equation}
wobei der Doppelpunkt ein doppeltes Skalarprodukt (oder <span class='cmti-12'>Kontraktion</span>) bezeichnet, \(\t {A}:\t {B}=A_{\alpha \beta }B_{\alpha \beta }\).
Wir können nun wieder den ersten Term in Gl. \eqref{eq:weakmech1} mit Hilfe
des Gaussschen Satzes in ein Oberflächenintegral, \begin {equation} \int _{\partial \Omega } \dif ^2 r\, \v {v}\cdot \left (\t {\sigma }\cdot \hat {n}\right ) - \int _\Omega \dif ^3 r\, \left (\nabla \v {v}\right ):\t {\sigma } = 0, \label {eq:weakmech2} \end {equation}
überführen, wobei die Tatsache genutzt wurde, dass \(\t {\sigma }\) symmetrisch ist. Dies ist
die schwache Form mit verringerter Differenzierbarkeitsanforderung des
mechanischen Gleichgewichts. Der Ausdruck \(\v {t}=\t {\sigma }\cdot \hat {n}\) sind wiederum die Flächenlasten
auf der Oberfläche. Ausgedrückt mit Hilfe der Flächenlasten wird die schwache
Form damit zu \begin {equation} \int _{\partial \Omega } \dif ^2 r\, \v {v}\cdot \v {t} - \int _\Omega \dif ^3 r\, \left (\nabla \v {v}\right ):\t {\sigma } = 0. \label {eq:weakmech3} \end {equation}
Die Flächenlast \(\v {t}\) ist eine (von Neumann) Randbedingung der elastostatischen
Differentialgleichungen!
</p><!-- l. 122 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>12.4 </span> <a id='x1-500012.4'></a>Diskretisierung</h3>
<!-- l. 124 --><p class='noindent'>Wir diskretisieren diese Gleichung nun mit Hilfe der Galerkin-Methode und setzen



gleich lineare finite Elemente als Basisfunktionen an. Dies erlaubt es uns,
die Diskretisierung direkt mit Hilfe der Formfunktionen und nicht der
Basisfunktionen zu schreiben. Wir setzen also innerhalb Element \((n)\) an, dass
\begin {equation} u_\beta (\v {r}) = a_{\beta ,Jn} N_J^{(n)}(\v {r}), \end {equation}
wobei \(Jn\) für den globalen Knotenindex steht, der dem lokalen Index des Knotens \(J\)
auf Element \((n)\) entspricht und Summation über \(J\) auf Grund des wiederholten
Indices impliziert ist.
</p><!-- l. 130 --><p class='indent'> Unsere Testfunktion \(\v {v}(\v {r})\) ist nun vektorwertig. Wir benötigen damit
einen Satz von \(DN\) Testvektoren, wobei \(D\) die Dimension des Raumes und \(N\) die
Anzahl der Elemente bezeichnet. Wir setzen daher innerhalb des Elements \((n)\)
\begin {equation} \v {v}_{I\alpha }(\v {r}) = N_I^{(n)}(\v {r}) \hat {e}_\alpha \end {equation}
mit \(\alpha \in [1,\ldots ,D]\) als Testvektor an. Hier bezeichnet \(\hat {e}_\alpha \) den Vektor, bei dem die \(\alpha \)-te Komponente \(1\)
und alle anderen Komponenten \(0\) sind, also den kanonischen Einheitsvektor in
Richtung \(\alpha \).
</p><!-- l. 136 --><p class='indent'> Mit diesen Ansatzfunktionen erhält man für die Dehnung auf Element \((n)\)
\begin {equation} \varepsilon ^{(n)}_{\alpha \beta } = \frac {1}{2} \left (a_{\alpha ,Jn} \partial _\beta N_J^{(n)} + a_{\beta ,Jn} \partial _\alpha N_J^{(n)}\right ). \end {equation}
Das Hooksche Gesetz wird damit zu \begin {equation} \sigma ^{(n)}_{\alpha \beta }(\v {r}) = \lambda (\v {r}) \delta _{\alpha \beta } a_{\gamma ,Jn} \partial _\gamma N_J^{(n)} + \mu (\v {r}) \left (a_{\alpha ,Jn} \partial _\beta N_J^{(n)} + a_{\beta ,Jn} \partial _\alpha N_J^{(n)}\right ) - \sigma _{0,\alpha \beta }(\v {r}) \end {equation}
mit \begin {equation} \sigma _{0,\alpha \beta }(\v {r}) = \lambda (\v {r}) \delta _{\alpha \beta } \varepsilon _{0,\gamma \gamma }(\v {r}) + 2\mu (\v {r}) \varepsilon _{0,\alpha \beta }(\v {r}). \end {equation}
Die diskretisierte Form des Volumenterms der Gleichgewichtsbedingung lautet
\begin {equation} \begin {split} \int \dif ^3 r\, \left (\nabla \v {v}_{I\alpha }\right ):\t {\sigma } =&amp; \int \dif ^3 r\, \left (\nabla N_I^{(n)}\otimes \hat {e}_\alpha \right ):\t {\sigma } \\ =&amp; \int \dif ^3 r\, \left (\partial _\beta N_I^{(n)}\right )\sigma _{\beta \alpha } \\ =&amp; \int \dif ^3 r\, \left \{ \lambda (\v {r}) a_{\gamma ,Jn} \delta _{\alpha \beta } \partial _\beta N_I^{(n)} \partial _\gamma N_J^{(n)}\right . \\ &amp; + \mu (\v {r}) \left (a_{\alpha ,Jn} \partial _\beta N_I^{(n)}\partial _\beta N_J^{(n)} + a_{\beta ,Jn} \partial _\beta N_I^{(n)}\partial _\alpha N_J^{(n)}\right ) \\ &amp;\left . - \sigma _{0,\beta \alpha }(\v {r}) \partial _\beta N_I^{(n)} \right \} \end {split} \label {eq:voleq} \end {equation}
mit impliziter Summation über \(\gamma \) (Einstein-Konvention!). Für lineare Elemente
sind bis auf die Materialkonstanten alle Terme in dieser Gleichung konstant. Das
Integral führt damit effektiv zu einer Mittelung der Materialkonstanten auf den
Element. Wir führen die mittleren Materialkonstanten \begin {equation} \lambda ^{(n)} = \frac {1}{V^{(n)}} \int \dif ^3 r\, \lambda (\v {r}) \end {equation}
und eine äquivalent Gleichung für \(\mu \) und \(\t {\sigma }_0\) ein. Hierbei ist nun \(V^{(n)}\) das Volumen des
Elements \((n)\). Wir können die Indizes umbenennen und damit Gl. \eqref{eq:voleq}
schreiben als \begin {equation} \begin {split} \int \dif ^3 r\, \left (\nabla \v {v}_{I\alpha }\right ):\t {\sigma } =&amp; \lambda ^{(n)} a_{\beta ,Jn}V^{(n)} \delta _{\alpha \gamma } \partial _\gamma N_I^{(n)} \partial _\beta N_J^{(n)} \\ &amp; + \mu ^{(n)} a_{\beta ,Jn} \delta _{\alpha \beta } V^{(n)}\partial _\gamma N_I^{(n)}\partial _\gamma N_J^{(n)} \\ &amp; + \mu ^{(n)} a_{\beta ,Jn} V^{(n)}\partial _\beta N_I^{(n)}\partial _\alpha N_J^{(n)} - V^{(n)}\sigma _{0,\alpha \beta }^{(n)} \partial _\beta N_I^{(n)}. \end {split} \end {equation}
Die Elementmatrix können wir nun direkt aus dieser Gleichung ablesen. Sie hat
die Komponenten \begin {equation} K^{(n)}_{I\alpha J\beta } = \lambda ^{(n)} k_{I\alpha J\beta }^{(n)} + \mu ^{(n)} \left (\delta _{\alpha \beta }k_{I\gamma J \gamma }^{(n)} + k_{I\beta J\alpha }^{(n)}\right ) \end {equation}
mit \(k_{I\alpha J\beta }^{(n)}=V^{(n)}\partial _\alpha N_I^{(n)} \partial _\beta N_J^{(n)}\) und der Beitrag des Elements zum Lastvektor lautet \(f_{I\alpha }^{(n)}=V^{(n)}\sigma _{0,\alpha \beta }^{(n)} \partial _\beta N_I^{(n)}\). Die \(6\times 6\) Matrix \(K^{(n)}_{I\alpha J\beta }\) kann
man sich aus \(2\times 2\) Blöcken zusammengebaut vorstellen. Dann ist z.B. der
Ausdruck \(k_{I\gamma J\gamma }^{(n)}\) die Spur über den \(2\times 2\) Block an Stelle \((I,J)\). Der Zusammenbau der
Systemmatrix funktioniert analog zu den vorherigen Kapiteln – nur das
nun \(2\times 2\) Blöcke anstelle von skalaren Matrixenträgen summiert werden
müssen.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 223 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Für unser strukturiertes zweidimensionales Gitter erhalten wir \(V^{(n)}=\Delta x\Delta y/2\)
und \begin {equation} \t {k} = \frac {1}{2} \begin {pmatrix} \Delta y/\Delta x &amp; 1 &amp; -\Delta y/\Delta x &amp; \cdot &amp; \cdot &amp; -1 \\ 1 &amp; \Delta x/\Delta y &amp; -1 &amp; \cdot &amp; \cdot &amp; -\Delta x/\Delta y \\ -\Delta y/\Delta x &amp; -1 &amp; \Delta y/\Delta x &amp; \cdot &amp; \cdot &amp; 1 \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ -1 &amp; -\Delta x/\Delta y &amp; 1 &amp; \cdot &amp; \cdot &amp; \Delta x/\Delta y \end {pmatrix} \end {equation}
sowohl für das untere linke als auch das obere rechte Dreieck. Der Lastvektor
wird zu \begin {equation} \v {f} = \frac {1}{2}\begin {pmatrix} -\sigma _{0,xx}\Delta y -\sigma _{0,xy}\Delta x \\ -\sigma _{0,xy}\Delta y -\sigma _{0,yy}\Delta x \\ \sigma _{0,xx}\Delta y \\ \sigma _{0,xy}\Delta y \\ \sigma _{0,xy}\Delta x \\ \sigma _{0,yy}\Delta x \end {pmatrix} \end {equation}



für das untere linke Dreieck. Der Lastvektor für das obere rechte Dreieck ist \(-\v {f}\).
Für \(\Delta x=\Delta y\) wird die Elementsteifigkeitsmatrix zu \begin {equation} \t {k} = \frac {1}{2} \begin {pmatrix} 1 &amp; 1 &amp; -1 &amp; \cdot &amp; \cdot &amp; -1 \\ 1 &amp; 1 &amp; -1 &amp; \cdot &amp; \cdot &amp; -1 \\ -1 &amp; -1 &amp; 1 &amp; \cdot &amp; \cdot &amp; 1 \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot &amp; \cdot \\ -1 &amp; -1 &amp; 1 &amp; \cdot &amp; \cdot &amp; 1 \end {pmatrix}. \end {equation}
Wenn wir hier die Spur von Untermatrizen der Größe \(2\times 2\) berechnen, erhalten wir
die Matrix des Laplace-Operators, Gl. \eqref{eq:elmat2d}.
</p><!-- l. 260 --><p class='indent'> Die Dehnung auf Element \((n)\) wird zu \begin {align} \varepsilon ^{(n)}_{xx} &amp;= a_{x,Jn} \partial _x N_J^{(n)} = -a_{x,0n}/\Delta x + a_{x,1n}/\Delta x \\ \varepsilon ^{(n)}_{yy} &amp;= a_{y,Jn} \partial _y N_J^{(n)} = -a_{y,0n}/\Delta _y + a_{y,2n}/\Delta y \\ \varepsilon ^{(n)}_{xy} &amp;= \frac {1}{2} \left (a_{x,Jn} \partial _y N_J^{(n)} + a_{y,Jn} \partial _x N_J^{(n)}\right ) \nonumber \\ &amp;= \frac {1}{2}\left (-a_{x,0n}/\Delta y + a_{x,2n}/\Delta y - a_{y,0n}/\Delta x + a_{y,1n}/\Delta x\right ) \end {align}
</p><!-- l. 267 --><p class='indent'> für das linke untere Dreieck. </p></div>



<h2 class='likechapterHead'><a id='x1-600012.4'></a>Literaturverzeichnis</h2>

