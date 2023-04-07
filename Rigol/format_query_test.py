qr = 'CH1:"PULSE,4.500000e-03,1.378650e+01,0.000000e+00"'
# 'CH1:"SWEEP,1.000000e+03,1.400000e+01,0.000000e+00"'
# CH1:"PULSE,3.456355e+03,1.378650e+01,0.000000e+00"
#            3456,355     13,7865
# "PULSE,1.893257e+04,1.378650e+01,0.000000e+00"
#        18932,57


# def

# props = qr.split(',')

# mode = props[0][5:]
# freq = props[1]
# ampl = props[2]
# print(float(freq))
# print(float(ampl))

def send_command(cmd):
    # self.dg1022.write(cmd)
    delay = float(f'0.1{len(cmd)}')
    print(delay)
    # time.sleep(delay)


send_command('hola mi nombre es freanco')
