import numpy as np
import matplotlib.pyplot as plt

g0 = 9.81  # m/s^2
I_sp_chem = 350  # s
I_sp_ntp = 900  # s
v_ex_chem = g0 * I_sp_chem
v_ex_ntp = g0 * I_sp_ntp

# Earth v_esc
R_earth = 6.371e6  # m
G = 6.67430e-11
M_earth = 5.972e24  # kg
v_esc_earth = np.sqrt(2 * G * M_earth / R_earth)  # ~11.2 km/s

# Super-Earth g=5g0, same R
v_esc_super = v_esc_earth * np.sqrt(5)  # ~25 km/s

# Mass ratios
ratio_chem_earth = np.exp(v_esc_earth / v_ex_chem)
ratio_ntp_super = np.exp(v_esc_super / v_ex_ntp)

print(f"Chemical Earth: {ratio_chem_earth:.0f}x")
print(f"NTP Super-Earth: {ratio_ntp_super:.0f}x")

# Plot
fig, ax = plt.subplots()
ax.bar(['Chemical Earth', 'NTP Super-Earth'], [ratio_chem_earth, ratio_ntp_super], color=['red', 'gold'])
ax.set_yscale('log')
ax.set_title('NTP vs Chemical Mass Ratio Ramp')
ax.set_ylabel('Mass Ratio (log scale)')
plt.savefig('ntp_mass_ratio_sim.png', dpi=300)
plt.show()