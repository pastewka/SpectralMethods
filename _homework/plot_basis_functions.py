import numpy as np
import matplotlib.pyplot as plt

###----- Plotte die linearen Basisfunktionen -----###
# Parameter Definitionen
L = 2
N = 4
offset = 0.1 # offset of the plotted axis with respect to the figure axis
w = 0.05 # width of the tick labels

n = np.linspace(0, L, N) + offset

# Figur vorbereiten
fig, ax = plt.subplots(figsize=(6, 3))
fig.suptitle('Hutfunktionen für N={}'.format(N), fontsize=18)
ax.axis('off')
ax.arrow(offset, offset, 2.2, 0, width=1e-3, head_width=0.03, head_length=0.03, 
         length_includes_head=True, fc='k', ec='k')
ax.arrow(offset, offset, 0, 1.2, width=1e-3, head_width=0.03, head_length=0.03, 
         length_includes_head=True, fc='k', ec='k')
ax.text(2.225+offset, offset, 'x', {'fontsize':15})
ax.text(0, 1.225+offset, r'$\varphi_i(x)$', {'fontsize':15})

ax.text(n[0], 0, r'$x_0 = 0$', {'ha':'center', 'fontsize':15})
ax.plot([n[0], n[0]], [offset-w/2, offset+w/2], color='k', linewidth=1.5)
for i in range(1, N-1):
    tick_text = r'$x_{}$'.format(i)
    ax.text(n[i], 0, tick_text, {'ha':'center', 'fontsize':15})
    ax.plot([n[i], n[i]], [offset-w/2, offset+w/2], color='k', linewidth=1.5)
ax.text(n[N-1], 0, r'$x_{}=L$'.format(N-1), {'ha':'center', 'fontsize':15})
ax.plot([n[N-1], n[N-1]], [offset-w/2, offset+w/2], color='k', linewidth=1.5)

ax.text(0, 1+offset, r'$1$', {'va':'center', 'fontsize':15})
ax.plot([offset-w/2, offset+w/2], [1+offset, 1+offset], color='k', linewidth=1.5)

# Hutfunktionen plotten
colors = ['black', 'blue', 'red', 'green', 'darkorange', 'cyan']
for i in range(N):
    g = np.zeros(N) + offset
    g[i] += 1
    ax.plot(n, g, color=colors[i], linewidth=2)
    # Hutfunktion labeln
    label = r'$\varphi_{}$'.format(i)
    ax.text(n[i]+0.02, offset+1, label, {'color':colors[i], 'fontsize':15})

# Plot speichern
fig.savefig('Hutfunktionen.pdf')
fig.savefig('Hutfunktionen.svg')