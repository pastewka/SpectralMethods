---
layout: default
title:  "Übungsblatt 1 [28. Nov.]"
parent: Übungsaufgaben
categories: homework
author : Lars Pastewka
nav_order: 1
---
#### Simulationstechniken - WS2020/21

# Übungsblatt 1: Einführung des Modellproblems

<div class="alert alert-warning">
Die Abgabe von Arbeitsblatt 1 bis 4 ist verpflichtend und konstituiert die Studienleistung der Veranstaltung <b>Simulationstechniken</b>. Die Arbeitsblätter führen von der mathematischen Formulierung eines Modellproblems hin zur numerischen Lösung dieses Problems und bauen aufeinander auf. Zum Bestehen der Veranstaltung müssen auf <b>jedem</b> Blatt mindestens 50% der erzielbaren Punkte erreicht werden.
</div>

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

<div class="alert alert-success">
<b>Lösung:</b>
\begin{align}
P(x, t+\tau) &= \frac{1}{2}P(x+h,t)+\frac{1}{2}P(x-h,t) \\
P(x, t+\tau) - P(x, t) &= \frac{1}{2}P(x+h,t) -P(x, t) +\frac{1}{2}P(x-h,t) \\
\frac{P(x, t+\tau) - P(x, t)}{\tau} &= \frac{\frac{1}{2}P(x+h,t) -P(x, t) +\frac{1}{2}P(x-h,t)}{\tau} \\
\frac{P(x, t+\tau) - P(x, t)}{\tau} &= \frac{\frac{1}{2}P(x+h,t) -P(x, t) +\frac{1}{2}P(x-h,t)}{\tau}\frac{h^2}{h^2} \\
\frac{P(x, t+\tau) - P(x, t)}{\tau} &= \frac{h^2}{2\tau}\frac{P(x+h,t) -2P(x, t) +P(x-h,t)}{h^2} \\
\end{align}
mit $$\tau \rightarrow 0$$, $$h \to 0$$ und $$\lim\limits_{h,\tau \to 0} \frac{h^2}{2\tau} = D_P$$
\begin{equation}
\frac{\partial P(x,t)}{\partial t} = D_P\frac{\partial^2 P(x,t)}{\partial x^2}
\end{equation}
    
Im Kontinuumsbereich ergibt sich 
\begin{equation}
\frac{\partial c(x,t)}{\partial t} = D_c\frac{\partial^2 c(x,t)}{\partial x^2}
\end{equation}
Unter Berücksichtigung der Kontinuitätsgleichung, die in Aufgabe 1 hergeleitet wurde ergibt sich 
\begin{align}
    -\nabla\cdot \vec{j}_c &= D_c\frac{\partial^2 c(x,t)}{\partial x^2} \\
    - \vec{j}_c &= D_c\frac{\partial c(x,t)}{\partial x}
\end{align}
auch bekannt als das 1. Ficksche Gesetz 
</div>

# Aufgabe 2 (4 Punkte)
## Die Kontinuitätsgleichung

Bilanzieren Sie die Stoffmengenkonzentration $$c$$ über ein zweidimensionales Gebiet. Geben Sie die stationäre (zeitunabhängige) und instationäre (zeitabhängige) Gleichung an, die diese Bilanzierung beschreibt. Berücksichtigen Sie hierbei auch einen Quellterm, also die Produktion eines Stoffes, im zu bilanzierenden Gebiet.

**Hinweis:**
Ohne Quellterm wird die Bilanzgleichung als Kontinuitätsgleichung bezeichnet: $$\frac{\partial c}{\partial t} = -\nabla\cdot\vec{j}_c$$. Bitte verwenden Sie diese Gleichung für Aufgabe 3 unabhängig davon, ob Sie Aufgabe 2 bearbeitet haben.


![surface_element.svg](surface_element.svg)

<div class="alert alert-success">
<b>Lösung:</b>

Wir betrachten ein quadratisches Flächenelement. 
    
zeitliche Änderung der Konzentration = eingehende - ausgehende ströme + quellterm

