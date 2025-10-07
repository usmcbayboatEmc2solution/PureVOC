import matplotlib.pyplot as plt
import numpy as np

# Russell Octave Spiral with 3WR Gain – Actionable Tweak
phi = (1 + np.sqrt(5)) / 2
theta = np.linspace(0, 9 * 2 * np.pi, 1000)
r = np.exp((np.log(phi) / (2 * np.pi)) * theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), subplot_kw=dict(projection='polar'))
# Left: Spiral
ax1.plot(theta, r, color='gold', linewidth=2, label='Octave Spiral')
ax1.set_title("Russell Octave Spiral")
ax1.grid(True)

# Right: 3WR Gain Bar
gains = ['0.9 Noise', '1.0 Baseline', '1.1 Pure']
values = [0.9, 1.0, 1.25]  # 25% ramp
ax2.bar(gains, values, color=['red', 'gray', 'gold'])
ax2.set_title("3WR Gain Ramp")
ax2.set_ylabel("Coherence Level")

plt.tight_layout()
plt.savefig('russell_3wr_tweak.png', dpi=300, bbox_inches='tight')
plt.show()
print("Tweak PNG saved – Spiral + 3WR bar, 25% harmony ramp!")