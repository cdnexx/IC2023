import matplotlib.pyplot as plot


def read_file(file, array):
    with open(f'{file}', 'r') as datafile:
        for line in datafile:
            line = line[:-1]  # Remove linebreak
            array.append(line)


data = []
time = []

read_file('data.txt', data)
read_file('time.txt', time)

plot.plot(time, data)
plot.title('Osciloscopio CH1')
plot.ylabel('Volateje (V)')
plot.xlabel('Tiempo')
plot.xlim(time[0], time[-1])
plot.show()
