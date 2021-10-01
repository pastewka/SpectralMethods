---
layout: default
title: "Kapitel 02"
parent: Vorlesung
date: 2021-10-01
categories: lecture
author: Lars Pastewka
nav_order: 2
---


<h2 class='chapterHead'><span class='titlemark'>Kapitel 2</span><br /><a id='x1-10002'></a>Gleichungstypen</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 7 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Kontext:</span></span> Die meisten Phänomene denen wir in den Ingenieurwissenschaften
begegnen, werden sehr gut durch Differentialgleichungen beschrieben. Wir
erinnern uns an die diskreten Netzwerkmodelle aus Elektrotechnik und
Systemtheorie. Sie werden z.B. durch ein System linearer gewöhnlicher
Differentialgleichungen (engl. “ordinary differential equations”) mit der Zeit als
unabängiger Veränderlicher beschrieben. Wir erinnern uns auch an den
Diffusionsprozess, wie z.B. den Wärmetransport in einem Bauteil auf einem
Kühlkörper, das einer Wärmequelle ausgesetzt ist. Dieses Phänomen
wird am Besten mit einer partiellen Differentialgleichung (engl. “partial
differential equation”) beschrieben. In diesem Kapitel beschäftigen wir
uns mit einer abstrakten Klassifikation von Differentialgleichungen. Der
Diffusionsprozess wird in mehr Detail im nächsten Kapitel wiederholt. </p></div>
<h3 class='sectionHead'><span class='titlemark'>2.1 </span> <a id='x1-20002.1'></a>Gewöhnliche Differentialgleichungen</h3>
<!-- l. 21 --><p class='noindent'>Wir erinnern uns an die Klassifizierung (Eigenschaften) der <span class='cmti-12'>gewöhnlichen</span>
Differentialgleichungen (GDGLs) und erkennen die verschiedenen Typen von
Differentialgleichungen. Bei all diesen Differentialgleichungen sind wir immer
an einer Lösung für einen bestimmten Anfangswert (oder Randwert)
interessiert, also z.B. \(x(t=0)=x_0\) etc. Dieser Anfangswert ist immer Teil der Definition der
Differentialgleichung.
</p><!-- l. 23 --><p class='indent'> <a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=c0711e7d-ca67-4039-a9f7-ac7201124448'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=c0711e7d-ca67-4039-a9f7-ac7201124448</span></a>
</p><!-- l. 25 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>2.1.1 </span> <a id='x1-30002.1.1'></a>Linear und nichtlinear</h4>
<!-- l. 27 --><p class='noindent'>Eine lineare Differentialgleichung ist beispielsweise \begin{equation} m\ddot{x}(t)+c\dot{x}(t)+kx=f(t) \label{eq:linear} \end{equation}
die den gedämpften und getriebenen harmonischen Oszillator beschreibt,
während \begin{equation} \frac{\dif ^2x}{\dif t^2}+\mu (x^2-1)\frac{\dif x}{\dif t}+x= 0 \label{eq:nichtlinear} \end{equation}
eine nichtlineare Bewegungsgleichung für \(x\) ist. Sie beschreibt den so genannten
Van-der-Pol Oszillator. Die Nichtlinearität ist hier dadurch zu erkennen, dass \(x^2\)
die Ableitung \(\dif x/\dif t\) multipliziert.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 40 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Ableitung erster oder höherer Ordnung ist eine lineare



