---
layout: default
title:  "Übungsblatt 1 [28. Nov.]"
parent: Übungsaufgaben
categories: homework
author : Lars Pastewka
nav_order: 1
---
# Übungsblatt 1: Einführung des Modellproblems

<div class="alert alert-warning">
Die Abgabe von Arbeitsblatt 1 bis 4 ist verpflichtend und konstituiert die Studienleistung der Veranstaltung <b>Simulationstechniken</b>. Die Arbeitsblätter führen von der mathematischen Formulierung eines Modellproblems hin zur numerischen Lösung dieses Problems und bauen aufeinander auf. Zum Bestehen der Veranstaltung müssen auf <b>jedem</b> Blatt mindestens 50% der erzielbaren Punkte erreicht werden.
</div>
<br>

<div class="alert alert-danger">
<b>Geben Sie bei allen Aufgaben die Lösungswege und Zwischenergebnisse mit an. Das Endergebnis alleine ist nicht ausreichend!</b> Wir empfehlen Ihnen die Nutzung von Python und Jupyter-Notebooks. Sollten Sie ein Jupyter-Notebook verwenden, dann können Sie dieses einfach direkt als Lösung bei uns einreichen. In allen anderen Fällen erzeugen Sie bitte ein PDF und legen die numerischen Codes als separate Datei dazu.
</div>

# Aufgabe 1 (4 Punkte)
## Der Diffusionsstrom

Die Diffusion führt ohne äußere Einwirkungen, wie bspw. ein Kraftfeld, zum Ausgleich von Konzentrationsunterschieden. Im Laufe des Diffusionsprozessen kommt es zu einer gleichmäßigen Verteilung der Teilchen. Bei den Teilchen kann es sich um Atome, Moleküle, Ladungsträger, etc. handeln. Die Diffusionsgleichung spielt für die Transportphänomene eine große Rolle und wird für die Beschreibung vieler unterschiedlicher Systeme eingesetzt (bspw. für Ladungstransport in Halbleitern oder Elektrolyten). Im Allgemeinen beruht die Diffusion auf der ungerichteten Zufallsbewegung von Teilchen. Aus dieser Zufallsbewegung soll in dieser Aufgabe die Diffusionsgleichung hergeleitet werden. Gehen Sie dazu von folgenden Annahmen aus:

* Die Teilchen können sich nur in einer Dimension bewegen.
* Die Sprungweite $$h$$ der Teilchen ist konstant.
* Die Wahrscheinlichkeit für Sprung nach rechts ist gegeben durch $$q = \frac{1}{2}$$.
* Die Wahrscheinlichkeit für Sprung nach links ist gegeben durch $$p = \frac{1}{2}$$.
* Ein Sprung dauert eine Zeitspanne $$\tau$$.
* Wenn $$P(x,t)$$ die Wahrscheinlichkeit beschreibt, ein Teilchen am Ort $$x$$ und zur Zeit $$t$$ zu finden, dann ist die Wahrscheinlichkeit dieses zur Zeit $$t+\tau$$ zu finden gegeben durch $$\Rightarrow P(x, t+\tau) = qP(x+h,t)+pP(x-h,t)$$.

Zeigen Sie, wie sich hieraus das 1. Ficksche Gesetz in einer Dimension ergibt:
\begin{equation}
    \vec{j}_{c,\text{Diffusion}} = -D \frac{\textrm{d} c}{\textrm{d} x}
\end{equation}
Bitte nutzen Sie diese Gleichung für Aufgabe 3 unabhängig davon, ob Sie Aufgabe 1 bearbeitet haben.

# Aufgabe 2 (4 Punkte)
## Die Kontinuitätsgleichung

Bilanzieren Sie die Stoffmengenkonzentration $$c$$ über ein zweidimensionales Gebiet. Geben Sie die stationäre (zeitunabhängige) und instationäre (zeitabhängige) Gleichung an, die diese Bilanzierung beschreibt. Berücksichtigen Sie hierbei auch einen Quellterm, also die Produktion eines Stoffes, im zu bilanzierenden Gebiet.

**Hinweis:**
* Die zeitliche Änderung einer Größe in einem betrachteten Gebiet ergibt sich aus der Summe aus eingehenden und ausgehenden Strömen unter Berücksichtigung von Quelltermen

