---
layout: default
title: "Kapitel 11 [Jan. 10-16 (2022)]"
parent: Vorlesung
date: 2021-11-10
categories: lecture
author: Lars Pastewka
nav_order: 11
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 11</span><br /><a id='x1-100011'></a>Datenstrukturen &amp; Implementierung</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 5 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> In diesem Kapitel wird Anhand unseres Beispiels, der Lösung der
Poisson-Gleichung, gezeigt, wie nun ein einfacher Finite-Elemente-Löser in der
Programmiersprache <span class='cmcsc-10x-x-120'>P<span class='small-caps'>ython</span> </span>implementiert werden kann. Wir nehmen hier an, dass
die Ladungsdichte verschwindet. Wir berechnen also die räumliche Verteilung des
elektrostatischen Potentials unter entsprechenden Randbedingungen. Dies werden
wir nutzen, um die Kapazität eines Plattenkondensators auszurechnen. </p></div>
<h3 class='sectionHead'><span class='titlemark'>11.1 </span> <a id='x1-200011.1'></a>Beispielproblem</h3>
<!-- l. 11 --><p class='noindent'>Wir werden nun unser Beispielproblem aus den vorhergehenden Kapitel
weiterentwickeln und die Kapazität eines Plattenkondensators berechnen.
Hierfür nehmen wir eine verschwindende Ladungsdichte im Kondensator an, \(\rho =0\).
Die Poisson-Gleichung wird dann zur <span class='cmti-12'>Laplace-Gleichung</span>, \begin {equation} \nabla ^2 \Phi = 0. \end {equation}
Die Platten des Kondensators werden als metallisch angenommen, d.h. das
Potential auf den Kondensatorplatten ist konstant (siehe Abb. <a href='#x1-2001r1'>11.1<!-- tex4ht:ref: fig:plate-capacitor --></a>a). Dies wird
durch eine Dirichlet-Randbedingung abgebildet. Der Rest des Gebiets erhält
eine Neumann-Randbedingung, in der die Ableitung auf der Oberfläche
verschwindet.
</p>
<figure class='figure'>







<!-- l. 21 --><p class='noindent'> <img width='507' alt='PIC' height='323' src='Figures/capacitor-.png' /> <a id='x1-2001r1'></a>
<a id='x1-2002'></a>
</p><!-- l. 23 --><p class='noindent'>figure(a) Geometrie des in diesem Kapitel betrachteten Plattenkondensators.
Auf den Elektroden ist das Potential \(\Phi \) konstant. (b) Ausschnitt aus dem
Randbereich mit Integrationsbereich für die Herleitung der Intepretation
der Richtungsableitung am Rand.
</p>
<figcaption class='caption'><span class='id'>Abbildung 11.1: </span><span class='content'>(a) Geometrie des in diesem Kapitel betrachteten
Plattenkondensators. Auf den Elektroden ist das Potential \(\Phi \) konstant. (b)
Ausschnitt aus dem Randbereich mit Integrationsbereich für die Herleitung
der Intepretation der Richtungsableitung am Rand.
</span></figcaption><!-- tex4ht:label?: x1-2001r11.1 -->



</figure>
<!-- l. 27 --><p class='indent'> Im Kontext der Poisson- bzw. Laplace-Gleichung haben Richtungsableitungen am
Rand eine einfache Interpretation. Wir schauen uns ein kleines Volumenelement \(\Delta \Omega \)
am Rand des Gebiets an (siehe Abb. <a href='#x1-2001r1'>11.1<!-- tex4ht:ref: fig:plate-capacitor --></a>b). Integration der Poisson-Gleichung
über dieses Gebiet ergibt, \begin {equation} \int _{\Delta \Omega }\dif ^3 r\, \nabla ^2 \Phi = \int _{\partial \Delta \Omega }\dif ^2 r\, \nabla \Phi \cdot \hat {n}(\v {r}) = \frac {1}{\varepsilon } \int _{\Delta \Omega }\dif ^3 r\, \rho (\v {r}), \end {equation}
wobei die Integration über \(\partial \Delta \Omega \) entlang des in Abb. <a href='#x1-2001r1'>11.1<!-- tex4ht:ref: fig:plate-capacitor --></a>b gezeigten Pfades erfolgt.
Nun nehmen wir an, dass die beiden Seiten des Pfades, die senkrecht auf den
Rand des Gebiets stehen, vernachlässigbar gegenüber den beiden anderen
Seiten sind. Weiterhin nehmen wir an, dass in dem Gebiet lediglich eine
Oberflächenladung \(\sigma (\v {r})\) lebt. Damit erhält man \begin {equation} \int _{\partial \Delta \Omega }\dif ^2 r\, \nabla \Phi \cdot \hat {n}(\v {r}) = \frac {1}{\varepsilon } \int _{\Delta A}\dif ^2 r\, \sigma (\v {r}), \end {equation}
wobei \(\Delta A\) die Fläche des Randes des Simulationsgebiets ist, welcher in \(\Delta \Omega \) liegt. Nimmt
man nun an, dass der Raum außerhalb des Simulationsgebietes feldfrei ist, also \(\nabla \Phi =0\),
dann erhält man \begin {equation} \nabla \Phi \cdot \hat {n}(\v {r}) = \frac {\sigma (\v {r})}{\varepsilon }, \label {eq:surfacecharge} \end {equation}
die Richtungsableitung ergibt also die Oberflächenladung am Rand.
</p><!-- l. 51 --><p class='indent'> Die Feldfreiheit außerhalb unserer Simulationsdomäne ist exakt nur an
den Elektroden erfüllt. Diese sind metallisch und daher per Definition
feldfrei. (Ein Feld innerhalb eines idealen Metalls führt sofort zu einer
Umordnung von Ladungen, die dieses Feld dann kompensieren.) D.h.
wir können Gl. \eqref{eq:surfacecharge} nutzen, um die auf den
Kondensatorplatten induzierte Ladung zu berechnen. Zusammen mit
dem durch die Dirichlet-Randbedingungen vorgegebenen Potential, kann
dies zur Berechnung der Kapazität auf den Kondensatorplatten genutzt
werden.
</p><!-- l. 53 --><p class='indent'> Auf der anderen Seite heißt die implizite Neumann-Randbedingung \(\nabla \Phi \cdot \hat {n}=0\), dass
unsere Simulation unter Bedingungen durchgeführt wird, in denen der Rand
ladungsfrei ist aber außerhalb der Simulationsdomäne das Feld verschwindet.
Dies ist eine künstliche Bedingung, die Fehler verursachen kann. Man muss
also sicherstellen, dass die Simulationsdomäne in Richtung parallel zu
den Kondensatorplatten groß genug ist, um die Streufelder am Rand den
Kondensators vernünftig zu erfassen.
</p>
<h3 class='sectionHead'><span class='titlemark'>11.2 </span> <a id='x1-300011.2'></a>Datenstrukturen</h3>
<!-- l. 57 --><p class='noindent'>Die zentrale Datenstruktur für numerische Anwendungen ist der multidimensionale
Array, <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>numpy.ndarray</span></span></span>, der <a href='https://numpy.org/'><span class='cmtt-12'>numpy</span></a>-Bibliothek. Multidimensionale Arrays halten
Speicher für eine gewisse Menge an Einträgen vor. (Diese Einträge werden
auch <span class='cmti-12'>Elemente </span>genannt, aber um diese nicht mit den finite Elementen
durcheinander zu werden, werden sie in diesem Dokument durchgehend Einträge
genannt.) Ein mit Nullen gefülltes Array der Länge \(10\) (also \(10\) Einträge) erhält



