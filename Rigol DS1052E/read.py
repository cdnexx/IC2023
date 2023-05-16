import matplotlib.pyplot as plot


def read_file(file, array):
    with open(f'{file}', 'r') as datafile:
        for line in datafile:
            array.append(float(line))


data = []
time = []

read_file('data.txt', data)
read_file('time.txt', time)

if (time[-1] < 1e-3):
    time = [t * 1e6 for t in time]
    tUnit = "uS"
elif (time[-1] < 1):
    time = [t * 1e3 for t in time]
    tUnit = "mS"
else:
    tUnit = "S"

plot.plot(time, data)
plot.title('Osciloscopio CH1')
plot.ylabel('Volateje (V)')
plot.xlabel("Tiempo (" + tUnit + ")")
plot.xlim(time[0], time[-1])
plot.show()
