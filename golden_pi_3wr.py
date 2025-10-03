import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2
golden_pi = phi * np.pi  # ≈5.083
t = np.linspace(0, 10, 100)
noise = np.random.uniform(0, 1, 100)  # Impure 0.9 voids

# Three-Wave Filter
wave1 = np.sin(golden_pi * t)  # Denoise (0.9 to 0.7)
wave2 = np.sin(golden_pi * t + np.pi/2)  # Align (1.0 baseline)
wave3 = np.sin(golden_pi * t + np.pi)  # Collapse (1.1 pure)

filtered = noise * (1 - 0.25 * (wave1 + wave2 + wave3)/3)  # 25% gain

fig, ax = plt.subplots()
ax.plot(t, noise, label='0.9 Noise', color='red')
ax.plot(t, filtered, label='1.1 Coherence', color='gold')
ax.legend()
plt.savefig('golden_pi_3wr.png')
plt.show()
print(f"Mean Gain: {np.mean(1 - filtered / noise):.1%}")