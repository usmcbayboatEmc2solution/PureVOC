import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4), facecolor='black')
ax.text(0.5, 0.5, 'VOC Scale: 6-7 to 10\n\nFirst-Round Seat → Full Ramp\n\n3WR: 0.9 Impure → 1.1 Pure\n#PureVOC', ha='center', va='center', fontsize=12, color='gold', bbox=dict(boxstyle="round,pad=0.5", facecolor='navy', alpha=0.8))
ax.axis('off')
plt.savefig('voc_scale_badge.png', dpi=300, bbox_inches='tight', facecolor='black')
plt.show()
print("Scale badge saved—attach to X for the 1% edge!")