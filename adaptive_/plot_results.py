import pandas as pd
import matplotlib.pyplot as plt

# Load the file
file_path = r'C:\Users\KIIT\OneDrive\Desktop\WBASN-HAR\adaptive_\adaptive_intervention_test.csv'
df = pd.read_csv(file_path)

# Convert Time to seconds
df['Time(s)'] = (df['Time(ms)'] - df['Time(ms)'].min()) / 1000

# Create the figure
plt.figure(figsize=(10, 6))

# Plot the RMSSD
# We use a scatter plot + line to show the individual heartbeats
plt.plot(df['Time(s)'], df['RMSSD'], color='red', label='Heart Rate Variability (RMSSD)', linewidth=2)
plt.scatter(df['Time(s)'], df['RMSSD'], color='darkred', s=20)

# Shade the Phases
plt.axvspan(0, 60, color='gray', alpha=0.1, label='Baseline')
plt.axvspan(60, 120, color='orange', alpha=0.2, label='Stress Task')
plt.axvspan(120, df['Time(s)'].max(), color='green', alpha=0.2, label='LED Biofeedback')

# Formatting
plt.title('Evidence of Adaptive Biofeedback Intervention', fontsize=14)
plt.xlabel('Time (Seconds)', fontsize=12)
plt.ylabel('RMSSD (ms)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Save for the book
plt.savefig('chapter_evidence_graph.png', dpi=300)
plt.show()

print("Graph saved as 'chapter_evidence_graph.png'!")