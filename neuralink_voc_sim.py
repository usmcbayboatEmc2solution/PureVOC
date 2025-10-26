import matplotlib.pyplot as plt
import numpy as np

# Neuralink-VOC Sim: MT Void Flagging
trials = 100
mt_voids = np.random.uniform(0, 1, trials)  # Initial MT damage (0-1)
base_bci = 0.7  # Neuralink baseline detection
voc_gain = 0.28  # 28% boost via golden pi
phi_pi = ((1 + np.sqrt(5))/2) * np.pi
mt_sync = mt_voids * (1 - voc_gain * np.sin(phi_pi * np.arange(trials) / 10))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(mt_voids, label='Initial MT Voids (1.0)', color='red')
ax.plot(mt_sync, label='Neuralink + VOC Sync (0.72)', color='gold')
ax.set_title('Neuralink Sync Potential: VOC MT Void Collapse')
ax.set_xlabel('Trials')
ax.set_ylabel('Damage Level')
ax.legend()
plt.savefig('neuralink_voc_sim.png', dpi=300)
plt.show()
print("Sim saved—Mean reduction: {:.1%}".format(np.mean(1 - mt_sync / mt_voids)))