import numpy as np
from scipy.signal import chirp, butter, filtfilt
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sample rate (Hz, scaled for sim; crank to 100e3+ for real CHIRP)
t = np.linspace(0, 0.1, int(fs * 0.1))  # 100ms window

# Active Forward-Facing CHIRP with Multipath + Bubbles
chirp_signal = chirp(t, f0=50, f1=200, t1=0.1, method='linear')
echo_delay = int(0.015 * fs)  # 15m range delay
echo = np.roll(chirp_signal, echo_delay) * 0.7
multipath = np.roll(echo, echo_delay // 2) * 0.3  # Ghost echo
bubbles = np.random.exponential(0.5, len(t)) * np.sin(2 * np.pi * np.random.uniform(200, 500, len(t)) * t)  # Bubble bursts (flagged: Bubbles Added)
noise = np.random.normal(0, 0.3, len(t))
raw_active = echo + multipath + bubbles + noise

# VOC Filter: Bandpass for target freqs (50-200Hz)
lowcut = 50
highcut = 200
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(4, [low, high], btype='band')
voc_active = filtfilt(b, a, raw_active)

# SNR Calc
def snr(sig, noise_est):
    return 10 * np.log10(np.var(sig) / np.var(noise_est))

snr_raw_active = snr(echo, raw_active - echo)
snr_voc_active = snr(echo, voc_active - echo)

# Passive Mode: Grunt + Waves/Bio + Bubbles
grunt = 0.8 * np.sin(2 * np.pi * 80 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)  # Fish sines
waves = 0.2 * np.sin(2 * np.pi * 5 * t)  # Low-freq waves
bio_noise = np.random.normal(0, 0.2, len(t))
raw_passive = grunt + waves + bio_noise + bubbles * 0.5  # Bubbles Added

# VOC: Bandpass for low-freq targets
lowcut_pass = 5
highcut_pass = 150
low_p = lowcut_pass / nyq
high_p = highcut_pass / nyq
b_p, a_p = butter(4, [low_p, high_p], btype='band')
voc_passive = filtfilt(b_p, a_p, raw_passive)

snr_raw_passive = snr(grunt, raw_passive - grunt)
snr_voc_passive = snr(grunt, voc_passive - grunt)

# Stability: Corr over 1000 noisy runs (passive example)
def stability_test(signal, noise_std, n_runs=1000):
    corrs = []
    for _ in range(n_runs):
        noisy = signal + np.random.normal(0, noise_std, len(t))
        filtered = filtfilt(b_p, a_p, noisy)
        corrs.append(np.corrcoef(signal, filtered)[0,1])
    return np.mean(corrs)

stab = stability_test(grunt, 0.3)

# Output results
print(f"Active Raw SNR: {snr_raw_active:.2f} dB")
print(f"Active VOC SNR: {snr_voc_active:.2f} dB (Gain: {snr_voc_active - snr_raw_active:.2f} dB)")
print(f"Passive Raw SNR: {snr_raw_passive:.2f} dB")
print(f"Passive VOC SNR: {snr_voc_passive:.2f} dB (Gain: {snr_voc_passive - snr_raw_passive:.2f} dB)")
print(f"Stability (1000 runs): {stab:.3f}")

# Plot
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0,0].plot(t[:500], raw_active[:500]); axs[0,0].set_title('Raw Active (w/ Bubbles)')
axs[0,1].plot(t[:500], voc_active[:500]); axs[0,1].set_title('VOC Active')
axs[1,0].plot(t[:500], raw_passive[:500]); axs[1,0].set_title('Raw Passive (w/ Bubbles)')
axs[1,1].plot(t[:500], voc_passive[:500]); axs[1,1].set_title('VOC Passive')
plt.tight_layout()
plt.savefig('voc_sim_bubbles.png')
print("Plot saved as voc_sim_bubbles.png")