Für ein infinitesimales Flächenelement ($$dx, dy \to 0$$) kann $$c$$ als konstant innerhalb des elementes und $$\vec j_c$$ als konstant entlang der Flanken approximiert werden.    
\begin{align}
    \Rightarrow \frac{\partial c(x, y)}{\partial t} dx dy 
    &= - \left( J_{links} + J_{rechts} + J_{unten} + J_{oben}  \right) + q_c dx dy
        \\
    &= - \left( \vec{j}_c(x,y) \cdot (- \hat x) \ dy + \vec{j}_c(x+dx,y)  \cdot \hat x \ dy + \vec{j}_c(x,y)  \cdot (-\hat y) \  dx  + \vec{j}_c(x,y+dy)  \cdot \hat y  \ dx  \right) + q_c dx dy 
\end{align}    
    
mit
\begin{equation}
    \vec{j}_c(x+dx, y) = \vec{j}_c(x,y) + \frac{\partial\vec{j}_c(x,y)}{\partial x} dx
\end{equation}
(für y analog):
\begin{equation}
    \frac{\partial c}{\partial t} = -\frac{\partial j_{c,x}}{\partial x} - \frac{\partial j_{c,y}}{\partial y} + q_c
\end{equation}

Wobei $$\vec j_c \cdot \hat x = j_{c,x}$$.

\begin{equation}
    \frac{\partial c}{\partial t} = -\nabla\cdot\vec{j}_c \text{   (instationär)}
\end{equation}

stationär: $$\frac{\partial c}{\partial t} = 0$$
$$\Rightarrow \nabla\cdot\vec{j}_c = 0$$
</div>

# Aufgabe 3 (5 Punkte)
## Die Diffusionsgleichung

Leiten Sie ausgehend von dem 1. Fickschen Gesetz (siehe Aufgabe 1) und der instationären Kontinuitätsgleichung (siehe Aufgabe 2) die Diffusionsgleichung, auch bekannt als das 2. Ficksches Gesetz, her. Klassifizieren Sie die resultierende Differentialgleichung. (Bitte schauen Sie sich für die Klassifizierung das Kapitel 2 "Gleichungstypen" der Vorlesung an.)

**Hinweis:**
* Sie werden hierzu die eindimensionale Gleichung aus Aufgabe 1 auf zwei Dimensionen erweitern müssen.

<div class="alert alert-success">
<b>Lösung:</b>
\begin{equation}
    \frac{\partial c}{\partial t} = -\nabla\cdot\vec{j}_c
\end{equation}
mit $$\vec{j}_c = \vec{j}_{c, Diffusion} = -D \ \nabla c$$
\begin{align}\Rightarrow \frac{\partial c}{\partial t} &= -\nabla\cdot (-D \ \nabla c) \\
\frac{\partial c}{\partial t} &= D\nabla\cdot(\nabla c) \\
\frac{\partial c}{\partial t} &= D\nabla^2 c \\
\frac{\partial c}{\partial t} &= D\left(\frac{\partial^2 c}{\partial x^2} + \frac{\partial^2 c}{\partial y^2}\right)
\end{align}
    
    
Allgemeine Darstellung von pDGL mit n unabhängigen Variablen und $$F$$ als Terme kleinerer Ordnung:
    
\begin{equation}
    \sum_{i = 1}^n \sum_{j=1}^n a_{ij} \frac{\partial^2 u}{\partial x_i \partial x_j} + F = 0
\end{equation}
    
Aus der Matrix mit den Einträgen $$a_{ij}$$ lässt sich die pDGL klassieren, wenn (n-1) Eigenwerte der Matrix alle positiv oder alle negativ sind und ein Eigenwert Null ist, handelt es sich um eine parabolische pDGL.
    
In der 2D-Diffusionsgleichung gibt es drei unabhängige Variablen $$(t, x, y)$$ die im folgenden mit $$(x_1, x_2, x_3)$$ bezeichnet werden. Entsprechend der oberen Darstellung ergibt sich:
    
