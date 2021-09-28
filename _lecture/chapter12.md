---
layout: default
title: "Kapitel 12"
parent: Vorlesung
date: 2021-09-27
categories: lecture
author: Lars Pastewka
nav_order: 12
---

                                                                          
   <h2 class='chapterHead'><span class='titlemark'>Kapitel 12</span><br /><a id='x1-100012'></a>Zeitabhängige Probleme</h2>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 3 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> Viele Probleme denen wir begegnen, wie z.B. der bereits diskutierte
Diffusionsprozess, sind zeitabhängig. Wir haben bislang nur die stationäre Lösung
von linearen Problemen behandelt. Eine Behandlung des Anfangswertproblems,
welches die Zeitabhängigkeit <span class='cmti-12'>explizit </span>beinhaltet, benötigt entsprechende
Integrationsalgorithmen. </p></div>
   <h3 class='sectionHead'><span class='titlemark'>12.1   </span> <a id='x1-200012.1'></a>Anfangswertprobleme</h3>
<!-- l. 9 --><p class='noindent'>Typische zeitabhängige PDGLs haben die Form, \begin{equation} \frac{\partial u}{\partial t} + \mathcal{L} u(\v{r}, t) = f(\v{r}, t), \label{eq:boundary-value-problem} \end{equation}
wobei \(\mathcal{L}\) ein irgendwie gearteter Operator ist, z.b. \(\mathcal{L}=-\nabla \cdot D\nabla \) für Diffusionsprozesse, siehe
auch Gl. \eqref{eq:drift-diffusion-full}. Die dazugehörige stationäre Lösung,
die üblicherweise für \(t\to \infty \) erreicht wird, ist durch \(\mathcal{L} u=0\) gegeben. Wir haben in den
letzten Kapiteln gelernt, wie man eine solche stationäre Lösung für lineare
Probleme numerisch berechnen kann.
</p><!-- l. 20 --><p class='indent'>   Gleichung \eqref{eq:boundary-value-problem} ist ein <span class='cmti-12'>Anfangswertproblem </span>(engl.
“initial value problem”), weil man das Feld \(u(\v{r},t)\) zu einem Zeitpunkt (üblicherweise \(t=0\))
festlegen muss. Man integriert dann diese Anfangswertprobleme von diesem
Zeitpunkt in die Zukunft. Eine Auswahl solcher Zeitintegrationsalgorithmen (engl.
“time marching”) werden in diesem Kapitel besprochen. Bevor wir dazu kommen,
müssen wir jedoch zunächst noch einmal zur Diskretisierung der räumlichen
Ableitungen kommen.
</p><!-- l. 22 --><p class='noindent'>
</p>
   <h3 class='sectionHead'><span class='titlemark'>12.2   </span> <a id='x1-300012.2'></a>Räumliche Ableitungen</h3>
