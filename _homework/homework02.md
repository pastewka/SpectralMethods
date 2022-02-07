---
layout: default
title:  "Übungsblatt 2 [9. Jan.]"
parent: Übungsaufgaben
categories: homework
author : Lars Pastewka
nav_order: 2
---
# Übungsblatt 2: Grundlagen der Methode der finiten Elemente

<div class="alert alert-warning">
Die Abgabe von Arbeitsblatt 1 bis 4 ist verpflichtend und konstituiert die Studienleistung der Veranstaltung <b>Simulationstechniken</b>. Die Arbeitsblätter führen von der mathematischen Formulierung eines Modellproblems hin zur numerischen Lösung dieses Problems und bauen aufeinander auf. Zum Bestehen der Veranstaltung müssen auf <b>jedem</b> Blatt mindestens 50% der erzielbaren Punkte erreicht werden.
</div>
<br>

<div class="alert alert-danger">
<b>Geben Sie bei allen Aufgaben die Lösungswege und Zwischenergebnisse mit an. Das Endergebnis alleine ist nicht ausreichend!</b> Wir empfehlen Ihnen die Nutzung von Python und Jupyter-Notebooks. Sollten Sie ein Jupyter-Notebook verwenden, dann können Sie dieses einfach direkt als Lösung bei uns einreichen. In allen anderen Fällen erzeugen Sie bitte ein PDF und legen die numerischen Codes als separate Datei dazu.
</div>

## Hinweise zu den numerischen Aufgaben: 
* Codes sollten immer möglichst übersichtlich und leicht lesbar sein. Beachten Sie insbesondere:
    * Verwenden Sie Namen anstelle von Symbolen um Ihre Variablen zu benennen, also z.Bsp. *concentration* oder *Konzentration* anstelle von *c*
    * Nutzen Sie Suffixe, um die Dimensionen von Matrizen und Vektoren zu beschreiben. *concentration_x* bedeutet beispielsweise, dass die Einträge im Vektor *concentration* von der Raumrichtung *x* abhängen.
    * Kommentieren Sie Ihren Code ausreichend!
* Verwenden Sie die *numpy*-interne Funktion `numpy.linalg.solve` zum lösen von linearen Gleichungssystemen. Ein eigener Algorithmus zum Lösen von Gleichungssystemen ist NICHT Teil dieses Übungsblatts.
* Folgende *numpy*-Funktionen können (aber müssen nicht) hilfreich sein: `full`, `linspace`, `zeros`, `eye`, `diag`, `maximum`
* Eine vollständige Dokumentation der *numpy*-Funktionen finden Sie auf https://numpy.org/doc/stable/
* Für die Erstellung der Plots können Sie beispielsweise `matplotlib.pyplot` verwenden. Die Dokumentation von matplotlib und Anwendungsbeispiele finden Sie auf https://matplotlib.org/index.html
* Um eine Stufenfunktion zu plotten empfiehlt sich beispielsweise die Funktion `matplotlib.pyplot.step` (https://matplotlib.org/gallery/lines_bars_and_markers/step_demo.html#sphx-glr-gallery-lines-bars-and-markers-step-demo-py) 
* Beachten Sie bitte die Regeln zur Erstellung von Graphiken!

# Aufgabe 1 (8 Punkte)
## Fourier-Basisfunktionen

### 1.1 Orthogonalität der 1D-Fourier-Basisfunktionen (3 Punkte)
Auf Übungsblatt 1 haben Sie eine analytische Lösung der Diffusionsgleichung mithilfe der eindimensionalen Fourier-Reihe bestimmt. Weisen Sie nach, dass die Basisfunktionen dieser Fourier-Reihe eine orthogonale Basis bilden. Das Skalarprodukt zweier $L$-periodischen Funktion sei dabei definiert als:
\begin{equation}
\left( f, g \right) = \frac{1}{L} \int_0^L dx \; \left( f^*(x) g(x) \right)
\end{equation}
wobei $f^*(x)$ für das komplex-konjugierte von $f(x)$ steht.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Die Basisfunktionen der Fourier-Reihe sind gegeben durch: $\varphi_k(x) = \exp{\left(\frac{2\pi i}{L}kx\right)}$ für alle $k\in \mathbb{Z}$.

Betrachten wir zunächst das Skalarprodukt zweier Funktionen für den Fall, dass $$k \neq k'$$:
\begin{equation}
\begin{aligned}
\left(\varphi_k, \varphi_{k'} \right) &= \frac{1}{L} \int_0^L dx \left(\exp{\left(\frac{2\pi i}{L}kx\right)}\right)^*\exp{\left(\frac{2\pi i}{L}k'x\right)} \\
&= \frac{1}{L}\int_0^L dx \exp{\left(-\frac{2\pi i}{L}kx\right)}\exp{\left(\frac{2\pi i}{L}k'x\right)} \\
&= \frac{1}{L}\int_0^L dx \exp{\left(\frac{2\pi i}{L}(k'-k)x\right)} \\
&= \frac{1}{L}\frac{L}{2\pi i (k'-k)} \left[ \exp{\left(\frac{2\pi i}{L}(k'-k)x\right)} \right]_0^L& \text{da } k'-k \neq 0 \\
&= \frac{1}{2\pi i (k'-k)} \left( e^{\left(2\pi i(k'-k)\right)} - 1 \right) \\
&= \frac{1}{2\pi i (k'-k)} \left( \cos{\left(2\pi (k'-k)\right)} + i\sin{\left(2\pi (k'-k)\right)} - 1 \right) & \text{Eulersche Formel} \\
&= 0 & \text{da } k'-k \in \mathbb{Z}
\end{aligned}
\label{eq:A1_1D_unterschiedliche_f}
\end{equation}

Für den Fall, dass $k=k'$ folgt:
\begin{equation}
\begin{aligned}
\left(\varphi_k, \varphi_{k'} \right) &= \frac{1}{L}\int_0^L dx \left(\exp{\left(\frac{2\pi i}{L}kx\right)}\right)^*\exp{\left(\frac{2\pi i}{L}k'x\right)} \\
&= \frac{1}{L}\int_0^L dx \exp{\left(-\frac{2\pi i}{L}kx\right)}\exp{\left(\frac{2\pi i}{L}k'x\right)} \\
&= \frac{1}{L}\int_0^L dx 1 & \text{für } k=k'\\
&= 1 \neq 0
\end{aligned}
\label{eq:A1_1D_gleiche_f}
\end{equation}

Per Definition folgt, dass die Funktionen $\varphi_k(x) = \exp{\left(\frac{2\pi i}{L}kx\right)}$ ein orthogonales Funktionensystem bilden.

</div>

### 1.2 Orthogonalität der 2D-Fourier-Basisfunktionen (3 Punkte)
Zeigen Sie, dass auch die Basisfunktionen der zweidimensionalen Fourier-Reihe eine orthogonale Basis bilden. Das Skalarprodukt zweier Funktionen, die in x-Richtung $L_x$-periodisch und in y-Richtung $L_y$-periodisch sind, sei dabei gegeben als
\begin{equation}
\left(f, g \right) = \frac{1}{L_x L_y} \int_0^{L_y} \int_0^{L_x} dx\,dy \, \left( f^*(x,y) g(x,y) \right)
\end{equation}

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Die Basisfunktionen der zweidimensionalen Fourier-Reihe sind gegeben durch: $$\varphi_{k_x,k_y}(x) = \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)}$$ für alle $$k_x, k_y \in \mathbb{Z}$$. Das Skalarprodukt von zwei dieser Funktionen ist dann gegeben durch:

$$
\begin{aligned}
\left(\varphi_{k_x,k_y}, \varphi_{k_x',k_y'} \right) &= \frac{1}{L_x L_y} \int_0^{L_y} \int_0^{L_x} dx dy \left(\exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)}\right)^* \exp{\left(\frac{2\pi i}{L_x}k_x' x + \frac{2\pi i}{L_y}k_y' y \right)}\\
&= \frac{1}{L_x L_y}\int_0^{L_y} \int_0^{L_x} dx dy \exp{\left(-\frac{2\pi i}{L_x}k_x x - \frac{2\pi i}{L_y}k_y y\right)} \exp{\left(\frac{2\pi i}{L_x}k_x' x + \frac{2\pi i}{L_y}k_y' y \right)} \\
&= \frac{1}{L_x L_y}\int_0^{L_y} dy \exp{\left(\frac{2\pi i}{L_y}\left(k_y'-k_y \right) y \right)} \int_0^{L_x} dx \exp{\left(\frac{2\pi i}{L_x}\left( k_x' - k_x \right) x \right)}
\end{aligned}
$$

Durch die Ergebnisse aus Aufgabe 1.1 (Glg. $\ref{eq:A1_1D_unterschiedliche_f}$ und $\ref{eq:A1_1D_gleiche_f}$) wissen wir, dass $\frac{1}{L}\int_0^L dx \exp{\left(\frac{2\pi i}{L}(k'-k)x\right)} = 0$ wenn $k \neq k'$ und $\frac{1}{L}\int_0^L dx \exp{\left(\frac{2\pi i}{L}(k'-k)x\right)} = 1$ wenn $k = k'$. Es folgt direkt, dass:
$$
\left(\varphi_{k_x,k_y}, \varphi_{k_x',k_y'} \right) = \begin{cases}
1 \neq 0 \quad \text{wenn } k_x=k_x' \text{ und } k_y = k_y' \\
0 \quad \text{andernfalls}
\end{cases}
$$
was bedeutet, dass die Basisfunktionen der zweidimensionalen Fourier-Reihe ein orthogonales Funktionensystem bilden.
</div>

### 1.3 Fourier-Koeffizienten (2 Punkte)
Leiten Sie die Formel für die Koeffizienten der zweidimensionalen Fourierreihe her, indem Sie die Funktion $f(x,y)$ auf die Fourierreihen-Basis projizieren.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Wir projizieren $f(x,y)$ auf die zweidimensionale Fourierreihen-Basis:
$$$$
\begin{aligned}
f(x,y) =& \sum_{k=-\infty}^{\infty} \left( \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)},f \right) \left( \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)},\exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)} \right)^{-1} \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)} \\
=& \sum_{k=-\infty}^{\infty} c_k \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)}
\end{aligned}
$$$$
Aus Aufgabe 1.2 folgt, dass $$\left( \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)},\exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)} \right) = 1$$. Die Koeffizienten der Fourier-Reihe sind also gegeben durch:
$$$$
\begin{aligned}
c_k &= \left( \exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)},f \right) \\
&= \frac{1}{L_x L_y}\int_0^{L_y}\int_0^{L_x} dx dy \; \left(\exp{\left(\frac{2\pi i}{L_x}k_x x + \frac{2\pi i}{L_y}k_y y\right)}\right)^* f(x,y) \\
&= \frac{1}{L_x L_y}\int_0^{L_y}\int_0^{L_x} dx dy \; f(x,y) \exp{\left(-\frac{2\pi i}{L_x}k_x x - \frac{2\pi i}{L_y}k_y y\right)}
\end{aligned}
$$$$
</div>