man durch </p><!-- l. 58 -->
<div class='lstlisting' id='listing-1'><span class='label'><a id='x1-3001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>import numpy as np </span><br />
<span class='label'><a id='x1-3002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>a = np.zeros(10)</span>
</div>
<!-- l. 62 --><p class='indent'> Diese Array hat die <span class='cmti-12'>Dimension</span> \(1\). Der mehrdimensionale Charakter der Arrays
äußert sich darin, dass die Arrays implizit eine Abbildung von mehreren
Koordinaten auf einen lineare Index, wie z.B. durch Gl. \eqref{eq:linindex} und
Gl. \eqref{eq:linindexel} gegeben, implementieren. Einen zweidimensionalen
Array bekommt man z.B. durch </p><!-- l. 63 -->
<div class='lstlisting' id='listing-2'><span class='label'><a id='x1-3003r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>b = np.zeros([2, 5])</span>
</div>
<!-- l. 66 --><p class='indent'> Man kann nun jeweils auf die Array-Einträge zugreifen, z.B. </p><!-- l. 67 -->
<div class='lstlisting' id='listing-3'><span class='label'><a id='x1-3004r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>a[6] </span><br />
<span class='label'><a id='x1-3005r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>b[1, 1]</span>
</div>
<!-- l. 71 --><p class='indent'> Beide Befehle greifen auf Eintrag \(6\) des zu Grunde liegenden Speicherbereichs
zu. Ein natürlicher Einsatz der multidimensionalen Arrays ist die
Repräsentation von Vektoren (\(1\)-dimensionale Arrays) oder Martrizen
(\(2\)-dimensionale Arrays).
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 75 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Aussage, dass </p><!-- l. 77 -->
<div class='lstlisting' id='listing-4'><span class='label'><a id='x1-3006r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>a[6] </span><br />
<span class='label'><a id='x1-3007r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>b[1, 1]</span>
</div>
<!-- l. 81 --><p class='indent'> in dem o.g. Beispiel auf den gleichen Eintrag des zu Grunde liegenden
Speicherbereichs zugreift, hängt von der Speicherreihenfolge (engl. “storage
order”) ab. Sie gilt nur dann, wenn der letzte Index kompakt im Speicher
steht. Diese Speicherreihenfolge nennt sich “row major”, weil in einem
zweidimensionalen Array, also einer Matrix, die Zeilen (engl. “row”) kompakt im
Speicher stehen. Ist der erste Index der kompakte spricht man von “column
major”. In <span class='cmtt-12'>numpy </span>heißt “row major” auch “C-continguous” und “column major”
heißt “F-contiguous”. Dies kommt daher, dass in der Programmiersprache <span class='cmtt-12'>C </span>die
Speicherreihenfolge “row major” und in der Programmiersprache <span class='cmtt-12'>Fortran </span>die
Speicherreihenfolge “column major” ist. Arrays in <span class='cmtt-12'>numpy </span>sind standardmäßig
“column major”, andere Speicherreihenfolgen werden aber unterstützt und
kommen auch vor. </p></div>



<!-- l. 84 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>11.3 </span> <a id='x1-400011.3'></a>Initialisierung</h3>
<!-- l. 86 --><p class='noindent'>Die Beispielimplementierungen folgen einfache Regeln für lesbaren Computercode.
Dieser sollte immer so geschrieben sein, dass eine dritte Person diesen lesen und
wiederverwenden kann. Wir werden daher...
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-4002x1'>...ausschließlich englische Sprache verwenden.
</li>
<li class='enumerate' id='x1-4004x2'>...Variablennamen ausschreiben und keine Symbole als Variablennamen
verwenden (also z.B. <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>potential</span></span></span> und nicht das ausgeschriebene Symbol
<span class='obeylines-h'><span class='verb'><span class='cmtt-12'>phi</span></span></span> als Name).
</li>
<li class='enumerate' id='x1-4006x3'>...Array-Variablen mit einem Suffix versehen, der den Typ der Indices
anzeigt (z.B. <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>potential_xy</span></span></span> um anzuzeigen, dass es zwei Indices gibt
die den Positionen \(x\) und \(y\) entsprechen).
</li>
<li class='enumerate' id='x1-4008x4'>...den Code
mit Kommentarblöcken und <span class='cmtt-12'>Python </span><a href='https://www.python.org/dev/peps/pep-0257/'>Docstrings</a> dokumentieren. Wir
empfehlen den <a href='https://numpydoc.readthedocs.io/en/latest/format.html'>numpydoc</a>-Standard für Docstrings.</li></ol>
<!-- l. 93 --><p class='noindent'>In dieser Implementierung verwenden wir explizite Schleifen, um die Lesbarkeit des
Codes zu verbessern. Der Code kann durch Verwenden von <span class='cmcsc-10x-x-120'><span class='small-caps'>numpy</span></span>-Operationen
noch vektorisiert werden.
</p><!-- l. 97 --><p class='indent'> Zunächst müssen wir den Code initialisieren und festlegen, wieviele
Gitterpunkte wir verwenden wollen. Wir definieren die Variablen </p><!-- l. 98 -->
<div class='lstlisting' id='listing-5'><span class='label'><a id='x1-4009r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'># Grid size, number of nodes </span><br />
<span class='label'><a id='x1-4010r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>nb_nodes = 32, 32 </span><br />
<span class='label'><a id='x1-4011r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>Nx, Ny = nb_nodes</span>
</div>
<!-- l. 103 --><p class='indent'> Wir legen nun auch noch fest, über welchen Bereich sich die beiden
Elektroden des Kondensators erstrecken sollen: </p><!-- l. 104 -->
<div class='lstlisting' id='listing-6'><span class='label'><a id='x1-4012r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'># Top capacitor plate </span><br />
<span class='label'><a id='x1-4013r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>top_left = Nx//4 </span><br />
<span class='label'><a id='x1-4014r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>top_right = 3*Nx//4-1 </span><br />
<span class='label'><a id='x1-4015r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>top_potential = 1 </span><br />
<span class='label'><a id='x1-4016r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-4017r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'># Bottom capacitor plate </span><br />
<span class='label'><a id='x1-4018r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>bottom_left = Nx//4 </span><br />
<span class='label'><a id='x1-4019r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>bottom_right = 3*Nx//4-1 </span><br />
<span class='label'><a id='x1-4020r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>bottom_potential = -1</span>



