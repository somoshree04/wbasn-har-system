import machine
import time

# Initialize ADC
ecg_adc = machine.ADC(26)

# Create/Open a file in "write" mode
# WARNING: This will overwrite previous data each time you run it
file = open("ecg_stress_log.csv", "w")
file.write("Timestamp(ms),Raw_ECG,Threshold\n") # CSV Headers

print("Logging started... Stay still for 20 seconds.")

start_time = time.ticks_ms()
duration = 20000  # Log for 20 seconds

try:
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        raw_value = ecg_adc.read_u16()
        current_time = time.ticks_ms() - start_time
        
        # Log to file
        file.write(f"{current_time},{raw_value},48000\n")
        
        # Print for Plotter (so you can still see it live)
        print((raw_value, 48000))
        
        time.sleep(0.01)
finally:
    file.close()
    print("Logging finished! File saved as ecg_stress_log.csv")
