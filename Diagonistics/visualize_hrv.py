import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
try:
    data = pd.read_csv('ecg_stress_log.csv')
except FileNotFoundError:
    print("Error: 'ecg_stress_log.csv' not found. Download it from your Pico first!")
    exit()

# 2. Create the Figure
plt.figure(figsize=(12, 6))
plt.style.use('seaborn-v0_8-whitegrid') # Professional style

# 3. Plot Raw ECG
plt.plot(data['Timestamp(ms)'], data['Raw_ECG'], label='Raw ECG Signal', color='#1f77b4', alpha=0.7)

# 4. Plot the Detection Threshold
plt.axhline(y=48000, color='r', linestyle='--', label='R-Peak Threshold', alpha=0.5)

# 5. Adding Scientific Labels (For your Paper)
plt.title('Real-Time ECG Acquisition and Peak Detection for HRV Analysis', fontsize=14)
plt.xlabel('Time (ms)', fontsize=12)
plt.ylabel('Amplitude (ADC Units)', fontsize=12)
plt.legend(loc='upper right')

# 6. Zoom in to show a clear heartbeat (optional)
# This zooms into the first 3 seconds of data
plt.xlim(0, 3000) 

# 7. Save the plot for your research paper
plt.tight_layout()
plt.savefig('ecg_research_plot.png', dpi=300) # High resolution for publication
plt.show()
