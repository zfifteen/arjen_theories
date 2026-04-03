import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Dijksman Inertial Onset Relation (DIOR) - Clean Version
# Effective Inertia Index Phi
# No Unicode glyphs outside LaTeX math mode -> zero font warnings
# =============================================================================

# Normalized units: omega0 = 1.0
omega0 = 1.0
omega_norm = np.linspace(0.1, 5.0, 500)

# Background medium strength S = n * sigma * v_rel / omega0
# (density dependence)
strengths = [0.2, 1.0, 5.0, 20.0]
labels = ['Sparse (S=0.2)', 'Medium (S=1.0)', 'Dense (S=5)', 'Very Dense (S=20)']

def effective_inertia_index(omega_norm, S):
    """Core DIOR formula (Phi) with proposed contact-duration model"""
    # Phi = S * max(0, omega_norm - 1)   for omega > omega0
    phi = np.where(omega_norm > 1.0, S * (omega_norm - 1.0), 0.0)
    return phi

phis = [effective_inertia_index(omega_norm, S) for S in strengths]

# ====================== PLOTS ======================
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dijksman Inertial Onset Relation (DIOR)\nEffective Inertia Index Phi', fontsize=16)

# 1. Linear scale - multiple densities
for phi, label in zip(phis, labels):
    axs[0,0].plot(omega_norm, phi, lw=2.5, label=label)
axs[0,0].axvline(1.0, color='red', ls='--', lw=2, label='omega0 threshold')
axs[0,0].set_xlabel(r'Normalized Angular Velocity $\omega / \omega_0$')
axs[0,0].set_ylabel(r'Effective Inertia Index $\Phi$')
axs[0,0].set_title('Linear Scale')
axs[0,0].legend()
axs[0,0].grid(True, alpha=0.3)

# 2. Log x-scale (highlights the hard onset)
for phi, label in zip(phis, labels):
    axs[0,1].plot(omega_norm, phi, lw=2.5, label=label)
axs[0,1].axvline(1.0, color='red', ls='--', lw=2, label='omega0')
axs[0,1].set_xlabel(r'Normalized Angular Velocity $\omega / \omega_0$ (log scale)')
axs[0,1].set_ylabel(r'$\Phi$')
axs[0,1].set_title('Log Scale - Sharp Onset at omega0')
axs[0,1].set_xscale('log')
axs[0,1].legend()
axs[0,1].grid(True, alpha=0.3)

# 3. Phi vs density at fixed high spin (omega = 3 omega0)
S_range = np.logspace(-1, 2, 200)
phi_high = S_range * (3.0 - 1.0)
axs[1,0].plot(S_range, phi_high, 'teal', lw=3)
axs[1,0].set_xlabel('Medium Strength S (proportional to n - background density)')
axs[1,0].set_ylabel(r'$\Phi$ at $\omega = 3\omega_0$')
axs[1,0].set_title('Inertia Increases Linearly with Background Density')
axs[1,0].set_xscale('log')
axs[1,0].grid(True, alpha=0.3)

# 4. Relative effective inertia example
for phi, label in zip(phis, labels):
    axs[1,1].plot(omega_norm, phi, lw=2.5, label=label)
axs[1,1].axvline(1.0, color='red', ls='--', lw=2)
axs[1,1].set_xlabel(r'$\omega / \omega_0$')
axs[1,1].set_ylabel('Relative Effective Inertia (proportional to Phi)')
axs[1,1].set_title('Example: How "Mass" Emerges Above Threshold')
axs[1,1].legend()
axs[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()   # or plt.savefig('DIOR_Phi_Clean_Demonstration.png', dpi=300)