# Aufgabe 2 (8 Punkte)
## Finite-Elemente
In dieser Aufgabe betrachten wir die Grundlagen der Finite Elemente Methode.
Als Beispielproblem nehmen wir die stationäre Diffusionsgleichung in 1D (Vgl. Übungsblatt 1, Aufgabe 4):
\begin{equation}
D \frac{\partial^2 c}{\partial x^2} = f(x)
\label{eq:Diffusion}
\end{equation}
Wie in Übungsblatt 1 ist dabei $D$ die Diffusionskonstante, $c(x)$ eine Stoffmengenkonzentration und $f(x)$ ein Quellterm.

### 2.1 Schwache Form (2 Punkte)
Leiten Sie die schwache Form von Gleichung $\ref{eq:Diffusion}$ her und verringern Sie die Anforderung an die Differenzierbarkeit von $c(x)$. Gehen Sie dabei von der Annahme aus, dass die Diffusionsgleichung auf einem endlichen Gebiet $[0; L]$ gilt.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Seien $v(x)$ die Testfunktionen. Dann folgt aus Glg. $\ref{eq:Diffusion}$:
\begin{equation}
\int_0^L dx \; v(x) D\frac{\partial^2 c}{\partial x^2} = \int_0^L dx \; v(x) f(x)
\end{equation}

Durch partielle Integration erhalten wir die schwache Form von Glg. $\ref{eq:Diffusion}$:
\begin{equation}
\left[ v(x) D\frac{\partial c}{\partial x} \right]_0^L - \int_0^L dx \; \frac{\partial v}{\partial x} D\frac{\partial c}{\partial x} = \int_0^L dx \; v(x) f(x)
\label{eq:Diffusion_schwache_Form}
\end{equation}
</div>

### 2.2 Galerkin-Methode (1 Punkt)

Jetzt wird $c(x)$ in einem Funktionensystem mit den linear unabhängigen Basisfunktionen $\varphi_i$ dargestellt:
\begin{equation}
c(x) = \sum a_i \varphi_i(x)
\label{eq:c_in_Funktionensys}
\end{equation}

Verwenden Sie die Galerkin-Methode, um ein System von Gleichungen für die Koeffizienten $a_i$ zu bekommen.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
In der Galerkin-Methode werden die Basisfunktionen $\varphi_j$ als Testfunktionen verwendet. Zusammen mit der Darstellung der gesuchten Funktion $$c(x)$$ im orthogonalen Funktionensystem (Glg. $\ref{eq:c_in_Funktionensys}$) werden sie in die schwache Form der Differentialgleichung (Glg. $\ref{eq:Diffusion_schwache_Form}$) eingesetzt. Dadurch ergibt sich:

\begin{equation}
\forall j : \qquad D \sum_i a_i \left[ \varphi_j(x) \frac{\partial \varphi_i(x)}{\partial x} \right]_0^L - D \sum_i a_i \int_0^L  dx \; \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_i(x)}{\partial x} = \int_0^L dx \; \varphi_j(x) f(x)
\label{eq:Diffusion_Galerkin}
\end{equation}
</div>

### 2.3 Diskretisierung und Basis-Funktionen (5 Punkte)
Als Diskretisierung wollen wir $N$ gleichmäßig verteilte Gitterpunkte verwenden. Als Basisfunktionen wählen wir die stückweise linearen Zeltfunktionen, wie sie in der Abbildung dargestellt sind.


![png](output_18_0.png)


Berechnen Sie die diskretisierten Gleichungen, d.h. $\left( \varphi_j, R\right)=0$, für die inneren Testfunktionen $\varphi_j$ für $j \in \{1; 2; ...; N-2\}$ für die Quellterme:
1. $$f(x) = -\delta\left(x - \frac{L}{3} \right) + \delta\left(x - \frac{2L}{3} \right)$$
2. $$f(x) = f_0$$

**Hinweise** zu der Berechnung mit Delta-Distributionen als Quellterm: 
* Um die Berechnung der diskretisierten Terme zu erleichtern, können Sie die Anzahl an Gitterpunkte $N$ immer so wählen, dass die dirac Quellterme auf einem Knoten liegen, also  $N=3N'+1$ mit $N' \in \mathbb{N}$.
* Die Delta-Distribution ist durch ihre Filter-Eigenschaft definiert:
$$
\int_0^L dx \; \delta (x-a) f(x) = f(a)
$$

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Wir betrachten die Glg. \ref{eq:Diffusion_Galerkin} für $j \in {1; N-2}$. Dann ist $\varphi(0) = \varphi(L) = 0$, so dass der Randterm wegfällt. Außerdem ist das Integral $\int_0^L dx \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_i(x)}{\partial x} = 0$, außer wenn $i=j-1$, $i=j$ oder $i=j+1$. Es bleibt also:

\begin{equation}
- a_{j-1}D\int_0^L dx \; \left(\frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j-1}(x)}{\partial x}\right) - a_j D\int_0^L dx \; \left(\frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_j(x)}{\partial x}\right) - a_{j+1}D\int_0^L dx \; \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j+1}(x)}{\partial x} = \int_0^L dx \; \varphi_j(x) f(x)
\label{eq:A2_Diffusion_Galerkin_innen}
\end{equation}

Sei $\Delta x=\frac{L}{N-1}$ der Abstand zwischen zwei Gitterpunkten. Dann sind die Hutfunktionen und ihre Ableitungen gegeben durch:
\begin{equation}
\begin{aligned}
\varphi_j = \begin{cases}
\frac{1}{\Delta x}x - \frac{x_{j-1}}{\Delta x}\quad x \in [x_{j-1}; x_j] \\
-\frac{1}{\Delta x}x + \frac{x_{j+1}}{\Delta x}\quad x \in [x_{j}; x_{j+1}] \\
0 \quad x \notin [x_{j-1}; x_{j+1}]
\end{cases}
\qquad \frac{\partial \varphi_j}{\partial x} = \begin{cases}
\frac{1}{\Delta x} \quad x \in (x_{j-1}; x_j) \\
-\frac{1}{\Delta x} \quad x \in (x_{j}; x_{j+1}) \\
0 \quad x \notin (x_{j-1}; x_{j+1})
\end{cases}
\end{aligned}
\end{equation}

