---
layout: default
title: "Übungsblatt 4 - Mechanik [31. März]"
parent: Übungsaufgaben
date: 2022-01-30
categories: homework
author: Lars Pastewka
nav_order: 4
---


<h2 class='chapterHead'><span class='titlemark'>Übungsblatt 4</span><br /><a id='x1-10004'></a>Finite-Elemente in der Mechanik</h2>
<div class='framedenv' id='shaded*-1'>
<!-- l. 12 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Die Abgabe von Arbeitsblatt 1 bis 4 ist verpflichtend und
konstituiert die Studienleistung der Veranstaltung Simulationstechniken.
Die Arbeitsblätter führen von der mathematischen Formulierung eines
Modellproblems hin zur numerischen Lösung dieses Problems und bauen
aufeinander auf. Zum Bestehen der Veranstaltung müssen auf jedem Blatt
mindestens 50% der erzielbaren Punkte erreicht werden.
</p><!-- l. 20 --><p class='indent'> Geben Sie bei allen Aufgaben die Lösungswege und Zwischenergebnisse mit
an. Das Endergebnis alleine ist nicht ausreichend! Wir empfehlen Ihnen die
Nutzung von Python und Jupyter-Notebooks. Sollten Sie ein Jupyter-Notebook
verwenden, dann können Sie dieses einfach direkt als Lösung bei uns einreichen.
In allen anderen Fällen erzeugen Sie bitte ein PDF und legen die numerischen
Codes als separate Datei dazu.
</p><!-- l. 27 --><p class='indent'> Sie werden durch die einzelnen Schritte der Modellimplementierung geleitet,
und wir geben Hinweise zur Implementierung. Es ist nicht zwingend notwendig,
diese 1-zu-1 zu verfolgen. Im Rahmen dieser Hinweise finden Sie Codeabschnitte,
die Sie verwenden können. Sie dürfen natürlich auch die Codebeispiele aus
dem Vorlesungsmaterial hier verwenden. </p></div>
<h3 class='sectionHead'><span class='titlemark'>4.1 </span> <a id='x1-20004.1'></a>Herleitung der diskretisierten Gleichungen</h3>
<!-- l. 37 --><p class='noindent'>In diesem Übungsblatt wollen wir das Verschiebungsfeld \(\vec {u}(\vec r)\) eines zweidimensionalen
Blocks im elastostatischen Gleichgewicht untersuchen, d.h. für die mechanische
Spannung \(\t {\sigma }\) gilt: \begin {equation} \nabla \cdot \t {\sigma } = \v {0} \label {eq:elastostaticeq_tensor} \end {equation}
bzw. unter Verwendung der Einsteinschen Summenkonvention und \(\partial _i\equiv \partial /\partial r_i\): \begin {equation} \partial _i \sigma _{ij} = 0 \label {eq:elastostaticeq_index} \end {equation}
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 48 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Beschränken Sie sich bitte der Einfachheit halber auf Systeme,
für die gilt: </p>
<ul class='itemize1'>
<li class='itemize'>Die Eigenspannung bzw. die Eigendehnung ist null.
</li>
<li class='itemize'>Das Materialverhalten ist isotrop und linear elastisch, d.h. es gilt:
\begin {equation} \sigma _{ij} = \lambda \delta _{ij} \varepsilon _{kk} + 2\mu \varepsilon _{ij} \label {eq:Hooke} \end {equation}
mit \(\t {\varepsilon } = \left [\nabla \vec u + (\nabla \vec u)^T \right ] / 2\) der Dehnung und \(\lambda \) und \(\mu \) den Lamé-Konstanten.