</div>
<!-- l. 115 --><p class='indent'> Der Bereich wird hier mit Knotenindices angegeben. Weiterhin benötigen
wir noch die Elementmatrix, Gl. \eqref{eq:elmat2d}, die wir in einem
<span class='obeylines-h'><span class='verb'><span class='cmtt-12'>numpy.ndarray</span></span></span> speichern: </p><!-- l. 116 -->
<div class='lstlisting' id='listing-7'><span class='label'><a id='x1-4021r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'># Element matrix, index l indicates element-local node </span><br />
<span class='label'><a id='x1-4022r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>element_matrix_ll = np.array([[1, -1/2, -1/2], </span><br />
<span class='label'><a id='x1-4023r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>                              [-1/2, 1/2, 0], </span><br />
<span class='label'><a id='x1-4024r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>                              [-1/2, 0, 1/2]])</span>
</div>
<!-- l. 122 --><p class='indent'> Der Suffix <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>_ll</span></span></span> bezeichnet hier, dass es zwei Indices gibt (der Array ist
zweidimensional), die beide einen lokalen Elementknoten bezeichnen. Wir
initialisieren weiterhin die Systemmatrix und die rechte Seite, zunächst mit
Nullen: </p><!-- l. 123 -->
<div class='lstlisting' id='listing-8'><span class='label'><a id='x1-4025r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'># System matrix, index g indicates global node </span><br />
<span class='label'><a id='x1-4026r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>system_matrix_gg = np.zeros([Nx*Ny, Nx*Ny]) </span><br />
<span class='label'><a id='x1-4027r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-4028r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'># Right hand side </span><br />
<span class='label'><a id='x1-4029r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>rhs_g = np.zeros(Nx*Ny)</span>
</div>
<!-- l. 130 --><p class='indent'> Der Suffix <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>_g</span></span></span> bezeichnet hier den Index des globalen Knoten. Die Variable
<span class='obeylines-h'><span class='verb'><span class='cmtt-12'>rhs_g</span></span></span> enthält den Vektor \(\v {f}\) und benötigt daher nur einen Index. Die Variable
<span class='obeylines-h'><span class='verb'><span class='cmtt-12'>system_matrix_gg</span></span></span> beinhaltet die Systemmatrix \(\t {K}\) und braucht daher zwei globale
Knotenindices.
</p><!-- l. 132 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>11.4 </span> <a id='x1-500011.4'></a>Systemmatrix</h3>
<!-- l. 134 --><p class='noindent'><a href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=a6057226-fa98-45ed-a69f-acc000e9f3e7' class='url'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=a6057226-fa98-45ed-a69f-acc000e9f3e7</span></a>
</p><!-- l. 136 --><p class='indent'> Kern des Simulationsprogramms ist der Aufbau der Systemmatrix. In diesem
Abschnitt wird dies durch explizite Schleifen realisiert. Im nächsten Abschnitt
wird gezeigt, wie dies mit speziellen <span class='cmtt-12'>numpy</span>-Befehlen kompakter (und effizienter),
aber weniger transparent gestaltet werden kann.
</p><!-- l. 138 --><p class='indent'> Zunächst definieren wir eine Funktion, die aus Knotenkoordinaten den
globalen Knotenindex macht: </p><!-- l. 139 -->
<div class='lstlisting' id='listing-9'><span class='label'><a id='x1-5001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def node_index(i, j, nb_nodes): </span><br />
<span class='label'><a id='x1-5002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    Turn node coordinates (i, j) into their global node index. </span><br />
<span class='label'><a id='x1-5004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-5006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-5007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    i : int </span><br />
<span class='label'><a id='x1-5008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>        x-coordinate (integer) of the node </span><br />
<span class='label'><a id='x1-5009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    j : int </span><br />
<span class='label'><a id='x1-5010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        y-coordinate (integer) of the node </span><br />
<span class='label'><a id='x1-5011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-5012r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-5013r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5014r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-5015r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-5016r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>    g : int </span><br />
<span class='label'><a id='x1-5017r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        Global node index </span><br />
<span class='label'><a id='x1-5018r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5019r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-5020r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    return i + Nx*j</span>
</div>
<!-- l. 161 --><p class='indent'> Dies nutzen wir in einer weiteren Hilfsfunktion, die die Elementmatrix zu der
Systemmatrix addiert. Hierzu muss zunächst die Elementmatrix auf die
Systemmatrix aufgespannt werden. Die Funktion sieht folgendermaßen aus:
</p><!-- l. 162 -->
<div class='lstlisting' id='listing-10'><span class='label'><a id='x1-5021r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def add_element_matrix(system_matrix_gg, element_matrix_ll, </span><br />
<span class='label'><a id='x1-5022r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>                       global_node_indices): </span><br />
<span class='label'><a id='x1-5023r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5024r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    Add element matrix to global system matrix. </span><br />
<span class='label'><a id='x1-5025r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5026r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-5027r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-5028r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    system_matrix_gg : array_like </span><br />
<span class='label'><a id='x1-5029r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>        N x N system matrix where N is the number of global </span><br />
<span class='label'><a id='x1-5030r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        nodes. This matrix will be modified by this function. </span><br />
<span class='label'><a id='x1-5031r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    element_matrix_ll : array_like </span><br />
<span class='label'><a id='x1-5032r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        n x n element matrix where n is the number of local </span><br />
<span class='label'><a id='x1-5033r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>        nodes </span><br />
<span class='label'><a id='x1-5034r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    global_node_indices : list of int </span><br />
<span class='label'><a id='x1-5035r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>        List of length n that contains the global node </span><br />
<span class='label'><a id='x1-5036r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        indices for the local node index that corresponds to </span><br />
<span class='label'><a id='x1-5037r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        the list position. </span><br />
<span class='label'><a id='x1-5038r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5039r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    assert element_matrix_ll.shape == \ </span><br />
<span class='label'><a id='x1-5040r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>        (len(global_node_indices), len(global_node_indices)) </span><br />
<span class='label'><a id='x1-5041r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    for i in range(len(global_node_indices)): </span><br />
<span class='label'><a id='x1-5042r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        for j in range(len(global_node_indices)): </span><br />
<span class='label'><a id='x1-5043r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>            system_matrix_gg[global_node_indices[i], </span><br />
<span class='label'><a id='x1-5044r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>                             global_node_indices[j]] += \ </span><br />
<span class='label'><a id='x1-5045r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>                element_matrix_ll[i, j]</span>