Operation, da \begin{equation} \frac{\dif ^n}{\dif x^n} \lambda f(x) = \lambda \frac{\dif ^n}{\dif x^n} f(x) \end{equation}
für eine Konstante \(\lambda \) und \begin{equation} \frac{\dif ^n}{\dif x^n} \left [f(x) + g(x)\right ] = \frac{\dif ^n}{\dif x^n} f(x) + \frac{\dif ^n}{\dif x^n} g(x). \end{equation}
Zeitliche Ableitungen werden mit einem Punkt angezeigt, \begin{equation} \dot{x}(t)=\frac{\dif }{\dif t} x(t). \end{equation}
Für Funktionen einer Variable wird die Ableitung oft mit einem Strich angezeigt,
\begin{equation} f'(x)=\frac{\dif }{\dif x} f(x). \end{equation}
Für Funktionen mehrere Variablen ist das nicht mehr möglich. Hier
werden wir daher immer explizit den Differentialoperator verwenden. </p></div>
<!-- l. 60 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>2.1.2 </span> <a id='x1-40002.1.2'></a>Ordnung</h4>
<!-- l. 62 --><p class='noindent'>Die Ordnung einer Differentialgleichung ist gegeben durch die höchste
Ableitung die in der Gleichung auftaucht. So sind Gl. \eqref{eq:linear} und
Gl. \eqref{eq:nichtlinear} Beispiele für Differentialgleichungen zweiter
Ordnung.
</p><!-- l. 64 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>2.1.3 </span> <a id='x1-50002.1.3'></a>Systeme</h4>
<!-- l. 66 --><p class='noindent'>Ein System von Differentialgleichungen 1. Ordnung bilden z.B. die Gleichungen \begin{align} \frac{\dif x}{\dif t} =&amp; x(m - n y), \label{eq:sys1} \\ \frac{\dif y}{\dif t} =&amp; - y(\gamma - \delta x), \label{eq:sys2} \end{align}
</p><!-- l. 71 --><p class='indent'> die bekannten Räuber-Beute-Gleichungen oder auch Lotka-Volterra-Gleichungen.
Gleichungen \eqref{eq:sys1} und \eqref{eq:sys2} sind weiterhin nichtlinear.
</p><!-- l. 73 --><p class='indent'> Differentialgleichungen höherer Ordnung können in ein System von
Gleichungen 1. Ordnung umgeschrieben werden. Im Beispiel des gedämpften
harmonische Oszillators, \begin{equation} \ddot{x}(t)+c\dot{x}(t)+kx=f(t), \end{equation}
ersetzen wir \(\dot{x} = y\) und erhalten dadurch zwei Gleichungen erster Ordnung anstatt der
ursprünglichen Gleichung zweiter Ordnung, nämlich \begin{align} \dot{x} =&amp; y \\ m\dot{y} =&amp; -cy-kx+f(t) \end{align}
</p><!-- l. 84 --><p class='noindent'>
</p>



