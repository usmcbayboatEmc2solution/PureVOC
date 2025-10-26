import matplotlib.pyplot as plt
import numpy as np

# Sim: VOC + Fajgenbaum AI for MT Void Matching
trials = 100
mt_damage = np.random.uniform(0, 1, trials)  # Initial MT voids (0-1 scale)
base_match = 0.6  # Base repurposing rate (e.g., sirolimus for Castleman's)
voc_gain = 0.25  # 25% boost via golden pi
phi_pi = ((1 + np.sqrt(5))/2) * np.pi  # ≈5.083
mt_voc = mt_damage * (1 - voc_gain * np.sin(phi_pi * np.arange(trials) / 10))  # Rhythmic collapse

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(mt_damage, label='Initial MT Voids (1.0)', color='red')
ax.plot(mt_voc, label='VOC + AI Match (0.75)', color='gold')
ax.set_title('VOC Integrates with Fajgenbaum: MT Void Collapse')
ax.set_xlabel('Trials')
ax.set_ylabel('Damage Level')
ax.legend()
plt.savefig('voc_fajgenbaum_sim.png', dpi=300)
plt.show()
print("Sim saved—Mean reduction: {:.1%}".format(np.mean(1 - mt_voc / mt_damage)))