</div>
<!-- l. 189 --><p class='indent'> Die <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>assert</span></span></span>-Anweisung ist hier ein Wächter, der darauf achtet, dass die lokale
Elementmatrix und der Array <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>global_node_indices</span></span></span> die gleiche Länge haben.
Die beiden <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>for</span></span></span>-Schleifen laufen dann über alle Einträge der Elementmatrix.
Der Ausdruck <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>global_node_indices[i]</span></span></span> liefert dann den globalen Knotenindex,
der zu dem lokalen Knotenindex der Elementmatrix gehört. Der Zusammenbau
der Systemmatrix erfolgt dann über einen Aufruf dieser Hilfsmethode pro
Element: </p><!-- l. 190 -->
<div class='lstlisting' id='listing-11'><span class='label'><a id='x1-5046r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def assemble_system_matrix(element_matrix_ll, nb_nodes): </span><br />
<span class='label'><a id='x1-5047r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5048r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    Assemble system matrix from the element matrix </span><br />
<span class='label'><a id='x1-5049r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5050r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-5051r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-5052r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    element_matrix_ll : array_like </span><br />
<span class='label'><a id='x1-5053r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>        3 x 3 element matrix </span><br />
<span class='label'><a id='x1-5054r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-5055r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-5056r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5057r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-5058r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-5059r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    system_matrix_gg : numpy.ndarray </span><br />
<span class='label'><a id='x1-5060r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>        System matrix </span><br />
<span class='label'><a id='x1-5061r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5062r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5063r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-5064r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    Mx, My = Nx-1, Ny-1 # number of boxes </span><br />
<span class='label'><a id='x1-5065r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5066r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    # System matrix </span><br />
<span class='label'><a id='x1-5067r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>    system_matrix_gg = np.zeros([Nx*Ny, Nx*Ny]) </span><br />
<span class='label'><a id='x1-5068r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5069r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    # Construct system matrix </span><br />
<span class='label'><a id='x1-5070r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>    for l in range(Mx): </span><br />
<span class='label'><a id='x1-5071r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>        for m in range(My): </span><br />
<span class='label'><a id='x1-5072r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>            # Element (0) </span><br />
<span class='label'><a id='x1-5073r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>            n0 = node_index(l, m, nb_nodes) </span><br />
<span class='label'><a id='x1-5074r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>            n1 = node_index(l+1, m, nb_nodes) </span><br />
<span class='label'><a id='x1-5075r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>            n2 = node_index(l, m+1, nb_nodes) </span><br />
<span class='label'><a id='x1-5076r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>            add_element_matrix(system_matrix_gg, </span><br />
<span class='label'><a id='x1-5077r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>                               element_matrix_ll, </span><br />
<span class='label'><a id='x1-5078r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>                               [n0, n1, n2]) </span><br />
<span class='label'><a id='x1-5079r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5080r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>            # Element (1) </span><br />
<span class='label'><a id='x1-5081r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'>            n0 = node_index(l+1, m+1, nb_nodes) </span><br />
<span class='label'><a id='x1-5082r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>            n1 = node_index(l, m+1, nb_nodes) </span><br />
<span class='label'><a id='x1-5083r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>            n2 = node_index(l+1, m, nb_nodes) </span><br />
<span class='label'><a id='x1-5084r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>            add_element_matrix(system_matrix_gg, </span><br />
<span class='label'><a id='x1-5085r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>                               element_matrix_ll, </span><br />
<span class='label'><a id='x1-5086r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>                               [n0, n1, n2]) </span><br />
<span class='label'><a id='x1-5087r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5088r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'>    return system_matrix_gg</span>
</div>
<!-- l. 235 --><p class='indent'> Hier laufen die beiden <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>for</span></span></span>-Schleifen über die einzelnen Kästen.
Die Schleife über die beiden Elemente pro Kasten ist explizit als zwei
Aufrufe zu <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>add_element_matrix</span></span></span> geschrieben. Die Variablen <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>n0</span></span></span>, <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>n1</span></span></span> und <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>n2</span></span></span>
enthalten die globalen Knotenindices, die die Ecken des jeweiligen Elements
beschreiben.
</p><!-- l. 237 --><p class='indent'> <a href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=de8eb963-78bb-4fd1-8387-acc000eee353' class='url'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=de8eb963-78bb-4fd1-8387-acc000eee353</span></a>
</p><!-- l. 239 --><p class='indent'> Die nun aufgebaute Systemmatrix hat (implizit) Neumann-Randbedingungen
mit \(\nabla \Phi \cdot \hat {n}(\v {r})=0\) auf dem Rand. Wir müssen nun noch die Dirichlet-Bedingungen für die
Elektroden hinzufügen. Hierzu ersetzen wir Zeilen der Systemmatrix und die
entsprechenden Einträge des Lastvektors: </p><!-- l. 240 -->
<div class='lstlisting' id='listing-12'><span class='label'><a id='x1-5089r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def capacitor_bc(system_matrix_gg, rhs_g, </span><br />
<span class='label'><a id='x1-5090r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>                 top_left, top_right, top_potential, </span><br />
<span class='label'><a id='x1-5091r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>                 bottom_left, bottom_right, bottom_potential, </span><br />
<span class='label'><a id='x1-5092r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>                 nb_nodes): </span><br />
<span class='label'><a id='x1-5093r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5094r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    Set boundary conditions for the parallel plate capacitor. </span><br />
<span class='label'><a id='x1-5095r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5096r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-5097r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-5098r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>    system_matrix_gg : numpy.ndarray </span><br />
<span class='label'><a id='x1-5099r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>        System matrix. The system matrix is modified by a call </span><br />
<span class='label'><a id='x1-5100r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        to this function </span><br />
<span class='label'><a id='x1-5101r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    rhs_g : numpy.ndarray </span><br />
<span class='label'><a id='x1-5102r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>        Right-hand side vector. The right-hand side vector is </span><br />
<span class='label'><a id='x1-5103r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>        modified by a call to this function. </span><br />
<span class='label'><a id='x1-5104r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>    top_left : int </span><br />
<span class='label'><a id='x1-5105r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        Leftmost node of the top electrode </span><br />
<span class='label'><a id='x1-5106r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    top_right : int </span><br />
<span class='label'><a id='x1-5107r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>        Rightmost node of the top electrode </span><br />
<span class='label'><a id='x1-5108r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    top_potential : float </span><br />
<span class='label'><a id='x1-5109r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>        Electrostatic potential of the top electrode </span><br />
<span class='label'><a id='x1-5110r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>    bottom_left : int </span><br />
<span class='label'><a id='x1-5111r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>        Leftmost node of the bottom electrode </span><br />
<span class='label'><a id='x1-5112r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    bottom_right : int </span><br />
<span class='label'><a id='x1-5113r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>        Rightmost node of the bottom electrode </span><br />
<span class='label'><a id='x1-5114r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>    bottom_potential : float </span><br />
<span class='label'><a id='x1-5115r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>        Electrostatic potential of the bottom electrode </span><br />
<span class='label'><a id='x1-5116r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-5117r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-5118r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-5119r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-5120r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>    # Dirichlet boundary conditions for top plate </span><br />
<span class='label'><a id='x1-5121r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>    for i in range(top_left, top_right+1): </span><br />
<span class='label'><a id='x1-5122r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>        n = node_index(i, Ny-1, nb_nodes) </span><br />
<span class='label'><a id='x1-5123r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>        mat_g = np.zeros(Nx*Ny) </span><br />
<span class='label'><a id='x1-5124r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'>        mat_g[n] = 1 </span><br />
<span class='label'><a id='x1-5125r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>        system_matrix_gg[n] = mat_g </span><br />
<span class='label'><a id='x1-5126r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>        rhs_g[n] = top_potential </span><br />
<span class='label'><a id='x1-5127r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5128r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>    # Dirichlet boundary conditions for bottom plate </span><br />
<span class='label'><a id='x1-5129r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>    for i in range(bottom_left, bottom_right+1): </span><br />
<span class='label'><a id='x1-5130r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>        n = node_index(i, 0, nb_nodes) </span><br />
<span class='label'><a id='x1-5131r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'>        mat_g = np.zeros(Nx*Ny) </span><br />
<span class='label'><a id='x1-5132r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'>        mat_g[n] = 1 </span><br />
<span class='label'><a id='x1-5133r45'></a><span class='cmr-6'>45</span></span><span class='cmtt-10'>        system_matrix_gg[n] = mat_g </span><br />
<span class='label'><a id='x1-5134r46'></a><span class='cmr-6'>46</span></span><span class='cmtt-10'>        rhs_g[n] = bottom_potential</span>
</div>
<!-- l. 289 --><p class='indent'> <a href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=cac3d182-6a34-4c9c-9b6c-acc000f19238' class='url'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=cac3d182-6a34-4c9c-9b6c-acc000f19238</span></a>
</p><!-- l. 291 --><p class='indent'> Der gesamte Simulationscode enthält nun Aufrufe dieser Funktionen,
gefolgt von der numerischen Lösung des linearen Gleichungssystems:
</p><!-- l. 292 -->
<div class='lstlisting' id='listing-13'><span class='label'><a id='x1-5135r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'># Construct system matrix </span><br />
<span class='label'><a id='x1-5136r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>system_matrix_gg = assemble_system_matrix(element_matrix_ll, </span><br />
<span class='label'><a id='x1-5137r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>                                          nb_nodes) </span><br />
<span class='label'><a id='x1-5138r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5139r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'># Boundary conditions </span><br />
<span class='label'><a id='x1-5140r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>capacitor_bc(system_matrix_gg, rhs_g, </span><br />
<span class='label'><a id='x1-5141r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>             top_left, top_right, top_potential, </span><br />
<span class='label'><a id='x1-5142r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>             bottom_left, bottom_right, bottom_potential, </span><br />
<span class='label'><a id='x1-5143r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>             nb_nodes) </span><br />
<span class='label'><a id='x1-5144r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-5145r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'># Solve system of linear equations </span><br />
<span class='label'><a id='x1-5146r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>potential_g = np.linalg.solve(system_matrix_gg, rhs_g)</span>
</div>
<!-- l. 306 --><p class='indent'> Die Variable <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>potential_g</span></span></span> enthält nun die Werte des elektrostatischen
Potentials auf den Knoten.
</p><!-- l. 308 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>11.5 </span> <a id='x1-600011.5'></a>Visualisierung</h3>
<!-- l. 310 --><p class='noindent'><a href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=61f0f7d8-e311-4dcf-9f01-acc000f4b8d4' class='url'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=61f0f7d8-e311-4dcf-9f01-acc000f4b8d4</span></a>