Die Integrale auf der linken Seite von Glg. $\ref{eq:A2_Diffusion_Galerkin_innen}$ sind also:
\begin{equation}
\begin{aligned}
&\int_0^L dx \; \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j-1}(x)}{\partial x} = \int_{x_{j-1}}^{x_j} dx \; \frac{1}{\Delta x}\frac{-1}{\Delta x} = -\frac{1}{\Delta x^2} \left(x_j - x_{j-1} \right) = -\frac{1}{\Delta x} \\
&\int_0^L dx \; \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j}(x)}{\partial x} = \int_{x_{j-1}}^{x_{j}} dx \; \frac{1}{\Delta x}\frac{1}{\Delta x} + \int_{x_{j}}^{x_{j+1}} dx \; \frac{-1}{\Delta x}\frac{-1}{\Delta x} = \frac{1}{\Delta x^2} \left(x_{j+1} - x_{j-1} \right) = \frac{2}{\Delta x} \\
&\int_0^L dx \; \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j+1}(x)}{\partial x} = \int_{x_{j}}^{x_{j+1}} dx \; \frac{-1}{\Delta x}\frac{1}{\Delta x} = -\frac{1}{\Delta x^2} \left(x_{j+1} - x_{j} \right) = -\frac{1}{\Delta x}
\end{aligned}
\end{equation}

woraus folgt, dass:
\begin{equation}
\frac{D}{\Delta x} a_{j-1} - \frac{2D}{\Delta x} a_j + \frac{D}{\Delta x} a_{j+1} = \int_0^L dx \; \varphi_j(x) f(x)
\label{eq:A2_Diffusion_Diskret}
\end{equation}

<br>
1. Quellterm:
$f(x) = -\delta\left(x - \frac{L}{3} \right) + \delta\left(x - \frac{2L}{3} \right)$
<br>
Die rechte Seite von Glg. $\ref{eq:A2_Diffusion_Diskret}$ ist:
\begin{equation}
\begin{aligned}
\int_0^L dx \; \varphi_j(x) f(x) &= \int_0^L dx \; \left(-\varphi_j(x) \delta\left(x-\frac{L}{3}\right) \right) + \int_0^L dx \; \left(\varphi_j(x) \delta(x-\frac{2L}{3}) \right) \\
&= -\varphi_j\left(\frac{L}{3}\right) + \varphi_j\left(\frac{2L}{3}\right) \\
&= \begin{cases}
-1 \qquad j=N'=\frac{1}{3}(N-1) \\
+1 \qquad j=2N'=\frac{2}{3}(N-1) \\
 0 \qquad j \in \{1; 2; ...; N-2\} \backslash \{ N'; 2N'\}
\end{cases}
\end{aligned}
\end{equation}
Zusammengesetzt ergibt sich:
\begin{equation}
\frac{D}{\Delta x} a_{j-1} - \frac{2D}{\Delta x} a_j + \frac{D}{\Delta x} a_{j+1} = \begin{cases}
-1 \qquad j=N' \\
+1 \qquad j=2N' \\
 0 \qquad j \in \{1; 2; ...; N-2\} \backslash \{ N'; 2N'\}
\end{cases}
\end{equation}
\begin{equation}
\label{eq:A2_Diffusion_Diskret_delta}
\Leftrightarrow \frac{1}{\Delta x} a_{j-1} - \frac{2}{\Delta x} a_j + \frac{1}{\Delta x} a_{j+1} = \begin{cases}
-\frac{1}{D} \qquad j=N' \\
+\frac{1}{D} \qquad j=2N' \\
 0 \qquad j \in \{1; 2; ...; N-2\} \backslash \{ N'; 2N'\}
\end{cases}
\end{equation}

<br>
2. Quellterm:  $f(x) = f_0$
<br>
Die rechte Seite von Glg. $\ref{eq:A2_Diffusion_Diskret}$ ist:
\begin{equation}
\begin{aligned}
\int_0^L dx \; \varphi_j(x) f(x) &= \int_0^L dx \; \varphi_j(x) f_0 \\
&= f_0 \int_{x_{j-1}}^{x_j} dx \; \left( \frac{1}{\Delta x}x - \frac{x_{j-1}}{\Delta x} \right) + f_0 \int_{x_{j}}^{x_{j+1}} dx \; \left(-\frac{1}{\Delta x}x + \frac{x_{j+1}}{\Delta x}\right) \\
&= \frac{f_0}{\Delta x} \left( x_j^2 + \frac{1}{2}x_{j-1}^2 + \frac{1}{2}x_{j+1}^2 - x_j x_{j-1} - x_j x_{j+1}\right) \\
&= f_0 \Delta x
\end{aligned}
\end{equation}
Zusammengesetzt ergibt sich:
\begin{equation}
\frac{D}{\Delta x} a_{j-1} - \frac{2D}{\Delta x} a_j + \frac{D}{\Delta x} a_{j+1} = f_0 \Delta x
\end{equation}
\begin{equation}
\label{eq:A2_Diffusion_Diskret_Constant}
\Leftrightarrow \frac{1}{\Delta x} a_{j-1} - \frac{2}{\Delta x} a_j + \frac{1}{\Delta x} a_{j+1} = \frac{f_0 \Delta x}{D}
\end{equation}
</div>

# Aufgabe 3 (9 Punkte)
## Finite-Element im periodischen Raum
In dieser Aufgabe wollen wir die Diffusionsgleichung mit periodischen Randbedingungen auf dem Gebiet $[0;L]$, die in Übungsblatt 1, Aufgabe 4 analytisch gelöst wurde mit Finiten Elementen lösen.

Dabei wählen wir die gleiche Diskretisierung und die gleichen Basisfunktionen wie in Aufgabe 2.3. Genau wie bei der analytischen Lösung ist der Quellterm $f(x) = -\delta\left(x - \frac{L}{3} \right) + \delta\left(x - \frac{2L}{3} \right)$.

### 3.1 Mittelwertbedingung (1 Punkt)
Wie wir auf dem Übungsblatt 1 gesehen haben, ist der Mittelwert der Lösungsfunktion nicht bestimmbar. Anders gesagt, wenn $c_1(x)$ eine periodische Lösung der Diffusionsgleichung ist, dann ist $c_2(x) = c_1(x) + \text{konst.}$ ebenfalls eine periodische Lösung der Diffusionsgleichung. Diese Unendlichkeit an Lösungen bedeutet, dass das Gleichungssystem, das wir mit den Finiten Elementen aufstellen, nicht eindeutig lösbar ist. 

Damit wir ein lösbares Gleichungssystem bekommen, brauchen wir ein Problem mit einer eindeutigen Lösung. Wir müssen deshalb die Forderung 'periodische Randbedingungen' mit einer weiteren Bedingung ergänzen. Wir wählen dafür einen vorgegebenen Mittelwert von 0, d.h. \begin{equation}\frac{1}{L}\int_0^L dx \; c(x) = 0\end{equation}

Dadurch ergibt sich eine weitere Gleichung für die Koeffizienten $a_i$. Stellen Sie diese Gleichung auf.

<div class="alert alert-success">
<b>Lösung:</b>
\begin{equation}
\begin{aligned}
 0 &= \frac{1}{L}\int_0^L dx \; c(x) \\
 &= \frac{1}{L} \sum_i a_i \int_0^L dx \; \varphi_i(x) \\
 &= \frac{1}{L} a_0 \int_0^L  dx \; \varphi_0(x) + \frac{1}{L} \sum_{i=1}^{N-2} a_i \int_0^L dx \; \varphi_i(x) + a_{N-1} \int_0^L dx \; \varphi_{N-1}(x) \\
 &= \frac{1}{N-1}  \left( \frac{a_0}{2} + \sum_{i=1}^{N-2} a_i + \frac{a_{N-1}}{2} \right)
\end{aligned}
\end{equation}
</div>

