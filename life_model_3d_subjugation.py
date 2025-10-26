import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

stages = [(0,3), (4,7), (8,16), (17,25), (25,100)]
line_y = 0.75
ie_port = (0, line_y, 0)
golden_ratio = (1 + np.sqrt(5)) / 2
golden_pi = golden_ratio * np.pi

def quadrant_vote():
    votes = [random.choice([1, 0]) for _ in range(4)]
    if sum(votes) == 4: return 1
    if sum(votes) == 2: return 2
    if len(set(votes)) == 2: return 3
    return 4

def quadrant_subjugation(votes):
    """Subjugation: Impure (0 pure votes) collapses to 0; pure (4 pure votes) activates 1.1."""
    pure_votes = sum(votes)
    if pure_votes == 0:  # Full impure subjugation
        return 0  # Null collapse
    if pure_votes == 4:  # Full pure
        return 1.1  # Activate develop ready
    if pure_votes == 3:  # 3:1 pure
        return 1.0  # Mediated
    return 0.9  # Impure lean

def three_wave_reconciliation(interval):
    base = np.exp(1j * 2 * np.pi * interval)
    pure = (abs(base)**2) * (1 + 0.1)
    impure = pure * (1 - 0.1)
    third = pure * (3/2) * 0.0001
    fifth = pure * (5/4) * 0.0001
    void_gate = (pure + impure + (third + fifth)/2) / 3
    return void_gate

def model_life():
    x_pure = [0]
    x_impure = [0]
    y = [line_y]
    z = [0]
    for i, stage in enumerate(stages):
        interval = i * golden_pi
        quanta = three_wave_reconciliation(interval)
        votes = [random.choice([1, 0]) for _ in range(4)]
        vote = quadrant_vote()
        purity = quadrant_subjugation(votes) if vote in [1, 4] else quanta
        stage_width = stage[1] - stage[0]
        if purity > 0.9:  # Pure or mediated
            x_pure.append(x_pure[-1] + stage_width * purity)
            x_impure.append(x_impure[-1])
        else:  # Impure or null
            x_impure.append(x_impure[-1] - stage_width * (2 - purity if purity > 0 else 1))
            x_pure.append(x_pure[-1])
        y.append(y[-1] - stage_width / 10)
        z.append(z[-1] + stage_width)
    return np.array(x_pure), np.array(x_impure), np.array(y), np.array(z)

x_pure, x_impure, y, z = model_life()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([x_pure[0] - 50, x_pure[0] + 50], [y[0], y[0]], [z[0], z[0]], 'k-', label='High Line')
ax.scatter([x_pure[0]], [y[0]], [z[0]], c='r', s=100, label='IEPort')
ax.plot(x_pure, y, z, 'g-', label='Pure Right/Up')
ax.plot(x_impure, y, z, 'r-', label='Impure Left/Down')
ax.set_title('VOC 3D MycNet Tree with Subjugation')
ax.set_xlabel('Purity Scale (X)')
ax.set_ylabel('Life Height (Y)')
ax.set_zlabel('Life Stages (Z)')
ax.legend()
plt.savefig('life_model_3d_subjugation.png')
plt.show()
print("3D Model: Subjugation-adjusted branches—impure collapse to 0, pure to 1.1.")