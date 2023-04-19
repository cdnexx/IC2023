import pyvisa
import time
rm = pyvisa.ResourceManager()
print(rm)
dg1022 = rm.open_resource('USB0::0x1AB1::0x0588::DS1ET200601265::INSTR')
dg1022.write('*IDN?')
time.sleep(0.5)
print(dg1022.read())


# DS1052E
# USB0::0x1AB1::0x0588::DS1ET200601265::INSTR

"""
Amplitud CH1 CH2
Base de tiempo (horizontal)
Fuente y nivel trigger
Adquirir, guardar y graficar
"""