### 3.2 Systemmatrix (1 Punkt)
Das Gleichungssystem aus diskretisierten Gleichungen für die Koeffizienten $a_i$ wird üblicherweise in Matrix-Form geschrieben:
\begin{equation}
\underline{K} \cdot \overrightarrow{a} = \overrightarrow{f}
\end{equation}
$\underline{K}$ nennt man dann die Systemmatrix. 

Stellen Sie die Systemmatrix für die Lösung der 1D-Diffusionsgleichung mit periodischen Randbedingungen und einem vorgegebenen Mittelwert mithilfe von lineare Finiten Elementen für 4 Gitterpunkte auf.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Wir fordern periodische Randbedingungen, d.h. $c(0) = c(L)$, woraus folgt dass $a_0 = a_{N-1}$. Zusammen mit der Mittelwertbedingung und Glg. $\ref{eq:A2_Diffusion_Diskret_Constant}$ ergibt sich ein System von 4 Gleichungen:
\begin{equation}
\begin{cases}
a_0 - a_3 = 0 \\
\frac{1}{\Delta x} a_{0} - \frac{2}{\Delta x} a_1 + \frac{1}{\Delta x} a_{2} = -\frac{1}{D} \\
\frac{1}{l} a_{\Delta x} - \frac{2}{\Delta x} a_2 + \frac{1}{\Delta x} a_{3} = \frac{1}{D} \\
\frac{a_0}{2} + a_1 + a_2 + \frac{a_{3}}{2} = 0
\end{cases} 
\qquad \Leftrightarrow \qquad
\frac{1}{\Delta x} \begin{pmatrix}
\Delta x & 0 & 0 & -\Delta x \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
\Delta x / 2 & \Delta x & \Delta x & \Delta x / 2
\end{pmatrix} \cdot \begin{pmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3
\end{pmatrix} = \begin{pmatrix}
0 \\
-\frac{1}{D} \\
\frac{1}{D} \\
0
\end{pmatrix} 
\end{equation}

Die Systemmatrix ist also gegeben durch:
\begin{equation}
\underline{K} = \frac{1}{\Delta x} 
\begin{pmatrix}
\Delta x & 0 & 0 & -\Delta x \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
\Delta x / 2 & \Delta x & \Delta x & \Delta x / 2
\end{pmatrix}
\end{equation}
    
Hier legitime alternative Schreibweisen zwecks schnellerer Korrektur:
    
$$\underline{K} =\left( \begin{array}{cccc}
\frac{1}{2} & 1 & 1 & \frac{1}{2} \\ 
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\ 
1 & 0 & 0 & -1 \\
\end{array}\right)$$, $$\vec{f}=\left(\begin{array}{c}
0 \\
-\frac{\Delta x}{D} \\
\frac{\Delta x}{D} \\
0 \\
\end{array}\right)$$.
</div>

### 3.3 Numerische Lösung (7 Punkte)
Beachten Sie bitte die Hinweise am Anfang des Übungsblattes!

Schreiben Sie eine python-Funktion, um die Diffusionsgleichung im periodischen Raum mit linearen Finiten Elementen zu lösen. Diese Funktion sollte als Argumente die Anzahl der Gitterpunkte $N$, den Abstand zwischen zwei Gitterpunkten $dx$ und einen Vektor mit der bereits diskretisierten rechten Seite des Problems erwarten. Verwenden Sie also bitte die Schnittstelle

```python
def fem_laplace_linear_1d_periodic(nb_grid_pts, dx, rhs_x)
    """
    Function to solve the 1D Laplace equation with periodic boundary conditions and an
    imposed average using a regular grid and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized 1D Laplace equation at each grid point
    """
```

Nutzen Sie Ihre Funktion, um einen Plot, zu erstellen, auf dem die FEM-Lösung mit der analytischen Lösung verglichen wird.
Auf dem Plot muss zu sehen sein:
* Analytische Lösung aus Übungsblatt 1, Aufgabe 4:
$c(x) = \frac{1}{D}(-\max(0, x-L/3)+\max(0, x-2L/3) + \frac{1}{3D} x$
* Lösung mit FEM für N=4
* Lösung mit FEM für N=7

Kommentieren Sie kurz, was man auf dem Plot beobachten kann. Was würden Sie erwarten, wenn der Dirac-Impuls nicht direkt auf einem Gitterpunkt liegt? (Eine Berechnung ist nicht nötig, ein kurzer Kommentar genügt.)

Verwenden Sie für den Plot folgende Werte für die Parameter:
* $$D = 0.8\frac{\mathrm{m}^2}{\mathrm{s}}$$
* $$L = 1.5\mathrm{m}$$

<div class="alert alert-success">
<b>Lösung:</b>
</div>


```python
### ----- Funktion zur Lösung der 1D Laplacegleichung mit linearen Finiten Elementen ----- ###
def FEM_Laplace_Linear_1D_periodic(nb_grid_pts, dx, rhs_x):
    """
    Function to solve the 1D Laplace equation with periodic boundary conditions and an 
    imposed average using a regular grid and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized 1D Laplace equation at each grid point
    """
    # Systemmatrix mit periodischen RB aufstellen
    d = np.full(nb_grid_pts-1, 1/dx)
    system_matrix_xx = np.diag(d, -1) - 2/dx  * np.eye(nb_grid_pts) + np.diag(d, 1)
    
    # Mittelwertbedingung
    system_matrix_xx[nb_grid_pts-1] = 1
    system_matrix_xx[nb_grid_pts-1, 0] = 0.5
    system_matrix_xx[nb_grid_pts-1, nb_grid_pts-1] = 0.5
    
    # Periodische Randbedingung
    system_matrix_xx[0, 1] = 0
    system_matrix_xx[0, 0] = 1
    system_matrix_xx[0, nb_grid_pts-1] = -1
    
    # Gleichungssystem lösen
    func_x = np.linalg.solve(system_matrix_xx,rhs_x)
    
    return func_x
```


```python
### ----- Vergleich FEM - analytische Lösung der 1D Diffusionsgleichung ----- ###
# Parameter definieren
length = 1.5 # Länge der Periode
diffusion_const = 0.8 # Diffusionskonstante
concentration_average = 0 # vorgegebener Mittelwert der Konzentration

N_list = np.array([2, 1])
nb_grid_pts_list = 3*N_list + 1 # Anzahl Gitterpunkte

# Plot vorbereiten
fig, ax = plt.subplots()
plt.subplots_adjust(top=0.85)
title = 'Lösung der 1D Diffusionsgleichung \n (periodische RB '
title += 'und Mittelwert={})'.format(concentration_average)
fig.suptitle(title, fontsize=15)
ax.set_xlabel(r'Position $x$ (m)', fontsize=13)
ax.set_ylabel(r'Konzentration $c$ (1/$\mathrm{m}^3$)', fontsize=13)

linestyles = ['--', '-.', ':']
markerstyles = ['o', 'v', '^']
markersize = 9
colors = ['red', 'blue', 'limegreen', 'black']

# Analytische Lösung der Diffusionsgleichung
x = np.linspace(0, length, 100)
concentration_ana_x = (np.maximum(0, x-2*length/3) - np.maximum(0, x-length/3)) / diffusion_const
concentration_ana_x += 1/3/diffusion_const * x
ax.plot(x, concentration_ana_x, label='Analytisch', color=colors[0], linewidth=3)

# FEM Lösung der Diffusionsgleichung
for i, nb_grid_pts in enumerate(nb_grid_pts_list):
    dx = length/(nb_grid_pts-1)
    # Rechte Seite der Gleichung ausrechnen
    rhs_x = np.zeros(nb_grid_pts)
    rhs_x[(nb_grid_pts-1)//3] = -1/diffusion_const
    rhs_x[2*(nb_grid_pts-1)//3] = 1/diffusion_const
    
    # Mittelwertbedinung in rhs berücksichtigen
    rhs_x[nb_grid_pts-1] = concentration_average * (nb_grid_pts-1)
    
    # Lösung der Diffusionsgleichung
    concentration_coeff_x = FEM_Laplace_Linear_1D_periodic(nb_grid_pts, dx, rhs_x)
    
    # Lösung plotten
    x = np.linspace(0, length, nb_grid_pts)
    ax.plot(x, concentration_coeff_x, linestyle=linestyles[i], marker=markerstyles[i],
            color=colors[i+1], label='FEM: N={}'.format(nb_grid_pts))

# Legende
ax.legend()
plt.show()
```


![png](output_32_0.png)


<div class="alert alert-success">
Es fällt auf, dass die analytische Lösung und die zwei FEM Lösungen für unterschiedliche Diskretisierungen übereinstimmen. Das liegt zum einen daran, dass die analytische Lösung linear ist und wir lineare Basisfunktionen gewählt haben. Zum anderen liegt es an der Wahl $N=3N'+1$, die bewirkt, dass die Knicke in der Lösungsfunktion richtig dargestellt werden können.
<br>
Wenn die Dirac-Impulse nicht genau auf den Knotenpunkten liegen würden, dann würde man erwarten, dass die Spitzen der Knicke abgeschnitten werden. Wenn man dann die Diskretisierung verfeinert, dann wird der abgeschnittene Bereich immer kleiner, so dass sich auch dann die FEM-Lösungen der analytischen Lösung annähern werden.
</div>

# Aufgabe 4 (16 Punkte)
## Finite-Elemente mit Dirichlet- und Neumann-Randbedingungen
In dieser Aufgabe betrachten wir die Diffusionsgleichung mit einer Dirichlet-Randbedingung bei $x=0$ und einer Neumann-Randbedingung bei $x=L$:
\begin{align}
c(x=0) &= c_0  \quad\text{(Dirichlet)}\\
\left.\frac{\partial c}{\partial x}\right\vert_{x=L} &= c'_L \quad\text{(Neumann)}
\end{align}

![openHalfspaceDiffusion1d.svg](openHalfspaceDiffusion1d.svg)

Physikalisch entspricht dies einem System, dass auf der einen Seite an ein unendliches Reservoir, in dem die Konzentration immer gleich bleibt, angeschlossen ist, während auf der anderen Seite ein konstanter Teilchenstrom in bzw. aus dem System fließt.

Zur Lösung mit Finiten Elementen wählen wir die gleiche Diskretisierung und die gleichen Basisfunktionen wie in Aufgabe 2.3.

### 4.1 Randbedingungen (2 Punkte)
Stellen Sie die Gleichungen für die Koeffizienten $a_i$ auf, die die Dirichlet und die Neumann Randbedingungen beschreiben. Setzen Sie dabei für den Quellterm:
1. $f(x) = -\delta\left(x - \frac{L}{3} \right) + \delta\left(x - \frac{2L}{3} \right)$
2. $f(x) = f_0$

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Dirichlet Randbedingung:
\begin{equation}
c(0) = a_0 = c_0
\end{equation}

Neumann Randbedingung:
<br>
Wir betrachten die Glg. $\ref{eq:Diffusion_Galerkin}$ für $\varphi_{N-1}$:
\begin{equation}
D \left( \varphi_{N-1}(L) \sum_i a_i \left. \frac{\partial \varphi_i(x)}{\partial x}\right\vert _{x=L} - \varphi_{N-1}(0) \sum_i a_i \left. \frac{\partial \varphi_i(x)}{\partial x}\right\vert _{x=0}\right) - D\sum_i a_i \int_0^L dx \; \frac{\partial \varphi_{N-1}(x)}{\partial x}\frac{\partial \varphi_i(x)}{\partial x} = \int_0^L dx \; \varphi_{N-1}(x) f(x)
\end{equation}

\begin{equation}
\Leftrightarrow D c'_L - Da_{N-2} \int_0^L dx \; \left(\frac{\partial \varphi_{N-1}(x)}{\partial x}\frac{\partial \varphi_{N-2}(x)}{\partial x}\right) - Da_{N-1} \int_0^L dx \; \frac{\partial \varphi_{N-1}(x)}{\partial x}\frac{\partial \varphi_{N-1}(x)}{\partial x} = \int_0^L dx \; \varphi_{N-1}(x) f(x)
\end{equation}

\begin{equation}
\Leftrightarrow \frac{D}{\Delta x} a_{N-2} - \frac{D}{\Delta x} a_{N-1} = - Dc_L' + \int_0^L dx \; \varphi_{N-1}(x) f(x)
\end{equation}

<br>
1. Quellterm: Für zwei Delta-Distributionen als Quellterm ist die rechte Seite dieser Gleichung:
\begin{equation}
\begin{aligned}
- Dc_L' + \int_0^L \varphi_{N-1}(x) f(x) dx &= \int_0^L dx \; \left(-\varphi_{N-1}(x) \delta\left(x+\frac{L}{3}\right) \right) + \int_0^L dx \; \left(\varphi_{N-1}(x) \delta(x+\frac{2L}{3}) \right) \\
&= - Dc_L' -\varphi_{N-1}\left(\frac{L}{3}\right) + \varphi_{N-1}\left(\frac{2L}{3}\right) \\
&= - Dc_L' \qquad \text{für } N \geq 4
\end{aligned}
\end{equation}
Die vollständig diskretisierte Neumann Randbedingung ist also:
\begin{equation}
\frac{D}{\Delta x} a_{N-2} - \frac{D}{\Delta x} a_{N-1} = - Dc_L'
\end{equation}
\begin{equation}
\Leftrightarrow \qquad \frac{1}{\Delta x} a_{N-2} - \frac{1}{\Delta x} a_{N-1} = - c_L'
\end{equation}

<br>
2. Quellterm:
Für einen konstanten Quellterm ist die rechte Seite der diskretisierten Neumann-Randbedingung:
\begin{equation}
\begin{aligned}
- Dc_L' + \int_0^L \varphi_{N-1}(x) f(x) dx &= - Dc_L' + f_0\int_0^L dx \; \varphi_{N-1}(x) = - Dc_L' + \frac{f_0 \Delta x}{2}
\end{aligned}
\end{equation}
Die vollständig diskretisierte Neumann Randbedingung ist also:
\begin{equation}
\frac{D}{\Delta x} a_{N-2} - \frac{D}{\Delta x} a_{N-1} = - Dc_L' + \frac{f_0 \Delta x}{2}
\end{equation}
\begin{equation}
\Leftrightarrow \qquad \frac{1}{\Delta x} a_{N-2} - \frac{1}{\Delta x} a_{N-1} = - c_L' + \frac{f_0 \Delta x}{2D}
\end{equation}
</div>

### 4.2 Numerische Lösung (14 Punkte)
Beachten Sie bitte die Hinweise am Anfang des Übungsblattes!

Schreiben Sie eine python-Funktion, um die Diffusionsgleichung mit einer Dirichlet- und einer Neumann-Randbedingung mit linearen Finiten Elementen zu lösen. Diese Funktion sollte als Argumente die Anzahl der Gitterpunkte $N$, den Abstand zwischen zwei Gitterpunkten $dx$ und einen Vektor mit der bereits diskretisierten rechten Seite des Problems erwarten. Ein zusätzliches Argument sollte angeben, ob die Systemmatrix zurückgegeben wird oder nicht. Verwenden Sie also bitte die Schittstelle

```python
def FEM_Laplace_Linear_1D(nb_grid_pts, dx, rhs_x, return_system_matrix=False):
    """
    Function to solve the 1D Laplace equation with a Dirichlet boundary condition
    and a Neumann boundary condition using a regular grid and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    return_system_matrix: boolean
        True if the system matrix should be returned. Default is False.
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized problem at each grid point
    system_matrix_xx: numpy.ndarray((nb_grid_pts, nb_grid_pts)) of floats
        System matrix of the discretized problem. Is only returned if the argument
        return_system_matrix is True.
    """
```


Nutzen Sie Ihre Funktion, um 4 Plots zu erstellen, auf denen Folgendes dargestellt wird:
* Lösung der Diffusionsgleichung mit zwei Delta-Distributionen als Quellterm: FEM-Lösung für N=4, N=7 und N=10 darstellen.
* Lösung der Diffusionsgleichung mit konstantem Quellterm: FEM-Lösung für N=4, N=7 und N=10 sowie die analytische Lösung
* Struktur der Systemmatrix für N=4, N=7 und N=10. Verwenden Sie dafür die Funktion matplotlib.pyplot.spy (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.spy.html). 
* Ableitung der Konzentration nach $x$ für einen konstanten Quellterm: Ableitung der FEM-Lösungen für N=4, N=7 und N=10 sowie die Ableitung der analytischen Lösung.

Kommentieren Sie jeweils kurz, was auf den Plots zu beobachten ist.

Verwenden Sie folgende Werte für die Parameter:
* $D = 0.8\frac{\mathrm{m}^2}{\mathrm{s}}$
* $L = 3\mathrm{m}$
* $c_0 = 2\mathrm{m}^{-3}$
* $c'_L = 0.7\mathrm{m}^{-4}$
* $f_0 = 0.5\mathrm{m}^{-3}\mathrm{s}^{-1}$

Hinweis: Die analytische Lösung können Sie durch Integration bestimmen.

<div class="alert alert-success">
<b>Lösung:</b>
</div>


```python
### ----- Funktion zur Lösung der Laplacegleichung mit linearen Finiten Elementen ----- ###
def FEM_Laplace_Linear_1D(nb_grid_pts, dx, rhs_x, return_system_matrix=False):
    """
    Function to solve the 1D Laplace equation with a Dirichlet boundary condition
    and a Neumann boundary condition using a regular grid and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    return_system_matrix: boolean
        True if the system matrix should be returned. Default is False.
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized problem at each grid point
    system_matrix_xx: numpy.ndarray((nb_grid_pts, nb_grid_pts)) of floats
        System matrix of the discretized problem. Is only returned if the argument
        return_system_matrix is True.
    """
    # Systemmatrix aufstellen
    d = np.full(nb_grid_pts-1, 1/dx)
    system_matrix_xx = np.diag(d, -1) - 2/dx  * np.eye(nb_grid_pts) + np.diag(d, 1)
    
    # Dirichlet Randbedingung bei x=0
    system_matrix_xx[0, 0] = 1
    system_matrix_xx[0, 1] = 0
    
    # Neumann Randbedingung
    system_matrix_xx[nb_grid_pts-1, nb_grid_pts-1] = - 1/dx
    
    # Gleichungssystem lösen
    func_x = np.linalg.solve(system_matrix_xx, rhs_x)
    
    if return_system_matrix:
        return func_x, system_matrix_xx
    else:
        return func_x
```


```python
### ----- 1D Diffusionsgleichung mit Dirichlet + Neumann-Randbedingung ----- ###
# --- Parameter definieren --- #
length = 3
diffusion_const = 0.8 # Diffusionskonstante
concentration_0 = 2 # Dirichlet RB bei x=0
concentration_diff_1 = 0.7 # Neumann RB bei x=L
quellterm_constant = 0.5

N_list = np.array([3, 2, 1])
nb_grid_pts_list = 3*N_list + 1 # Anzahl Gitterpunkte

# --- Plots vorbereiten --- #
# Plot Lösung Diffusionsglg. vorbereiten
fig, ax = plt.subplots(1, 2, figsize=(10*1.5, 5*1.5))
plt.subplots_adjust(top=0.9)
fig.suptitle('FEM-Lösung der 1D Diffusionsgleichung: Dirichlet und Neumann RB', fontsize=15)
ax[0].set_xlabel(r'Position $x$ (m)', fontsize=13)
ax[0].set_ylabel(r'Konzentration $c$ (1/$\mathrm{m}^3$)', fontsize=13)
ax[1].set_xlabel(r'Position $x$ (m)', fontsize=13)
ax[1].set_ylabel(r'Konzentration $c$ (1/$\mathrm{m}^3$)', fontsize=13)
ax[0].set_title('Delta-Distributionen als Quellterm', fontsize=13)
ax[1].set_title('Konstanter Quellterm', fontsize=13)

linestyles = ['--', ':', '-.']
markerstyles = ['o', 'v', '^']
markersize = 9
colors = ['blue', 'black', 'green']

# Plot Struktur Systemmatrix vorbereiten
fig_struktur, ax_struktur = plt.subplots(1, len(nb_grid_pts_list), figsize=(8, 3))
fig_struktur.suptitle('Struktur der Systemmatrix für lineare FEM', fontsize=15)
plt.subplots_adjust(top=0.7)

# Plot Ableitung vorbereiten
fig_diff, ax_diff = plt.subplots()
plt.subplots_adjust(top=0.85)
fig_diff.suptitle('Ableitung der 1D Diffusionsgleichung \n (Dirichlet und Neumann RB mit konst.Quellterm)', 
                  fontsize=15)
ax_diff.set_xlabel(r'Position $x$ (m)', fontsize=13)
ax_diff.set_ylabel(r'$dc/dx$ (1/$\mathrm{m}^4$)', fontsize=13)

# --- Analytisch Lösung --- #
# Lösung der Diffusionsgleichung mit konstantem Quellterm
x = np.linspace(0, length, 100)
concentration_ana = 0.5*quellterm_constant/diffusion_const * x**2 
concentration_ana += (concentration_diff_1 - quellterm_constant/diffusion_const*length) * x
concentration_ana += concentration_0
ax[1].plot(x, concentration_ana, linewidth=2, color='red', label='Analytisch')

# Ableitung der analytischen Lösung mit konstantem Quellterm
concentration_diff_ana = quellterm_constant/diffusion_const * x 
concentration_diff_ana += concentration_diff_1 - quellterm_constant/diffusion_const*length
ax_diff.plot(x, concentration_diff_ana, '-', linewidth=2, color='red', label='Analytisch')

# --- FEM Lösung --- #
for i, nb_grid_pts in enumerate(nb_grid_pts_list):
    dx = length/(nb_grid_pts-1)
    
    # --- Delta-Distributionen als Quellterm --- #
    # Rechte Seite der Gleichung ausrechnen
    rhs_x = np.zeros(nb_grid_pts)
    rhs_x[(nb_grid_pts-1)//3] = -1/diffusion_const
    rhs_x[2*(nb_grid_pts-1)//3] = 1/diffusion_const
    
    # Randbedingungen in rhs berücksichtigen
    rhs_x[0] = concentration_0
    rhs_x[nb_grid_pts-1] = - concentration_diff_1
    
    # Lösung der Diffusionsgleichung
    concentration_coeff_x = FEM_Laplace_Linear_1D(nb_grid_pts, dx, rhs_x)
    
    # Lösung plotten
    x = np.linspace(0, length, nb_grid_pts)
    ax[0].plot(x, concentration_coeff_x, color=colors[i], linestyle=linestyles[i], marker=markerstyles[i], 
            markersize=markersize, linewidth=2, label='N={}'.format(nb_grid_pts))
    
    # --- Konstanter Quellterm + Struktur der Systemmatrix --- #
    # Rechte Seite der Gleichung ausrechnen
    rhs_x = np.full(nb_grid_pts, quellterm_constant*dx/diffusion_const)
    
    # Randbedingungen in rhs berücksichtigen
    rhs_x[0] = concentration_0
    rhs_x[nb_grid_pts-1] = rhs_x[nb_grid_pts-1]/2 - concentration_diff_1
    
    # Lösung der Diffusionsgleichung
    concentration_coeff_x, system_matrix_xx = FEM_Laplace_Linear_1D(nb_grid_pts, dx, rhs_x, return_system_matrix=True)
    
    # Lösung plotten
    x = np.linspace(0, length, nb_grid_pts)
    ax[1].plot(x, concentration_coeff_x, color=colors[i], linestyle=linestyles[i], marker=markerstyles[i], 
            markersize=markersize, linewidth=2, label='FEM: N={}'.format(nb_grid_pts))
    
    # Struktur der Systemmatrix plotten
    ax_struktur[len(nb_grid_pts_list)-1-i].spy(system_matrix_xx)
    ax_struktur[len(nb_grid_pts_list)-1-i].set_title('FEM: N={}'.format(nb_grid_pts), fontsize=13)
    
    # --- Konstanter Quellterm: Ableitung --- #
    concentration_diff_x = -1/dx * concentration_coeff_x + 1/dx * np.roll(concentration_coeff_x, -1)
    concentration_diff_x[nb_grid_pts-1] = concentration_diff_1
    ax_diff.step(x, concentration_diff_x, where='post', color=colors[i], linestyle=linestyles[i], 
            linewidth=2, label='FEM: N={}'.format(nb_grid_pts))

# Legenden
ax[0].legend()
ax[1].legend()
ax_diff.legend()

plt.show()
```


![png](output_42_0.png)



![png](output_42_1.png)



![png](output_42_2.png)


<div class="alert alert-success">
Auf dem ersten Plot sieht man, dass die Lösung mit Delta-Distributionen als Quellterm wie im periodischen Raum stückweise linear ist. Da wir lineare Basisfunktionen gewählt haben, ist schon eine sehr grobe Diskretisierung ausreichend, um die Lösung korrekt darzustellen und eine Verfeinerung der Diskretisierung bringt keine weiteren Informationen. Anders sieht es aus, wenn wir den Fall mit einem konstanten Quellterm betrachten: Dann ist die Lösung nichtlinear und deshalb können die linearen Basisfunktionen die Lösungsfunktion nicht genau wiedergeben. Hier bringt eine Verfeinerung der Diskretisierung, dass die FEM-Lösung allmählich zu der analytischen Lösung konvergiert.
<br>
Auf dem zweiten Plot erkennt man, dass die Systemmatrix eine dünnbesetzte Matrix ist: Nur ein kleiner Teil der Einträge ist nicht 0. Je feiner die Diskretisierung, desto größer der Anteil an 0-Einträgen. Außerdem ist die Systemmatrix eine Dreibandmatrix, da nur auf der Hauptdiagonale und den beiden ersten Nebendiagonalen Einträge auftreten, die nicht null sind.
<br>
Auf dem dritten Plot kann man beobachten, dass die FEM-Lösung zwar die Werte der Ableitung der analytischen Lösung relativ gut annähert, aber nicht die Form der analytischen Ableitung: Da wir lineare Basisfunktionen gewählt haben, ist die Ableitung der FEM-Lösung eine Stufenfunktion und also immer nur stückweise stetig, während die analytische Ableitung eine stetige Funktion, in diesem Fall eine Gerade, ist. Daran ändert sich auch nichts, wenn die Anzahl der Finiten Elemente erhöht wird.
</div>

# Aufgabe 5 (13 Punkte)
## Finite-Elemente Lösung der linearisierten Poisson-Boltzmann Gleichung
Nachdem wir die Grundlagen der FEM betrachtet haben, wollen wir jetzt zu unserem Modell-Problem zurückkehren und die linearisierte Poisson-Boltzmann-Gleichung für den symmetrischen Elektrolyten in 1D lösen, die in Übungsblatt 1, Aufgabe 7 hergeleitet wurde. In 1D lautet sie
\begin{equation}
\frac{\partial^2 \Phi(x)}{\partial x^2} = \frac{2 c^{\infty} q^2}{\varepsilon k_B T} \Phi(x) = \lambda^{-2} \Phi(x) \, \text{,}
\label{eq:A5_Poisson_Boltzmann}
\end{equation}
wobei $\Phi(x)$ das elektrostatische Potential, $\varepsilon$ die Permittivität, $k_B$ die Boltzmann-Konstante, $q$ der Ladungsbetrag der betrachteten Ionen, $$T$$ die Temperatur, $c^{\infty}$ die Referenzkonzentration der Ionen und $\lambda$ die Debye-Länge ist.

Wir betrachten die Gleichung auf einem endlichen Gebiet $[0; L]$. An den Rändern von diesem Gebiet befinden sich zwei inerte Elektroden mit elektrostatischem Potential $\Phi_0$ und $\Phi_1$, bei dem System könnte es ich also um einen Plattenkondensator handeln.

![electrochemicalCell1dLinearizedPB.svg](electrochemicalCell1dLinearizedPB.svg)

### 5.1 Schwache Formulierung (2 Punkte)
Leiten Sie die schwache Formulierung von Glg. $\ref{eq:A5_Poisson_Boltzmann}$ her und verringern Sie die Anforderung an die Differenzierbarkeit von $\Phi(x)$.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
Seien $v(x)$ die Testfunktionen. Dann folgt aus Glg. $\ref{eq:A5_Poisson_Boltzmann}$:
$$
\int_0^L dx \; v(x) \left( \frac{\partial^2 \Phi(x)}{\partial x^2} - \frac{1}{\lambda^2}\Phi \right) = \int_0^L dx \; v(x) \cdot 0 = 0
$$
Mit partieller Integration folgt die schwache Formulierung:
\begin{equation}
\begin{aligned}
\left[ v(x) \frac{\partial \Phi(x)}{\partial x}\right]_0^L - \int_0^L dx\; \left( \frac{\partial v(x)}{\partial x}\frac{\partial \Phi(x)}{\partial x} + \frac{1}{\lambda^2}\Phi(x)v(x)\right) = 0
\end{aligned}
\label{eq:A5_schwache_Form}
\end{equation}
</div>

### 5.2 Galerkin - Methode (1 Punkt)
Nutzen Sie die Galerkin Methode, um ein System von Gleichungen für die Koeffizienten $a_i$ herzuleiten, wenn $\Phi(x) = \sum_i a_i \varphi_i(x)$ in einem Funktionensystem mit Basisfunktionen $\varphi_i$ dargestellt wird.

<div class="alert alert-success">
<b>Lösung:</b>
<br>
In Glg. $\ref{eq:A5_schwache_Form}$ werden $\Phi(x) = \sum_i a_i \varphi_i(x)$ und die Testfunktionen $v(x) = \varphi_j(x)$ eingesetzt:
$$
\begin{aligned}
\left[ \varphi_j(x) \frac{\partial \Phi(x)}{\partial x}\right]_0^L - \sum_i a_i \int_0^L dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_i(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_i(x)\varphi_j(x)\right) = 0 \qquad \forall j
\end{aligned}
$$
</div>

### 5.3 Diskretisierung (3 Punkte)
Als Diskretisierung wollen wir $N$ gleichmäßig verteilte Gitterpunkte verwenden. Als Basisfunktionen wählen wir die stückweise linearen Hutfunktionen aus Aufgabe 2.3

Stellen Sie die diskretisierten Gleichungen für die inneren Testfunktionen auf.


<div class="alert alert-success">
<b>Lösung:</b>
<br>
Für $j \in \{1; 2; ...; N-2\}$ sind die Testfunktionen am Rand null, so dass der Randterm aus Glg. wegfällt. Außerdem ist $\varphi_i(x)\varphi_j(x)=0$ und $\frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_i(x)}{\partial x}=0$, außer wenn $i=j-1$, $i=j$ oder $i=j+1$. Es bleibt also:
$$
\begin{aligned}
0 &=&& - a_{j-1} \int_0^L dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j-1}(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_{j-1}(x)\varphi_j(x)\right) - a_j \int_0^L dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_j(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_j(x)\varphi_j(x)\right) \\
&&& - a_{j+1} \int_0^L dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j+1}(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_{j+1}(x)\varphi_j(x)\right) \\
&=&& - a_{j-1} \int_{x_{j-1}}^{x_j} dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j-1}(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_{j-1}(x)\varphi_j(x)\right) - a_j \int_{x_{j-1}}^{x_j} dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_j(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_j(x)\varphi_j(x)\right) \\
&&& - a_j \int_{x_{j}}^{x_{j+1}} dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_j(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_j(x)\varphi_j(x)\right) - a_{j+1} \int_{x_{j}}^{x_{j+1}} dx\; \left( \frac{\partial \varphi_j(x)}{\partial x}\frac{\partial \varphi_{j+1}(x)}{\partial x} + \frac{1}{\lambda^2}\varphi_{j+1}(x)\varphi_j(x)\right) \\
&=&& -a_{j-1}\left( \frac{1}{\Delta x^2} \left( -x_j + x_{j-1}\right) + \frac{1}{\lambda^2}\frac{1}{\Delta x^2} \left( \frac{1}{6}x_{j}^3 - \frac{1}{2}x_j^2 x_{j-1} - \frac{1}{6}x_{j-1}^3 + \frac{1}{2}x_j x_{j-1}^2\right)\right) \\
&&& -a_{j}\left( \frac{1}{\Delta x^2} \left( -x_{j+1} + x_{j-1}\right) + \frac{1}{\lambda^2}\frac{1}{\Delta x^2} \left( x_j^2 x_{j+1} - x_j^2 x_{j-1} - x_j x_{j+1}^2 + x_j x_{j-1}^2 + \frac{1}{3}x_{j+1}^3 - \frac{1}{3}x_{j-1}^3\right)\right) \\
&&& -a_{j+1}\left( \frac{1}{\Delta x^2} \left( x_j - x_{j+1}\right) + \frac{1}{\lambda^2}\frac{1}{\Delta x^2} \left( \frac{1}{6}x_{j+1}^3 - \frac{1}{2}x_{j+1}^2 x_{j} - \frac{1}{6}x_{j}^3 + \frac{1}{2}x_{j+1} x_{j}^2\right)\right) \\
&=&& a_{j-1}\left( \frac{1}{\Delta x} - \frac{1}{6}\frac{\Delta x}{\lambda^2}\right) - a_{j}\left( \frac{2}{\Delta x} + \frac{2}{3}\frac{\Delta x}{\lambda^2}\right) + a_{j+1}\left( \frac{1}{\Delta x} - \frac{1}{6}\frac{\Delta x}{\lambda^2}\right)
\end{aligned}
$$
Dabei ist $\Delta x=\frac{L}{N-1}$ der Abstand zwischen zwei Gitterpunkten.
</div>