</li>
<li class='itemize'>Die Lamé-Konstanten sind konstant über das gesamte Simulationsgebiet.
</li>
<li class='itemize'>Das Simulationsgebiet besteht aus einem Rechteck.</li></ul>
</div>
<!-- l. 63 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.1.1 </span> <a id='x1-30004.1.1'></a>Diskretisierung mithilfe der Methode der finiten Element</h4>
<!-- l. 64 --><p class='noindent'><span class='cmbx-12'>5 Punkte</span><br class='newline' />Wir wollen hier die Differenzialgleichung für das Verschiebungsfeld \(\vec {u}(\vec r)\) mit der
Finite-Elemente-Methode approximieren. Benutzen Sie dabei lineare finite
Elemente auf einem strukturierten Gitter mit rechteckigen Dreiecken, genau wie
auf Übungsblatt 3. Abb. <a href='#x1-3001r1'>4.1<!-- tex4ht:ref: fig:discretization --></a> zeigt z.B. ein Gitter mit jeweils vier Knoten in x-
und y-Richtung.
</p><!-- l. 68 --><p class='indent'> Leiten Sie das Gleichungssystem für die Koeffizienten des diskretisierten
Verschiebungsfeldes her, und definieren Sie die Elementmatrix. Vernachlässigen
Sie dabei zunächst die Randbedingungen.
</p>
<figure class='figure'>







<!-- l. 73 --><p class='noindent'><img src='Gitter.svg' alt='PIC' /> <a id='x1-3001r1'></a>
<a id='x1-3002'></a>
</p>
<figcaption class='caption'><span class='id'>Abbildung 4.1: </span><span class='content'>Diskretisierung für jeweils vier Gitterpunkte in x- und
y-Richtung </span></figcaption><!-- tex4ht:label?: x1-3001r4.1 -->



</figure>
<h4 class='subsectionHead'><span class='titlemark'>4.1.2 </span> <a id='x1-40004.1.2'></a>Randbedingungen</h4>
<!-- l. 184 --><p class='noindent'><span class='cmbx-12'>4 Punkte</span><br class='newline' />Wir wollen in diesem Übungsblatt drei verschiedene Lastfälle betrachten:
</p><ol class='enumerate1'>
<li class='enumerate' id='x1-4002x1'>Wie in Abb. <a href='#x1-4007r2'>4.2<!-- tex4ht:ref: fig:tensile_1D_displ --></a> dargestellt ist links eine feste Einspannung (die
Verschiebung dort muss also null sein) und rechts eine vorgegebene
Verschiebung \(\v {u}=(u_0; 0)^T\). Die Oberflächen unten und oben sind spannungsfrei,
d.h. für die Flächenlast gilt: \(\v {t} = \v {0}\).
</li>
<li class='enumerate' id='x1-4004x2'>Wie in Abb. <a href='#x1-4009r3'>4.3<!-- tex4ht:ref: fig:tensile_1D_trac --></a> dargestellt, ist links eine feste Einspannung und rechts
eine vorgegebene Flächenlast \(\v {t}=(t_0; 0)^T\). Die Oberflächen unten und oben sind
spannungsfrei.
</li>
<li class='enumerate' id='x1-4006x3'>Wie in Abb. <a href='#x1-4011r4'>4.4<!-- tex4ht:ref: fig:pressure_sensor --></a> dargestellt, sind links und rechts feste Einspannungen.
Von unten wird das System durch eine vorgegebene Flächenlast \(\v {t}=(0; p)^T\)
belastet. Die Oberfläche oben ist spannungsfrei.</li></ol>
<figure class='figure'>







<!-- l. 194 --><p class='noindent'><img src='Zug_Verschiebung.svg' alt='PIC' /> <a id='x1-4007r2'></a>
<a id='x1-4008'></a>
</p>
<figcaption class='caption'><span class='id'>Abbildung 4.2: </span><span class='content'>Zugversuch mit vorgegebener Verschiebung </span></figcaption><!-- tex4ht:label?: x1-4007r4.1 -->



</figure>
<figure class='figure'>







<!-- l. 201 --><p class='noindent'><img src='Zug_Flaechenlast.svg' alt='PIC' /> <a id='x1-4009r3'></a>
<a id='x1-4010'></a>
</p>
<figcaption class='caption'><span class='id'>Abbildung 4.3: </span><span class='content'>Zugversuch mit vorgegebener Flächenlast </span></figcaption><!-- tex4ht:label?: x1-4009r4.1 -->



</figure>
<figure class='figure'>







