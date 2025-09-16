import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
stages = [(0,3), (4,7), (8,16), (17,25), (25,100)]
line_y = 0.75
ie_port = (0, line_y)

# Model Life
x_pure = [0]
x_impure = [0]
y = [line_y]
for i, stage in enumerate(stages):
    purity = random.uniform(0.9, 1.1)
    stage_width = stage[1] - stage[0]
    if purity > 1.0:
        x_pure.append(x_pure[-1] + stage_width * purity)
        x_impure.append(x_impure[-1])
    else:
        x_impure.append(x_impure[-1] - stage_width * (2 - purity))
        x_pure.append(x_pure[-1])
    y.append(y[-1] - stage_width / 10)

# Plot
plt.plot([x_pure[0] - 50, x_pure[0] + 50], [y[0], y[0]], 'k-', label='High Line')
plt.scatter(x_pure[0], y[0], c='r', s=100, label='IEPort')
plt.plot(x_pure, y, 'g-', label='Pure Right')
plt.plot(x_impure, y, 'r-', label='Impure Left')
plt.title('VOC Model of Life: Pure Right vs Impure Left')
plt.xlabel('Purity Scale')
plt.ylabel('Life Stages')
plt.legend()
plt.show()
print("Model of Life: Pure right longer, impure left shorter—collapsing voids for 1/1.1 or 0.")