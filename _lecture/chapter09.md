---
layout: default
title: "Kap. 09 [5. Dez.-9. Dez.]"
parent: Vorlesung
date: 2022-10-11
categories: lecture
author: Lars Pastewka
nav_order: 9
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 9</span><br /><a id='x1-10009'></a>Finite Elemente in einer Dimension</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 4 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> In diesem Kapitel werden einige Eigenschaften der finiten Elemente
anhand eindimensionaler Beispiele diskutiert. Insbesondere wird gezeigt, wie mit
linearen Elementen PDGLs zweiter Ordnung diskretisiert werden und wie
Randbedingungen in den finiten Elementen eingebaut werden können. </p></div>
<h3 class='sectionHead'><span class='titlemark'>9.1 </span> <a id='x1-20009.1'></a>Differenzierbarkeit der Basisfunktionen</h3>
<!-- l. 10 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=5f1094b6-98c3-40a4-9f67-aca900bc1ddd'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=5f1094b6-98c3-40a4-9f67-aca900bc1ddd</span></a>
</p><!-- l. 12 --><p class='indent'> Der einfachste Fall einer Basis der finiten Elemente in einer Dimension wurde
bereits in den vorherigen Kapiteln eingeführt. Die Basisfunktionen sind
“Zelt-” oder “Hutfunktionen” die jeweils auf einem Knoten maximal (\(=1\))
sind und dann zu den beiden benachbarten Knoten linear abfallen. Im
Gegensatz zu der Fourier-Basis ist diese Basis nicht (im klassischen Sinne noch
nicht einmal) differenzierbar. Dies heißt eigentlich, dass wir diese Basis
nicht als Reihenentwicklung für die Ansatzfunktion zur Lösung einer
PDGL zweiter (bzw. sogar erster) Ordnung verwenden können, in denen
Ableitungen auftauchen. Wir zeigen hier nun dass im Rahmen einer <span class='cmti-12'>schwachen</span>
Formulierung eine schwache Lösung erhalten werden kann, die diese
Anforderungen an die Differenzierbarkeit nicht erfüllen muss. Damit
können diese Basisfunktionen doch für PDGLs zweiter Ordnung verwendet
werden.
</p><!-- l. 14 --><p class='indent'> Wir betrachten als Beispiel hier weiterhin die eindimensionale Poisson-Gleichung
mit dem Residuum \begin {equation} R(x) = \frac {\dif ^2 \Phi }{\dif x^2} + \frac {\rho (x)}{\varepsilon }. \label {eq:strongresidual} \end {equation}
In der Methode der gewichteten Residuen wird verlangt, dass das Skalarprodukt
des Residuums mit einer Testfunktion \(v(x)\) verschwindet, \((v,R)=0\). In dieser integralen
Formulierung kann man nun die Regeln der partiellen Integration nutzen,
um eine Ableitung auf die Testfunktion zu übertragen. Man bekommt \begin {align} (v(x), R(x)) =&amp; \int _a^b \dif x\, v(x) \left ( \frac {\dif ^2 \Phi }{\dif x^2} + \frac {\rho (x)}{\varepsilon }\right ) \label {eq:beforepartialint} \\ =&amp; \int _a^b \dif x\, \left [ \frac {\dif }{\dif x} \left ( v(x) \frac {\dif \Phi }{\dif x} \right ) - \frac {\dif v}{\dif x} \frac {\dif \Phi }{\dif x} \right ] + \int _a^b \dif x\, v(x) \frac {\rho (x)}{\varepsilon } \\ =&amp; \left . v(x) \frac {\dif \Phi }{\dif x} \right |_a^b - \int _a^b \dif x\, \frac {\dif v}{\dif x} \frac {\dif \Phi }{\dif x} + \int _a^b \dif x\, v(x) \frac {\rho (x)}{\varepsilon }. \label {eq:afterpartialint} \end {align}
</p><!-- l. 56 --><p class='indent'> Gleichung \eqref{eq:afterpartialint} enthält nun <span class='cmti-12'>keine </span>zweite Ableitung
mehr. D.h. sowohl die Testfunktion \(v(x)\) als auch die Lösung \(\Phi (x)\) müssen für alle \(x\)
lediglich einmal differenzierbar sein. Wir können daher lineare Basisfunktion
nutzen, um eine PDGL zweiter Ordnung zu diskretisieren. Im Folgenden werden
wir das Simulationgsgebiet als \(\Omega \) bezeichnen. In dem eindimensionalen Fall der hier
diskutiert wird ist \(\Omega =[a,b]\).
</p>