<!-- l. 208 --><p class='noindent'><img src='Drucksensor.svg' alt='PIC' /> <a id='x1-4011r4'></a>
<a id='x1-4012'></a>
</p>
<figcaption class='caption'><span class='id'>Abbildung 4.4: </span><span class='content'>Modellierung des Drucksensors </span></figcaption><!-- tex4ht:label?: x1-4011r4.1 -->



</figure>
<!-- l. 213 --><p class='indent'> Erläutern Sie, wie Sie das Gleichungssystem aus Aufgabe 1.1 verändern
müssen, um die Randbedingungen in diesen drei Fällen zu berücksichtigen?
</p>
<h3 class='sectionHead'><span class='titlemark'>4.2 </span> <a id='x1-50004.2'></a>Implementierung</h3>
<!-- l. 251 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.1 </span> <a id='x1-60004.2.1'></a>Implementierung der Systemmatrix</h4>
<!-- l. 252 --><p class='noindent'><span class='cmbx-12'>1 Punkte</span><br class='newline' />Nutzen Sie Ihre Ergebnisse aus Aufgabe 4.1.1 um eine Funktion zu implementieren,
die die Systemmatrix und den Lastvektor unter Vernachlässigung der
Randbedingung aufstellt. Wir schlagen dafür folgende Funktionen vor:
</p>
<!-- l. 255 -->
<div class='lstlisting' id='listing-1'><span class='label'><a id='x1-6001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def derivative_matrix(dx, dy): </span><br /><span class='label'><a id='x1-6002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-6003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    Compute matrix of shape function derivatives </span><br /><span class='label'><a id='x1-6004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-6005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-6006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-6007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    dx : float </span><br /><span class='label'><a id='x1-6008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>        Grid spacing in x-direction </span><br /><span class='label'><a id='x1-6009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    dy : float </span><br /><span class='label'><a id='x1-6010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Grid spacing in y-direction </span><br /><span class='label'><a id='x1-6011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    """</span>
</div>
<!-- l. 269 -->
<div class='lstlisting' id='listing-2'><span class='label'><a id='x1-6012r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def assemble_system_matrix(lame1, lame2, nb_rectangles, lengths): </span><br /><span class='label'><a id='x1-6013r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-6014r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    Assemble system matrix from the matrix of shape function </span><br /><span class='label'><a id='x1-6015r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    derivatives. </span><br /><span class='label'><a id='x1-6016r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-6017r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-6018r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-6019r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    lame1 : float </span><br /><span class='label'><a id='x1-6020r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>        First Lame constant (constant over domain) </span><br /><span class='label'><a id='x1-6021r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>    lame2 : float </span><br /><span class='label'><a id='x1-6022r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>        Second Lame constant (constant over domain) </span><br /><span class='label'><a id='x1-6023r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>    nb_rectangles : tuple of ints </span><br /><span class='label'><a id='x1-6024r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>        Number of rectangles in the discretized domain in the     Cartesian directions </span><br /><span class='label'><a id='x1-6025r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>    lengths : tuple of float </span><br /><span class='label'><a id='x1-6026r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>        Physical lengths of the simulation cell </span><br /><span class='label'><a id='x1-6027r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-6028r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>    Returns </span><br /><span class='label'><a id='x1-6029r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    ------- </span><br /><span class='label'><a id='x1-6030r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>    system_matrix_gg : numpy.ndarray </span><br /><span class='label'><a id='x1-6031r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>        System matrix </span><br /><span class='label'><a id='x1-6032r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>    load_vector_g: numpy.ndarray </span><br /><span class='label'><a id='x1-6033r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        Load vector. </span><br /><span class='label'><a id='x1-6034r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>    """</span>
</div>
<div class='framedenv' id='shaded*-1'>
<!-- l. 295 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> </p>
<ul class='itemize1'>
<li class='itemize'>Die Beziehung zwischen dem Index für die Elementnummer, dem
Index für die lokale Knotennummer und dem Index für die
globale Knotennummer haben Sie in Übungbsblatt 3 schon in der
Funktion <span class='obeylines-h'><span class='verb'><span class='cmtt-12'>make_grid</span></span></span> implementiert. Sie können diese Funktion gerne
wiederverwenden.
</li>
<li class='itemize'>Der Unterschied zum Übungsblatt 3 besteht in einem weiteren Index:
Einem Index für die Raumrichtung der Verschiebung. Machen Sie sich
klar, was das für den globalen Index bedeutet.</li></ul>



</div>
<!-- l. 310 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.2 </span> <a id='x1-70004.2.2'></a>Implementierung der Randbedingungen</h4>
<!-- l. 311 --><p class='noindent'><span class='cmbx-12'>1 Punkte</span><br class='newline' />Nutzen Sie Ihre Ergebnisse aus Aufgabe 4.1.2 um vier Funktionen zu
implementieren, die die Systemmatrix und den Lastvektor so verändern, dass die
Randbedingungen berücksichtigt werden: Eine Funktion für die eine feste
Einspannung links (d.h. eine vorgegebene Verschiebung von \(0\) m), eine Funktion
für eine vorgegebene Verschiebung rechts, eine Funktion für eine vorgegebene
Flächenlast rechts und eine Funktion für eine vorgegebene Flächenlast
unten.
</p><!-- l. 321 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.2.3 </span> <a id='x1-80004.2.3'></a>Darstellung der Ergebnisse</h4>
<!-- l. 322 --><p class='noindent'><span class='cmbx-12'>0 Punkte</span><br class='newline' />Für die Darstellung Ihrer Ergebnisse können Sie folgende Funktion verwenden:
</p><!-- l. 324 -->
<div class='lstlisting' id='listing-3'><span class='label'><a id='x1-8001r1'></a><span class='cmr-6'>1</span></span><span class='cmtt-10'>def plot_tri(nb_grid_pts, x_g=None, y_g=None, values_g=None, </span><br /><span class='label'><a id='x1-8002r2'></a><span class='cmr-6'>2</span></span><span class='cmtt-10'>             values_e=None, mesh_style=None, ax=None): </span><br /><span class='label'><a id='x1-8003r3'></a><span class='cmr-6'>3</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-8004r4'></a><span class='cmr-6'>4</span></span><span class='cmtt-10'>    Plot results of a finite-element calculation on a </span><br /><span class='label'><a id='x1-8005r5'></a><span class='cmr-6'>5</span></span><span class='cmtt-10'>    two-dimensional structured grid using matplotlib. </span><br /><span class='label'><a id='x1-8006r6'></a><span class='cmr-6'>6</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-8007r7'></a><span class='cmr-6'>7</span></span><span class='cmtt-10'>    Parameters </span><br /><span class='label'><a id='x1-8008r8'></a><span class='cmr-6'>8</span></span><span class='cmtt-10'>    ---------- </span><br /><span class='label'><a id='x1-8009r9'></a><span class='cmr-6'>9</span></span><span class='cmtt-10'>    nb_grid_pts : tuple of ints </span><br /><span class='label'><a id='x1-8010r10'></a><span class='cmr-6'>10</span></span><span class='cmtt-10'>        Number of nodes in the Cartesian directions </span><br /><span class='label'><a id='x1-8011r11'></a><span class='cmr-6'>11</span></span><span class='cmtt-10'>    x_g : array_like </span><br /><span class='label'><a id='x1-8012r12'></a><span class='cmr-6'>12</span></span><span class='cmtt-10'>        x-positions of the nodes </span><br /><span class='label'><a id='x1-8013r13'></a><span class='cmr-6'>13</span></span><span class='cmtt-10'>    y_g : array_like </span><br /><span class='label'><a id='x1-8014r14'></a><span class='cmr-6'>14</span></span><span class='cmtt-10'>        y-positions of the nodes </span><br /><span class='label'><a id='x1-8015r15'></a><span class='cmr-6'>15</span></span><span class='cmtt-10'>    values_g : array_like </span><br /><span class='label'><a id='x1-8016r16'></a><span class='cmr-6'>16</span></span><span class='cmtt-10'>        Expansion coefficients (values of the field) on the </span><br /><span class='label'><a id='x1-8017r17'></a><span class='cmr-6'>17</span></span><span class='cmtt-10'>        global nodes </span><br /><span class='label'><a id='x1-8018r18'></a><span class='cmr-6'>18</span></span><span class='cmtt-10'>    values_e : array_like </span><br /><span class='label'><a id='x1-8019r19'></a><span class='cmr-6'>19</span></span><span class='cmtt-10'>        Values on elements </span><br /><span class='label'><a id='x1-8020r20'></a><span class='cmr-6'>20</span></span><span class='cmtt-10'>    mesh_style : str, optional </span><br /><span class='label'><a id='x1-8021r21'></a><span class='cmr-6'>21</span></span><span class='cmtt-10'>        Will show the underlying finite-element mesh with </span><br /><span class='label'><a id='x1-8022r22'></a><span class='cmr-6'>22</span></span><span class='cmtt-10'>        the given style if set, e.g. ’ko-’ to see edges </span><br /><span class='label'><a id='x1-8023r23'></a><span class='cmr-6'>23</span></span><span class='cmtt-10'>        and mark nodes by points </span><br /><span class='label'><a id='x1-8024r24'></a><span class='cmr-6'>24</span></span><span class='cmtt-10'>        (Default: None) </span><br /><span class='label'><a id='x1-8025r25'></a><span class='cmr-6'>25</span></span><span class='cmtt-10'>    ax : matplotlib.Axes, optional </span><br /><span class='label'><a id='x1-8026r26'></a><span class='cmr-6'>26</span></span><span class='cmtt-10'>        Axes object for plotting </span><br /><span class='label'><a id='x1-8027r27'></a><span class='cmr-6'>27</span></span><span class='cmtt-10'>        (Default: None) </span><br /><span class='label'><a id='x1-8028r28'></a><span class='cmr-6'>28</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-8029r29'></a><span class='cmr-6'>29</span></span><span class='cmtt-10'>    Returns </span><br /><span class='label'><a id='x1-8030r30'></a><span class='cmr-6'>30</span></span><span class='cmtt-10'>    ------- </span><br /><span class='label'><a id='x1-8031r31'></a><span class='cmr-6'>31</span></span><span class='cmtt-10'>    trim : matplotlib.collections.Trimesh </span><br /><span class='label'><a id='x1-8032r32'></a><span class='cmr-6'>32</span></span><span class='cmtt-10'>        Result of tripcolor </span><br /><span class='label'><a id='x1-8033r33'></a><span class='cmr-6'>33</span></span><span class='cmtt-10'>    """ </span><br /><span class='label'><a id='x1-8034r34'></a><span class='cmr-6'>34</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-8035r35'></a><span class='cmr-6'>35</span></span><span class='cmtt-10'>    Nx, Ny = nb_grid_pts </span><br /><span class='label'><a id='x1-8036r36'></a><span class='cmr-6'>36</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-8037r37'></a><span class='cmr-6'>37</span></span><span class='cmtt-10'>    # These are the node positions on the full global grid. </span><br /><span class='label'><a id='x1-8038r38'></a><span class='cmr-6'>38</span></span><span class='cmtt-10'>    if x_g is None and y_g is None: </span><br /><span class='label'><a id='x1-8039r39'></a><span class='cmr-6'>39</span></span><span class='cmtt-10'>        y_g, x_g = np.mgrid[:Ny, :Nx] </span><br /><span class='label'><a id='x1-8040r40'></a><span class='cmr-6'>40</span></span><span class='cmtt-10'>        x_g.shape = (-1,) </span><br /><span class='label'><a id='x1-8041r41'></a><span class='cmr-6'>41</span></span><span class='cmtt-10'>        y_g.shape = (-1,) </span><br /><span class='label'><a id='x1-8042r42'></a><span class='cmr-6'>42</span></span><span class='cmtt-10'>    elif not (x_g is not None and y_g is not None): </span><br /><span class='label'><a id='x1-8043r43'></a><span class='cmr-6'>43</span></span><span class='cmtt-10'>        raise ValueError(’You need to specify both, x_g and y_g.’) </span><br /><span class='label'><a id='x1-8044r44'></a><span class='cmr-6'>44</span></span><span class='cmtt-10'> </span><br /><span class='label'><a id='x1-8045r45'></a><span class='cmr-6'>45</span></span><span class='cmtt-10'>    # Gouraud shading linearly interpolates the color between </span><br /><span class='label'><a id='x1-8046r46'></a><span class='cmr-6'>46</span></span><span class='cmtt-10'>    # the nodes </span><br /><span class='label'><a id='x1-8047r47'></a><span class='cmr-6'>47</span></span><span class='cmtt-10'>    if ax is None: </span><br /><span class='label'><a id='x1-8048r48'></a><span class='cmr-6'>48</span></span><span class='cmtt-10'>        ax = plt </span><br /><span class='label'><a id='x1-8049r49'></a><span class='cmr-6'>49</span></span><span class='cmtt-10'>    triangulation = matplotlib.tri.Triangulation( </span><br /><span class='label'><a id='x1-8050r50'></a><span class='cmr-6'>50</span></span><span class='cmtt-10'>        x_g, y_g, make_grid(nb_grid_pts)) </span><br /><span class='label'><a id='x1-8051r51'></a><span class='cmr-6'>51</span></span><span class='cmtt-10'>    if values_e is not None: </span><br /><span class='label'><a id='x1-8052r52'></a><span class='cmr-6'>52</span></span><span class='cmtt-10'>        c = ax.tripcolor(triangulation, facecolors=values_e) </span><br /><span class='label'><a id='x1-8053r53'></a><span class='cmr-6'>53</span></span><span class='cmtt-10'>    elif values_g is not None: </span><br /><span class='label'><a id='x1-8054r54'></a><span class='cmr-6'>54</span></span><span class='cmtt-10'>        c = ax.tripcolor(triangulation, values_g, </span><br /><span class='label'><a id='x1-8055r55'></a><span class='cmr-6'>55</span></span><span class='cmtt-10'>                         shading=’gouraud’) </span><br /><span class='label'><a id='x1-8056r56'></a><span class='cmr-6'>56</span></span><span class='cmtt-10'>    else: </span><br /><span class='label'><a id='x1-8057r57'></a><span class='cmr-6'>57</span></span><span class='cmtt-10'>        c = ax.tripcolor(triangulation, np.zeros_like(x_g), </span><br /><span class='label'><a id='x1-8058r58'></a><span class='cmr-6'>58</span></span><span class='cmtt-10'>                         shading=’gouraud’) </span><br /><span class='label'><a id='x1-8059r59'></a><span class='cmr-6'>59</span></span><span class='cmtt-10'>    if mesh_style is not None: </span><br /><span class='label'><a id='x1-8060r60'></a><span class='cmr-6'>60</span></span><span class='cmtt-10'>        ax.triplot(triangulation, mesh_style) </span><br /><span class='label'><a id='x1-8061r61'></a><span class='cmr-6'>61</span></span><span class='cmtt-10'>    return c</span>
</div>
<!-- l. 388 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>4.3 </span> <a id='x1-90004.3'></a>Modellvalidierung</h3>
<!-- l. 390 --><p class='noindent'>In dieser Aufgabe wollen wir die Implementierung aus Aufgabe 4.2 überprüfen.