</p><!-- l. 312 --><p class='indent'> Das Ergebnis der Rechnung kann mit Hilfe der <a href='https://matplotlib.org/'><span class='cmtt-12'>matplotlib</span></a>-Bibliothek
visualisiert werden. Die Funktion <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>matplotlib.pyplot.tripcolor</span></span></span> kann Daten auf
einem triangulierten 2D-Gitter darstellen. Der folgende Codeblock visualisiert das
Ergebnis der Simulation mit Hilfe dieser Funktion. </p><!-- l. 313 -->
<div class='lstlisting' id='listing-14'><span class='label'><a id='x1-6001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>import matplotlib.pyplot as plt </span><br />
<span class='label'><a id='x1-6002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>import matplotlib.tri </span><br />
<span class='label'><a id='x1-6003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>def make_grid(nb_nodes): </span><br />
<span class='label'><a id='x1-6005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-6006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    Make an array that contains all elements of the grid. The </span><br />
<span class='label'><a id='x1-6007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    elements are described by the global node indices of </span><br />
<span class='label'><a id='x1-6008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    their corners. The order of the corners is in order of </span><br />
<span class='label'><a id='x1-6009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    the local node index. </span><br />
<span class='label'><a id='x1-6010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    They are sorted in geometric positive order and the first </span><br />
<span class='label'><a id='x1-6012r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>    is the node with the right angle corner at the bottom </span><br />
<span class='label'><a id='x1-6013r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    left. Elements within the same box are consecutive. </span><br />
<span class='label'><a id='x1-6014r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6015r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    This is the first element per box: </span><br />
<span class='label'><a id='x1-6016r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6017r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        2 </span><br />
<span class='label'><a id='x1-6018r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>        | \ </span><br />
<span class='label'><a id='x1-6019r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>        |  \ </span><br />
<span class='label'><a id='x1-6020r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    dy  |   \ </span><br />
<span class='label'><a id='x1-6021r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>        |    \ </span><br />
<span class='label'><a id='x1-6022r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        0 --- 1 </span><br />
<span class='label'><a id='x1-6023r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6024r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>          dx </span><br />
<span class='label'><a id='x1-6025r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6026r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>    This is the second element per box: </span><br />
<span class='label'><a id='x1-6027r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6028r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>           dx </span><br />
<span class='label'><a id='x1-6029r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>         1 ---0 </span><br />
<span class='label'><a id='x1-6030r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>          \   | </span><br />
<span class='label'><a id='x1-6031r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>           \  |  dy </span><br />
<span class='label'><a id='x1-6032r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>            \ | </span><br />
<span class='label'><a id='x1-6033r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>             \| </span><br />
<span class='label'><a id='x1-6034r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>              2 </span><br />
<span class='label'><a id='x1-6035r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6036r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-6037r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-6038r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-6039r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-6040r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6041r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-6042r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-6043r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'>    triangles_el : numpy.ndarray </span><br />
<span class='label'><a id='x1-6044r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'>        Array containing the global node indices of the </span><br />
<span class='label'><a id='x1-6045r45'></a><span class='cmr-6'>45</span></span><span class='cmtt-10'>        element corners. The first index (suffix _e) </span><br />
<span class='label'><a id='x1-6046r46'></a><span class='cmr-6'>46</span></span><span class='cmtt-10'>        identifies the element number and the second index </span><br />
<span class='label'><a id='x1-6047r47'></a><span class='cmr-6'>47</span></span><span class='cmtt-10'>        (suffix _l) the local node index of that element. </span><br />
<span class='label'><a id='x1-6048r48'></a><span class='cmr-6'>48</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-6049r49'></a><span class='cmr-6'>49</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-6050r50'></a><span class='cmr-6'>50</span></span><span class='cmtt-10'>    # These are the node position on a subsection of the grid </span><br />
<span class='label'><a id='x1-6051r51'></a><span class='cmr-6'>51</span></span><span class='cmtt-10'>    # that excludes the rightmost and topmost nodes. The </span><br />
<span class='label'><a id='x1-6052r52'></a><span class='cmr-6'>52</span></span><span class='cmtt-10'>    # suffix _G indicates this subgrid. </span><br />
<span class='label'><a id='x1-6053r53'></a><span class='cmr-6'>53</span></span><span class='cmtt-10'>    y_G, x_G = np.mgrid[:Ny-1, :Nx-1] </span><br />
<span class='label'><a id='x1-6054r54'></a><span class='cmr-6'>54</span></span><span class='cmtt-10'>    x_G.shape = (-1,) </span><br />
<span class='label'><a id='x1-6055r55'></a><span class='cmr-6'>55</span></span><span class='cmtt-10'>    y_G.shape = (-1,) </span><br />
<span class='label'><a id='x1-6056r56'></a><span class='cmr-6'>56</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6057r57'></a><span class='cmr-6'>57</span></span><span class='cmtt-10'>    # List of triangles </span><br />
<span class='label'><a id='x1-6058r58'></a><span class='cmr-6'>58</span></span><span class='cmtt-10'>    lower_triangles = np.vstack( </span><br />
<span class='label'><a id='x1-6059r59'></a><span class='cmr-6'>59</span></span><span class='cmtt-10'>        (node_index(x_G, y_G, nb_nodes), </span><br />
<span class='label'><a id='x1-6060r60'></a><span class='cmr-6'>60</span></span><span class='cmtt-10'>         node_index(x_G+1, y_G, nb_nodes), </span><br />
<span class='label'><a id='x1-6061r61'></a><span class='cmr-6'>61</span></span><span class='cmtt-10'>         node_index(x_G, y_G+1, nb_nodes))) </span><br />
<span class='label'><a id='x1-6062r62'></a><span class='cmr-6'>62</span></span><span class='cmtt-10'>    upper_triangles = np.vstack( </span><br />
<span class='label'><a id='x1-6063r63'></a><span class='cmr-6'>63</span></span><span class='cmtt-10'>        (node_index(x_G+1, y_G+1, nb_nodes), </span><br />
<span class='label'><a id='x1-6064r64'></a><span class='cmr-6'>64</span></span><span class='cmtt-10'>         node_index(x_G, y_G+1, nb_nodes), </span><br />
<span class='label'><a id='x1-6065r65'></a><span class='cmr-6'>65</span></span><span class='cmtt-10'>         node_index(x_G+1, y_G, nb_nodes))) </span><br />
<span class='label'><a id='x1-6066r66'></a><span class='cmr-6'>66</span></span><span class='cmtt-10'>    # Suffix _e indicates global element index </span><br />
<span class='label'><a id='x1-6067r67'></a><span class='cmr-6'>67</span></span><span class='cmtt-10'>    return np.vstack( </span><br />
<span class='label'><a id='x1-6068r68'></a><span class='cmr-6'>68</span></span><span class='cmtt-10'>        (lower_triangles, upper_triangles)).T.reshape(-1, 3) </span><br />
<span class='label'><a id='x1-6069r69'></a><span class='cmr-6'>69</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6070r70'></a><span class='cmr-6'>70</span></span><span class='cmtt-10'>def plot_results(values_g, nb_nodes, mesh_style=None, </span><br />
<span class='label'><a id='x1-6071r71'></a><span class='cmr-6'>71</span></span><span class='cmtt-10'>                 ax=None): </span><br />
<span class='label'><a id='x1-6072r72'></a><span class='cmr-6'>72</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-6073r73'></a><span class='cmr-6'>73</span></span><span class='cmtt-10'>    Plot results of a finite-element calculation on a </span><br />
<span class='label'><a id='x1-6074r74'></a><span class='cmr-6'>74</span></span><span class='cmtt-10'>    two-dimensional structured grid using matplotlib. </span><br />
<span class='label'><a id='x1-6075r75'></a><span class='cmr-6'>75</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6076r76'></a><span class='cmr-6'>76</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-6077r77'></a><span class='cmr-6'>77</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-6078r78'></a><span class='cmr-6'>78</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-6079r79'></a><span class='cmr-6'>79</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-6080r80'></a><span class='cmr-6'>80</span></span><span class='cmtt-10'>    values_g : array_like </span><br />
<span class='label'><a id='x1-6081r81'></a><span class='cmr-6'>81</span></span><span class='cmtt-10'>        Expansion coefficients (values of the field) on the </span><br />
<span class='label'><a id='x1-6082r82'></a><span class='cmr-6'>82</span></span><span class='cmtt-10'>        global nodes </span><br />
<span class='label'><a id='x1-6083r83'></a><span class='cmr-6'>83</span></span><span class='cmtt-10'>    mesh_style : str, optional </span><br />
<span class='label'><a id='x1-6084r84'></a><span class='cmr-6'>84</span></span><span class='cmtt-10'>        Will show the underlying finite-element mesh with </span><br />
<span class='label'><a id='x1-6085r85'></a><span class='cmr-6'>85</span></span><span class='cmtt-10'>        the given style if set, e.g. ’ko-’ to see edges </span><br />
<span class='label'><a id='x1-6086r86'></a><span class='cmr-6'>86</span></span><span class='cmtt-10'>        and mark nodes by points </span><br />
<span class='label'><a id='x1-6087r87'></a><span class='cmr-6'>87</span></span><span class='cmtt-10'>        (Default: None) </span><br />
<span class='label'><a id='x1-6088r88'></a><span class='cmr-6'>88</span></span><span class='cmtt-10'>    ax : matplotlib.Axes, optional </span><br />
<span class='label'><a id='x1-6089r89'></a><span class='cmr-6'>89</span></span><span class='cmtt-10'>        Axes object for plotting </span><br />
<span class='label'><a id='x1-6090r90'></a><span class='cmr-6'>90</span></span><span class='cmtt-10'>        (Default: None) </span><br />
<span class='label'><a id='x1-6091r91'></a><span class='cmr-6'>91</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6092r92'></a><span class='cmr-6'>92</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-6093r93'></a><span class='cmr-6'>93</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-6094r94'></a><span class='cmr-6'>94</span></span><span class='cmtt-10'>    trim : matplotlib.collections.Trimesh </span><br />
<span class='label'><a id='x1-6095r95'></a><span class='cmr-6'>95</span></span><span class='cmtt-10'>        Result of tripcolor </span><br />
<span class='label'><a id='x1-6096r96'></a><span class='cmr-6'>96</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-6097r97'></a><span class='cmr-6'>97</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-6098r98'></a><span class='cmr-6'>98</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6099r99'></a><span class='cmr-6'>99</span></span><span class='cmtt-10'>    # These are the node positions on the full global grid. </span><br />
<span class='label'><a id='x1-6100r100'></a><span class='cmr-6'>100</span></span><span class='cmtt-10'>    y_g, x_g = np.mgrid[:Ny, :Nx] </span><br />
<span class='label'><a id='x1-6101r101'></a><span class='cmr-6'>101</span></span><span class='cmtt-10'>    x_g.shape = (-1,) </span><br />
<span class='label'><a id='x1-6102r102'></a><span class='cmr-6'>102</span></span><span class='cmtt-10'>    y_g.shape = (-1,) </span><br />
<span class='label'><a id='x1-6103r103'></a><span class='cmr-6'>103</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6104r104'></a><span class='cmr-6'>104</span></span><span class='cmtt-10'>    # Gouraud shading linearly interpolates the color between </span><br />
<span class='label'><a id='x1-6105r105'></a><span class='cmr-6'>105</span></span><span class='cmtt-10'>    # the nodes </span><br />
<span class='label'><a id='x1-6106r106'></a><span class='cmr-6'>106</span></span><span class='cmtt-10'>    if ax is None: </span><br />
<span class='label'><a id='x1-6107r107'></a><span class='cmr-6'>107</span></span><span class='cmtt-10'>        ax = plt </span><br />
<span class='label'><a id='x1-6108r108'></a><span class='cmr-6'>108</span></span><span class='cmtt-10'>    triangulation = matplotlib.tri.Triangulation( </span><br />
<span class='label'><a id='x1-6109r109'></a><span class='cmr-6'>109</span></span><span class='cmtt-10'>        x_g, y_g, make_grid(nb_nodes)) </span><br />
<span class='label'><a id='x1-6110r110'></a><span class='cmr-6'>110</span></span><span class='cmtt-10'>    c = ax.tripcolor(triangulation, values_g, </span><br />
<span class='label'><a id='x1-6111r111'></a><span class='cmr-6'>111</span></span><span class='cmtt-10'>                     shading=’gouraud’) </span><br />
<span class='label'><a id='x1-6112r112'></a><span class='cmr-6'>112</span></span><span class='cmtt-10'>    if mesh_style is not None: </span><br />
<span class='label'><a id='x1-6113r113'></a><span class='cmr-6'>113</span></span><span class='cmtt-10'>        ax.triplot(triangulation, mesh_style) </span><br />
<span class='label'><a id='x1-6114r114'></a><span class='cmr-6'>114</span></span><span class='cmtt-10'>    return c </span><br />
<span class='label'><a id='x1-6115r115'></a><span class='cmr-6'>115</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-6116r116'></a><span class='cmr-6'>116</span></span><span class='cmtt-10'>plt.subplot(111, aspect=1) </span><br />
<span class='label'><a id='x1-6117r117'></a><span class='cmr-6'>117</span></span><span class='cmtt-10'>plot_results(potential_g, nb_nodes, show_mesh=True) </span><br />
<span class='label'><a id='x1-6118r118'></a><span class='cmr-6'>118</span></span><span class='cmtt-10'>plt.xlabel(r’</span><span class='tctt-1000'>$</span><span class='cmtt-10'>x</span><span class='tctt-1000'>$</span><span class='cmtt-10'>-position (</span><span class='tctt-1000'>$</span><span class='cmtt-10'>\Delta x</span><span class='tctt-1000'>$</span><span class='cmtt-10'>)’) </span><br />
<span class='label'><a id='x1-6119r119'></a><span class='cmr-6'>119</span></span><span class='cmtt-10'>plt.ylabel(r’</span><span class='tctt-1000'>$</span><span class='cmtt-10'>y</span><span class='tctt-1000'>$</span><span class='cmtt-10'>-position (</span><span class='tctt-1000'>$</span><span class='cmtt-10'>\Delta y</span><span class='tctt-1000'>$</span><span class='cmtt-10'>)’) </span><br />
<span class='label'><a id='x1-6120r120'></a><span class='cmr-6'>120</span></span><span class='cmtt-10'>plt.colorbar().set_label(r’Potential </span><span class='tctt-1000'>$</span><span class='cmtt-10'>\Phi</span><span class='tctt-1000'>$</span><span class='cmtt-10'> (V)’) </span><br />
<span class='label'><a id='x1-6121r121'></a><span class='cmr-6'>121</span></span><span class='cmtt-10'>plt.tight_layout() </span><br />
<span class='label'><a id='x1-6122r122'></a><span class='cmr-6'>122</span></span><span class='cmtt-10'>plt.show()</span>
</div>
<!-- l. 437 --><p class='indent'> Die Funktion <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>make_grid</span></span></span> erzeugt hier eine Liste der globalen Knotenindices
pro Element. Der erste Index ist der Index des Elements (Suffix <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>e</span></span></span>), der zweite
Index ist der lokale Knotenindex innerhalb des Elements (Suffix <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>l</span></span></span>). Die
Reihenfolge der Dreiecke entspricht Abb. <span class='cmbx-12'>??</span>a. Die Knoten des jeweiligen
Elements sind gegen den Uhrzeigersinn nummeriert. Für die Visualisierung wird
“Gouraud”-Schattierung genutzt. Diese Art der Färbung interpoliert
den Wert der Knoten linear auf den Dreiecken und entspricht exakt der
Interpolationsvorschrift unserer Formfunktionen. Wir können damit die volle
interpolierte Funktion \(\Phi _N(\v {r})\) darstellen.
</p><!-- l. 439 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>11.6 </span> <a id='x1-700011.6'></a>Kapazität eines Plattenkondensators</h3>
<!-- l. 441 --><p class='noindent'>Mit Hilfe des hier entwickelten Codes kann nun das elektrostatische Potential
innerhalb eines Plattenkondensators berechnet werden. Abbildung <a href='#x1-7001r2'>11.2<!-- tex4ht:ref: fig:plate-capacitor-potential --></a> zeigt das
Ergebnis dieser Rechnung für unterschiedliche Auflösung der Simulation, also
unterschiedliche Anzahl an Elementen. Durch Erhöhung der Auflösung kann die
Simulation systematisch verbessert werden.
</p>
<figure class='figure'>