<!-- l. 24 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=f7743809-a4c4-47ee-aa5b-acc1012a8425'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=f7743809-a4c4-47ee-aa5b-acc1012a8425</span></a>
</p><!-- l. 26 --><p class='indent'>   Wir approximieren nun wiederum die (nun zeitabhängige) Funktion \(u(\v{r}, t)\) durch
eine Reihenentwicklung \(u_N(\v{r})\). Im Unterschied zu den vorhergehenden Kapiteln nehmen
wir nun an, dass die Koeffizienten nicht mehr konstant sondern zeitabhängig
sind. D.h. wir schreiben \begin{equation} u_N(\v{r}, t) = \sum _n a_n(t) \varphi _n(\v{r}). \end{equation}
Nun multiplizieren wir die gesamte zeitabhängige PDGL
Gl. \eqref{eq:boundary-value-problem} mit den Basisfunktionen \(\varphi _n(\v{r})\) der
Reihenentwicklung, \begin{equation} \frac{\partial }{\partial t} (\varphi _n, u_N) + (\varphi _n, \mathcal{L} u_N) = (\varphi _n, f), \end{equation}
In den vorhergehenden Kapiteln, haben wir bereits gelernt, wie wir die beiden
rechten Terme dieser Gleichung ausrechnen müssen, \begin{align} (\varphi _n, \mathcal{L} u_N) &amp;= \sum _k K_{nk} a_k(t),\\ (\varphi _n, f) &amp;= f_n(t) \end{align}
                                                                          

                                                                          
</p><!-- l. 45 --><p class='indent'>   wobei \(\t{K}\) die bekannte Systemmatrix ist und \(\v{f}(t)\) der (nun potentiell zeitabhängige)
Lastvektor. Nun ziehen wir die Zeitableitung in das Skalarprodukt hinein. Man
erhält damit \begin{equation} \sum _k M_{nk} \frac{\dif a_k}{\dif t} + \sum _k K_{nk} a_k(t) = f_n(t), \label{eq:discrete-time-dependent} \end{equation}
mit \(M_{nk}=(\varphi _n, \varphi _k)\), der <span class='cmti-12'>Massenmatrix</span>. Dies ist ein System gekoppelter <span class='cmti-12'>gewöhnlicher</span>
Differentialgleichungen. Wir haben also die PDGL durch die räumliche
Diskretisierung in ein <span class='cmti-12'>System </span>von GDGLs umgewandelt. Für eine
Fourier-Basis ist die Massenmatrix diagonal, für eine finite-Elemente
Basis ist diese dünnbesetzt aber nicht mehr diagonal. Wir können aber
Gl. \eqref{eq:discrete-time-dependent} formal von links mit \(\t{M}^{-1}\) multiplizieren und
erhalten, \begin{equation} \frac{\dif \v{a}}{\dif t} = - \t{M}^{-1} \cdot \t{K} \cdot \v{a}(t) + \t{M}^{-1} \cdot \v{f}(t) \equiv \v{g}(\v{a}(t), t). \label{eq:discrete-time-dependent-invmass} \end{equation}
</p>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 68 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Da sich die Massematrix in der Zeitentwicklung nicht ändert,
kann \(\t{M}^{-1}\) hier einmal vorberechnet werden. Da \(\t{M}\) üblicherweise dünnbesetzt
ist, kann es aber auch numerisch effizienter sein, in jedem Schritt das
entsprechende Gleichungssystem zu lösen. Dies liegt daran, dass die Inverse einer
dünnbesetzten Matrix nicht mehr dünnbesetzt ist. Damit braucht die
Multiplikation mit \(\t{M}^{-1}\) \(\sim N^2\) Operationen, während das Lösen des Gleichungssystems
nur \(\sim N\) Operationen benötigt. Die Anzahl der benötigten Operationen nennt man
die <span class='cmti-12'>Komplexität </span>eines Algorithmus. </p></div>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 72 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> Für die Basis der finite Elemente, die in Kapitel <span class='cmbx-12'>??</span> eingeführt wurde,
kann die Massematrix wieder als Summe über entsprechende Elementmatrizen \(\t{M}^{(n)}\)
ausgedrückt werden. Die Komponenten dieser Elementmassematrizen sind durch
\begin{equation} M^{(n)}_{IJ} = (N_I^{(n)}, N_J^{(n)}) \end{equation}
gegeben. Man erhält beispielsweise \begin{equation} \begin{split} M_{11}^{(0)} = M_{22}^{(0)} &amp;= \Delta x\Delta y \int _0^1 \dif \xi \int _0^{1-\xi } \dif \eta \, \xi ^2 \\ &amp;= \Delta x\Delta y \int _0^1 \dif \xi \, \xi ^2 (1-\xi ) \\ &amp;= \Delta x\Delta y/12, \end{split} \end{equation}
wobei die Integrationsgrenzen für das Integral über das Dreieck gewählt sind.
Die weiteren Integrale können entsprechend ausgeführt werden. Hiermit
bekommt man \begin{equation} \t{M}^{(n)} = \frac{\Delta x\Delta y}{24} \begin{pmatrix} 2 &amp; 1 &amp; 1 \\ 1 &amp; 2 &amp; 1 \\ 1 &amp; 1 &amp; 2 \end{pmatrix}. \end{equation}
Der Ausdruck ist für beide Elementmassematrizen identisch. Die globale
Systemmassematrix erhält man auf dem gleichen Weg wie die Systemmatrix. </p></div>
                                                                          

                                                                          
<!-- l. 111 --><p class='noindent'>
</p>
   <h3 class='sectionHead'><span class='titlemark'>12.3   </span> <a id='x1-400012.3'></a>Runge-Kutta Methoden</h3>