\begin{align}
    \sum_{i = 1}^3 \sum_{j=1}^3 a_{ij} \frac{\partial^2 u}{\partial x_i \partial x_j}& + F = 0 \\
    \sum_{i = 1}^3 \left(a_{i1} \frac{\partial^2 u}{\partial x_i \partial x_1} + a_{i2}\frac{\partial^2 u}{\partial x_i \partial x_2} + a_{i3}\frac{\partial^2 u}{\partial x_i \partial x_3} \right)& + F = 0 \\
    a_{11}\frac{\partial^2 u}{\partial x_1 \partial x_1} + a_{12}\frac{\partial^2 u}{\partial x_1 \partial x_2} + a_{13}\frac{\partial^2 u}{\partial x_1 \partial x_3} & \\
    + a_{21}\frac{\partial^2 u}{\partial x_2 \partial x_1} + a_{22}\frac{\partial^2 u}{\partial x_2 \partial x_2} + a_{23}\frac{\partial^2 u}{\partial x_2 \partial x_3} & \\
    + a_{31}\frac{\partial^2 u}{\partial x_3 \partial x_1} + a_{32}\frac{\partial^2 u}{\partial x_3 \partial x_2} + a_{33}\frac{\partial^2 u}{\partial x_3 \partial x_3} &+ F = 0
\end{align}
    
Aus einem Koeffizientenvergleich mit der 2D-Diffusionsgleichung ergibt sich, dass $$a_{22} = A_{33} = D$$ und alle weiteren $$a_{ij} = 0$$ sind. Daraus ergibt sich eine Diagonalmatrix
    
\begin{pmatrix}
    0 & 0 & 0 \\
    0 & D & 0 \\
    0 & 0 & D \\
\end{pmatrix}
    
mit den Eigenwerten $$\lambda_1 = 0, \lambda_{2,3} = D$$  
    
$$\rightarrow$$ es handelt sich um eine parabolische lineare pDGL 2. Ordnung
</div>

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

3. Plotten Sie anschließend die Lösung der Fourier-Reihe. Schneiden Sie die Fourier-Reihe bei $$N = 1$$, $$5$$, $$10$$ und $$20$$ Termen ab. Zeigen Sie dazu die Lösung durch Integration und vergleichen Sie die Ergebnisse. Nutzen Sie die folgenden Parameter zum plotten:
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

<div class="alert alert-success">
<b>Lösung:</b>
Fourier-Reihe von $$c(x)$$:

$$\begin{align}
c(x) &= \sum_{n=-\infty}^{\infty} c_n \exp\left(\frac{i2\pi n x}{L}\right) \\
&= c_0 + \sum_{n=1}^{\infty} c_n \exp\left(\frac{i2\pi n x}{L}\right) + \sum_{n=-1}^{-\infty} c_n \exp\left(\frac{i2\pi n x}{L}\right)
\end{align}$$

zweite Ableitung der Reihe:

$$\begin{align}
\frac{\partial^2 c(x)}{\partial x^2} = \sum_{n=-\infty}^{\infty} c_n \left(-\frac{4\pi^2 n^2}{L^2}\right) \exp\left(\frac{i2\pi n x}{L}\right)
\end{align}$$

Fourier-Reihe des allgemeinen Quellterms:

$$\begin{align}
f(x) = \sum_{n=-\infty}^{\infty} f_n \exp\left(\frac{i2\pi n x}{L}\right)
\end{align}$$

Einsetzen in die Diffusionsgleichung un umformen nach $$c_n$$:

$$\begin{align}
\frac{\partial^2 c(x)}{\partial x^2} & = \frac{1}{D}f(x) \\
\Rightarrow \sum_{n=-\infty}^{\infty} c_n \left(-\frac{4\pi^2 n^2}{L^2}\right) \exp\left(\frac{i2\pi n x}{L}\right) &= \frac{1}{D} \sum_{n=-\infty}^{\infty} f_n \exp\left(\frac{i2\pi n x}{L}\right) \\
\sum_{n=-\infty}^{\infty} \left(\frac{1}{D}f_n +\frac{4\pi^2 n^2}{L^2}c_n\right)\exp\left(\frac{i2\pi n x}{L}\right)  &= 0\\
\frac{1}{D}f_n +\frac{4\pi^2 n^2}{L^2}c_n &= 0 \\
c_n &= -\frac{1}{D}f_n\frac{L^2}{4\pi^2 n^2}
\end{align}$$

Einsetzen von $$c_n$$ in Fourier-Reihe von $$c(x)$$:

$$\begin{align}
c(x) = c_0 + \sum_{n=1}^{\infty} -\frac{1}{D}f_n\frac{L^2}{4\pi^2 n^2} \exp\left(\frac{i2\pi n x}{L}\right) + \sum_{n=-1}^{-\infty} -\frac{1}{D}f_n\frac{L^2}{4\pi^2 n^2} \exp\left(\frac{i2\pi n x}{L}\right)
\end{align}$$

