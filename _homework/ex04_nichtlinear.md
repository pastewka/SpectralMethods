---
layout: default
title: "Übungsblatt 4 - Nichtlinear [31. März]"
parent: Übungsaufgaben
date: 2022-01-31
categories: homework
author: Lars Pastewka
nav_order: 4
---


<h2 class='chapterHead'><span class='titlemark'>Übungsblatt 4</span><br /><a id='x1-10004'></a>Nichtlineare finite Elemente</h2>
<div id='shaded*-1' class='framedenv'>
<!-- l. 11 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Abgabe von Arbeitsblatt 1 bis 4 ist verpflichtend und
konstituiert die Studienleistung der Veranstaltung Simulationstechniken.
Die Arbeitsblätter führen von der mathematischen Formulierung eines
Modellproblems hin zur numerischen Lösung dieses Problems und bauen
aufeinander auf. Zum Bestehen der Veranstaltung müssen auf jedem Blatt
mindestens 50% der erzielbaren Punkte erreicht werden.
</p><!-- l. 19 --><p class='indent'> Geben Sie bei allen Aufgaben die Lösungswege und Zwischenergebnisse mit
an. Das Endergebnis alleine ist nicht ausreichend! Wir empfehlen Ihnen die
Nutzung von Python und Jupyter-Notebooks. Sollten Sie ein Jupyter-Notebook
verwenden, dann können Sie dieses einfach direkt als Lösung bei uns einreichen.
In allen anderen Fällen erzeugen Sie bitte ein PDF und legen die numerischen
Codes als separate Datei dazu.
</p><!-- l. 26 --><p class='indent'> Sie werden durch die einzelnen Schritte der Modellimplementierung geleitet,
und wir geben Hinweise zur Implementierung. Es ist nicht zwingend notwendig,
diese 1-zu-1 zu verfolgen. Im Rahmen dieser Hinweise finden Sie Codeabschnitte,
die Sie verwenden können. Sie dürfen natürlich auch die Codebeispiele aus
dem Vorlesungsmaterial hier verwenden. </p></div>
<h3 class='sectionHead'><span class='titlemark'>4.1 </span> <a id='x1-20004.1'></a>Newton-Raphson-Verfahren</h3>
<!-- l. 36 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.1.1 </span> <a id='x1-30004.1.1'></a>Skalarwertige Funktionen</h4>
<!-- l. 38 --><p class='noindent'>
</p>
<h5 class='subsubsectionHead'><a id='x1-40004.1.1'></a>Implementierung eines Newton-Lösers</h5>
<!-- l. 39 --><p class='noindent'><span class='cmbx-12'>6 Punkte</span><br class='newline' />
</p><!-- l. 41 --><p class='indent'> Finden Sie eine Nullstelle für beliebige \(f(x)\) numerisch. Schreiben Sie dazu einen
Löser, der \(f(x) = 0\) mittels eines einfachen Newton-Iterationsverfahren lokal löst.
Nutzen Sie hierfür folgende Schnittstelle: </p><!-- l. 44 -->