### 5.4 Randbedingungen (1 Punkt)
Um welche Art von Randbedingungen handelt es sich? Stellen Sie die Gleichungen für die Koeffizienten $a_i$ auf, die die Randbedingungen beschreiben. 

<div class="alert alert-success">
<b>Lösung:</b>
<br>
An Plattenkondensatoren ist das elektrostatische Potential fest vorgegeben. An beiden Rändern liegt also eine Dirichlet Randbedingung vor:
$$
\Phi(0) = a_0 = \Phi_0
$$
$$
\Phi(L) = a_{N-1} = \Phi_1
$$
</div>

### 5.5 Numerische Lösung (6 Punkte)
Beachten Sie bitte die Hinweise am Anfang des Übungsblatts!

Schreiben Sie eine python-Funktion, um die 1D-Poisson-Boltzmann Gleichung mit zwei Dirichlet-Randbedingungen mit linearen Finiten Elementen zu lösen. Diese Funktion sollte als Argumente die Anzahl der Gitterpunkte $N$, den Abstand zwischen zwei Gitterpunkten $l$, die Debye-Länge $\lambda = \sqrt \frac{\varepsilon k_B T}{2 c^\infty q^2}$ und einen Vektor mit der bereits diskretisierten rechten Seite des Problems nehmen. Verwenden Sie also die Schnittstelle