<h3 class='sectionHead'><span class='titlemark'>2.2 </span> <a id='x1-60002.2'></a>Partielle Differentialgleichungen</h3>
<!-- l. 87 --><p class='noindent'>Partielle Differentialgleichungen (PDGLs) sind Differentialgleichungen mit
mehr als einer unabhängigen Variablen. Als Beispiel stellen wir uns ein
zeitabhängiges Wärmetransportproblem in einer Dimension vor. Dieses wird
mit einer Diffusionsgleichung für die lokale Temperatur des Systems dargestellt.
Die Temperatur wird daher als Funktion zweier unabhängiger Variablen, der Zeit
\(t\) und der räumlichen Position \(x\), dargestellt: \(T(x, t)\). Die Zeitentwicklung der Temperatur
ist gegeben durch \begin{equation} \frac{\partial T(x,t)}{\partial t}=\kappa \frac{\partial ^2 T(x,t)}{\partial x^2}, \label{eq:heateq} \end{equation}
wobei \(\kappa \) den Wärmeleitungskoeffizienten bezeichnet. Diese Gleichung wurde von
Joseph Fourier (*1768, \(\dagger \)1830) entwickelt, dem wir im Laufe dieser Veranstaltung
wieder begegnen werden.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 99 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In Gl. \eqref{eq:heateq} bezeichnet \(\partial /\partial t\) die <span class='cmti-12'>partielle Ableitung</span>. Dies
ist die Ableitung nach einem der Argumente (hier \(t\)), also die Variation der
Funktion, wenn alle anderen Argumente konstant gehalten werden. Bei
GDGLs tauchen im Gegensatz zu PDGLs nur Ableitung nach einer Variable
(üblicherweise der Zeit \(t\)) auf, die dann mit dem Differentialoperator \(\dif /\dif t\) bezeichnet
werden. </p></div>
<!-- l. 103 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>2.2.1 </span> <a id='x1-70002.2.1'></a>Erste Ordnung</h4>
<!-- l. 104 --><p class='noindent'>Quasilineare PDGLs erster Ordnung, also Gleichungen der Form \begin{equation} P(x,t;u)\frac{\partial u(x,t)}{\partial x}+ Q(x,t;u)\frac{\partial u(x,t)}{\partial t}= R(x,t;u), \label{eq:PDE1Oquasi} \end{equation}
für eine (unbekannte) Funktion \(u(x,t)\) und der Anfangsbedingung \(u(x,t=0)=u_0(x)\) können
systematisch auf ein System gekoppelter GDGLs erster Ordnung zurückgeführt
werden. Diese wichtige Eigenschaft wollen wir untersuchen. </p><div class='framedenv' id='shaded*-1'>
<!-- l. 111 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> In Gl. \eqref{eq:PDE1Oquasi} wurde zur Illustration eine
Darstellung mit zwei Variablen \(x\) und \(t\) gewählt. Allgemein können wir schreiben:
\begin{equation} \sum \limits _i P_i(\{x_i\};u)\frac{\partial u(\{x_i\})}{\partial x_i}= R(\{x_i\};u) \end{equation}
Hier wurde als Notation \(u(\{x_i\})=u(x_0, x_1, x_2, \ldots )\) genutzt, also die geschweiften Klammern bezeichnen alle
Freiheitsgrade \(x_i\). </p></div>
<!-- l. 120 --><p class='indent'> Gleichung \eqref{eq:PDE1Oquasi} können wir auf ein System von GDGLs
transformieren. Dies wird die Methode der Charakteristiken genannt. Wir können
dann die Formalismen (analytisch oder numerisch) zur Lösung von Systemen von



GDGLs anwenden, die wir in der Vorlesung “Differentialgleichungen”
kennengelernt haben.
</p><!-- l. 122 --><p class='indent'> Wir gehen folgendermaßen vor:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-7002x1'>Zunächst parametrisieren wir die unabhängigen Veränderlichen in
Gl. \eqref{eq:PDE1Oquasi} mit einem Parameter \(s\) gemäß \(x(s)\) und \(t(s)\).
</li>
<li class='enumerate' id='x1-7004x2'>Wir bilden dann die <span class='cmti-12'>totale Ableitung </span>von \(u(x(s),t(s))\) nach \(s\) \begin{equation} \frac{\dif u(x(s),t(s))}{\dif s}= \frac{\partial u(x(s),t(s))}{\partial x}\frac{\dif x(s)}{\dif s}+ \frac{\partial u(x(s),t(s))}{\partial t}\frac{\dif t(s)}{\dif s}. \label{eq:totalderiv} \end{equation}
</li>
<li class='enumerate' id='x1-7006x3'>Durch den Vergleich der Koeffizienten der totalen Ableitung \eqref{eq:totalderiv}
mit der PDGL \eqref{eq:PDE1Oquasi} sieht man, dass diese DGL genau
denn gelöst wird, wenn \begin{align} \frac{dx(s)}{ds}&amp;=P(x,t,u),\label{eq:transode1}\\ \frac{dt(s)}{ds}&amp;=Q(x,t,u)\quad \text{und}\\ \frac{du(s)}{ds} &amp;= R(u(s)).\label{eq:transode3} \end{align}
<!-- l. 138 --><p class='noindent'>erfüllt ist. Dies beschreibt die Lösung entlang bestimmter Kurven in der
\((x,t)\)-Ebene.</p></li></ol>
<!-- l. 140 --><p class='noindent'>Wir haben damit die PDGL in einen Satz gekoppelter GDGLs erster Ordnung,
Gl. \eqref{eq:transex1}-\eqref{eq:transex3} umgewandelt.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 142 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> Die Transportgleichung \begin{equation} \frac{\partial u(x,t)}{\partial t}+c\frac{\partial u(x,t)}{\partial x}=0 \label{eq:transportexample} \end{equation}
mit der Anfangsbedingung \(u(x,t=0)=u_0(x)\) soll gelöst werden. Wir gehen nach obigem Rezept
vor:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-7008x1'>Wir parameterisieren die Variablen \(x\) und \(t\) mit Hilfe einer neuen Variable
\(s\), also \(x(s)\) und \(t(s)\). Wir suchen nun nach einem Ausdruck, mit dem wir \(x(s)\) und \(t(s)\)
bestimmen können.
</li>
<li class='enumerate' id='x1-7010x2'>Wir stellen nun die Frage, wie sich die Funktion \(u(x(s),t(s))\) verhält. Diese Funktion
beschreibt die Änderung eines Anfangswertes \(u(x(0),t(0))\) mit der Variable \(s\). Die totale
Ableitung wird zu \begin{equation} \frac{\dif u(x(s),t(s))}{\dif s}=\frac{\partial u}{\partial t}\frac{\dif t(s)}{\dif s}+\frac{\partial u}{\partial x}\frac{\dif x(s)}{\dif s}. \end{equation}
</li>
<li class='enumerate' id='x1-7012x3'>Die totale Ableitung ist genau dann identisch zu der partiellen
Differentialgleichung, die wir lösen wollen, wenn \begin{align} \frac{\dif x(s)}{\dif s} &amp;=c\quad \text{und} \label{eq:transex1}\\ \frac{\dif t(s)}{\dif s} &amp;=1. \end{align}