<!-- l. 113 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=13ac878b-710a-4f49-9653-acc1012a83f0'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=13ac878b-710a-4f49-9653-acc1012a83f0</span></a>
</p><!-- l. 115 --><p class='noindent'>
</p>
   <h4 class='subsectionHead'><span class='titlemark'>12.3.1   </span> <a id='x1-500012.3.1'></a>Euler-Verfahren</h4>
<!-- l. 117 --><p class='noindent'>Gleichung \eqref{eq:discrete-time-dependent-invmass} kann in der Zeit
propagiert werden. Wir nehmen an \(a_n(t)\) sei bekannt, dann können wir \(a_n(t+\Delta t)\) um \(t\) in eine
Taylorreihe entwickeln. Dies ergibt \begin{equation} \v{a}(t+\Delta t) = \v{a}(t)+\Delta t \v{g}(\v{a}(t),t)+\mathcal{O}(\Delta t^2), \label{eq:Euler} \end{equation}
wobei \(\mathcal{O}(\Delta t^2)\) für quadratische und höhere Terme steht, die hier vernachlässigt werden.
Gleichung \eqref{eq:Euler} kann direkt eingesetzt werden, um die Koeffizienten \(\v{a}\)
einen Schritt \(\Delta t\) in die Zukunft zu propagieren. Der Euler-Algorithmus ist
allerdings nicht sonderlich stabil und verlangt sehr kleine Zeitschritte
\(\Delta t\).
</p><!-- l. 126 --><p class='noindent'>
</p>
   <h4 class='subsectionHead'><span class='titlemark'>12.3.2   </span> <a id='x1-600012.3.2'></a>Heun-Verfahren</h4>
<!-- l. 128 --><p class='noindent'>Basierend auf der Euler Integration kann ein einfaches Verfahren mit höherer
Konvergenzordnung konstruiert werden. Die Konvergenzordnung besagt, wie sich
der Fehler verringert wenn die Schrittweite reduziert wird. Bei einem Verfahren
erster Ordnung reduziert sich der Fehler linear mit der Schrittweite, bei einem
Verfahren zweiter Ordnung quadratisch.
</p><!-- l. 130 --><p class='indent'>   Im Heun-Verfahren schätzt man zunächst den Funktionswert zum Zeitpunkt
\(t+\Delta t\) mit dem Euler-Verfahren ab. Man berechnet also \begin{equation} \tilde{\v{a}}(t+\Delta t) = \v{a}(t)+\Delta t \v{g}(\v{a}(t),t), \end{equation}
und benutzt dann die Trapezregel mit diesem abgeschätzten Funktionswert um
die Funktion einen Zeitschritt \(\Delta t\) zu integrieren: \begin{equation} \v{a}(t+\Delta t) = \v{a}(t)+\frac{\Delta t}{2} \left (\v{g}(\v{a}(t),t) + \v{g}(\tilde{\v{a}}(t+\Delta t),t)\right ) \end{equation}
Das Heun-Verfahren hat quadratische Konvergenzordnung. Verfahren die
zunächst Funktionswerte schätzen und dann korrigieren nennt man auch
<span class='cmti-12'>Predictor-Corrector </span>Verfahren.
</p><!-- l. 140 --><p class='noindent'>
</p>
   <h4 class='subsectionHead'><span class='titlemark'>12.3.3   </span> <a id='x1-700012.3.3'></a>Automatische Schrittweitenkontrolle</h4>
                                                                          

                                                                          
