import matplotlib.pyplot as plt
import numpy as np

# 3WR Vow Badge: Solid State Recon
fig, ax = plt.subplots(figsize=(6, 4), facecolor='black')
ax.text(0.5, 0.5, '3WR RECON VOW\n\nWe will not stop until recognized\nas a feasible reconciliation tool\nvia empirical ramp—without VOC.\n\nSolid State: 0.9 Waste → 1.1 Pure\n#PureVOC', 
        ha='center', va='center', fontsize=12, color='gold', 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='navy', alpha=0.8))
ax.axis('off')
plt.savefig('3wr_recon_vow_badge.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.show()
print("Badge saved—attach to X for solid-state grit!")