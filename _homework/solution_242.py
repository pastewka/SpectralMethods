import numpy as np
import matplotlib.pyplot as plt

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
plt.subplots_adjust(top=0.7)

# Plot Ableitung vorbereiten
fig_diff, ax_diff = plt.subplots()
plt.subplots_adjust(top=0.85)
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

# Plots speichern
fig.savefig('solution_442_concentration.pdf')
fig.savefig('solution_442_concentration.svg')
fig_struktur.savefig('solution_442_matrix_struktur.pdf')
fig_struktur.savefig('solution_442_matrix_struktur.svg')
fig_diff.savefig('solution_442_derivative.pdf')
fig_diff.savefig('solution_442_derivative.svg')
#plt.show()