<!-- l. 447 --><p class='noindent'><img width='702' alt='PIC' height='280' src='Figures/capacitor_potential.svg' /> <a id='x1-7001r2'></a>
<a id='x1-7002'></a>
</p><!-- l. 449 --><p class='noindent'>figureElektrostatisches Potential
innerhalb des Plattenkondensators, gerechnet mit (a) \(4\times 4\) Knoten (\(18\) Elemente)
und (b) \(32\times 32\) Knoten (\(1922\) Elemente). In (a) sieht man in der farblichen Codierung
den linearen Funktionsverlauf innerhalb der Elemente.
</p>
<figcaption class='caption'><span class='id'>Abbildung 11.2: </span><span class='content'>Elektrostatisches Potential
innerhalb des Plattenkondensators, gerechnet mit (a) \(4\times 4\) Knoten (\(18\) Elemente)
und (b) \(32\times 32\) Knoten (\(1922\) Elemente). In (a) sieht man in der farblichen Codierung
den linearen Funktionsverlauf innerhalb der Elemente.
</span></figcaption><!-- tex4ht:label?: x1-7001r11.6 -->



</figure>
<!-- l. 453 --><p class='indent'> Für die Berechnung der Kapazität müssen wir nun noch die Ladung auf
den Kondensatorplatten ermitteln. Die Gesamtladung \(Q_\alpha \) auf der Elektrode \(\alpha \) erhält
man aus der Oberflächenladung, die durch Gl. \eqref{eq:surfacecharge} gegeben
ist. Durch Integration über die Fläche der Kondensatorplatten \(A_\alpha \) erhält man
\begin {equation} Q_\alpha = \int _{A_\alpha } \dif ^2 r\, \sigma (\v {r}) = \varepsilon \int _{A_\alpha } \dif ^2 r\, \nabla \Phi _N\cdot \hat {n}(\v {r}). \end {equation}
Hier spielt nun die Permittivität \(\varepsilon \) eine wichtige Rolle für die Einheit der
Ladung. Wir können nun wieder die Reihenentwicklung einsetzen. Zum Integral
trägt nur Elementtyp \((1)\) bei, und hier nur die Formfunktionen, bei denen die
Ableitung in \(y\)-Richtung nicht verschwindet, da \(\nabla \Phi _N\cdot \hat {n}(\v {r})=\pm \partial \Phi _N/\partial y\). Das Vorzeichnen ist bei oberer
und unterer Kondensatorplatte umgedreht. Nicht-verschwindende Beiträge
kommen von den Formfunktionen \(N_0^{(1)}\) und \(N_2^{(1)}\) (siehe Gl. \eqref{eq:N10der} und
\eqref{eq:N12der}). Man erhält \begin {align} \int _0^{\Delta x} \dif x \frac {\partial N_0^{(1)}}{\partial y} &amp;= \int _0^{\Delta x} \dif x \frac {1}{\Delta y} = \frac {\Delta x}{\Delta y} \\ \int _0^{\Delta x} \dif x \frac {\partial N_2^{(1)}}{\partial y} &amp;= \int _0^{\Delta x} \dif x \left (-\frac {1}{\Delta y}\right ) = -\frac {\Delta x}{\Delta y} \end {align}
</p><!-- l. 466 --><p class='indent'> und damit für \(\Delta x=\Delta y\) \begin {equation} Q^{(n)} = \varepsilon t(a_0 - a_2) \end {equation}
als Beitrag des Elements \((n)\) zur Ladung auf der Elektrode. Hierbei bezeichnen die
Indices der Koeffizienten \(a_0\) und \(a_2\) die jeweiligen lokalen Knotenindices. Die Größe \(t\)
ist die Tiefe der Simulationsdomäne. Da wir das Problem hier in zwei
Dimensionen betrachten sind alle Ladungen effektiv Linienladungen (pro Tiefe)
und der Faktor \(t\) wird benötigt, um auf eine absolute Ladung zu kommen. Unser
Plattenkondensator ist in die dritte Dimension unendlich lang. Der Faktor \(\varepsilon t\) hat die
Einheit Farad und ist damit eine Kapazität.
</p><!-- l. 472 --><p class='indent'> Die Kapazität des Kondensators ist nun gegeben als \(C=Q_0/\Delta \Phi \), wobei \(Q_0\) nun die Ladung
auf einer Kondensatorplatte ist und \(\Delta \Phi \) der (vorgegebene) Potentialunterschied. Die
zweite Kondensatorplatte muss die Ladung \(Q_1=-Q_0\) tragen. Der Code für die Berechnung
der Ladung auf den Kondensatorplatten sieht daher folgendermaßen aus:
</p><!-- l. 473 -->
<div class='lstlisting' id='listing-15'><span class='label'><a id='x1-7003r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def get_charge(potential_g, nb_nodes, </span><br />
<span class='label'><a id='x1-7004r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>               top_left, top_right, </span><br />
<span class='label'><a id='x1-7005r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>               bottom_left, bottom_right): </span><br />
<span class='label'><a id='x1-7006r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-7007r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Compute charge on both capacitor plates. </span><br />
<span class='label'><a id='x1-7008r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7009r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-7010r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-7011r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    potential_g : array_like </span><br />
<span class='label'><a id='x1-7012r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Electrostatic potential </span><br />
<span class='label'><a id='x1-7013r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-7014r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-7015r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    top_left : int </span><br />
<span class='label'><a id='x1-7016r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>        Leftmost node of the top electrode </span><br />
<span class='label'><a id='x1-7017r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    top_right : int </span><br />
<span class='label'><a id='x1-7018r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        Rightmost node of the top electrode </span><br />
<span class='label'><a id='x1-7019r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>    bottom_left : int </span><br />
<span class='label'><a id='x1-7020r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>        Leftmost node of the bottom electrode </span><br />
<span class='label'><a id='x1-7021r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    bottom_right : int </span><br />
<span class='label'><a id='x1-7022r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>        Rightmost node of the bottom electrode </span><br />
<span class='label'><a id='x1-7023r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7024r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-7025r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-7026r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    charge_top : float </span><br />
<span class='label'><a id='x1-7027r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>        Charge (divided by permittivity and thickness) on top </span><br />
<span class='label'><a id='x1-7028r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>        plate </span><br />
<span class='label'><a id='x1-7029r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>    charge_bottom : float </span><br />
<span class='label'><a id='x1-7030r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>        Charge (divided by permittivity and thickness) on </span><br />
<span class='label'><a id='x1-7031r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>        bottom plate </span><br />
<span class='label'><a id='x1-7032r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-7033r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-7034r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>    charge_top = 0.0 </span><br />
<span class='label'><a id='x1-7035r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>    for i in range(top_left+1, top_right+1): </span><br />
<span class='label'><a id='x1-7036r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>        charge_top += \ </span><br />
<span class='label'><a id='x1-7037r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>            potential_g[node_index(i, Ny-1, nb_nodes)] - \ </span><br />
<span class='label'><a id='x1-7038r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'>            potential_g[node_index(i, Ny-2, nb_nodes)] </span><br />
<span class='label'><a id='x1-7039r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7040r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>    charge_bottom = 0.0 </span><br />
<span class='label'><a id='x1-7041r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>    for i in range(bottom_left+1, bottom_right+1): </span><br />
<span class='label'><a id='x1-7042r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>        charge_bottom += \ </span><br />
<span class='label'><a id='x1-7043r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>            potential_g[node_index(i, 0, nb_nodes)] - \ </span><br />
<span class='label'><a id='x1-7044r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>            potential_g[node_index(i, 1, nb_nodes)] </span><br />
<span class='label'><a id='x1-7045r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7046r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'>    return charge_top, charge_bottom</span>
</div>
<!-- l. 520 --><p class='indent'> Natürlich wissen wir, wie die Kapazität eines Plattenkondensators aussieht.
Sie ist gegeben durch \begin {equation} C = \varepsilon \frac {A}{d}, \label {eq:anacapacity} \end {equation}
wobei \(A=tL\) die Fläche der Kondensatorplatte ist und \(d\) der Abstand der Platten. (\(L\) ist
die Länge der Platten, siehe Abb. <a href='#x1-2001r1'>11.1<!-- tex4ht:ref: fig:plate-capacitor --></a>a.) Dies können wir entdimensionalisiert
als \begin {equation} \frac {C}{\varepsilon t} = \frac {L}{d} \end {equation}
schreiben. Die linke Seite erhalten wir direkt aus unserer Simulation. Das Ergebnis
der Rechnung mit finiten Elementen ist in Abb. <a href='#x1-7047r3'>11.3<!-- tex4ht:ref: fig:plate-capacitor-capacity --></a> im Vergleich mit diesem
analytischen Ausdruck gezeigt. Man sieht, dass der analytische Ausdruck nur bei
kleinen Aspektverhältnissen \(d/L&lt;1\) gilt. Die Herleitung dieses Ausdrucks nimmt an,
dass die Feldlinien überall parallel und senkrecht zu den Kondensatorplatten