Bestimmung von $$f_n$$ für Dirac Kamm mit $$f(x)= -\delta(x-L/3)+\delta(x-2L/3)$$:

$$\begin{align}
f_n &= \frac{1}{L}\int_{-L/2}^{L/2}\text{d}xf(x)\exp\left(\frac{-i2\pi n x}{L}\right) \\
&= \frac{1}{L}\int_{-L/2}^{L/2}\text{d}x\left(-\delta(x-L/3)+\delta(x-2L/3)\right)\exp\left(\frac{-i2\pi n x}{L}\right) \\
&= -\frac{1}{L}\int_{-L/2}^{L/2}\text{d}x\delta(x-L/3)\exp\left(\frac{-i2\pi n x}{L}\right) + \frac{1}{L}\int_{-L/2}^{L/2}\text{d}x\delta(x-2L/3)\exp\left(\frac{-i2\pi n x}{L}\right) \\
&= -\frac{1}{L}\exp\left(-i\frac{2}{3}\pi n\right) + \frac{1}{L}\exp\left(-i\frac{4}{3}\pi n\right) \\
&= \frac{1}{L}\left(\exp\left(-i\frac{4}{3}\pi n\right)-\exp\left(-i\frac{2}{3}\pi n\right)\right)
\end{align}$$

Einsetzen von $$f_n$$ in $$c(x)$$ und umformen:

$$\begin{align}
c(x) =& \sum_{n=1}^{\infty} -\frac{1}{D}\frac{1}{L}\left(\exp\left(-i\frac{4}{3}\pi n\right)-\exp\left(-i\frac{2}{3}\pi n\right)\right)\frac{L^2}{4\pi^2 n^2} \exp\left(\frac{i2\pi n x}{L}\right) \\
& + c_0 + \sum_{n=-1}^{-\infty} -\frac{1}{D}\frac{1}{L}\left(\exp\left(-i\frac{4}{3}\pi n\right)-\exp\left(-i\frac{2}{3}\pi n\right)\right)\frac{L^2}{4\pi^2 n^2} \exp\left(\frac{i2\pi n x}{L}\right) \\
=& \sum_{n=1}^{\infty} -\frac{1}{D}\frac{L}{4\pi^2 n^2} \left(\exp\left(-\frac{i2\pi n x}{L}+ i\frac{4}{3}\pi n\right) - \exp\left( \frac{i2\pi n x}{L}- i\frac{2}{3}\pi n\right) \right) \\
& + c_0 + \sum_{n=1}^{\infty} -\frac{1}{D}\frac{L}{4\pi^2 n^2} \left(\exp\left(\frac{i2\pi n x}{L}- i\frac{4}{3}\pi n\right) - \exp\left( \frac{i2\pi n x}{L}- i\frac{2}{3}\pi n\right) \right)\\
=& c_0 + \sum_{n=1}^{\infty} \frac{-2}{D}\frac{L}{4\pi^2 n^2}\left(\cos\left(\frac{2\pi n x}{L}- \frac{4}{3}\pi n\right) - \cos\left(\frac{2\pi n x}{L}- \frac{2}{3}\pi n\right) \right)
\end{align}$$
    
Der Koeffizient $$c_0$$ ist der Mittelwert der Funktion und ohne entsprechende Randbedingung nicht bestimmbar.    
</div>

<div class="alert alert-success">
    <b>Lösung durch Integration:</b>

$$
\begin{align}
\frac{\partial^2 c(x)}{\partial x^2} &= \frac{1}{D}(-\delta(x-\frac{L}{3})+\delta(x-\frac{2L}{3})) \\
\frac{\partial c(x)}{\partial x} &= \frac{1}{D}(-H(x-\frac{L}{3})+H(x-\frac{2L}{3})) +k_1 \\
c(x) &= \frac{1}{D}(-(x-\frac{L}{3})H(x-\frac{L}{3})+(x-\frac{2L}{3})H(x-\frac{2L}{3})) +k_1 x + k_2 \\
c(x) &= \frac{1}{D}(-\max(0, x-L/3)+\max(0, x-2L/3)) +k_1 x + k_2
\end{align}
$$