</p><!-- l. 392 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.3.1 </span> <a id='x1-100004.3.1'></a>1D - Zugversuch mit vorgegebener Verschiebung</h4>
<!-- l. 393 --><p class='noindent'><span class='cmbx-12'>5 Punkte</span><br class='newline' />Als erstes wollen wir unser System unter Zug anschauen, wie in Abb. <a href='#x1-4007r2'>4.2<!-- tex4ht:ref: fig:tensile_1D_displ --></a>)
dargestellt. Für \(\lambda =0\)MPa vereinfacht sich das Problem zu einem eindimensionalen
Problem: \begin {equation} \partial _x \sigma _{xx} = \partial _x \left ( 2\mu \varepsilon _{xx}\right ) = 0 \label {eq:1D_tensile} \end {equation}
</p><!-- l. 400 --><p class='indent'> Berechnen Sie die analytische Lösung und erstellen Sie einen Plot, der zeigt,
dass diese mit der Lösung Ihres Modells übereinstimmt.
</p><!-- l. 402 --><p class='indent'> Verwenden Sie für die numerischen Berechnungen folgende Parameter:
</p>
<ul class='itemize1'>
<li class='itemize'>\(L_x \times L _y = 50\)cm \(\times 10\) cm
</li>
<li class='itemize'>\(\mu = 77\) GPa
</li>
<li class='itemize'>\(u_0 = 3\) mm
</li>
<li class='itemize'>\(10 \times 5\) Gitterpunkte in x- und y-Richtung</li></ul>
<!-- l. 427 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.3.2 </span> <a id='x1-110004.3.2'></a>Zugversuch mit vorgegebener Verschiebung</h4>
<!-- l. 428 --><p class='noindent'><span class='cmbx-12'>4 Punkte</span><br class='newline' />
</p><!-- l. 430 --><p class='indent'> Zeigen Sie, dass für \(\lambda = 115\)GPa \(u_y \neq 0\) und dass das Problem nicht mehr eindimensional
ist. Plotten Sie dafür \(u_y(x, y)\). Zeigen Sie außerdem, dass die analytische Lösung aus
Aufgabe 3.1 trotzdem eine gute Näherung für die Verschiebung in x-Richtung
darstellt.



