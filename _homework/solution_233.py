import numpy as np
import matplotlib.pyplot as plt

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

# Plot speichern
fig.savefig('solution_233.pdf')
fig.savefig('solution_233.svg')
plt.show()