<!-- l. 160 --><p class='noindent'>In diesem Fall gilt \begin{equation} \frac{\dif u(s)}{\dif s} = 0.\label{eq:transex3} \end{equation}
</p></li>
<li class='enumerate' id='x1-7014x4'>Die allgemeinen Lösungen für die drei gewöhnlichen
Differentialgleichungen \eqref{eq:transex1}-\eqref{eq:transex3} sind
gegeben durch \begin{align} x(s) &amp;= cs + \text{const.},\\ t(s) &amp;= s + \text{const.}\quad \text{und}\\ u(s) &amp;= \text{const.} \end{align}
</li>
<li class='enumerate' id='x1-7016x5'>Mit den Anfangsbedingungen \(t(0)=0\), \(x(0)=\xi \) und \(u(x,t=0)=f(\xi )\) erhält man \(t=s\), \(x=ct+\xi \) und \(u=f(\xi )=f(x-ct)\),</li></ol>
<!-- l. 172 --><p class='noindent'>Die Anfangsbedingung \(f(\xi )\) wird mit der Geschwindigkeit \(c\) in die positive x-Richtung
transportiert. Die Lösung für \(u\) bleibt konstant, da die Ableitung von \(u\)
Null ist, also behält \(u\) den durch die Anfangsbedingung gegebenen Wert.
Das Feld \(u(x,0)\) wird also mit einer konstanten Geschwindigkeit \(c\) verschoben: \(u(x,t)=u(x-ct,0)\). </p></div>
<!-- l. 175 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>2.2.2 </span> <a id='x1-80002.2.2'></a>Zweite Ordnung</h4>
<!-- l. 179 --><p class='noindent'>Beispiele von PDGLs zweiter Ordnung sind die... </p>
<ul class='itemize1'>
<li class='itemize'>...Wellengleichung: \begin{equation} \frac{\partial ^2 u}{\partial t^2}-\frac{\partial ^2 u}{\partial x^2}=0 \end{equation}
</li>
<li class='itemize'>...Diffusionsgleichung (mit der wir uns hier näher beschäfigen werden): \begin{equation} \frac{\partial u}{\partial t}-\frac{\partial ^2 u}{\partial x^2}=0 \end{equation}
</li>
<li class='itemize'>...Laplacegleichung (die wir auch näher kennen lernen werden):
\begin{equation} \frac{\partial ^2 u}{\partial x^2}+\frac{\partial ^2 u}{\partial y^2}=0 \end{equation}
</li></ul>
<!-- l. 194 --><p class='noindent'>Die zweite Ordnung bezieht sich hier auf die zweite Ableitung. Diese Beispiel sind
für zwei Variablen formuliert, aber diese Differentialgleichungen können auch
für mehr Freiheitsgrade aufgeschrieben werden.