<!-- l. 142 --><p class='noindent'>Mit Hilfe zweier Integrationsverfahren mit unterschiedlicher Konvergenzordnung
lässt sich eine automatische Schrittweitenkontrolle realisieren, in der der
Zeitschritt \(\Delta t\) so angepasst wird, dass ein bestimmer Fehler nicht überschritten
wird. Die Verfahren sind insbesondere dann interessant, wenn die Berechnungen
der niedrigen Fehlerordnung in der Berechnung der höheren Fehlerordnung
wiederverwendet werden kann, wie dies z.B. bei dem Heun-Verfahren der Fall
ist.
</p><!-- l. 144 --><p class='indent'>   Für eine Kombination zweier Verfahren (z.B. Euler und Heun), ergibt sich
eine Abschätzung des Fehlers aus der Differenz der beiden Integrationen.
Unter Vorgabe einer globalen Fehlerschranke, kann dann der Zeitschritt
so angepasst werden, dass der Fehler immer unterhalb dieser Schranke
bleibt.
</p>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 146 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Sowohl die Euler-Integration als auch das Heun-Verfahren
gehören zur Klasse der <span class='cmti-12'>Runge-Kutta Methoden</span>. Es gibt eine ganze Reihe von
Runge-Kutta Methoden mit unterschiedlichen Konvergenzordnungen. Interessant
sind insbesondere Methoden mit automatische Schrittweitenkontrolle wie hier
beispielhaft beschrieben. In <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>scipy</span></span></span> sind insbesondere Verfahren mit den
Konvergenzordnungen \(2\)/\(3\) und \(4\)/\(5\) implementiert. Diese können über die Funktion
<a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html'><span class='cmtt-12'>scipy.integrate.solve_ivp</span></a> genutzt werden. </p></div>
<!-- l. 150 --><p class='noindent'>
</p>
   <h3 class='sectionHead'><span class='titlemark'>12.4   </span> <a id='x1-800012.4'></a>Stabilitätsanalyse</h3>