Ohne Quellterm wird die Bilanzgleichung als Kontinuitätsgleichung bezeichnet: $$\frac{\partial c}{\partial t} = -\nabla\cdot\vec{j}_c$$. Bitte verwenden Sie diese Gleichung für Aufgabe 3 unabhängig davon, ob Sie Aufgabe 2 bearbeitet haben.

# Aufgabe 3 (5 Punkte)
## Die Diffusionsgleichung

Leiten Sie ausgehend von dem 1. Fickschen Gesetz (siehe Aufgabe 1) und der instationären Kontinuitätsgleichung (siehe Aufgabe 2) die Diffusionsgleichung, auch bekannt als das 2. Ficksches Gesetz, her. Klassifizieren Sie die resultierende Differentialgleichung. (Bitte schauen Sie sich für die Klassifizierung das Kapitel 2 "Gleichungstypen" der Vorlesung an.)

**Hinweis:**
* Sie werden hierzu die eindimensionale Gleichung aus Aufgabe 1 auf zwei Dimensionen erweitern müssen.

# Aufgabe 4 (8 Punkte)
## Stationäre Lösung der Diffusionsgleichung

Betrachten Sie die eindimensionale stationäre Diffusionsgleichung unter Berücksichtigung eines Quellterms
\begin{equation}
\frac{\partial^2 c(x)}{\partial x^2} = \frac{1}{D}f(x)
\end{equation}
mit dem Quellterm
\begin{equation}
f(x) = -\delta(x-L/3)+\delta(x-2L/3)
\end{equation}
wobei $$\delta(x)$$ ein Dirac-Impuls ist.

1. Bestimmen Sie mit Hilfe der Fourier-Reihe eine Lösung der Differentialgleichung in einem periodischen Gebiet der Länge L. Diskutieren Sie zudem, was der Koeffizient $$c_0$$ der Fourier-Lösung bedeutet.

2. Bestimmen Sie zusätzlich eine analytische Lösung durch Integration.

3. Plotten Sie anschließend die Lösung der Fourier-Reihe. Schneiden Sie die Fourier-Reihe bei $$N = 1, 5, 10 und 20$$ Termen ab. Zeigen Sie dazu die Lösung durch Integration und vergleichen Sie die Ergebnisse. Nutzen Sie die folgenden Parameter zum plotten:
    * $$L = 3$$
    * $$D = 0.8$$

**Hinweise:**
* Für eine $$L-$$periodische Funktion $$s(x)$$ ist die Fourier-Reihe gegeben als $$s(x) = \sum_{n=-\infty}^{\infty}s_n \exp\left(\frac{i2\pi n x}{L}\right)$$. Diese Summe wird oft abgeschnitten, so dass sie von $$-N$$ bis $$N$$ läuft.
* Die Koeffizienten sind gegeben als $$s_n = \frac{1}{L}\int_{-L/2}^{L/2}\text{d}x\, s(x)\exp\left(\frac{-i2\pi n x}{L}\right)$$.
* Für das periodische Gebiet wird der Dirac-Impuls zu einem Dirac-Kamm.
* Die Integration eines Dirac-Impulses ist die Heaviside-Funktion
* Zur Bestimmung der Integrationskonstanten beachten Sie zudem, dass
    * aufgrund der Periodizität $$c(x) = c(x+L)$$ gelten muss
    * in diesem Fall der Mittelwert $$\frac{1}{L}\int_{0}^{L} \text{d}x\, c(x) = 0$$ gelten soll

# Aufgabe 5 (5 Punkte)
## Poisson-Nernst-Planck Gleichung

Ein Ion der Ladung $$q$$ erfährt in einem elektrischen Feld $$\vec{E}$$ die Coulomb-Kraft $$\vec{F}_C = q\vec{E} = - q \nabla \Phi$$. Unter der Annahme einer einfachen Kugelform steht einem solchen Teilchen in verdünnter Lösung der stokesche Strömungswiderstand $$\vec{F}_d = - 6 \pi \eta a \vec{v}$$ gegenüber, wobei es sich bei $$\eta$$ um die Viskosität der Lösung und bei $$a$$ um den effektiven Ionenradius handelt. $$\vec v$$ ist die Geschwindigkeit des Teilchens relativ zum Fluid. Der Fluid ist in Ruhe.