Bestimmung von $$k_1$$ aus Periodizitätsbedingung:

$$
\begin{align}
c(x) &= c(x+L) \\
c(0) &= c(L) \\
\frac{1}{D}(-\max(0, -L/3)+\max(0, -2L/3) +k_1*0 + k_2 &= \frac{1}{D}(-\max(0, L-L/3)+\max(0, L-2L/3) +k_1*L + k_2 \\
0 &= \frac{1}{D}(-2L/3 + L/3) +k_1*L \\
k_1 = \frac{1}{3D}
\end{align}
$$

Bestimmung von $$k_2$$ aus Mittelwertbedingung:

$$
\begin{align}
\frac{1}{L}\int_{0}^{L} \text{d}x c(x) &= 0 \\
\frac{1}{L}\int_{0}^{L} \text{d}x \frac{1}{D}(-\max(x, -L/3)+\max(x, -2L/3) +\frac{1}{3D}x + k_2 &= 0 \\
... \\
k_2 &= 0
\end{align}
$$
</div>


```python
import numpy as np
import matplotlib.pyplot as plt
import math

length = 3
diffusion_const = 0.8 # Diffusionskonstante

def C_series(x, k):
    n = np.arange(1,k)
    X, N = np.meshgrid(x, n)
    val = -2*length/(diffusion_const*4*math.pi**2*N**2)*(np.cos(2*math.pi*N*X/length-4*math.pi*N/3)-np.cos(2*math.pi*N*X/length - 2*math.pi*N/3))
    return np.sum(val, axis=0)
x = np.linspace(0, length, 100)

c_integrated = (-(x-length/3)*np.heaviside(x-length/3, 0.5)+(x-length*2/3)*np.heaviside(x-2*length/3, 0.5))/diffusion_const
c_integrated +=  x*1/(3*diffusion_const)

x0 =0
xf= length


for k in [1, 5, 10, 20]:
    plt.plot(x, C_series(x, k), label = "k = "+str(k))
plt.plot(x, c_integrated, label="Integration")

plt.xlabel('Position $$x$$')
plt.ylabel('Konzentration $$c$$')
plt.legend(loc="lower left")
plt.show()
```


    
![png](output_14_0.png)
    


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

<div class="alert alert-success">
    <b>Lösung:</b>

aus Kräftegleichgewicht:

$$
\begin{align}
\vec{F}_C &= -\vec{F}_d \\
-q\nabla\phi &= 6 \pi \eta a \cdot \vec{v} \\
\text{mit } \vec{j}_{c,Drift} = c\vec{v}\text{:   } \ \  \vec{j_c} &= \frac{-q}{6\pi\eta a}c\nabla\phi \\
\vec{j}_{c,Drift} &= -\mu c \nabla\phi \\
\vec{j}_{c,Drift} &= -\frac{qe}{k_B T}D c \nabla\phi \\
\vec{j}_c &= \vec{j}_{c,Diffusion} + \vec{j}_{c,Drift}\\
\vec{j}_c &= -D\nabla c -\frac{q}{k_B T}D c \nabla\phi \\
\frac{\partial c}{\partial t} &= D\nabla\cdot\left(\nabla c + \frac{q}{k_B T}c\nabla\phi\right)
\end{align}$$

Ladungsdichte mit N Ionenspezies: $$\rho = \sum{q_i c_i}$$

$$\Rightarrow \nabla^2\phi = \frac{-\rho}{\varepsilon}$$

$$ \nabla^2(\varepsilon\phi)= -\sum{q_i c_i} $$
</div>

# Aufgabe 6 (8 Punkte)
## Poisson-Boltzmann Gleichung

### 6.1 Linearisierte Poisson-Boltzmann Gleichung

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
* $$\Phi_0 = -1\,k_B T/q$$
* $$\Phi_1 = 1\,k_B T/q$$
* $$L = 1\,\lambda$$
* $$1/\lambda^2 = 20$$
auf einem eindimensionalen Intervall, wie unten dargestellt.

![electrochemicalCell1dLinearizedPB.svg](electrochemicalCell1dLinearizedPB.svg)

<div class="alert alert-success">
    <b>Lösung:</b>
Die Poisson-Gleichung und Nernst-Gleichung koppeln über die Ladungsdichte,
\begin{equation}
\rho(\vec{r}) = \sum_{i=1}^N q_i c_i(\vec{r}).
\end{equation}

Mit der Boltzmann-Verteilung für die Konzentrationsverteilung

$$\begin{align}
c(\vec{r}) = c_0 \exp\left(\frac{-q\Phi(\vec{r})}{k_B T}\right)
\end{align}$$

ergibt sich die Poisson-Boltzmann-Gleichung zu

$$\begin{align}
\nabla^2\Phi &= -\frac{1}{\varepsilon}\rho \\
&= -\frac{1}{\varepsilon}\sum_{i=1}^N q_i c_i \\
&= -\frac{1}{\varepsilon}\sum_{i=1}^N q_i c_{i0} \exp\left(\frac{-q_i\Phi}{k_B T}\right)\\
\end{align}$$

Zum Linearisieren der e-Funktion wird eine Taylorreihe verwendet, es gilt $$\exp(x) = \sum_{n=0}^{\infty}\frac{x^n}{n!} \approx 1+x$$

$$\begin{align}
\nabla^2\Phi &= -\frac{1}{\varepsilon}e\sum_{i=1}^N q_i c_{i0} \exp\left(\frac{-q_i\Phi}{k_B T}\right)\\
&= -\frac{1}{\varepsilon}\sum_{i=1}^N q_i c_{i0} \left(1+ \left(\frac{-q_i\Phi}{k_B T}\right)\right)\\
&= -\frac{1}{\varepsilon}\sum_{i=1}^N \left(q_i c_{i0} -\frac{q_{i}^{2}c_i\Phi}{k_B T}\right)\\
\end{align}$$

Für elektrisch neutrale Systeme gilt $$\sum_{i=1}^N q_i c_{i0}=0$$, in diesem Fall vereinfacht sich die Gleichung zu
\begin{equation}
\nabla^2\Phi = \frac{1}{\varepsilon}\sum_{i=1}^N\frac{q_{i}^{2}c_i \Phi}{k_B T}
\end{equation}
Mit N=2, c1 = c2 ergibt sich
\begin{equation}
\nabla^2\Phi = \frac{2q^2c}{k_B T\varepsilon}\Phi = \frac{1}{\lambda^2}\Phi
\end{equation}
mit der Debye-Länge $$\lambda$$.

Die Lösung der linearisierten Gleichung ergibt sich zu
\begin{equation}
\Phi(x) = B\exp(-x/\lambda) + C\exp(x/\lambda).
\end{equation}
Die Integrationskonstanten $$B$$ und $$C$$ werden allgemein bestimmt mit den folgenden Bedingungen:

* $$\Phi(x=0) = \Phi_{0}$$
* $$\Phi(x=L) = \Phi_{1}$$

wobei $$L$$ der Plattenabstand ist. Aus der ersten Bedingung folgt:

$$
\begin{align}
B + C &= \Phi_0 \\
B &= \Phi_0 -C
\end{align}
$$

Aus der zweiten Bedingung folgt:

$$
\begin{align}
\Phi_1 &= (\Phi_0 -C)\exp(-L/\lambda) + C\exp(L/\lambda)  \\
C &= \frac{\Phi_1 - \Phi_0\exp(-L/\lambda )}{\exp(L/\lambda )-\exp(-L/\lambda)} \\
&= \frac{\Phi_0 -\Phi_1\exp(L/\lambda)}{1-\exp(2L/\lambda)} \\
&= \frac{\Phi_1 -\Phi_0\exp(-L/\lambda)}{2 \sinh(L/\lambda)}\\
B &= \Phi_0 - C \\
&=\Phi_0 - \frac{\Phi_1 - \Phi_0\exp(-L/\lambda )}{\exp(L/\lambda )-\exp(-L/\lambda)} \\
&=\frac{\Phi_0\exp(L/\lambda ) - \Phi_1}{\exp(L/\lambda )-\exp(-L/\lambda)} \\
&= \Phi_0 - \frac{\Phi_1 -\Phi_0\exp(-L/\lambda)}{2 \sinh(L/\lambda)} \\
&= \frac{\Phi_0 \exp(L/\lambda) - \Phi_1}{2 \sinh(L/\lambda)}\\
\Phi(x) &= B\exp(-x/\lambda) + C\exp(x/\lambda) \\
&= \left[\frac{\Phi_0 \exp(L/\lambda) - \Phi_1}{2 \sinh(L/\lambda)}\right]\exp(-x/\lambda) 
+ \left[\frac{\Phi_1 -\Phi_0\exp(-L/\lambda)}{2 \sinh(L/\lambda)}\right]\exp(x/\lambda) \\
&= \frac{1}{2 \sinh(L/\lambda)}\left[
\Phi_0 \exp\left(\frac{L-x}{\lambda}\right) - \Phi_1\exp(-x/\lambda) + \Phi_1 \exp(x/\lambda) -\Phi_0\exp\left(-\frac{L-x}{\lambda}\right)\right] \\
&= \frac{1}{\sinh(L/\lambda)}\left[\Phi_0 \sinh\left(\frac{L-x}{\lambda}\right) + \Phi_1 \sinh\left(\frac{x}{\lambda}\right)\right]
\end{align}
$$
</div>


```python
import numpy as np
import matplotlib.pyplot as plt
import math

def poisson_boltzmann_linear_1d_ana(x, A, potential_links, potential_rechts, platten_abstand):

    # A ist 1/lambda^2
    a = np.sqrt(A)

    C = (potential_links - potential_rechts* np.exp(a * platten_abstand))/(1 - np.exp(2 * a * platten_abstand))
    B = potential_links - C


    return B * np.exp(- a* x) + C * np.exp(a * x)

fig, ax = plt.subplots()

potential_links = -1.0
potential_rechts = 1.0
platten_abstand = 1.0
A = 20

x = np.linspace(0,1., 50)
ax.plot(x, poisson_boltzmann_linear_1d_ana(x, A, potential_links,potential_rechts, platten_abstand), "k", label="analytisch linearisiert")
ax.legend()

ax.set_xlabel("Position $$x$$ ($$\lambda$$)")
ax.set_ylabel("Elektrostatisches Potential $$\Phi$$ ($$k_B T/q$$)")
plt.show()
```


    
![png](output_20_0.png)
    


### 6.2 Nicht-lineare Poisson-Boltzmann Gleichung

Wir diskutieren nun die Lösung der Poisson-Boltzmann-Gleichung für lediglich eine Spezies ($$N=1$$). Zeigen Sie (ausgehend von der nicht-linearen Poisson-Boltzmann-Gleichung) durch Einsetzen, dass $$\Phi = \frac{k_B T}{q}\ln(\cos^2(Kx))$$ mit $$K^2 = \frac{q^2 c_0}{2\varepsilon k_B T} = \frac{1}{4 \lambda^2}$$ eine Lösung der Differentialgleichung.

<div class="alert alert-success">
Lösung der nicht-linearisierte Gleichung gegeben durch $$\Phi = \frac{k_B T}{q} \ln(\cos^2(Kx))$$ mit $$K^2 = \frac{(q)^2 c_0}{2\varepsilon k_B T}$$

Es folgt:

$$
\begin{align}
\Phi' &= \frac{-2k_B T}{q}K \tan(Kx) \\
\Phi '' &= \frac{-2k_B T}{q}K^2 \frac{1}{\cos^2(Kx)}\\
&= \frac{-qc_0}{\varepsilon}\frac{1}{\cos^2(Kx)}
\end{align}
$$

Einsetzen der Lösung in die Poisson-Boltzmann-Gleichung zeigt:

$$
\begin{align}
\Phi'' &= \frac{-q c_0}{\varepsilon}\exp\left(\frac{-q}{k_B T}\Phi\right)\\
&= \frac{-q c_0}{\varepsilon}\exp\left(\frac{-q}{k_B T}\frac{k_B T}{q}\ln(\cos^2(Kx))\right)\\
&= \frac{-q c_0}{\varepsilon}\exp\left(\frac{-q}{k_B T}\frac{k_B T}{q}\ln(\cos^2(Kx))\right)\\
&= \frac{-q c_0}{\varepsilon}\frac{1}{\cos^2(Kx)}
\end{align}
$$

Gleichungen stimmen überein $$\rightarrow$$ die angegebene Gleichung ist eine Lösung der Differentialgleichung.
</div>
