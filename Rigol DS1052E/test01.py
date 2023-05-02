import pyvisa
import numpy as np
import matplotlib.pyplot as plt

# Connect to the oscilloscope
rm = pyvisa.ResourceManager()
scope = rm.open_resource('USB0::0x1AB1::0x0588::DS1ED141904883')

# Set up the oscilloscope for data acquisition
scope.write(':STOP')
scope.write(':WAV:SOUR CHAN1')
scope.write(':WAV:MODE NORM')
scope.write(':WAV:FORM ASCII')
scope.write(':WAV:POINTS:MODE RAW')
scope.write(':WAV:POINTS 1000')

# Acquire data from the oscilloscope
data_str = scope.query(':WAV:DATA?')

# Convert the data from string format to a numpy array
data = np.array(data_str.strip().split(','), dtype=float)

# Calculate the time array
timestep = float(scope.query(':WAV:XINC?'))
time = np.arange(len(data)) * timestep

# Plot the data
plt.plot(time, data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Oscilloscope data')
plt.show()
