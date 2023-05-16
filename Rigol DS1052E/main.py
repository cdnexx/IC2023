import sys
from osc_ui import *
from PyQt5 import QtCore
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pyvisa


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.plot = GraphCanvas()
        self.ui.time_layout.addWidget(self.plot)


class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.ax.grid()
        # self.ax.margin(x=0)

        # Connect to oscilloscope
        self.rm = pyvisa.ResourceManager()
        self.osc = self.rm.open_resource('USB0::0x1AB1::0x0588::DS1ET200601265::INSTR',
                                         timeout=20, chunk_size=1024000)
        self.plot_data()

    def plot_data(self):
        # Grab raw data from CH1
        self.osc.write(":STOP")

        # Get the timescale
        timescale = float(self.osc.query(":TIM:SCAL?"))

        # Get the timescale offset
        timeoffset = float(self.osc.query(":TIM:OFFS?")[0])
        voltscale = float(self.osc.query(':CHAN1:SCAL?')[0])

        # Get the voltage offset
        voltoffset = float(self.osc.query(":CHAN1:OFFS?")[0])

        self.osc.write(":WAV:POIN:MODE RAW")
        self.osc.write(":WAV:DATA? CHAN1")  # Request the data
        raw_data = self.osc.read_raw()  # Read the data
        raw_data = raw_data[10:]  # Remove header (first 10 characters)
        data_size = len(raw_data)
        # sample_rate = float(self.osc.query(':ACQ:SAMP?')[0]) # Get the sample rate

        self.osc.write(":KEY:FORCE")
        self.osc.write(":RUN")

        data = np.frombuffer(raw_data, 'B')
        data = data * -1 + 255
        data = (data - 130.0 - voltoffset/voltscale*25) / 25 * voltscale

        time = np.linspace(timeoffset - 6 * timescale,
                           timeoffset + 6 * timescale,
                           num=len(data))

        if (time[-1] < 1e-3):
            time = [t * 1e6 for t in time]
            tUnit = "uS"
        elif (time[-1] < 1):
            time = [t * 1e3 for t in time]
            tUnit = "mS"
        else:
            tUnit = "S"

        plt.plot(time, data)
        plt.title('Osciloscopio CH1')
        plt.ylabel('Volateje (V)')
        plt.xlabel("Tiempo (" + tUnit + ")")
        plt.xlim(time[0], time[-1])

        self.draw()

        # Clear axes for next plot
        plt.cla()

        # Update plot every 100 ms
        update_time = 100
        QtCore.QTimer.singleShot(update_time, self.plot_data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