</p><!-- l. 196 --><p class='indent'> Für zwei Variablen lautet die allgemeine Form linearer PDGLs zweiter
Ordnung, \begin{equation} a(x,y) \frac{\partial ^2 u}{\partial x^2}+ b(x,y)\frac{\partial ^2 u}{\partial x\partial y}+ c(x,y)\frac{\partial ^2 u}{\partial y^2}=F\left (x,y;u,\frac{\partial u}{\partial x},\frac{\partial u}{\partial y}\right ), \end{equation}
wobei \(F\) selbst natürlich auch linear in den Argumenten sein muss, wenn die
gesamte Gleichung linear sein soll. Wir nehmen nun eine Klassifizierung von
PDGLs 2. Ordnung vor, stellen aber vorweg, dass diese Klassifizierung nicht
erschöpfend ist und dass sie nur punktweise gilt. Letzteres heißt, dass die PDGL
an unterschiedlichen Raumpunkten in eine andere Klassifizierung fallen
kann.
</p><!-- l. 205 --><p class='indent'> <a class='url' href='https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=676322ed-a634-4f96-9561-ac7201129f7c'><span class='cmtt-12'>https://uni-freiburg.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=676322ed-a634-4f96-9561-ac7201129f7c</span></a>
</p><!-- l. 207 --><p class='indent'> Wir nehmen zunächst an, dass \(F=0\) und \(a\), \(b\), \(c\) konstant seien. Dann erhalten wir:
\begin{equation} a\frac{\partial ^2 u}{\partial x^2}+b\frac{\partial ^2 u}{\partial x\partial y}+ c\frac{\partial ^2 u}{\partial y^2}=0. \label{eq:n2ndoconst} \end{equation}
Wir schreiben diese Gleichung um als die quadratische Form \begin{equation} \begin{pmatrix} \partial /\partial x \\ \partial /\partial y \end{pmatrix} \cdot \begin{pmatrix} a &amp; b/2 \\ b/2 &amp; c \end{pmatrix} \cdot \begin{pmatrix} \partial /\partial x \\ \partial /\partial y \end{pmatrix} u = \nabla \cdot \t{C} \cdot \nabla u =0 \label{eq:quadform} \end{equation}
Die Koeffizientenmatrix \(\t{C}\) können wir nun diagonalisieren. Dies für zu
\begin{equation} \t{C} = \t{U} \cdot \begin{pmatrix} \lambda _1 &amp; 0 \\ 0 &amp; \lambda _2 \end{pmatrix}\cdot \t{U}^T, \label{eq:diagquadform} \end{equation}
wobei \(\t{U}\) auf Grund der Symmetrie von \(\t{C}\) unitär ist, \(\t{U}^T \cdot \t{U}=\t{1}\). Die geometrische
Interpretation der Operation \(\t{U}\) ist eine Rotation. Wir führen nun transformierte
Koordinaten \(x'\) und \(y'\) ein, so dass \begin{equation} \nabla = \t{U} \cdot \nabla ' \end{equation}
mit \(\nabla '=(\partial /\partial x', \partial /\partial y')\). Mit anderen Worten, die Transformationsmatrix ist gegeben als
\begin{equation} \t{U} = \begin{pmatrix} \partial x'/\partial x &amp; \partial y'/\partial x \\ \partial x'/\partial y &amp; \partial y'/\partial y \end{pmatrix}. \end{equation}
Gleichung \eqref{eq:n2ndoconst} wird zu \begin{equation} \lambda _1 \frac{\partial ^2 u}{\partial x'^2} + \lambda _2 \frac{\partial ^2 u}{\partial y'^2} = 0. \label{eq:diag2nd} \end{equation}
Wir haben die Koeffizienten der Differentialgleichung diagonalisiert. Für eine
beliebige zweifach differenzierbare Funktion \(f(z)\), ist \begin{equation} u(x', y') = f\left (\sqrt{\lambda _2} x' + i\sqrt{\lambda _1} y'\right ) \end{equation}
eine Lösung von Gl. \eqref{eq:diag2nd}.
</p><!-- l. 275 --><p class='indent'> Wir unterscheiden nun drei Fälle: </p>
<ul class='itemize1'>
<li class='itemize'>Der Fall \(\det \t{C}=\lambda _1\lambda _2=ac-b^4/4=0\) mit \(b\ne 0\) und \(a\ne 0\) führt zu einer parabolischen PDGL. Diese PDGL heißt
parabolisch, weil die quadratische Form Gl. \eqref{eq:quadform} bzw.
\eqref{eq:diagquadform} eine Parabel beschreibt. (Dies ist natürlich eine
Analogie. Man muss die Differentialoperatoren durch Koordinaten ersetzen
damit diese funktioniert.) Ohne Beschränkung der Allgemeinheit sei \(\lambda _2=0\). Dann
bekommen wir \begin{equation} \frac{\partial ^2 u}{\partial x'^2}=0. \label{eqnparab} \end{equation}
Dies ist die kanonische Form einer parabolischen PDGL.
</li>
<li class='itemize'>Der Fall \(\det \t{C}=\lambda _1 \lambda _2=ac-b^2/4&gt;0\) führt zu einer elliptischen PDGL. Diese PDGL heißt
elliptisch, weil die quadratische Form Gl. \eqref{eq:quadform} bzw.
\eqref{eq:diagquadform} für eine konstante rechte Seite eine Ellipse
beschreibt. (Für \(\lambda _1=\lambda _2\) ist es ein Kreis.) Wir formen nun die Gleichung für den
elliptischen Fall auf eine standardisierte Form um und führen die skalierten
Koordinaten \(x'=\sqrt{\lambda _1} x''\) und \(y'=\sqrt{\lambda _2} y''\) ein. Dann wird aus Gl. \eqref{eq:diag2nd} die
kanonische elliptische PDGL \begin{equation} \frac{\partial ^2 u}{\partial x''^2}+\frac{\partial ^2 u}{\partial y''^2}=0. \label{eqnelliptic} \end{equation}



Die kanonische elliptische PDGL ist daher die Laplace-Gleichung,
Gl. \eqref{eqnelliptic} (hier im Zweidimensionalen). Lösungen der
Laplace-Gleichung heißen <span class='cmti-12'>harmonische Funktionen</span>.
</li>
<li class='itemize'>Der Fall \(\det \t{C}=\lambda _1\lambda _2=ac-b^2/4&lt;0\) ergibt die so genannte hyperbolische PDGL. Diese PDGL heißt
hyperbolisch, weil die quadratische Form Gl. \eqref{eq:quadform} bzw.
\eqref{eq:diagquadform} für eine konstante rechte Seite eine Hyperbel
beschreibt. Ohne Beschränkung der Allgemeinheit fordern wir nun \(\lambda _1&gt;0\) und \(\lambda _2&lt;0\).
Dann können wir wieder skalierte Koordinaten \(x'=\sqrt{\lambda _1}x''\) und \(y'=\sqrt{-\lambda _2}y''\) einführen, so dass
\begin{equation} \frac{\partial ^2 u}{\partial x''^2} - \frac{\partial ^2 u}{\partial y''^2} = \begin{pmatrix} \partial u/\partial x'' \\ \partial u/\partial y'' \end{pmatrix} \cdot \begin{pmatrix} 1 &amp; 0 \\ 0 &amp; -1 \end{pmatrix} \cdot \begin{pmatrix} \partial u/\partial x'' \\ \partial u/\partial y'' \end{pmatrix} = 0. \label{eq:hyb} \end{equation}
Wir können nun durch eine weitere Koordinatentransformation, nämlich
eine Rotation um \(45^\circ \), die Koeffizientenmatrix in Gl. \eqref{eq:hyb} auf eine
Form bringen, in der die Diagonalelemente \(0\) und die Nebendiagonalelemente \(1\)
sind. Dies ergibt die Differentialgleichung \begin{equation} \frac{\partial ^2 u}{\partial x''' \partial y'''}=0, \label{eqnd2udxideta0} \end{equation}
wobei \(x'''\) und \(y'''\) die entsprechend rotierten Koordinaten sind. Diese
Gleichung ist die kanonische Form einer hyperbolischen PDGL und
äquivalent zu Gl. \eqref{eq:n2ndoconst} in den neuen Variablen \(x'''\) und
\(y'''\).</li></ul>
<!-- l. 323 --><p class='indent'> Für höherdimensionale Probleme müssen wir uns die Eigenwerte
der Koeffizientenmatrix \(\t{C}\) anschauen. Die PDGL heißt <span class='cmti-12'>parabolisch</span>, wenn
es einen Eigenwert gibt der verschwindet, aber alle anderen Eigenwerte
entweder größer oder kleiner als Null sind. Die PDGL heißt <span class='cmti-12'>elliptisch</span>, wenn
alle Eigenwerte entweder größer Null oder kleiner Null sind. Die PDGL
heißt <span class='cmti-12'>hyperbolisch</span>, wenn es genau einen negativen Eigenwert gibt und alle
anderen positiv sind oder es genau einen positiven Eigenwert gibt und alle
anderen negativ sind. Es ist klar, dass für PDGLs mit mehr als zwei
Variablen, diese drei Klassen von PDGLs nicht erschöpfend sind und es
Koeffizientenmatrizen gibt, die aus diesem Klassifizierungschema fallen. Für
Probleme mit genau zwei Variablen führt diese Klassifzierung zu den
Bedingungen für die Determinanten der Koeffizientenmatrix die oben genannt
wurden.
</p><!-- l. 325 --><p class='indent'> Diese drei Typen linearer PDEs 2. Ordnung lassen sich für manche
Problemstellungen auch analytisch lösen. Wir geben im Folgenden ein Beispiel
hierzu.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 329 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Beispiel:</span></span> Wir lösen die eindimensionale Wellengleichung. \begin{equation} \frac{\partial ^2 u}{\partial x^2}-\frac{1}{c^2}\frac{\partial ^2 u}{\partial t^2}=0 \label{eqn1Dwaveeqn} \end{equation}
durch Separation der Variablen. Dafür machen wir den Ansatz \(u(x,t)=X(x)T(t)\), was zu
\begin{equation} \frac{1}{X}\frac{\partial ^2 X}{\partial x^2}=\frac{1}{c^2}\frac{1}{T}\frac{\partial ^2 T}{\partial t^2} \label{eqnseparate} \end{equation}
führt. In Gl. \eqref{eqnseparate} hängt die linke Seite nur von der Variablen \(x\)



ab, während die rechte Seite nur von \(t\) abhängt. Für beliebige \(x\) und \(t\) kann diese
Gleichung nur erfüllt werden, wenn beide Seiten gleich einer Konstanten sind
und wir erhalten somit \begin{equation} \frac{1}{X}\frac{\partial ^2 X}{\partial x^2}=-k^2=\frac{1}{c^2}\frac{1}{T}\frac{\partial ^2 T}{\partial t^2}\,\mathrm{.} \end{equation}
Dies ergibt die folgenden zwei Gleichungen \[\frac{\partial ^2 X}{\partial x^2}+k^2X=0\] mit der Lösung \(X(x)=e^{\pm ikx}\) und \[\frac{\partial ^2 T}{\partial t^2}+\omega ^2T=0\] mit der
Lösung \(T(t)=e^{\pm i\omega t}\), wobei wir \(\omega ^2=c^2k^2\) gesetzt haben. Dieses Beispiel braucht zur Ergänzung
Anfangsbedingungen, damit wir eine Lösung finden können. </p></div>



<h2 class='likechapterHead'><a id='x1-90002.2.2'></a>Literaturverzeichnis</h2>