<div id='listing-1' class='lstlisting'><span class='label'><a id='x1-4001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def newton(fun, x0, jac, tol=1e-6, maxiter=200, </span><br /><span class='label'><a id='x1-4002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>           callback=None): </span><br /><span class='label'><a id='x1-4003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-4004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    Newton solver expects scalar function fun and scalar </span><br /><span class='label'><a id='x1-4005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    initial value x0. </span><br /><span class='label'><a id='x1-4006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-4007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-4008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-4009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    fun : callable(x) </span><br /><span class='label'><a id='x1-4010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Scalar function of a scalar. </span><br /><span class='label'><a id='x1-4011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    x0 : float </span><br /><span class='label'><a id='x1-4012r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        Scalar initial value. </span><br /><span class='label'><a id='x1-4013r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    jac : callable(f, x) </span><br /><span class='label'><a id='x1-4014r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>        Scalar derivative of f at position x. </span><br /><span class='label'><a id='x1-4015r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    tol : float, optional </span><br /><span class='label'><a id='x1-4016r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        Tolerance (with respect to the zero value) for </span><br /><span class='label'><a id='x1-4017r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        convergence. </span><br /><span class='label'><a id='x1-4018r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    maxiter : int, optional </span><br /><span class='label'><a id='x1-4019r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>        Maximum number of Newton iterations. </span><br /><span class='label'><a id='x1-4020r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    callback : callable(x, **kwargs), optional </span><br /><span class='label'><a id='x1-4021r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>        Callback function to handle logging and convergence </span><br /><span class='label'><a id='x1-4022r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        stats. </span><br /><span class='label'><a id='x1-4023r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-4024r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    Returns </span><br /><span class='label'><a id='x1-4025r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>    ------- </span><br /><span class='label'><a id='x1-4026r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>    x : float </span><br /><span class='label'><a id='x1-4027r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>        Approximate local root. </span><br /><span class='label'><a id='x1-4028r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>    """</span>
</div>
<!-- l. 75 --><p class='noindent'>
</p>
<h5 class='subsubsectionHead'><a id='x1-50004.1.1'></a>Abbruch der Newton-Iteration</h5>
<!-- l. 77 --><p class='noindent'>Das Newton-Verfahren muss zu einem bestimmten Punkt abgebrochen werden.
Die Funktionssignatur sieht hierfür zwei Mechanismen vor: Der Parameter <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>tol</span></span></span>
gibt eine Toleranz \(\varepsilon \) vor, um den sich der Funktionswert von Null unterscheiden
darf. Das heißt die Schleife wird abgebrochen, wenn zum Zeitschritt \(i\) der
Funktionswert \(|f(x_i)|&lt;\varepsilon \) erfüllt ist. Um Situationen zu vermeiden, in denen keine
Konvergenz erreicht werden kann, sieht die Funktion noch eine maximale Anzahl
an Schritten (Parameter <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>maxiter</span></span></span>) vor. Die Iteration wird abgebrochen, wenn
eines dieser beiden Kriterien erfüllt ist. Da das Newton-Verfahren bei
Erfüllung des zweiten Kriterium nicht konvergiert ist, sollte hier ein Fehler
gemeldet werden. Dies kann z.B. über eine <a href='https://docs.python.org/3/library/exceptions.html'>Ausnahme</a> mit dem <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>raise</span></span></span>-Befehl
geschehen.
</p><!-- l. 79 --><p class='noindent'>
</p>
<h5 class='subsubsectionHead'><a id='x1-60004.1.1'></a>Callback</h5>
<!-- l. 81 --><p class='noindent'>Die o.g. Schnittstelle enthält eine sogenannte <span class='cmti-12'>Callback</span>-Funktion. Diese sollte der
Schnittstelle </p><!-- l. 82 -->
<div id='listing-2' class='lstlisting'><span class='label'><a id='x1-6001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def solver_callback(x): </span><br /><span class='label'><a id='x1-6002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>    """Solver callback for logging. </span><br /><span class='label'><a id='x1-6003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-6004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-6005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-6006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    x : float or np.ndarray </span><br /><span class='label'><a id='x1-6007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>        Current approximate solution </span><br /><span class='label'><a id='x1-6008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-6009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    ...</span>
</div>
<!-- l. 93 --><p class='indent'> gehorchen und, falls angegeben, einmal je Newton-Iteration mit aktueller
Näherungslösung \(x\) aufgerufen werden. Dieser Callback kann dann beispielsweise
über alle Zwischenlösungen Buch führen, aktuelle Konvergenzkriterien
ausgeben und Ihnen so bei der Fehlersuche helfen.
</p><!-- l. 98 --><p class='indent'> Implementieren Sie einen solchen Callback. Was genau angezeigt wird, bleibt
Ihnen überlassen.
</p><!-- l. 101 --><p class='noindent'>
</p>
<h5 class='subsubsectionHead'><a id='x1-70004.1.1'></a>Veranschaulichung an einem einfachen Polynom</h5>



<!-- l. 103 --><p class='noindent'>Testen Sie Ihren Newton-Löser zunächst an dem einfachen Polynom \(f(x)=x^3 + x^2 - x + 1\).
Wählen Sie hierfür verschiedene Startwerte. Für \(x_0 = 0.9\) und einem relativen
Konvergenzkriterium von \(\varepsilon =0.01\) könnnte die Ausgabe Ihres Callbacks, die besuchten
Näherungslösungen und der Konvergenzverlauf z.B. so aussehen:



</p>
<pre id='verbatim-1' class='verbatim'>
           X          FUN          JAC
           =          ===          ===
   9.000e-01    1.639e+00    3.230e+00
   3.926e-01    8.220e-01    2.475e-01
  -2.929e+00   -1.262e+01    1.888e+01
  -2.261e+00   -3.182e+00    9.810e+00
  -1.936e+00   -5.741e-01    6.375e+00
  -1.846e+00   -3.827e-02    5.533e+00
  -1.839e+00   -2.168e-04    5.471e+00
  -1.839e+00   -7.094e-09    5.470e+00
  -1.839e+00   -2.220e-16    5.470e+00
</pre>
<!-- l. 120 --><p class='nopar'> Finden Sie nun die Nullstelle im selben Polynom, indem Sie bei \(x_0 = -1.1\) starten. Zeigen
Sie die Schritte des Newton-Solvers für die Startpunkte \(x_0=0.9\) und \(x_0=-1.1\), in dem Sie die die
aktuelle Position \(x_i\) gegen die Nummer der Iteration \(i\) graphisch plotten. Was
beobachten Sie?
</p><!-- l. 137 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.1.2 </span> <a id='x1-80004.1.2'></a>Vektorwertige Funktionen</h4>
<!-- l. 138 --><p class='noindent'><span class='cmbx-12'>7 Punkte</span><br class='newline' />Verallgemeinern Sie die Implementierung Ihres Newton-Lösers auf vektorwertige
Funktionen \(\v {f}(\v {x})\). Die Funktion <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>fun</span></span></span> in der obigen Funktionssignatur muss nun einen
Vektor (also einen <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>numpy</span></span></span> Array) zurückliefern. Die Funktion <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>jac</span></span></span> liefert eine
Matrix. Es kann Sinn machen, für die vektorwertige Implementierung eine
separate Funktion zu implementieren. Nutzen Sie Ihren Solver um das Minimum
der Funktion \(f(x,y)=2\exp (-10(x^2+y^2)+x^2+y^2+x\) zu finden.
</p><!-- l. 141 --><p class='indent'> Bitte beantworten Sie im Rahmen der Lösung dieser Aufgabe folgende
Fragen: </p>
<ul class='itemize1'>
<li class='itemize'>Wir haben bislang über das Newton-Verfahren für die Lösung von
gekoppelten nichtlinearen Gleichungen gesprochen. Hier fragen wir nun
nach der Minimierung einer Funktion und fordern damit die Lösung
eines <span class='cmti-12'>Optimierungsproblems</span>. Wie passt dies zusammen?



</li>
<li class='itemize'>Welche spezielle Struktur
hat die Jacobi-Matrix für ein Optimierungsproblem? Wie nennt man
diese Matrix in diesem Fall auch?
</li>
<li class='itemize'>Sie müssen sich überlegen, wann die Newton-Iteration abgebrochen
wird. Was könnte hier ein vernünftiges Kriterium sein und warum?
</li>
<li class='itemize'>Wie sieht die Iterationen Ihres Lösers in einem zweidimensionalen Plot
in der \(x\)-\(y\)-Ebene, ausgehend von den Startpunkten \((1/2,1/2)\) und \((5,5)\), aus? Zeigen Sie
Hintergrund die Funktionswerte \(f(x,y)\) farbkodiert. Dies geht beispielsweise
mit der <span class='cmtt-12'>matplotlib</span>-Funktion <a href='https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html'><span class='cmtt-12'>pcolormesh</span></a> oder <a href='https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html'><span class='cmtt-12'>contour</span></a>.</li></ul>
<!-- l. 160 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>4.2 </span> <a id='x1-90004.2'></a>Poisson-Boltzmann-Gleichung</h3>
<!-- l. 162 --><p class='noindent'>Wir wenden uns nun der Lösung der eindimensionalen Poisson-Boltzmann-Gleichung
zu. In ihrer entdimensionalisierten Form lautet diese \begin {equation} \frac {\dif ^2 \Phi }{\dif x^2} = \sinh \Phi . \end {equation}
Ziel dieser Aufgabe ist es, einen Löser für diese nichtlineare Gleichung zu
implementieren.
</p><!-- l. 168 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.1 </span> <a id='x1-100004.2.1'></a>Diskretisierung</h4>
<!-- l. 169 --><p class='noindent'><span class='cmbx-12'>3 Punkte</span><br class='newline' />Zunächst muss die nichtlineare Poisson-Gleichung diskretisiert werden. Führen
Sie diese Diskretisierung eigenständig durch und leiten Sie alle Schritte
her. Unterscheiden Sie dabei zwischen der Formulierung der schwachen
Form (inklusive der Reduktion der Differenzierbarkeitsanforderungen), des
Galerkin-Ansatzes und des finite-Element Ansatzes. Nutzen Sie lineare Elemente
und reguläre Gitter. Dies entspricht exakt dem Vorgehen aus den vorherigen
Übungsblättern.
</p>
<div id='shaded*-1' class='framedenv'>



<!-- l. 172 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Wenn Sie finite Elemente ansetzen, dann reicht es die Basisfunktionen
mit Hilfe der Formfunktionen auszudrücken. Die exakten Ausdrücke für die
Formfunktionen spielen hier noch keine Rolle. </p></div>
<!-- l. 185 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.2 </span> <a id='x1-110004.2.2'></a>Numerische Quadratur des Residuums</h4>
<!-- l. 186 --><p class='noindent'><span class='cmbx-12'>2 Punkte</span><br class='newline' />Die finalen Gleichungen für das (diskrete) Residuum enthalten Terme der Form \((\varphi _k, \sinh \Phi _N)\),
wobei \(\varphi _k\) die Basisfunktionen und \(\Phi _N\) die approximierte Lösung der DGL ist. Diese
Terme sollen mit Hilfe der Gauß-Quadratur gelöst werden. Schreiben Sie die
Skalarprodukte/Integrale die nicht analytisch gelöst werden können mit Hilfe
der Art numerischer Quadratur. Fixieren Sie hier noch nicht die Anzahl der
Quadraturpunkte, sondern leiten Sie diese Gleichungen für eine beliebige Anzahl
Quadraturpunkte her.
</p><!-- l. 196 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.3 </span> <a id='x1-120004.2.3'></a>Tangentenmatrix</h4>
<!-- l. 197 --><p class='noindent'><span class='cmbx-12'>3 Punkte</span><br class='newline' />Leiten Sie die Tangentenmatrix her. Zeigen Sie, welche Form die Tangentenmatrix
in der linearisierten Form annimmt. Vergleichen Sie diese linearisierte
Tangentenmatrix mit der Systemmatrix des linearen Problems.
</p><!-- l. 208 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.4 </span> <a id='x1-130004.2.4'></a>Implementation des Residuumvektors und der Tangentenmatrix</h4>
<!-- l. 209 --><p class='noindent'><span class='cmbx-12'>4 Punkte</span><br class='newline' />Implementieren Sie den Residuumsvektor und die Tangentenmatrix. Wir
schlagen folgende Signaturen für die Funktionen vor, welche die Berechnung
implementieren: </p><!-- l. 211 -->



<div id='listing-3' class='lstlisting'><span class='label'><a id='x1-13001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def residual(potential_g, </span><br /><span class='label'><a id='x1-13002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>             potential_left=0, potential_right=0, </span><br /><span class='label'><a id='x1-13003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>             dx=1, nb_quad=2, linear=False): </span><br /><span class='label'><a id='x1-13004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Assemble global residual vector for a specific potential. </span><br /><span class='label'><a id='x1-13006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-13008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-13009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    potential_g : np.ndarray </span><br /><span class='label'><a id='x1-13010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Current potential on the nodes (the expansion </span><br /><span class='label'><a id='x1-13011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>        coefficients); the length of the array is the number </span><br /><span class='label'><a id='x1-13012r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        of nodes. </span><br /><span class='label'><a id='x1-13013r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    potential_left : float </span><br /><span class='label'><a id='x1-13014r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>        Left Dirichlet boundary condition. </span><br /><span class='label'><a id='x1-13015r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    potential_right : float </span><br /><span class='label'><a id='x1-13016r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        Right Dirichlet boundary condition. </span><br /><span class='label'><a id='x1-13017r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>    dx : float, optional </span><br /><span class='label'><a id='x1-13018r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>        Grid spacing. (Default: 1) </span><br /><span class='label'><a id='x1-13019r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    nb_quad : int, optional </span><br /><span class='label'><a id='x1-13020r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>        Number of quadrature points. (Default: 2) </span><br /><span class='label'><a id='x1-13021r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    linear : bool, optional </span><br /><span class='label'><a id='x1-13022r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        Linearize mass matrix. (Default: False) </span><br /><span class='label'><a id='x1-13023r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13024r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    Returns </span><br /><span class='label'><a id='x1-13025r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>    ------- </span><br /><span class='label'><a id='x1-13026r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>    residual_g : np.ndarray </span><br /><span class='label'><a id='x1-13027r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>        Residual vector (same shape as ‘potential_g‘) </span><br /><span class='label'><a id='x1-13028r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13029r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>    ... </span><br /><span class='label'><a id='x1-13030r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13031r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>def tangent(potential_g, </span><br /><span class='label'><a id='x1-13032r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>            potential_left=0, potential_right=0, </span><br /><span class='label'><a id='x1-13033r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>            dx=1, nb_quad=2, linear=False): </span><br /><span class='label'><a id='x1-13034r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13035r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>    Assemble global tangent matrix for a specific potential. </span><br /><span class='label'><a id='x1-13036r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13037r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-13038r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-13039r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>    potential_g : np.ndarray </span><br /><span class='label'><a id='x1-13040r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>        Current potential on the nodes (the expansion </span><br /><span class='label'><a id='x1-13041r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>        coefficients); the length of the array is the number </span><br /><span class='label'><a id='x1-13042r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>        of nodes </span><br /><span class='label'><a id='x1-13043r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'>    potential_left : float </span><br /><span class='label'><a id='x1-13044r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'>        Left Dirichlet boundary condition. </span><br /><span class='label'><a id='x1-13045r45'></a><span class='cmr-6'>45</span></span><span class='cmtt-10'>    potential_right : float </span><br /><span class='label'><a id='x1-13046r46'></a><span class='cmr-6'>46</span></span><span class='cmtt-10'>        Right Dirichlet boundary condition. </span><br /><span class='label'><a id='x1-13047r47'></a><span class='cmr-6'>47</span></span><span class='cmtt-10'>    dx : float, optional </span><br /><span class='label'><a id='x1-13048r48'></a><span class='cmr-6'>48</span></span><span class='cmtt-10'>        Grid spacing. (Default: 1) </span><br /><span class='label'><a id='x1-13049r49'></a><span class='cmr-6'>49</span></span><span class='cmtt-10'>    nb_quad : int, optional </span><br /><span class='label'><a id='x1-13050r50'></a><span class='cmr-6'>50</span></span><span class='cmtt-10'>        Number of quadrature points. (Default: 2) </span><br /><span class='label'><a id='x1-13051r51'></a><span class='cmr-6'>51</span></span><span class='cmtt-10'>    linear : bool, optional </span><br /><span class='label'><a id='x1-13052r52'></a><span class='cmr-6'>52</span></span><span class='cmtt-10'>        Linearize mass matrix. (Default: False) </span><br /><span class='label'><a id='x1-13053r53'></a><span class='cmr-6'>53</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13054r54'></a><span class='cmr-6'>54</span></span><span class='cmtt-10'>    Returns </span><br /><span class='label'><a id='x1-13055r55'></a><span class='cmr-6'>55</span></span><span class='cmtt-10'>    ------- </span><br /><span class='label'><a id='x1-13056r56'></a><span class='cmr-6'>56</span></span><span class='cmtt-10'>    tangent_gg : np.ndarray </span><br /><span class='label'><a id='x1-13057r57'></a><span class='cmr-6'>57</span></span><span class='cmtt-10'>        Tangent matrix (quadratic, number of rows and columns </span><br /><span class='label'><a id='x1-13058r58'></a><span class='cmr-6'>58</span></span><span class='cmtt-10'>        equal number of nodes) </span><br /><span class='label'><a id='x1-13059r59'></a><span class='cmr-6'>59</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13060r60'></a><span class='cmr-6'>60</span></span><span class='cmtt-10'>    ...</span>
</div>
<!-- l. 273 --><p class='indent'> Bei der Implementierung sollten Sie schrittweise vorgehen: Ignorieren Sie
zunächst die Dirichlet-Bedingungen und implementieren Sie lediglich den
Laplace-Operator. Schreiben Sie den Code für die Massematrix (der Term \(\sinh \Phi \) der
Differentialgleichung) erst dann, wenn der Laplace-Operator funktioniert. Die
Option <span class='cmbx-12'>linear </span>ist nützlich, um mit der linearisierten Lösung vergleichen zu
können.
</p>
<div id='shaded*-1' class='framedenv'>
<!-- l. 275 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Es ist wichtig, dass die Funktion <span class='cmtt-12'>tangent </span>die korrekte(n)
Ableitung(en) von <span class='cmtt-12'>residual </span>liefert. Dies kann numerisch getestet werden. So
können Sie z.B. numerisch über den Differenzenquotienten die Ableitung aus
der Funktion <span class='cmtt-12'>residual </span>berechnen und mit der analytischen Berechnung von
<span class='cmtt-12'>tangent </span>überprüfen. Im folgenden finden Sie einen Codeblock, der diese
numerische Berechnung der Ableitung für Sie macht: </p><!-- l. 277 -->
<div id='listing-4' class='lstlisting'><span class='label'><a id='x1-13061r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def check_tangent(value_g, residual_fun, tangent_fun, </span><br /><span class='label'><a id='x1-13062r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>                  eps=1e-6): </span><br /><span class='label'><a id='x1-13063r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13064r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    Check that tangent_fun is gives the derivative_fun </span><br /><span class='label'><a id='x1-13065r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    using finite differences. </span><br /><span class='label'><a id='x1-13066r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13067r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-13068r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-13069r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    value_g : numpy.nd_array </span><br /><span class='label'><a id='x1-13070r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Nodal value for which to check the derivative </span><br /><span class='label'><a id='x1-13071r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    residual_fun : callable </span><br /><span class='label'><a id='x1-13072r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        Function that takes the values and returns an array </span><br /><span class='label'><a id='x1-13073r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>        of residual values </span><br /><span class='label'><a id='x1-13074r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    tangent_fun : callable </span><br /><span class='label'><a id='x1-13075r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>        Function that takes the values and return the </span><br /><span class='label'><a id='x1-13076r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        tangent/jacobian matrix </span><br /><span class='label'><a id='x1-13077r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>    eps : float, optional </span><br /><span class='label'><a id='x1-13078r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>        Finite difference used for numeric computation of </span><br /><span class='label'><a id='x1-13079r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>        the derivative (Default: 1e-6) </span><br /><span class='label'><a id='x1-13080r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-13081r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    nb_nodes = len(value_g) </span><br /><span class='label'><a id='x1-13082r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>    tangent_gg = tangent_fun(value_g) </span><br /><span class='label'><a id='x1-13083r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>    numeric_tangent_gg = np.zeros_like(tangent_gg) </span><br /><span class='label'><a id='x1-13084r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    for i in range(nb_nodes): </span><br /><span class='label'><a id='x1-13085r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>        _value_g = value_g.copy() </span><br /><span class='label'><a id='x1-13086r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>        _value_g[i] += eps </span><br /><span class='label'><a id='x1-13087r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>        residual_plus_g = residual_fun(_value_g) </span><br /><span class='label'><a id='x1-13088r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>        _value_g[i] -= 2 * eps </span><br /><span class='label'><a id='x1-13089r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>        residual_minus_g = residual_fun(_value_g) </span><br /><span class='label'><a id='x1-13090r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>        numeric_tangent_gg[:, i] = ( </span><br /><span class='label'><a id='x1-13091r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>            residual_plus_g - residual_minus_g </span><br /><span class='label'><a id='x1-13092r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>            ) / (2 * eps) </span><br /><span class='label'><a id='x1-13093r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>    np.testing.assert_array_almost_equal( </span><br /><span class='label'><a id='x1-13094r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>        tangent_gg, numeric_tangent_gg) </span><br /><span class='label'><a id='x1-13095r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13096r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-13097r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'># Check if tangent is implemented correctly </span><br /><span class='label'><a id='x1-13098r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>for i in range(10): </span><br /><span class='label'><a id='x1-13099r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>    check_tangent(np.random.random(21)-0.5, residual, tangent)</span>
</div>
</div>
<!-- l. 328 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.5 </span> <a id='x1-140004.2.5'></a>Anwendung des Newton-Lösers</h4>
<!-- l. 329 --><p class='noindent'><span class='cmbx-12'>7 Punkte</span><br class='newline' /> </p><div id='shaded*-1' class='framedenv'>
<!-- l. 330 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Falls ihr Newton-Löser für multidimensionale Probleme
nicht funktioniert, dürfen Sie hier auch auf den Newton-Löser im Paket
<span class='cmtt-12'>scipy </span>zurückgreifen. Diesen finden Sie unter <a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html'><span class='cmtt-12'>scipy.optimize.newton</span></a>. </p></div>
<!-- l. 334 --><p class='indent'> Implementierung Sie die Lösung der nichtlinearen Poisson-Boltzmann-Gleichung
mit zwei Dirichlet Randbedingungen, jeweils am linken und rechten Rand. Zeigen
Sie die Lösungen der Gleichung für \(1\), \(2\) und \(3\) Gaußsche Quadraturpunkte für ein



System der Länge \(L=5\lambda \) und einem Potential von \(-1 k_B T/|e|\) auf der linken Elektrode und \(5 k_B T/|e|\) auf
der rechten Elektrode, wobei \(\lambda \) die Debye-Länge ist. Zeigen Sie eine Lösung mit \(\approx 10\)
und \(\approx 100\) Knoten. Vergleichen Sie diese Lösung der Lösung der linearisierten
Gleichung.
</p>
<div id='shaded*-1' class='framedenv'>
<!-- l. 336 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> </p>
<ul class='itemize1'>
<li class='itemize'>Die linearisierte Gleichung haben Sie im Rahmen von Übungsblatt 2
numerisch gelöst. Evtl. können Sie auf der Implementierung dieser
Lösung hier aufbauen.
</li>
<li class='itemize'>Sie müssen die Newton-Iteration von einem bestimmten Potential \(\Phi \)
starten. Was ist hier ein guter Startpunkt?
</li>
<li class='itemize'>Wenn Sie obige Funktionssignaturen verwandt haben, sollte der Aufruf des
Newton-Lösers ungefähr so aussehen: <!-- l. 341 -->
<div id='listing-5' class='lstlisting'><span class='label'><a id='x1-14001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>nb_nodes = 21  # Number of notes </span><br /><span class='label'><a id='x1-14002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>potential0_g = ...  # Initial condition </span><br /><span class='label'><a id='x1-14003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>potential_g = newton(residual, potential0_g, tangent)</span>

</div>
<!-- l. 346 --><p class='noindent'>Unter Umständen wollen Sie noch eine Callback-Funktion übergeben, um
die Konvergenz des Lösers zu verfolgen.
</p><!-- l. 348 --><p class='noindent'>Zusätzlich sollten Sie noch die Potentialrandbedingungen und zusätzliche
Parameter, wie z.B. die Anzahl der Quadraturpunkte, an die Funktionen
<span class='cmtt-12'>residual </span>und <span class='cmtt-12'>tangent </span>übergeben. Dies können Sie z.B. mit
<a href='https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions'>lambda-Ausdrücken</a> realisieren.</p></li></ul>
</div>
<!-- l. 361 --><p class='noindent'>
</p>
<h4 class='likesubsectionHead'><a id='x1-150004.2.5'></a>Punkte</h4>
<!-- l. 361 --><p class='noindent'>Sie können auf diesem Übungsblatt insgesamt 32 Punkte erzielen.
</p>

