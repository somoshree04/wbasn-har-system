import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 1. Load your real research data
df = pd.read_csv('ecg_stress_log.csv')

# 2. Butterworth Filter Implementation (Scientific standard)
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

# Parameters adjusted for your AD8232 sampling rate (~100Hz)
fs = 100.0
lowcut = 0.5  # Removes Baseline Wander (breathing artifacts)
highcut = 40.0 # Removes Powerline Noise (50/60Hz fuzziness)

# 3. Apply the filter
df['Filtered_ECG'] = butter_bandpass_filter(df['Raw_ECG'], lowcut, highcut, fs) * -1
# 4. Generate the Comparison Plot for your Paper
plt.figure(figsize=(12, 7))

# Plot Raw Data (What you saw in Thonny)
plt.subplot(2, 1, 1)
plt.plot(df['Raw_ECG'].tail(500), color='salmon', label='Raw Signal (Thonny Output)')
plt.title('Stage 1: Raw Data Acquisition with Motion Noise')
plt.ylabel('Amplitude')
plt.legend()

# Plot Filtered Data (The "New Research" result)
plt.subplot(2, 1, 2)
plt.plot(df['Filtered_ECG'].tail(500), color='seagreen', label='Bandpass Filtered (0.5-40Hz)')
plt.title('Stage 2: Digital Signal Conditioning (DSP)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.savefig('DSP_Comparison_Research.png', dpi=300) # Save as high-res for publication
plt.show()