verlaufen. Für große Abstände der Kondensatorplatten ist dies nicht mehr der
Fall und Streufelder am Rand der Platten fangen an, eine Rolle für die
Kapazität zu spielen. Diese sind nicht von Gl. \eqref{eq:anacapacity} erfasst,
werden aber in der Simulation abgebildet.
</p>
<figure class='figure'>







<!-- l. 536 --><p class='noindent'><img width='585' alt='PIC' height='438' src='Figures/capacity.svg' /> <a id='x1-7047r3'></a>
<a id='x1-7048'></a>
</p><!-- l. 538 --><p class='noindent'>figureKapazität \(C\) eines Plattenkondensators gegen den Abstand der Platten
\(d\). Beide Achsen sind entdimensionalisiert und zeigen Größen ohne Einheit.
Die gestrichelte Linie ist die klassische Vorhersage für die Kapazität, die
blaue Linie zeigt die Simulation. Hierbei wurde die Simulationsbox immer
mindestens so Breit wie das dreifache der Plattenlänge \(L\) oder dem Abstand
der Platten \(d\) gewählt. Die Plattenlänge \(L\) wurde mit \(8\) Elementen diskretisiert.
</p>
<figcaption class='caption'><span class='id'>Abbildung 11.3: </span><span class='content'>Kapazität \(C\) eines Plattenkondensators gegen den Abstand
der Platten \(d\). Beide Achsen sind entdimensionalisiert und zeigen Größen
ohne Einheit. Die gestrichelte Linie ist die klassische Vorhersage für
die Kapazität, die blaue Linie zeigt die Simulation. Hierbei wurde
die Simulationsbox immer mindestens so Breit wie das dreifache der
Plattenlänge \(L\) oder dem Abstand der Platten \(d\) gewählt. Die Plattenlänge
\(L\) wurde mit \(8\) Elementen diskretisiert.
</span></figcaption><!-- tex4ht:label?: x1-7047r11.6 -->