```python
def FEM_Poisson_Boltzmann_1D(nb_grid_pts, dx, debye_length, rhs_x):
    """
    Function to solve the 1D Poisson Boltzmann equation with a Dirichlet 
    boundary condition and a Neumann boundary condition using a regular grid 
    and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    debye_length: float
        Debye length
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized problem at each grid point
    """
```

Nutzen Sie Ihre Funktion, um einen Plot mit der Lösung der 1D-Poisson-Boltzmann Gleichung zu erstellen. Der Plot sollte enthalten:
* Analytische Lösung aus Übungsblatt 1, Aufgabe 7: \begin{equation}\Phi(x) = K_1 \exp{\left( \frac{1}{\lambda}x\right)} + K_2\exp{\left( -\frac{1}{\lambda}x\right)}\end{equation} mit $K_1 = \left( \Phi_1 - \Phi_0 \exp{\left( -\frac{L}{\lambda}\right)}\right)\left( \exp{\left( \frac{L}{\lambda}\right)} - \exp{\left( -\frac{L}{\lambda}\right)} \right)^{-1}$ und $K_2 = \Phi_0 - K_1$
* FEM Lösung für N=4
* FEM Lösung für N=8
* FEM Lösung für N=16

Verwenden Sie folgende Werte für die Parameter: 
* $L = 3 \mathrm{nm}$
* $\Phi_0 = -0.01 \mathrm{V}$
* $\Phi_1 = 0.04 \mathrm{V}$
* $c^{\infty} = 10^{3}\mathrm{mol}\, \mathrm{m}^{-3}$
* $q = e = 1.602\cdot 10^{-19}\mathrm{A} \mathrm{s}$
* $\varepsilon = 80 \cdot 8.85\cdot 10^{-12}\mathrm{A} \, \mathrm{s} \, \mathrm{V}^{-1} \, \mathrm{m}^{-1}$
* $k_B = 1.380649\cdot 10^{-23} \mathrm{J} \, \mathrm{K}^{-1}$
* $T = 293.15 \mathrm{K}$
* Avogrado-Zahl $N_A = 6.022\cdot 10^{23}$