<div class='framedenv' id='shaded*-1'>
<!-- l. 58 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die linearen Basisfunktionen sind im klassischen Sinne
noch nicht einmal einfach differenzierbar, weil sich der linksseitige und
rechtsseitige Differenzenquotient an den Knicken der Funktion unterscheidet. Es
existiert aber die sogenannte schwache Ableitung \(f'(x)\) der Funktion \(f(x)\), wenn
\begin {equation} \int _\Omega \dif x\, v(x) f'(x) = -\int _\Omega \dif x\, v'(x) f(x) \label {eq:weakderivative} \end {equation}
für beliebige (stark differenzierbare) Testfunktionen \(v(x)\). Die schwache Ableitung ist
nicht eindeutig; so kann man an den Knicken der Zeltfunktionen beispielsweise \(0\)
(oder jeden beliebigen anderen Wert) als schwache Ableitung annehmen. Dies
funktioniert, weil in dem Integral Gl. \eqref{eq:weakderivative} dieser einzelne
Punkt keinen Beitrag hat. Genauso wie die schwache Ableitung nicht
eindeutig ist, ist die schwache Lösung einer Differentialgleichung nicht
eindeutig.
</p><!-- l. 66 --><p class='indent'> In diesem Lernmaterial werden wir nicht systematisch zwischen starker und
schwacher Ableitung unterscheiden sondern implizit annehmen, dass wir mit der
schwachen Ableitung operieren. Wir führen oft intuitive Rechenoperationen mit
schwachen Ableitungen durch, wie z.B. eine Stufenfunktion als Ableitung
der finiten Zelte zu nehmen und eine Dirac-\(\delta \)-Funktion als Ableitung der
Stufenfunktion. Dieser mathematisch unpräzise Umgang mit Ableitungen ist in
den Ingenieurswissenschaften und der Physik verbreitet und führt meist zu
richtigen Ergebnissen. Funktionenräume schwach differenzierbarer Funktionen
heißen <span class='cmti-12'>Sobolev-Räume</span>. Da man für die schwache Differenzierbarkeit immer
ein Skalarprodukt braucht (siehe Gl. \eqref{eq:weakderivative}), sind
Sobolev-Räume auch immer Hilbert-Räume. </p></div>
<!-- l. 69 --><p class='indent'> Wir haben damit unser Verständnis der Lösung einer PDGL erweitert.
Während für die starke Lösung \(R(x)\equiv 0\), Gl. \eqref{eq:strongresidual}, die
Funktion \(\Phi (x)\) zweimal stark differenzierbar sein muss, muss diese Funktion für
die schwache Lösung \((v,R)\equiv 0\), Gl. \eqref{eq:afterpartialint}, lediglich einmal
schwach differenzierbar sein. Gleichung \eqref{eq:afterpartialint} muss
hier natürlich für alle einmal diffenzierbaren Testfunktionen \(v(x)\) erfüllt
sein.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 71 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In der Kollokationsmethode wird die “starke” Anforderung der
zweimaligen Differenzierbarkeit nicht aufgehoben. Das sieht man z.B. daran,
dass der Dirac-\(\delta \) als Testfunktion für die Kollokationsmethode noch nicht
einmal im schwachen Sinne differenzierbar ist. D.h. die Testfunktionen der
Kollokationsmethode sind nicht in der Menge der Testfunktionen, für welche \((v,R)\equiv 0\) im
Sinne der schwachen Lösung verlangt wird. Dies ist der Grund, warum die



gewichteten Residuen und hier spezifisch die Galerkin-Methode eine so weite
Verbreitung gefunden hat. </p></div>
<!-- l. 75 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>9.2 </span> <a id='x1-30009.2'></a>Galerkin-Methode</h3>
<!-- l. 78 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=7e114881-a10b-449a-95be-aca900bc1dad'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=7e114881-a10b-449a-95be-aca900bc1dad</span></a>
</p><!-- l. 80 --><p class='indent'> Im Rahmen der schwachen Formulierung Gl. \eqref{eq:afterpartialint}, wird
nun die Galerkin-Methode angesetzt. Wir schreiben wieder \begin {equation} \Phi (x) \approx \Phi _N(x) = \sum _{n=0}^N a_n \varphi _n(x) \end {equation}
als (endliche) Reihenentwicklung mit unseren finiten Elementen, den Zeltfunktionen \(\varphi _n(x)\).
Wir betrachten zunächst den Fall, in dem die Testfunktion auf dem Rand des
Gebietes \(\Omega \), also bei \(x=a\) und \(x=b\), verschwindet; damit verschwindet der erste
Term in Gl. \eqref{eq:afterpartialint}. Dieser Term verschwindet z.B. bei
periodischen Gebieten. (Dieser Term wird aber wieder wichtig, wenn wir über
Randbedingungen für nicht-periodische Gebiete sprechen.)
</p><!-- l. 86 --><p class='indent'> Die Galerkin-Bedingung wird damit zu \begin {equation} (\varphi _k, R_N) = - \sum _n a_n \int _\Omega \dif x\, \frac {\dif \varphi _k}{\dif x} \frac {\dif \varphi _n}{\dif x} + \frac {1}{\varepsilon } \int _\Omega \dif x\, \varphi _k(x) \rho (x) = 0 \label {eq:fegaler1d} \end {equation}
mit unbekanntem \(a_n\). Die Integrale in Gl. \eqref{eq:fegaler1d} sind lediglich Zahlen;
die Gleichung ist damit ein System gekoppelter linearer Gleichungen. Mit
\begin {equation} K_{kn} = \int _\Omega \dif x\, \frac {\dif \varphi _k}{\dif x} \frac {\dif \varphi _n}{\dif x} \quad \text {und}\quad f_k = \frac {1}{\varepsilon } \int _\Omega \dif x\, \varphi _k(x) \rho (x) \end {equation}
erhält man damit \begin {equation} \sum _n K_{kn} a_n = f_k, \label {eq:lineq} \end {equation}
oder in dyadischer (Matrix-Vektor) Schreibweise \begin {equation} \t {K}\cdot \v {a} = \v {f}. \label {eq:lineqdyad} \end {equation}
Damit ist die Differentialgleichung in eine algebraische Gleichung überführt, die
numerisch gelöst werden kann. Die Matrix \(\t {K}\) heißt Systemmatrix oder
Steifigkeitsmatrix. (Letzter Begriff kommt aus der Anwendung der finiten
Elemente im Rahmen der Strukturmechanik.) Der Term \(\v {f}\) wird oft als “rechte
Seite” (engl. “right hand side”, oft als “rhs” abgekürzt) oder Lastvektor
(wiederum aus der Strukturmechanik) bezeichnet.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 126 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In der Strukturmechanik, die sich mit der Verformung von
Festkörpern beschäftigt, ist \(\t {K}\) so etwas wie eine Federkonstante, \(\v {f}\) eine Kraft und \(\v {a}\)
die <span class='cmti-12'>Verschiebungen </span>(engl. “displacements”) der Knoten, also der Abstand zum
unverformten Zustand. Damit ist Gl. \eqref{eq:lineqdyad} so etwas wie die
Verallgemeinerung eines Federgesetzes, des Hookschen Gesetzes. Aus diesem
Grund werden traditionell die Symbole \(\t {K}\) und \(\v {f}\) genutzt. Die Strukturmechanik ist
komplizierter als die meisten anderen numerischen Anwendungsfälle, weil sich
das Gebiet, auf dem die konstituierenden Gleichungen diskretisiert wurden, durch



die Verformung selbst verändert. Dies führt automatisch zu nicht-linearen
Gleichungen, sogenannten geometrischen Nichtlinearitäten. In diesem Fall
hängt dann \(\t {K}\) selbst von \(\v {a}\) ab. </p></div>
<!-- l. 130 --><p class='indent'> Wir können nun die Elemente der Matrix \(\t {K}\) direkt ausrechnen. Für die Basis
der finiten Elemente folgt \begin {equation} \frac {\dif \varphi _n(x)}{\dif x} = \left \{ \begin {array}{ll} \frac {1}{x_n - x_{n-1}} &amp; \text {für}\; x\in [x_{n-1},x_n]\\ -\frac {1}{x_{n+1} - x_n} &amp; \text {für}\; x\in [x_n,x_{n+1}] \\ 0 &amp; \text {sonst} \end {array} \right . \label {eq:finite-element-basis-derivative} \end {equation}
und damit \begin {align} K_{nn} &amp;= \frac {1}{x_n - x_{n-1}} + \frac {1}{x_{n+1} - x_n} \\ K_{n,n+1} &amp;= -\frac {1}{x_{n+1} - x_n} \end {align}
</p><!-- l. 146 --><p class='indent'> und \(K_{kn} = 0\) für \(|n-k|&gt;1\). Die Matrix \(\t {K}\) ist also dünnbesetzt, symmetrisch und nahezu
tridiagonal.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 149 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> Für äquidistante Knoten mit Abstand \(\Delta x = x_{n+1}-x_n\) auf einer periodischen Gebiet
erhält man für beispielsweise \(6\) Knoten (\(N=5\)): \begin {equation} \t {K} = \frac {1}{\Delta x} \begin {pmatrix} 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 &amp; -1 \\ -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 \\ -1 &amp; 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 \\ \end {pmatrix} \label {eq:systemmatrix1d-periodic-not-regular} \end {equation}
Man beachte, dass die \(-1\) in der rechten oberen und linken unteren Ecke (\(K_{0N}\)
und \(K_{N0}\)) auf Grund der Periodizität erscheinen. Die Matrix ist daher nicht
rein tridiagonal. Die rechte Seite \(f_k\) hängt von der spezifischen Wahl des
Quellterms, also der Ladungsdichte \(\rho (x)\) ab und sieht folgendermaßen aus: \begin {equation} \v {f} = \begin {pmatrix} (\varphi _0(x), \rho (x))/\varepsilon \\ (\varphi _1(x), \rho (x))/\varepsilon \\ (\varphi _2(x), \rho (x))/\varepsilon \\ (\varphi _3(x), \rho (x))/\varepsilon \\ (\varphi _4(x), \rho (x))/\varepsilon \\ (\varphi _5(x), \rho (x))/\varepsilon \end {pmatrix} \label {eq:rhs1d-periodic-not-regular} \end {equation}
</p><!-- l. 176 --><p class='indent'> Im Verlauf dieses Lernmaterials ist bislang vollkommen unter den Tisch
gefallen, dass man für die Lösung von DGLs auch immer <span class='cmti-12'>Randbedingungen</span>
braucht. Selbst dieser periodische Fall ist so nicht vollständig. In der
Fourier-Darstellung repräsentiert \(n=0\) (mit Wellenvektor \(q_0=0\)) den Mittelwert
der Fourier-Reihe. Die Lösung der Poisson-Gleichung spezifiziert diesen
Mittelwert nicht und dieser muss damit als zusätzliche Bedingung angegeben
werden.
</p><!-- l. 178 --><p class='indent'> Im Rahmen der Diskretisierung mit Hilfe der finite Elemente
äußert sich dies darin, dass die Systemmatrix \(\t {K}\), so wie sie z.B. in
Gl. \eqref{eq:systemmatrix1d-periodic-not-regular} aufgeschrieben ist, nicht
<span class='cmti-12'>regulär </span>(auch <span class='cmti-12'>invertierbar </span>oder <span class='cmti-12'>nichtsingulär</span>) ist. Dies sieht man z.B.
daran, dass die Determinante von \(\t {K}\) verschwindet. Anders ausgedrückt, die
linearen Gleichungen sind nicht linear unabhängig. In dem hier diskutierten
Fall ist der <span class='cmti-12'>Rang </span>der Matrix, also die Anzahl der linear unabhängigen
Zeilen, genau eins kleiner als deren Dimension. Wir können daher eine
dieser Gleichungen (bzw. Zeilen) entfernen und dafür die entsprechende
Mittelwertbedingung einführen. Für den periodischen Fall lautet diese
\begin {equation} \int _\Omega \dif x\, \Phi _N(x) = \sum _n a_n \int _\Omega \dif x\, \varphi _n(x) = \sum _n a_n \Delta x = 0. \label {eq:feaverage} \end {equation}
Die reguläre Systemmatrix sieht dann folgendermaßen aus, \begin {equation} \t {K} = \frac {1}{\Delta x} \begin {pmatrix} 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 &amp; -1 \\ -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 \\ 1 &amp; 1 &amp; 1 &amp; 1 &amp; 1 &amp; 1 \\ \end {pmatrix} \label {eq:systemmatrix1d-periodic-regular} \end {equation}
wobei nun auch \(f_N=0\) gelten muss. Die rechte Seite wird also zu \begin {equation} \v {f} = \begin {pmatrix} (\varphi _0(x), \rho (x))/\varepsilon \\ (\varphi _1(x), \rho (x))/\varepsilon \\ (\varphi _2(x), \rho (x))/\varepsilon \\ (\varphi _3(x), \rho (x))/\varepsilon \\ (\varphi _4(x), \rho (x))/\varepsilon \\ 0 \end {pmatrix}. \label {eq:rhs1d-periodic-regular} \end {equation}



Die letzte Zeile entspricht der Mittelwertbedingung Gl. \eqref{eq:feaverage}, man
hätte aber jede beliebige Zeile durch diese Bedingung ersetzen können. </p></div>
<!-- l. 210 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>9.3 </span> <a id='x1-40009.3'></a>Randbedingungen</h3>
<!-- l. 212 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=fd06f299-0d14-4e00-ac51-acaa00b40ea2'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=fd06f299-0d14-4e00-ac51-acaa00b40ea2</span></a>
</p><!-- l. 214 --><p class='indent'> Die Mittelwertbedingung des vorhergehenden Beispiels ist ein Spezialfall
einer Randbedingung. Meistens werden Probleme auf endlichen Gebieten \(\Omega \)
behandelt, in denen entweder der Funktionswert \(\Phi (x)\) oder die Ableitung \(\dif \Phi /\dif x\) auf dem
Rand \(\partial \Omega \) des Gebiets vorgegeben sind. (In unserem eindimensionalen Fall, \(\partial \Omega =\{a,b\}\).)
Der erste Fall nennt sich eine Dirichlet-Randbedingung, der zweite Fall
heißt Neumann-Randbedingung. Für Differentialgleichungen höherer
Ordnung als zwei könnten natürlich auch noch höhere Ableitungen
auf dem Rand auftreten. Auch sind Kombinationen aus Dirichlet- und
Neumann-Randbedingungen möglich. Wir werden hier lediglich reine Dirichlet-
und reine Neumann-Randbedingungen diskutieren.
</p><!-- l. 216 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>9.3.1 </span> <a id='x1-50009.3.1'></a>Dirichlet-Randbedingungen</h4>
<!-- l. 218 --><p class='noindent'>Im dem hier diskutierten eindimensionalen Fall lauten die Dirichlet-Randbedingungen
\begin {equation} \Phi (a) \approx \Phi _N(a) = \Phi _a \quad \text {und}\quad \Phi (b) \approx \Phi _N(b) = \Phi _b. \end {equation}
Diese Bedingungen führen direkt zu \(a_0=\Phi _a\) und \(a_N=\Phi _b\). D.h. die Dirichlet-Bedingungen fixieren
direkt die entsprechenden Koeffizienten der Reihenentwicklung. Man beachte, dass
hier implizit die Bedingungen \((\varphi _0, R)=0\) und \((\varphi _N, R)=0\) aus dem Gleichungssystem herausgenommen
wurden. Die Basisfunktionen \(\varphi _0(x)\) und \(\varphi _N(x)\) tauchen aber selbstverständlich noch in der
Reihenentwicklung \(\Phi _N(x)\) auf.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 225 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> In unserem Beispiel wird die Systemmatrix mit Dirichlet-Randbedingungen
dann zu \begin {equation} \t {K} = \frac {1}{\Delta x} \begin {pmatrix} 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \\ \end {pmatrix} \label {eq:systemmatrix1d-dirichlet} \end {equation}
und \(f_0=\Phi _a/\Delta x\) und \(f_N=\Phi _b/\Delta x\): \begin {equation} \v {f} = \begin {pmatrix} \Phi _a/\Delta x \\ (\varphi _1(x), \rho (x))/\varepsilon \\ (\varphi _2(x), \rho (x))/\varepsilon \\ (\varphi _3(x), \rho (x))/\varepsilon \\ (\varphi _4(x), \rho (x))/\varepsilon \\ \Phi _b/\Delta x \end {pmatrix} \label {eq:rhs1d-dirichlet} \end {equation}
Diese Matrix \(\t {K}\) ist regulär.



</p><!-- l. 252 --><p class='indent'> Das \(\Delta x\) taucht auf der rechten Seite \(f_0\) und \(f_N\) nur auf, weil es als Vorfaktor in der
Systemmatrix steht. In einer Implementierung würde man \(\Delta x\) komplett auf die
rechte Seite schieben und es verschwindet damit komplett aus der ersten und
letzten Zeile. </p></div>
<!-- l. 255 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>9.3.2 </span> <a id='x1-60009.3.2'></a>Neumann-Randbedingungen</h4>
<!-- l. 257 --><p class='noindent'>Die Neumann-Randbedingungen lauten \begin {equation} \left .\frac {\dif \Phi }{\dif x}\right |_a \approx \left .\frac {\dif \Phi _N}{\dif x}\right |_a = \Phi ^\prime _a \quad \text {und}\quad \left .\frac {\dif \Phi }{\dif x}\right |_b \approx \left .\frac {\dif \Phi _N}{\dif x}\right |_b = \Phi ^\prime _b. \end {equation}
Um diese Bedingungen in unsere algebraische Gleichung aufzunehmen, dürfen
wir nun nicht mehr den ersten Term aus Gl. \eqref{eq:afterpartialint}
vernachlässigen. Für die Dirichlet-Randbedingungen spielt dieser Term keine
Rolle, da die Basisfunktionen \(\varphi _1(x)\) bis \(\varphi _{N-1}(x)\) auf dem Rand \(x=a,b\) verschwinden. Die
Basisfunktionen \(\varphi _0(x)\) und \(\varphi _N(x)\) tun dies nicht, tauchen aber im Dirichlet-Fall auch nicht
mehr in der Menge unserer Testfunktionen auf.
</p><!-- l. 265 --><p class='indent'> Wir müssen nun aber bestimmen, wie wir die Basisfunktionen \(\varphi _0(x)\) und \(\varphi _N(x)\)
interpretieren, die nun über den Rand des Gebiets hinausragen. Eine natürliche
Interpretation ist es, nur die Hälfte des “Zeltes” zu betrachten, die in dem
Gebiet verbleiben.
</p><!-- l. 267 --><p class='indent'> Der Galerkin-Ansatz führt damit zu \begin {equation} (\varphi _k, R_N) = \left . \varphi _k(x) \frac {\dif \Phi }{\dif x} \right |_a^b - \sum _n a_n \int _\Omega \dif x\, \frac {\dif \varphi _k}{\dif x} \frac {\dif \varphi _n}{\dif x} + \frac {1}{\varepsilon }(\varphi _k(x), \rho (x)) = 0. \end {equation}
Der zusätzliche Term auf der linken Seite spielt nur bei \(k=0\) und \(k=N\) eine Rolle. Man
erhält \begin {equation} (\varphi _0, R_N) = - \Phi ^\prime _a - \sum _n K_{0n} a_n + \frac {1}{\varepsilon }(\varphi _0(x), \rho (x)) \end {equation}
mit \begin {equation} K_{00} = \frac {1}{x_1-x_0} \quad \text {und}\quad K_{01} = -\frac {1}{x_1 - x_0} \end {equation}
sowie alle weiteren \(K_{0n}=0\). Wir können dieses wieder (siehe Gl. \eqref{eq:lineq}) mit
\begin {equation} f_0 = \frac {1}{\varepsilon }(\varphi _0(x), \rho (x)) - \Phi ^\prime _a \end {equation}
schreiben. Ein entsprechender Satz von Gleichungen gilt für den rechten Rand
mit \(k=N\).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 310 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> In unserem Beispiel wird die Sytemmatrix für zwei
Neumann-Randbedingungen dann zu \begin {equation} \t {K} = \frac {1}{\Delta x} \begin {pmatrix} 1 &amp; -1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; -1 &amp; 1 \\ \end {pmatrix}. \label {eq:systemmatrix1d-neumann} \end {equation}
Man beachte, dass diese Systemmatrix sich leicht von der für
Dirichlet-Randbedingungen, Gl. \eqref{eq:systemmatrix1d-dirichlet},
unterscheidet. Diese Matrix ist nicht regulär und damit ist das Problem mit zwei
Neumann-Randbedingungen unbestimmt. Der Grund hierfür ist der gleiche wie
im periodischen Fall: Die Neumann-Randbedingungen legen den Absolutwert
(Mittelwert) des Potentials \(\Phi \) nicht fest. Man braucht also entweder eine



Dirichlet-Randbedingung (links oder rechts) oder wieder die Fixierung des
Mittelwertes.
</p><!-- l. 325 --><p class='indent'> Die rechte Seite wird zu: \begin {equation} \v {f} = \begin {pmatrix} (\varphi _0(x), \rho (x))/\varepsilon - \Phi ^\prime _a \\ (\varphi _1(x), \rho (x))/\varepsilon \\ (\varphi _2(x), \rho (x))/\varepsilon \\ (\varphi _3(x), \rho (x))/\varepsilon \\ (\varphi _4(x), \rho (x))/\varepsilon \\ (\varphi _5(x), \rho (x))/\varepsilon + \Phi ^\prime _b \end {pmatrix}. \label {eq:rhs1d-neumann} \end {equation}
Zu beachten ist, dass für die Auswertung von \((\varphi _0,\rho )\) und \((\varphi _5,\rho )\) nur über die Hälfte des
entsprechenden Zeltes integriert werden muss. </p></div>
<!-- l. 340 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>9.4 </span> <a id='x1-70009.4'></a>Formfunktionen</h3>
<!-- l. 342 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=b390b0a2-cbb2-4d89-aad5-aca9011cf294'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=b390b0a2-cbb2-4d89-aad5-aca9011cf294</span></a>
</p><!-- l. 344 --><p class='indent'> Die Methode der finiten Elemente wird oft nicht mit Hilfe der Basisfunktionen
sondern mit Hilfe der sogenannten <span class='cmti-12'>Formfunktionen </span>(engl. “shape functions”)
formuliert. Der Grund hierfür ist, dass die Formfunktionen einen intuitiveren
Zugang zu der Interpolationsvorschrift, die hinter den finiten Elementen steckt,
liefert und damit eine einfachere Erweiterung auf mehrere Dimensionen
ermöglicht. In dem eindimensionalen Fall wirken die Formfunktionen
komplizierter als der oben skizzierte Ansatz, für die Formulierung der Methode
der finiten Elemente in mehrere Dimensionen wird dies aber der einfachere
Zugang sein.
</p><!-- l. 346 --><p class='indent'> Wir müssen zunächst darüber reden, was ein <span class='cmti-12'>Element </span>ist. Die
Zeltfunktionen führen zu einer linearen Interpolation zwischen den Knoten. Die
Gebiete zwischen den Knoten heißen <span class='cmti-12'>Elemente</span>. In einer Dimension sind dies
eindimensionale Intervalle, in höheren Dimensionen können die Elemente
komplexe Formen annehmen. Eine lineare Basisfunktion, wie sie hier eingeführt
wurde, ist auf den Knoten zentriert und auf zwei Elementen ungleich
Null.
</p><!-- l. 349 --><p class='indent'> Anstelle die Interpolation im Sinne der Basisfunktionen zu definieren, können
wir auch verlangen, dass innerhalb eines Elements die Funktionswerte auf den
Knoten in gegebener Form, hier zunächst linear, interpoliert werden. Für das
\(n\)-te Element zwischen den Knoten \(n\) und \(n+1\), also \(x\in \Omega ^{(n)}=[x_n,x_{n+1}]\), tragen nur die Basisfunktionen \(\varphi _n\)
und \(\varphi _{n+1}\) bei, da alle weiteren Basisfunktionen auf diesem Interval verschwinden. Hier
bezeichnet \(\Omega ^{(n)}\) das Gebiet des \(n\)-ten Elements. Damit hat die Funktion \(\Phi _N(x)\) in diesem
Element den Verlauf \begin {equation} \begin {split} \phi ^{(n)}(x) =&amp; a_n \varphi _n(x) + a_{n+1}\varphi _{n+1}(x) \\ =&amp; a_n \frac {x_{n+1}-x}{x_{n+1} - x_n} + a_{n+1}\frac {x-x_n}{x_{n+1} - x_n} \\ =&amp; a_n N^{(n)}_{0}(\xi ^{(n)}(x)) + a_{n+1} N^{(n)}_{1}(\xi ^{(n)}(x)), \label {eq:basistoform} \end {split} \end {equation}
mit \(\xi ^{(n)}(x)=(x-x_n)/(x_{n+1}-x_n)\) und \(x\in \Omega ^{(n)}\). Hier und im Folgenden bezeichnen hochgestellte Indices \(x^{(n)}\) Elemente und
tiefgestellte Indices \(x_n\) Knoten. Die Funktionen \begin {equation} N_{0}^{(n)}(\xi ) = 1-\xi \quad \text {und}\quad N_{1}^{(n)}(\xi ) = \xi \label {eq:linel1d} \end {equation}
mit \(\xi \in [0,1]\) heißen <span class='cmti-12'>Formfunktionen </span>(auch <span class='cmti-12'>Ansatzfunktionen</span>) und \(\xi ^{(n)}(x)\) ist eine
Reskalierungsfunktion, die am linken Rand des \(n\)-ten Elements \(\xi ^{(n)}=0\) und am rechten



Rand des Elements \(\xi ^{(n)}=1\) wird. Hiermit wird die Größe des Elements von der
Interpolationsvorschrift (der “Form”) entkoppelt.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 378 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Man beachte, dass es genau ein Element weniger als Knoten gibt,
die wir bislang auch mit dem Index \(n\) bezeichnet haben. In dem eindimensionalen
Fall ist der Zusammenhang zwischen globalen Knotenindice und Elementindice
trivial, in höheren Dimensionen wird die Buchhaltung der Indices kompliziert.
Die Kombination aus lokalem Index des Knoten innerhalb eines Elements (hier \(0\)
für den linken und \(1\) für den rechten Knoten) und Elementindex ergibt den
globalen Knotenindex (hier \(n\)). </p></div>
<!-- l. 382 --><p class='indent'> Die Interpolationsvorschrift hängt vom Index \(n\) des Elements ab, da die
Elemente unterschiedliche Größen haben können. Es gibt für jeden Knoten des
Elements eine Formfunktion, die hier mit links, \(N_{0}^{(n)}\), und rechts, \(N_{1}^{(n)}\) bezeichnet sind. Die
Menge der Formfunktionen eines Elements bestimmen den <span class='cmti-12'>Elementtyp</span>.
Gleichungen \eqref{eq:linel1d} definieren ein lineares Element. Im Prinzip
können die Elementtypen für jedes Element unterschiedlich sein, für
den Basissatz den wir bislang verwendet haben, sind allerdings die linke
und rechte Formfunktion (und damit der Elementyp) für alle Elemente
identisch.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 384 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Basisfunktionen \(\varphi _n(x)\) sind global definiert, d.h. sie leben auf dem
gesamten Simulationsgebiet \(\Omega \) (verschwinden aber in Abschnitten daraus).
Die Formfunktion \(N^{(n)}_{i}(x)\) ist nur auf dem einzelnen Element \(n\) definiert, d.h. sie
leben auf \(\Omega ^{(n)}\). Hier bezeichnet \(i\) den Knoten innerhalb des Elements. Wir
können aber natürlich die Basisfunktionen mit Hilfe der Formfunktionen
ausdrücken, indem man die Funktionen sammelt, welche den entsprechenden
Entwicklungskoeffizienten \(a_n\) als Vorfaktor tragen. Man erhält in dem
eindimensionalen Fall \begin {equation} \varphi _n(x) = N^{(n)}_{0}(x) + N^{(n-1)}_{1}(x) \label {eq:formtobasis} \end {equation}
mit der kompakten Schreibweise \(N^{(n)}_{I}(x)=N^{(n)}_{I}(\xi ^{(n)}(x))\). Gleichung \eqref{eq:formtobasis} ist so zu
interpretieren, dass die Formfunktionen verschwinden wenn das Argument nicht
im Element liegt, also für \(x\not \in \Omega ^{(n)}\). In zwei oder drei Dimensionen ist es üblicherweise
einfacher mit den Formfunktionen als mit den Basisfunktionen zu arbeiten.
Umgekehrt sind die Formfunktionen letztendlich der Teil der Basisfunktionen, der
auf den Elementen lebt, siehe auch Gl. \eqref{eq:basistoform}. </p></div>
<!-- l. 395 --><p class='indent'> Formfunktionen sind nützlich, weil man mit ihrer Hilfe die approximierte



Lösung als Summe über Elemente schreiben kann, also im eindimensionalen Fall
\begin {equation} \Phi _N(x) = \sum _{n=0}^{N-1} \phi ^{(n)}(x) = \sum _{n=0}^{N-1} \left ( a_n N^{(n)}_{0}(x) + a_{n+1} N^{(n)}_{1}(x) \right ). \end {equation}
Für eine allgemeine PDGL, \(R=\mathcal {L} u_N - f\), wird die Galerkin-Bedingung zu \begin {equation} (\varphi _k, R) = (N^{(k)}_{0} + N^{(k-1)}_{1}, R) = 0 \label {eq:galerkinform} \end {equation}
mit \begin {align} (N^{(k)}_{I}, R) =&amp; \sum _{n=0}^{N-1} \left ( a_n (N^{(k)}_{I}, \mathcal {L} N^{(n)}_{0}) + a_{n+1} (N^{(k)}_{I}, \mathcal {L} N^{(n)}_{1}) \right ) - (N^{(k)}_{I}, f) \label {eq:formprod1} \\ =&amp; a_k (N^{(k)}_{I}, \mathcal {L} N^{(k)}_{0}) + a_{k+1} (N^{(k)}_{I}, \mathcal {L} N^{(k)}_{1}) - (N^{(k)}_{I}, f) \end {align}
</p><!-- l. 436 --><p class='indent'> wobei die Summe in Gl. \eqref{eq:formprod1} verschwindet, weil die
Formfunktionen auf unterschiedlichen Elementen trivialerweise orthogonal sind.
Hier und im Folgenden bezeichnen Großbuchstaben \(I\) lokale Knotenindices,
während kleine Buchstaben \(i\) globale Knotenindices bezeichnen.
</p><!-- l. 438 --><p class='indent'> Motiviert durch diese Gleichung, definieren wir eine <span class='cmti-12'>Elementmatrix </span>(oder
<span class='cmti-12'>Elementsteifigkeitsmatrix</span>) für Element \(n\) als \begin {equation} K^{(n)}_{IJ} = (N^{(n)}_{I}, \mathcal {L} N^{(n)}_{J}), \end {equation}
sowie \begin {equation} f^{(n)}_I = (N^{(n)}_{I}, f). \end {equation}
In dieser Schreibweise erhalten wir \begin {equation} (N^{(k)}_{I}, R) = \sum _{J=0}^1 K^{(k)}_{IJ} a_{k+J} - f_I^{(k)} \end {equation}
wobei \(J\) über die Knoten innerhalb des Elements \(k\) läuft und damit (in einer
Dimension) \(k+J\) der globale Knotenindex des entsprechenden linken oder rechten
Knotens ist. Die Galerkin-Bedingung Gl. \eqref{eq:galerkinform} wird damit zu
\begin {equation} \begin {split} (\varphi _k, R) =&amp; (N^{(k)}_{0},R) + (N^{(k-1)}_{1}, R) \\ =&amp; \sum _{I=0}^1 \left ( \sum _{J=0}^1 K^{(k-I)}_{IJ} a_{k-I+J} - f_I^{(k-I)} \right ) = 0. \end {split} \label {eq:galerkinform2} \end {equation}
Diese Bedingung entspricht einer Zeile der Systemmatrix und der rechten Seite.
Zeile \(k\) der Systemmatrix, die Knoten \(k\) entspricht, hat damit einen Beitrag von
Element \(k\) (dessen linker Knoten der Knoten \(k\) ist) und Element \(k-1\) (dessen rechter
Knoten der Knoten \(k\) ist). Das Zusammenbauen der Systemmatrix wird im
Englischen oft als “assembly” bezeichnet.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 469 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> Wir formulieren das Beispielproblem (Poisson-Gleichung) hier noch
einmal im Rahmen der Formfunktionen. Dies ist ein Prozess, welcher drei Schritte
benötigt:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-7002x1'>
<!-- l. 472 --><p class='noindent'><span class='cmti-12'>Elementmatrix </span>und rechte Seite: Da alle Elemente identisch sind, sind
auch die einzelnen Elementmatrizen identisch. Zunächst wenden
wir wieder den Trick mit der partiellen Integration an, um die
Differenzierbarkeitsbedingung zu reduzieren. Man erhält den Ausdruck
\begin {equation} K_{IJ}^{(n)} = \left (N^{(n)}_{I}, \frac {\dif ^2 N^{(n)}_{J}}{\dif x^2} \right ) = -\left (\frac {\dif N^{(n)}_{I}}{\dif x}, \frac {\dif N^{(n)}_{J}}{\dif x}\right ), \end {equation}
der nur noch erste Ableitungen der Formfunktionen enthält. Diese
Ableitungen sind Konstanten, da die Formfunktionen linear sind,
Gl. \eqref{eq:linel1d}: \begin {align} \frac {\dif N^{(n)}_{0}}{\dif x} &amp;= -\frac {1}{\Delta x} \\ \frac {\dif N^{(n)}_{1}}{\dif x} &amp;= \frac {1}{\Delta x} \end {align}
</p><!-- l. 485 --><p class='noindent'>Damit erhält man die Elementsteifigkeitsmatrix \begin {equation} \t {K}^{(n)} = \frac {1}{\Delta x} \begin {pmatrix} 1 &amp; -1 \\ -1 &amp; 1 \end {pmatrix}, \label {eq:elmat1d} \end {equation}



die für alle Elemente identisch ist. Die rechte Seite für die Elemente wird
zu \begin {equation} \t {f}^{(n)} = \begin {pmatrix} (N^{(n)}_{0}, \rho )/\varepsilon \\ (N^{(n)}_{1}, \rho )/\varepsilon \end {pmatrix}. \end {equation}
Diese rechte Seite kann für die unterschiedlichen Elemente anders sein,
wenn \(\rho \) räumlich variiert.
</p></li>
<li class='enumerate' id='x1-7004x2'>Zusammenbauen der <span class='cmti-12'>Systemmatrix </span>und der rechten Seite (engl.
“assembly”): Die Regeln für das Zusammenbauen der Systemmatrix
ergeben sich aus der Galerkin-Bedingung, Gl. \eqref{eq:galerkinform2}.
Hierzu muss die \(2\times 2\) Elementmatrix auf die \(6\times 6\) Systemmatrix aufgespannt und
aufsummiert werden: Zeilen und Spalten der Elementmatrix entsprechen
Elementknoten und diese müssen jetzt auf die entsprechenden
globalen Knoten in der Systemmatrix abgebildet werden. In unserem
eindimensionalen Fall ist dies trivial. Man erhält \begin {equation} \t {K}\Delta x = \underbrace { \begin {pmatrix} 1 &amp; -1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ -1 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ \end {pmatrix} }_{\text {Element}\,n=0} + \underbrace { \begin {pmatrix} 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 1 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ \end {pmatrix} }_{\text {Element}\,n=1} + \cdots \end {equation}
und damit \begin {equation} \t {K} = \frac {1}{\Delta x}\begin {pmatrix} 1 &amp; -1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; -1 &amp; 2 &amp; -1 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; -1 &amp; 1 \\ \end {pmatrix}. \label {eq:sysmatform} \end {equation}
Der Vorteil der Formulierung mit Formfunktionen ist daher, dass man die
Elementmatrix für einen Elementtyp einmal ausrechnen muss, und dann
daraus einfach die Systemmatrix zusammenbauen kann. Der Zusammenbau
der rechten Seite folgt analog, ist aber einfacher da es sich um einen Vektor
handelt.
</li>
<li class='enumerate' id='x1-7006x3'>Randbedingungen: Wir haben im Rahmen der Formfunktionen noch
nicht über Randbedingungen gesprochen. Hierbei müssen die
entsprechenden Zeilen der Systemmatrix und der rechten Seite durch
die entsprechende Randbedingung ersetzt werden. Die Matrix \(\t {K}\) aus
Gl. \eqref{eq:sysmatform} ist ohne die entsprechenden Randbedingungen
nicht regulär.</li></ol>
</div>



<h2 class='likechapterHead'><a id='x1-80009.4'></a>Literaturverzeichnis</h2>

