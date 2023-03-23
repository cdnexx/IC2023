"""Rigol DG1022 control."""
import pyvisa
import time

# ('USB0::0x0400::0x09C4::DG1D200200107::INSTR', 'ASRL1::INSTR', 'ASRL8::INSTR')
rm = pyvisa.ResourceManager()
print(rm.list_resources())
DG1022 = rm.open_resource('USB0::0x0400::0x09C4::DG1D200200107::INSTR')


def send(msg: str):
    """"Send message to Rigol and calculate a delay time"""
    DG1022.write(msg)
    delay = 0.001 * len(msg)
    if delay < 0.2:
        delay = 0.2
    print(F'SEND: {msg}')
    time.sleep(delay)


def set_voltage(low: float, high: float):
    """"Set min and max value for Vpp"""
    send()

#send('APPLY SIN')
#send('FREQ MAX')


while True:
    msg = input('CMD: ')
    send(msg)
    if msg[-1] == '?':
        time.sleep(0.2)
        print(DG1022.read())
# DG1022.query('*IDN?')
# Output CH1 off
# "OUTP OFF"
# Output CH1 -> Memory User
# "FUNC USER"
# Output CH2 -> Memory User
# "FUNC:CH2 USER"

# Preguntar sobre los "Points"
# Preguntar sobre los modos "Vpp Vdc" (frecuencia y amplitud?)
