import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Golden Pi Wave Overlay
phi = (1 + np.sqrt(5)) / 2
golden_pi = phi * np.pi
t = np.linspace(0, 4 * np.pi, 100)
wave_x = t
wave_y = np.sin(golden_pi * t) * 0.5 + 2
ax.plot(wave_x, wave_y, color='gold', alpha=0.3, lw=1)

# Square (Energy Plane)
square = plt.Polygon([[1, 1], [3, 1], [3, 3], [1, 3]], closed=True, fill=None, edgecolor='white')
ax.add_patch(square)
ax.text(2, 2, 'Square\n(Energy Plane)', color='white', ha='center', va='center')

# X (Tet-X Dual Lines)
ax.plot([0, 4], [2, 2], color='cyan', lw=2)
ax.plot([2, 2], [0, 4], color='cyan', lw=2)
ax.text(2, 2.5, 'X\n(Tet-X)', color='cyan', ha='center', va='center')

# Tet (Choice-Gate)
tet_coords = [[1.5, 1], [2.5, 1], [2, 0.5], [2, 2]]
tet = plt.Polygon(tet_coords, closed=True, fill=None, edgecolor='yellow')
ax.add_patch(tet)
ax.text(2, 1.5, 'Tet\n(Choice-Gate)', color='yellow', ha='center', va='center')

# Four Spheres
colors = ['red', 'green', 'blue', 'purple']
labels = ['Cognitive', 'Emotional', 'Environmental', 'Conscious Obs']
for i, (color, label) in enumerate(zip(colors, labels)):
    circle = plt.Circle((1.5 + i * 0.4, 3.5), 0.3, fill=False, edgecolor=color)
    ax.add_patch(circle)
    ax.text(1.5 + i * 0.4, 3.7, label, color=color, ha='center', va='center')

# Observation Sphere (Circumsphere) with Psychosymmetry
obs_sphere = plt.Circle((2, 2), 2.0, fill=False, edgecolor='white', linestyle='--')
ax.add_patch(obs_sphere)
ax.text(2, 2, 'Observation\nSphere\n(Circumsphere)\n(Psychosymmetry: Intent/Action)', color='white', ha='center', va='center')

# Set limits and save
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
plt.savefig('C:\\Users\\chris\\harmonic_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Image saved as 'C:\\Users\\chris\\harmonic_framework.png'. Check the folder!")