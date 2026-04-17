import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def clean_data(data):
    # Standard filter for your paper
    b, a = butter(2, [0.5/50, 40/50], btype='band')
    return lfilter(b, a, data) * -1

# Load your 3 research files
df_calm = pd.read_csv('calm.csv')
df_stress = pd.read_csv('stress.csv')
df_exer = pd.read_csv('exercise.csv')

plt.figure(figsize=(15, 10))

# 1. Calm Graph
plt.subplot(3, 1, 1)
# Use [500:1500] instead of .iloc[500:1500]
plt.plot(clean_data(df_calm['Raw_ECG'])[500:1500], color='blue')
plt.title('Figure A: Baseline (Calm State) - Regular HRV', fontsize=12)
plt.ylabel('Amplitude')

# 2. Stress Graph
plt.subplot(3, 1, 2)
plt.plot(clean_data(df_stress['Raw_ECG'])[500:1500], color='red')
plt.title('Figure B: Emotional Stress - Increased Inter-beat Variability', fontsize=12)
plt.ylabel('Amplitude')

# 3. Exercise Graph
plt.subplot(3, 1, 3)
plt.plot(clean_data(df_exer['Raw_ECG'])[500:1500], color='green')
plt.title('Figure C: Physical Exertion - High Frequency/Low HRV', fontsize=12)
plt.xlabel('Samples (at 100Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.savefig('Comparative_ECG_Analysis.png', dpi=300)
plt.show()