<!-- l. 152 --><p class='noindent'><a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=90f02a91-a31d-47f8-b085-acc101358727'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=90f02a91-a31d-47f8-b085-acc101358727</span></a>
</p><!-- l. 154 --><p class='indent'>   Zeitpropagationsverfahren werden bei zu hohen Zeitschritten instabil. Eine
Schrittweitenkontrolle ist eine automatisierte Methode solche Instabilitäten zu
verhindern.
</p><!-- l. 156 --><p class='indent'>   Um zu verstehen, warum solche Instabilitäten auftreten analysieren wir nun
beispielhaft die eindimensionale Diffusionsgleichung, \begin{equation} \frac{\partial c}{\partial t} = D \frac{\partial ^2 c}{\partial x^2}. \end{equation}
Eine Diskretisierung der räumlichen Ableitung mit linearen finiten Elementen
führt zu \begin{equation} \frac{\partial c}{\partial t} = \frac{D}{\Delta x^2} \left (c(x-\Delta x) - 2c(x) + c(x+\Delta x)\right ). \label{eq:fediff} \end{equation}
</p>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 166 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Eigenlich müsste auf der linken Seite von Gl. \eqref{eq:fediff} die
                                                                          

                                                                          
Massematrix auftauchen. Wir vernachlässigen diese hier und approximieren \(\t{M}=\t{1}\).
Diese Art diskretisierter Gleichung erhält man durch eine Diskretisierung mit der
Methode der finiten Differenzen. </p></div>
<!-- l. 170 --><p class='indent'>   Wir schreiben nun die Funktion \(c(x)\) als Entwicklung in eine Fourier-Basis, also
\begin{equation} c(x) = \sum _n c_n \exp (ik_nx). \end{equation}
Damit werden Term der Form \(c(x+\Delta x)\) zu \begin{equation} c(x+\Delta x,t) = \sum _n c_n(t) \exp \left [ik_n (x+\Delta x)\right ] = \sum _n \exp (ik_n \Delta x) c_n(t) \exp (ik_n x). \end{equation}
Wir schreiben nun Gl. \eqref{eq:fediff} als \begin{equation} \begin{split} \frac{\partial c_n}{\partial t} &amp;= \frac{D}{\Delta x^2} \left (\exp (-ik_n\Delta x) - 2 + \exp (ik_n\Delta x)\right ) c_n(t) \\ &amp;= \frac{2D}{\Delta x^2} \left (\cos (k_n\Delta x) - 1\right ) c_n(t), \end{split} \end{equation}
Diese Gleichung können wir aber analytisch für ein Zeitinterval \(\Delta t\) lösen,
\begin{equation} c_n(t+\Delta t) = c_n(t) \exp \left [\frac{2D}{\Delta x^2} \left (\cos (k_n\Delta x) - 1\right ) \Delta t \right ], \label{eq:cfl-exact} \end{equation}
wohingegen Euler Integration \begin{equation} c_n(t+\Delta t) \approx \left [1 + \frac{2D}{\Delta x^2} \left (\cos (k_n\Delta x) - 1\right ) \Delta t\right ] c_n(t) \label{eq:cfl-euler} \end{equation}
liefert. Der Wert des Terms \(\cos (k_n \Delta x)-1\) liegt zwischen \(-2\) und \(0\). D.h. wir können
Gl. \eqref{eq:cfl-exact} für beliebige \(\Delta t\) propagieren, ohne dass die Konzentration \(c_n(t)\)
zeitlich divergiert. Außer für \(k_n=0\) werden die Koeffizienten \(c_n(t)\) zeitlich kleiner.
</p><!-- l. 200 --><p class='indent'>   Für das Euler-Verfahren, Gl. \eqref{eq:cfl-euler}, ist dies aber nur den Fall,
wenn \begin{equation} \mu = \frac{D \Delta t}{\Delta x^2} &lt; \frac{1}{2}. \label{eq:diff-cfl} \end{equation}
Für \(\mu &gt;1/2\) wachsen einige der Koeffizienten \(c_n(t)\) mit \(t\) an, der Algorithmus wird instabil.
Die dimensionslose Zahl \(\mu \) nennt sich eine Courant-Friedrich-Lewy-(CFL)-Zahl und
die Bedingung Gl. \eqref{eq:diff-cfl} eine <span class='cmti-12'>CFL-Bedingung</span>. Die exakte
Form der CFL-Bedingung hängt von der PDGL und dem Algorithmus
ab.
</p>
   <div class='framedenv' id='shaded*-1'>
<!-- l. 208 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die CFL-Bedingung sagt, dass der maximale Zeitschritt
\begin{equation} \Delta t &lt; \frac{1}{2D} \Delta x^2 \end{equation}
von der räumlichen Diskretisierung \(\Delta x\) abhängt. D.h. wenn wir die räumliche
Diskretisierung feiner machen, müssen wir auch einen kleineren Zeitschritt
wählen. Eine Halbierung der räumlichen Diskretierung braucht einen Zeitschritt
der um ein viertel kleiner ist. Dies erhöht die Kosten einer Simulation der
gleichen Simulationsdauer um einen Faktor \(8\). Fein aufgelöste Simulationen
werden also schnell numerisch aufwändig. Für Verfahren mit automatischer
Schrittkontrolle passiert diese Anpassung des Zeitschritts natürlich automatisch. </p></div>
                                                                          

                                                                          
   <h2 class='likechapterHead'><a id='x1-900012.4'></a>Literaturverzeichnis</h2>
    
