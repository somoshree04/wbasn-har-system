import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter

#clean the signals, find the heartbeats, and generate the final data

def analyze_file(filename):
    # 1. Load Data
    df = pd.read_csv(filename)
    
    # 2. Filter (Same bandpass as before, but inverting the signal)
    def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return lfilter(b, a, data)

    fs = 100.0
    # Clean and Invert (to make peaks positive)
    filtered = butter_bandpass_filter(df['Raw_ECG'], 0.5, 40.0, fs) * -1
    
    # 3. Simple R-Peak Detection
    # We look for values above a relative threshold
    threshold = np.percentile(filtered, 95) 
    peaks = []
    for i in range(1, len(filtered)-1):
        if filtered[i] > threshold and filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1]:
            peaks.append(df['Timestamp_ms'].iloc[i])
    
    # Filter out "double counts" (peaks too close together < 300ms)
    real_peaks = []
    if len(peaks) > 0:
        real_peaks.append(peaks[0])
        for i in range(1, len(peaks)):
            if peaks[i] - real_peaks[-1] > 300:
                real_peaks.append(peaks[i])

    # 4. Calculate HRV Metrics
    rr_intervals = np.diff(real_peaks)
    bpm = 60000 / np.mean(rr_intervals) if len(rr_intervals) > 0 else 0
    rmssd = np.sqrt(np.mean(np.square(np.diff(rr_intervals)))) if len(rr_intervals) > 1 else 0
    
    return bpm, rmssd

# Run analysis on your three files
files = ["calm.csv", "stress.csv", "exercise.csv"]
results = []

print(f"{'Condition':<15} | {'Avg BPM':<10} | {'RMSSD (ms)':<10}")
print("-" * 45)

for f in files:
    bpm, rmssd = analyze_file(f)
    print(f"{f.replace('.csv',''):<15} | {bpm:<10.2f} | {rmssd:<10.2f}")