</figure>
<div class='framedenv' id='shaded*-1'>
<!-- l. 542 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Systemmatrix der finite-Elemente Methode ist dünnbesetzt
(engl. “sparse”). Für dünnbesetzte Matrizen gibt es spezielle Datenstrukturen,
die den Umgang mit diesen Matrizen vereinfachen. Diese sind in dem Paket
<a href='https://docs.scipy.org/doc/scipy/reference/sparse.html'><span class='cmtt-12'>scipy.sparse</span></a> implementiert. Wir können diese Routinen nutzen, um eine
dünnbesetzte Systemmatrix zu konstruieren: </p><!-- l. 544 -->
<div class='lstlisting' id='listing-16'><span class='label'><a id='x1-7049r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>from scipy.sparse import coo_matrix </span><br />
<span class='label'><a id='x1-7050r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7051r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>def assemble_system_matrix(element_matrix_ll, nb_nodes): </span><br />
<span class='label'><a id='x1-7052r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-7053r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Assemble system matrix from the element matrix </span><br />
<span class='label'><a id='x1-7054r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7055r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br />
<span class='label'><a id='x1-7056r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br />
<span class='label'><a id='x1-7057r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    element_matrix_ll : array_like </span><br />
<span class='label'><a id='x1-7058r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        3 x 3 element matrix </span><br />
<span class='label'><a id='x1-7059r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    nb_nodes : tuple of ints </span><br />
<span class='label'><a id='x1-7060r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br />
<span class='label'><a id='x1-7061r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7062r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    Returns </span><br />
<span class='label'><a id='x1-7063r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    ------- </span><br />
<span class='label'><a id='x1-7064r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>    system_matrix_gg : numpy.ndarray </span><br />
<span class='label'><a id='x1-7065r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        System matrix </span><br />
<span class='label'><a id='x1-7066r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    """ </span><br />
<span class='label'><a id='x1-7067r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    Nx, Ny = nb_nodes </span><br />
<span class='label'><a id='x1-7068r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7069r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    # Compute grid </span><br />
<span class='label'><a id='x1-7070r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>    grid_el = make_grid(nb_nodes) </span><br />
<span class='label'><a id='x1-7071r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7072r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>    # Get number of elements </span><br />
<span class='label'><a id='x1-7073r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>    nb_elements, nb_corners = grid_el.shape </span><br />
<span class='label'><a id='x1-7074r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7075r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>    # Spread out grid and element matrix such that they can </span><br />
<span class='label'><a id='x1-7076r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'>    # be used as global node coordinates for the sparse </span><br />
<span class='label'><a id='x1-7077r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>    # matrix </span><br />
<span class='label'><a id='x1-7078r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>    grid1_ell = np.stack( </span><br />
<span class='label'><a id='x1-7079r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>        [grid_el, grid_el, grid_el], axis=1) </span><br />
<span class='label'><a id='x1-7080r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>    grid2_ell = np.stack( </span><br />
<span class='label'><a id='x1-7081r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>        [grid_el, grid_el, grid_el], axis=2) </span><br />
<span class='label'><a id='x1-7082r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'>    element_matrix_ell = np.stack( </span><br />
<span class='label'><a id='x1-7083r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>        [element_matrix_ll]*nb_elements, axis=0) </span><br />
<span class='label'><a id='x1-7084r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7085r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>    # Construct sparse system matrix </span><br />
<span class='label'><a id='x1-7086r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>    # ‘coo_matrix‘ will automatically sum duplicate entries </span><br />
<span class='label'><a id='x1-7087r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>    system_matrix_gg = coo_matrix( </span><br />
<span class='label'><a id='x1-7088r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>        (element_matrix_ell.reshape(-1), </span><br />
<span class='label'><a id='x1-7089r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>         (grid1_ell.reshape(-1), grid2_ell.reshape(-1))), </span><br />
<span class='label'><a id='x1-7090r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>        shape=(Nx*Ny, Nx*Ny)) </span><br />
<span class='label'><a id='x1-7091r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'> </span><br />
<span class='label'><a id='x1-7092r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'>    return system_matrix_gg.todense()</span>
</div>
<!-- l. 590 --><p class='indent'> Diese Methode ersetzt die obige Implementation von <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>assemble_system_matrix</span></span></span>.
Sie liefert (aus Gründen der Kompatibiltät zum Rest der hier gezeigten
Implementierung) zum Schluss wieder eine dichtbesetzte (engl. “dense”) Matrix,
man kann aber durchaus mit der dünnbesetzten Matrix weiterrechnen. Im
Rahmen der Anwendung von <a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_matrix.html'><span class='cmtt-12'>coo_matrix</span></a> werden hier die globalen Knotenindizes
als “Koordinaten” der Matrixeinträge eingesetzt. Hierzu müssen sowohl die
Knotenindizes als auch die Einträge der Elementmatrix auf die Größe der
Systemmatrix vervielfältigt werden. Dies geschieht durch die <a href='https://numpy.org/doc/stable/reference/generated/numpy.stack.html'><span class='cmtt-12'>numpy.stack</span></a>
Befehle in diesen Codefragment. </p></div>



<h2 class='likechapterHead'><a id='x1-800011.6'></a>Literaturverzeichnis</h2>

