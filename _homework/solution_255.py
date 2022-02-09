import numpy as np
import matplotlib.pyplot as plt

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

# Plot fertig stellen
# Legende
ax.legend()

# Plot speichern
fig.savefig('solution_255.pdf')
fig.savefig('solution_255.svg')
plt.show()