</p><!-- l. 443 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.3.3 </span> <a id='x1-120004.3.3'></a>1D - Zugversuch mit vorgegebener Flächenlast</h4>
<!-- l. 444 --><p class='noindent'><span class='cmbx-12'>2 Punkte</span><br class='newline' />Um die Implementierung der Neumann - Randbedingungen zu testen wollen wir
den 1D-Zugversuch (d.h. \(\lambda = 0\)MPa) jetzt mit einer vorgegebenen Flächenlast rechts
berechnen (vgl. Abb. <span class='cmbx-12'>??</span>). Zeigen Sie, dass für \(\v {t}_{rechts}(y) = \left ( 2\mu u_0 / L_x; 0 \right )^T\) und den Parametern
aus Aufgabe 3.1 die Verschiebung mit der Verschiebung aus Aufgabe 3.1
übereinstimmt.
</p><!-- l. 455 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>4.4 </span> <a id='x1-130004.4'></a>Drucksensor</h3>
<!-- l. 457 --><p class='noindent'>Als Anwendungsfall wollen wir einen Drucksensor betrachten. Dieser besteht aus
einer Membran, die an beiden Enden fest eingespannt ist und sich unter
Druckbelastung durchbiegt. Die Durchbiegung wird gemessen und erlaubt den
direkten Rückschluss auf die Belastung, d.h. den Druck.
</p><!-- l. 459 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.4.1 </span> <a id='x1-140004.4.1'></a>Modellierung</h4>
<!-- l. 460 --><p class='noindent'><span class='cmbx-12'>1 Punkte</span><br class='newline' />Wir wollen den Drucksensor folgendermaßen modellieren (vgl. Abb. <a href='#x1-4011r4'>4.4<!-- tex4ht:ref: fig:pressure_sensor --></a>): Das
Simulationsgebiet besteht aus einem perfekten Rechteck. Das Material
ist im ganzen Gebiet konstant und folgt dem Hookeschen Gesetz. Als
Randbedingung verwenden wir eine feste Einspannung links und rechts,
eine spannungsfreie Oberfläche oben und eine konstante Flächenlast
unten.
</p><!-- l. 463 --><p class='indent'> In dieser Modellierung stecken mehrere vereinfachende Annahmen. Zählen Sie
mindestens zwei davon auf.
</p><!-- l. 483 --><p class='noindent'>
</p>
<h4 class='subsectionHead'><span class='titlemark'>4.4.2 </span> <a id='x1-150004.4.2'></a>Vergleich mit der Biegebalken-Differentialgleichung</h4>