Aus diesen Kräften soll zunächst die Nernst-Planck-Gleichung hergeleitet werden. Gehen Sie dazu von einem stationären Kräftegleichgewicht ($$\vec{F}_C = - \vec{F}_d$$) aus und leiten Sie zuerst die Beziehung zwischen dem Driftstrom $$\vec{j}_{c,\text{Drift}}$$ und Diffusionskoeffizienten $$D$$ her. Die Nernst-Planck-Gleichung beschreibt die Bewegung von Ionen in einem elektrischen Feld, dabei ist $$\vec{j}_{c} = \vec{j}_{c,\text{Diffusion}} +\vec{j}_{c, Drift}$$. Setzen Sie den Ausdruck für den Teilchenstrom $$\vec{j}_{c}$$ in die Kontinuitätsgleichung (siehe Aufgabe 2) ein und geben Sie die instationäre Nernst-Planck-Gleichung an.

**Hinweise:**
* $$\vec{j}_{c,\text{Drift}} = c\vec{v}$$
* Die Ladungsträgerbeweglichkeit (auch Mobilität) ist gegeben durch $$\mu = \frac{q}{6\pi\eta a}$$
* Die Einstein-Smoluchowski-Beziehung verknüpft die Mobilität $$\mu$$ mit dem Diffusionskoeffizienten über $$\mu = \frac{q}{k_B T}D$$

In einem System mit $$N$$ Ionenspezies koppeln Poisson-Gleichung und Nernst-Planck-Gleichung über die Ladungsdichte
\begin{equation}
\rho = \sum_{i=1}^N q_i c_i
\end{equation}
Geben Sie die Poisson-Gleichung unter Verwendung des obigen Ausdrucks für die Ladungsdichte an.

# Aufgabe 6 (8 Punkte)
## Poisson-Boltzmann Gleichung

Leiten Sie die Poisson-Boltzmann-Gleichung her. Linearisieren Sie diese anschließend, indem Sie die Ladungsdichte mithilfe einer Taylor-Reihe für $$\Phi$$ nahe Null entwickeln und plotten Sie die 1D-Lösung.

**Hinweise**:
* Nutzen Sie den Ausdruck für die Ladungsdichte zur Koppelung von Poisson-Gleichung und Nernst-Planck-Gleichung aus Aufgabe 5.
* Nehmen Sie die Konzentrationsverteilung einer Spezies $$i$$ als Boltzmann-verteilt $$c_i = c_i^\infty \exp\left(\frac{-q_i \,\Phi}{k_B T}\right)$$ an. Wann ist das gerechtfertigt?
* Nutzen Sie eine Taylor-Reihe um $$\Phi = 0$$ (bis zur 1. Ordnung) um die Gleichung zu linearisieren.
* Gehen Sie spätestens ab hier vereinfachend von einem symmetrischen Elektrolyten aus, also $$N=2$$ Spezies mit $$q_1 = - q_2 = q$$ und $$c_1^\infty = c_2^\infty = c^\infty$$, wie z.B.  $$\mathrm{NaCl}$$.
* Identifizieren Sie in der linearisierten Gleichung die *Debye-Länge* $$\lambda = \sqrt{\frac{\varepsilon k_B T }{2q^2c^\infty}}$$. Was bedeutet diese Größe physikalisch?
* Bestimmen Sie die Integrationkonstanten mit folgenden Randbedingungen:
    * Das Potential an der linken Seite beträgt $$\Phi(x=0) = \Phi_0$$
    * Das Potential an der rechten Seite beträgt $$\Phi(x=L) = \Phi_1$$
    * Dabei ist $$L$$ der Abstand zwischen den Platten
    
Plotten Sie die Lösung der linearisierten Gleichung für 
* $$\Phi_0 = -1$$
* $$\Phi_1 = 1$$
* $$L = 1$$
* $$\frac{1}{\lambda^2} = 20$$
auf einem eindimensionalen Intervall, wie unten dargestellt.

![electrochemicalCell1dLinearizedPB.svg](electrochemicalCell1dLinearizedPB.svg)


Zeigen Sie (ausgehend von der nicht-linearen Poisson-Boltzmann-Gleichung) durch Einsetzen, dass $$\Phi = \frac{k_B T}{q}\ln(\cos^2(Kx))$$ mit $$K^2 = \frac{q^2 c_0}{2\varepsilon k_B T} = \frac{1}{4 \lambda^2}$$ eine Lösung der Differentialgleichung ist. Plotten Sie die nicht-lineare Lösung im Vergleich zur linearisierten Lösung und diskutieren Sie die Unterschiede.
