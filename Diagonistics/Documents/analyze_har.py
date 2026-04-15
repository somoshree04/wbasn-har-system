import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'real_world_har.csv')
# This is where your image will be saved
save_path = os.path.join(script_dir, 'har_magnitude_plot.png')

try:
    df = pd.read_csv(file_path)
    df['Am'] = np.sqrt(df['x_accel']**2 + df['y_accel']**2 + df['z_accel']**2)
    
    # 2. Plotting with "Publication Quality" settings
    plt.figure(figsize=(12, 6), dpi=300) # High resolution for your book chapter
    plt.plot(df['Am'], color='#0047AB', linewidth=1, label='Raw Magnitude (Am)')
    
    plt.title('Real-World HAR: MPU-9250 Acceleration Magnitude', fontsize=14)
    plt.xlabel('Sample Index', fontsize=12)
    plt.ylabel('Magnitude (Raw Units)', fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.6)

    # 3. SAVE the image BEFORE showing it
    plt.savefig(save_path, bbox_inches='tight')
    print(f"✅ Plot successfully saved as: {save_path}")

    # 4. Show the plot
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")