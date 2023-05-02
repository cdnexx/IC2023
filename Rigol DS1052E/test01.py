import pyvisa
import numpy as np
import matplotlib.pyplot as plt

# Connect to the instrument
rm = pyvisa.ResourceManager()
scope = rm.open_resource('USB0::0x1AB1::0x0588::DS1ET200601265::INSTR')

# Set up the waveform acquisition parameters
scope.write(':WAV:SOUR CHAN1')  # select channel 1
scope.write(':WAV:MODE NORM')  # set normal mode
scope.write(':WAV:FORM ASC')   # set ASCII waveform format
scope.write(':WAV:POIN:MODE RAW')  # set raw point mode
scope.write(':WAV:POIN 1000')  # set number of points to acquire

# Acquire the waveform data
data_ascii = scope.query(':WAV:DATA?')
data = np.fromstring(data_ascii, sep=',')  # convert ASCII data to numpy array

# Plot the waveform data
plt.plot(data)
plt.xlabel('Time (samples)')
plt.ylabel('Voltage (V)')
plt.show()