<!-- l. 484 --><p class='noindent'><span class='cmbx-12'>6 Punkte</span><br class='newline' />Die Euler-Bernoulli-Gleichung \begin {equation} \frac {\dif ^2}{\dif x^2}\left ( EI(x) \frac {\dif ^2 w}{\dif x^2} \right ) = q(x) \end {equation}
beschreibt die Durchbiegung \(w\) eines Balkens. Dabei ist \(E\) das Elastizitätsmodul, \(I\)
das Flächenträgheitsmoment und \(q\) die Belastung in y-Richtung. Lösen Sie
diese Gleichung analytisch und vergleichen Sie die Lösung mit Ihrer numerischen
Lösung für verschiedene Längen \(L_x\).
</p><!-- l. 491 --><p class='indent'> Verwenden Sie für die Simulation folgende Parameter: </p>
<ul class='itemize1'>
<li class='itemize'>\(L_x=50\)mm; \(75\)mm; \(100\)mm; \(125\)mm und \(150\)mm
</li>
<li class='itemize'>\(L_y = 10\)mm
</li>
<li class='itemize'>\(\mu = 77\)GPa und \(\lambda = 115\)GPa
</li>
<li class='itemize'>\(p=82.5\)MPa
</li>
<li class='itemize'>\(101\) x \(11\) Gitterpunkte in x- und y-Richtung</li></ul>
<div class='framedenv' id='shaded*-1'>
<!-- l. 500 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> </p>
<ul class='itemize1'>
<li class='itemize'>Das Elastizitätsmodul \(E\) und die Lamé-Konstanten sind durch
folgende Gleichung miteinander verknüpft: \(E = \mu (3\lambda + 2\mu ) / (\lambda + \mu )\)
</li>
<li class='itemize'>Sie können von einem rechteckigen Querschnitt ausgehen. In diesem
Fall ist das Flächenträgheitsmoment gegeben durch \(I = L_y^3 L_z / 12\) Verwenden Sie
\(L_z=10\)mm.
</li>
<li class='itemize'>Beachten Sie, dass der Druck \(p\) einer Kraft pro Fläche entspricht,
während die Belastung in der Euler-Bernoulli-Gleichung \(q\) einer Kraft
pro Länge entsprechen muss.
</li>
<li class='itemize'>Eine feste Einspannung bedeutet neben einer Durchbiegung von null
auch, dass die Ableitung der Durchbiegung null sein muss.</li></ul>



