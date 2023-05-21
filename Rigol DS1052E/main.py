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

        self.initial_slider_value()

        self.ui.ch1_slider.valueChanged.connect(
            lambda: self.change_scale(channel=1, value=self.ui.ch1_slider.value()))
        self.ui.ch2_slider.valueChanged.connect(
            lambda: self.change_scale(channel=2, value=self.ui.ch2_slider.value()))

    def initial_slider_value(self):
        # Slider values according to scale values when probe is 1x
        slider_value = {
            10: 1,
            5: 2,
            2: 3,
            1: 4,
            0.5: 5,
            0.2: 6,
            0.1: 7,
            0.05: 8,
            0.02: 9,
            0.01: 10,
            0.005: 11,
            0.002: 12
        }
        current_value_ch1 = float(self.plot.osc.query(f":CHAN1:SCAL?"))
        current_value_ch2 = float(self.plot.osc.query(f":CHAN2:SCAL?"))

        self.ui.ch1_slider.setValue(slider_value[current_value_ch1])
        self.ui.ch2_slider.setValue(slider_value[current_value_ch2])

    def change_scale(self, channel: int, value: int):
        # Scale values according to slider values when probe is 1x
        scale_value = {
            1: 10,
            2: 5,
            3: 2,
            4: 1,
            5: 0.5,
            6: 0.2,
            7: 0.1,
            8: 0.05,
            9: 0.02,
            10: 0.01,
            11: 0.005,
            12: 0.002
        }

        self.plot.osc.write(f":CHAN{channel}:SCAL {scale_value[value]}")


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

    def get_channel_data(self, channel: int):
        # Get volt scale
        voltscale = float(self.osc.query(f':CHAN{channel}:SCAL?')[0])

        # Get the voltage offset
        voltoffset = float(self.osc.query(f":CHAN{channel}:OFFS?")[0])

        self.osc.write(f":WAV:DATA? CHAN{channel}")  # Request the data
        raw_data = self.osc.read_raw()  # Read the data
        raw_data = raw_data[10:]  # Remove header (first 10 characters)

        data = np.frombuffer(raw_data, 'B')
        data = data * -1 + 255
        data = (data - 130.0 - voltoffset/voltscale*25) / 25 * voltscale

        return data

    def plot_data(self):

        # Grab raw data from CH1
        # self.osc.write(":STOP")

        # Get the timescale
        timescale = float(self.osc.query(":TIM:SCAL?"))

        # Get the timescale offset
        timeoffset = float(self.osc.query(":TIM:OFFS?")[0])

        self.osc.write(":WAV:POIN:MODE RAW")

        # data_size = len(raw_data)
        # sample_rate = float(self.osc.query(':ACQ:SAMP?')[0]) # Get the sample rate

        self.osc.write(":KEY:FORCE")
        # self.osc.write(":RUN")

        # Get data from each channel
        data_ch1 = self.get_channel_data(channel=1)
        data_ch2 = self.get_channel_data(channel=2)

        time = np.linspace(timeoffset - 6 * timescale,
                           timeoffset + 6 * timescale,
                           num=len(data_ch1))

        if (time[-1] < 1e-3):
            time = [t * 1e6 for t in time]
            tUnit = "uS"
        elif (time[-1] < 1):
            time = [t * 1e3 for t in time]
            tUnit = "mS"
        else:
            tUnit = "S"

        # Plot each channel
        ax = plt.subplot()
        ax.plot(time, data_ch1)
        ax.plot(time, data_ch2)

        # plt.ylabel('Voltaje (V)')
        # plt.xlabel("Tiempo (" + tUnit + ")")
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
