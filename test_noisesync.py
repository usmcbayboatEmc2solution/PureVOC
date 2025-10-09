import numpy as np

n_runs = 1000  # More runs for average
results = []
for _ in range(n_runs):
    z = np.random.choice([-1,1],5)
    result = 1.25*z[0] - 2.7*z[1] + 1.05*z[2] - 1.0*z[3] + 1.05*z[4]
    results.append(np.sign(result))

average_stability = np.mean(np.abs(results))
print(f"Average stability (over {n_runs} runs): {average_stability:.3f}")