</div>
<!-- l. 529 --><p class='noindent'>
</p>
<h3 class='sectionHead'><span class='titlemark'>4.5 </span> <a id='x1-160004.5'></a>Dünnbesetzte Algorithmik</h3>
<!-- l. 530 --><p class='noindent'><span class='cmbx-12'>0 Punkte</span><br class='newline' />Schreiben Sie Ihre Funktion so um, dass sie dünnbesetzte Arithmetik aus dem
Paket <a href='https://docs.scipy.org/doc/scipy/reference/sparse.html'><span class='cmtt-12'>scipy.sparse</span></a> nutzt. Dies reduziert die Komplexität der Lösung eines
linearen Gleichungssystem von \(\mathcal {O}(N^2)\) auf \(\mathcal {O}(N)\). D.h. wenn Sie Ihre Gitterpunkte
verdoppeln, sollte der Code dann nur doppelt (und nicht viermal) so langsam
laufen.
</p>
<div class='framedenv' id='shaded*-1'>
<!-- l. 533 --><p class='noindent'><span class='underline'><span class='cmbx-12'>Anmerkung:</span></span> Nutzen Sie das “compressed sparse row (CSR)” Format
<span class='obeylines-h'><span class='verb'><span class='cmtt-12'>scipy.sparse.csr_matrix</span></span></span>. Für die Lösung linearer Gleichungssysteme
müssen Sie dann <a href='https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.spsolve.html'><span class='cmtt-12'>scipy.sparse.linalg.spsolve</span></a> nutzen. </p></div>
<!-- l. 537 --><p class='noindent'>
</p>
<h4 class='likesubsectionHead'><a id='x1-170004.5'></a>Punkte</h4>
<!-- l. 537 --><p class='noindent'>Sie können auf diesem Übungsblatt insgesamt 29 Punkte erzielen.
</p>

