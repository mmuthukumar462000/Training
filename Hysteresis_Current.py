import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
T = 4  # Duration in seconds
AMPLITUDE = 1
HYSTERESIS_BAND = 0.1
NUM_CYCLES = 4
DUTY_CYCLE = 0.5

# Calculate total number of samples
total_samples = Fs * T

# Generate time vector
t = np.arange(0, T, 1/Fs)

# Initialize current waveform
current = np.zeros(total_samples)

# Generate trapezoidal waveform with hysteresis
on_samples = int(DUTY_CYCLE * Fs)
off_samples = int((1 - DUTY_CYCLE) * Fs)

for cycle in range(NUM_CYCLES):
    start_index = cycle * (on_samples + off_samples)
    end_index = start_index + on_samples
    # On period
    current[start_index:end_index] = AMPLITUDE

    # Hysteresis region
    for i in range(end_index, start_index + on_samples + off_samples):
        if current[i-1] > AMPLITUDE * (1 - HYSTERESIS_BAND):
            current[i] = AMPLITUDE * (1 + HYSTERESIS_BAND)
        elif current[i-1] < AMPLITUDE * (1 + HYSTERESIS_BAND):
            current[i] = AMPLITUDE * (1 - HYSTERESIS_BAND)
        else:
            current[i] = AMPLITUDE * (1 if current[i-1] == AMPLITUDE * (1 - HYSTERESIS_BAND) else -1)

# Plotting
plt.plot(t, current)
plt.xlabel('Time (s)')
plt.ylabel('Current')
plt.title('Four Trapezoidal Current Waveforms with Hysteresis')
plt.grid(True)
plt.show()
