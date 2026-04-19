import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
try:
    # 'comment' ignores our timer lines, 'skipinitialspace' removes accidental spaces
    df = pd.read_csv('stress_analysis.csv', comment='#', skipinitialspace=True)
    
    # --- CLEANING STEP: This fixes the KeyError ---
    # Removes hidden characters and forces everything to UPPERCASE
    df.columns = df.columns.str.strip().str.upper()
    print("Columns found:", df.columns.tolist()) 
    
except Exception as e:
    print(f"Error: {e}")
    exit()

# 2. Pre-processing
# Now 'TIMESTAMP' is guaranteed to be recognized
df['SEC'] = df['TIMESTAMP'] / 1000

# 3. Create the Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot A: ECG Signal
ax1.plot(df['SEC'], df['ECG'], color='#e74c3c', linewidth=0.7)
ax1.set_title('Cardiac Response (AD8232 Sensor)', fontsize=14, fontweight='bold')
ax1.set_ylabel('ADC Amplitude')
ax1.grid(True, linestyle='--', alpha=0.6)

# Plot B: Movement Magnitude
ax2.plot(df['SEC'], df['MOVEMENT'], color='#3498db', linewidth=1.2)
ax2.set_title('Inertial Context (MPU-9250 Sensor)', fontsize=14, fontweight='bold')
ax2.set_ylabel('G-Force (Magnitude)')
ax2.set_xlabel('Time (Seconds)')
ax2.grid(True, linestyle='--', alpha=0.6)

# 4. Highlight Phases
ax1.axvspan(0, 60, color='green', alpha=0.1, label='Baseline')
ax1.axvspan(60, 120, color='orange', alpha=0.1, label='Exertion')
ax1.axvspan(120, 180, color='purple', alpha=0.1, label='Stress')
ax1.legend(loc='upper right')

plt.tight_layout()
plt.savefig('stress_validation_plot.png', dpi=300)
plt.show()