<div class="alert alert-success">
<b>Lösung:</b>
</div>


```python
### ----- Funktion: Lösung 1D Poisson-Boltzmann Glg. mit linearen Finiten Elementen ----- ###
def FEM_Poisson_Boltzmann_1D(nb_grid_pts, dx, debye_length, rhs_x):
    """
    Function to solve the 1D Poisson Boltzmann equation with a Dirichlet boundary condition
    and a Neumann boundary condition using a regular grid and linear finite elements.
    
    Arguments
    ---------
    nb_grid_pts: int
        Number of grid points
    dx: float
        Length between two adjacent grid points
    debye_length: float
        Debye length
    rhs_x: numpy.ndarray(nb_grid_pts) of floats
        Right-hand-side vector
    
    Returns
    -------
    func_x: numpy.ndarray(nb_grid_pts) of floats
        Solution of the discretized problem at each grid point
    """
    # Systemmatrix aufstellen
    d = np.full(nb_grid_pts-1, 1/dx - 1/debye_length**2 * dx/6)
    system_matrix_xx = np.diag(d, -1) - (2/dx + 2/3*1/debye_length**2*dx) * np.eye(nb_grid_pts) + np.diag(d, 1)
    
    # Dirichlet Randbedingungen
    system_matrix_xx[0, 0] = 1
    system_matrix_xx[0, 1] = 0
    system_matrix_xx[nb_grid_pts-1, nb_grid_pts-1] = 1
    system_matrix_xx[nb_grid_pts-1, nb_grid_pts-2] = 0
    
    # Gleichungssystem lösen
    potential_x = np.linalg.solve(system_matrix_xx, rhs_x)
    
    return potential_x
```


```python
### ----- FEM-Lösung der 1D Poisson-Boltzmann Gleichung ----- ###
# --- Definitionen --- #
# Parameter
avogrado_constant = 6.022e23
length = 3 * 1e-9
potential_0 = -0.01 # Dirichlet RB bei x=0
potential_1 = 0.04 # Dirichlet RB bei x=length
concentration_bulk = 1e3*avogrado_constant
elementary_charge = 1.602e-19
permittivity = 80*8.85e-12
boltzmann_constant = 1.380649e-23
temperatur = 293.15

# Anzahl Gitterpunkte
nb_grid_pts_list = [4, 8, 16]

# Debye Länge
debye_length = np.sqrt(permittivity*boltzmann_constant*temperatur / concentration_bulk / elementary_charge**2 / 2)

# --- Plot vorbereiten --- #
fig, ax = plt.subplots()
plt.subplots_adjust(top=0.85)
title = 'Lösung der 1D Poisson-Boltzmann-Gleichung \n (mit 2 Dirichlet-Randbedingungen)'
fig.suptitle(title, fontsize=15)
ax.set_xlabel(r'Position $x$ (nm)', fontsize=13)
ax.set_ylabel(r'Elektrostatisches Potential $\Phi$ (V)', fontsize=13)

linestyles = ['--', '-.', ':', '-']
markerstyles = ['o', 'v', '^', 'o']
markersize = 1
colors = ['red', 'blue', 'limegreen', 'black', 'black']

# --- Analytische Lösung --- #
x = np.linspace(0, length, 101)
const_1 = (potential_1 - potential_0*np.exp(-1/debye_length*length))
const_1 = const_1 / (np.exp(1/debye_length*length) - np.exp(-1/debye_length*length))
const_2 = potential_0 - const_1
potential_ana_x = const_1 * np.exp(1/debye_length*x) + const_2 * np.exp(-1/debye_length*x)

ax.plot(x*1e9, potential_ana_x, linewidth=2, color='red', label='Analytical')

# --- FEM Lösung --- #
for i, nb_grid_pts in enumerate(nb_grid_pts_list):
    dx = length/(nb_grid_pts-1)

    # Rechte Seite der Gleichung mit Randbedingungen aufstellen
    rhs_x = np.zeros(nb_grid_pts)
    rhs_x[0] = potential_0
    rhs_x[nb_grid_pts-1] = potential_1
    
    # FEM-Funktion aufrufen
    potential_FEM_coeff_x = FEM_Poisson_Boltzmann_1D(nb_grid_pts, dx, debye_length, rhs_x)
    
    # Lösung plotten
    x = np.linspace(0, length, nb_grid_pts)
    ax.plot(x*1e9, potential_FEM_coeff_x, linestyle=linestyles[i], marker=markerstyles[i], 
            markersize=markersize, linewidth= 2, color=colors[i+1], 
            label='N={}'.format(nb_grid_pts))

# - Plot fertig stellen - #
# Legende
ax.legend()

plt.show()
```


![png](output_58_0.png)



