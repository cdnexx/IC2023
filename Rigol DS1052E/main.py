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

        self.initial_channel_slider_value()

        self.ui.ch1_slider.valueChanged.connect(
            lambda: self.change_channel_scale(channel=1, value=self.ui.ch1_slider.value()))
        self.ui.ch2_slider.valueChanged.connect(
            lambda: self.change_channel_scale(channel=2, value=self.ui.ch2_slider.value()))
        self.ui.time_slider.valueChanged.connect(
            lambda: self.change_time_scale(value=self.ui.time_slider.value()))

    def initial_channel_slider_value(self):
        # Slider values according to scale values when probe is 1x
        channel_slider_value = {
            1e+01: 1,
            5e+00: 2,
            2e+00: 3,
            1e+00: 4,
            5e-01: 5,
            2e-01: 6,
            1e-01: 7,
            5e-02: 8,
            2e-02: 9,
            1e-02: 10,
            5e-03: 11,
            2e-03: 12
        }

        time_slider_value = {
            5e+01: 1,
            2e+01: 2,
            1e+01: 3,
            5e+00: 4,
            2e+00: 5,
            1e+00: 6,
            5e-01: 7,
            2e-01: 8,
            1e-01: 9,
            5e-02: 10,
            2e-02: 11,
            1e-02: 12,
            5e-03: 13,
            2e-03: 14,
            1e-03: 15,
            5e-04: 16,
            2e-04: 17,
            1e-04: 18,
            5e-05: 19,
            2e-05: 20,
            1e-05: 21,
            5e-06: 22,
            2e-06: 23,
            1e-06: 24,
            5e-07: 25,
            2e-07: 26,
            1e-07: 27,
            5e-08: 28,
            2e-08: 29,
            1e-08: 30,
            5e-09: 31
        }

        current_value_ch1 = float(self.plot.osc.query(":CHAN1:SCAL?"))
        current_value_ch2 = float(self.plot.osc.query(":CHAN2:SCAL?"))
        current_value_time = float(self.plot.osc.query(":TIM:SCAL?"))

        self.ui.ch1_slider.setValue(channel_slider_value[current_value_ch1])
        self.ui.ch2_slider.setValue(channel_slider_value[current_value_ch2])
        self.ui.time_slider.setValue(time_slider_value[current_value_time])

        self.update_scale_label("all")

    def change_channel_scale(self, channel: int, value: int):
        # Scale values according to slider values when probe is 1x
        scale_value = {
            1: 1e+01,
            2: 5e+00,
            3: 2e+00,
            4: 1e+00,
            5: 5e-01,
            6: 2e-01,
            7: 1e-01,
            8: 5e-02,
            9: 2e-02,
            10: 1e-02,
            11: 5e-03,
            12: 2e-03
        }

        self.plot.osc.write(f":CHAN{channel}:SCAL {scale_value[value]}")
        self.update_scale_label(f"ch{channel}")

    def change_time_scale(self, value: int):
        scale_value = {
            1: 5e+01,
            2: 2e+01,
            3: 1e+01,
            4: 5e+00,
            5: 2e+00,
            6: 1e+00,
            7: 5e-01,
            8: 2e-01,
            9: 1e-01,
            10: 5e-02,
            11: 2e-02,
            12: 1e-02,
            13: 5e-03,
            14: 2e-03,
            15: 1e-03,
            16: 5e-04,
            17: 2e-04,
            18: 1e-04,
            19: 5e-05,
            20: 2e-05,
            21: 1e-05,
            22: 5e-06,
            23: 2e-06,
            24: 1e-06,
            25: 5e-07,
            26: 2e-07,
            27: 1e-07,
            28: 5e-08,
            29: 2e-08,
            30: 1e-08,
            31: 5e-09
        }

        self.plot.osc.write(f":TIM:SCAL {scale_value[value]}")
        self.update_scale_label("time")

    def update_scale_label(self, slider: str):
        if slider == "ch1":
            scale = float(self.plot.osc.query(":CHAN1:SCAL?"))
            self.ui.ch1_scale_label.setText(
                f"{self.get_prefix(float(scale))}V")
        elif slider == "ch2":
            scale = float(self.plot.osc.query(":CHAN2:SCAL?"))
            self.ui.ch2_scale_label.setText(
                f"{self.get_prefix(float(scale))}V")
            print(scale)
        elif slider == "time":
            scale = float(self.plot.osc.query(":TIM:SCAL?"))
            self.ui.time_scale_label.setText(
                f"{self.get_prefix(float(scale))}S")
            print(scale)
        elif slider == "all":
            self.update_scale_label("ch1")
            self.update_scale_label("ch2")
            self.update_scale_label("time")

    def get_prefix(self, value):
        # pre_number = str(value).split("e")[0]
        number = {
            5e+01: "5",
            2e+01: "2",
            1e+01: "1",
            5e+00: "5",
            2e+00: "2",
            1e+00: "1",
            5e-01: "5",
            2e-01: "2",
            1e-01: "1",
            5e-02: "5",
            2e-02: "2",
            1e-02: "1",
            5e-03: "5",
            2e-03: "2",
            1e-03: "1",
            5e-04: "5",
            2e-04: "2",
            1e-04: "1",
            5e-05: "5",
            2e-05: "2",
            1e-05: "1",
            5e-06: "5",
            2e-06: "2",
            1e-06: "1",
            5e-07: "5",
            2e-07: "2",
            1e-07: "1",
            5e-08: "5",
            2e-08: "2",
            1e-08: "1",
            5e-09: "5",
        }

        prefix = {
            5e+01: "0 ",
            2e+01: "0 ",
            1e+01: "0 ",
            5e+00: " ",
            2e+00: " ",
            1e+00: " ",
            5e-01: "00 m",
            2e-01: "00 m",
            1e-01: "00 m",
            5e-02: "0 m",
            2e-02: "0 m",
            1e-02: "0 m",
            5e-03: " m",
            2e-03: " m",
            1e-03: " m",
            5e-04: "00 u",
            2e-04: "00 u",
            1e-04: "00 u",
            5e-05: "0 u",
            2e-05: "0 u",
            1e-05: "0 u",
            5e-06: " u",
            2e-06: " u",
            1e-06: " u",
            5e-07: "00 n",
            2e-07: "00 n",
            1e-07: "00 n",
            5e-08: "0 n",
            2e-08: "0 n",
            1e-08: "0 n",
            5e-09: " n",
        }

        return f"{number[value]}{prefix[value]}"


class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax1 = plt.subplots()
        self.ax2 = self.ax1.twinx()
        super().__init__(self.fig)

        # self.ax.margin(x=0)

        # Connect to oscilloscope
        self.rm = pyvisa.ResourceManager()
        self.osc = self.rm.open_resource('USB0::0x1AB1::0x0588::DS1ET200601265::INSTR',
                                         timeout=20, chunk_size=1024000)
        self.plot_data()

    def get_channel_data(self, channel: int):
        # Get volt scale
        voltscale = float(self.osc.query(f':CHAN{channel}:SCAL?'))  # [0]

        # Get the voltage offset
        voltoffset = float(self.osc.query(f":CHAN{channel}:OFFS?"))  # [0]

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
        # ax = plt.subplot()
        self.ax1.plot(time, data_ch1)
        self.ax2.plot(time, data_ch2, 'r-')
        self.ax1.grid(True)
        self.ax2.grid(True)

        # plt.ylabel('Voltaje (V)')
        # plt.xlabel("Tiempo (" + tUnit + ")")
        plt.xlim(time[0], time[-1])

        self.draw()

        # Clear axes for next plot
        self.ax1.cla()
        self.ax2.cla()
        # plt.cla()

        # Update plot every 100 ms
        update_time = 100
        QtCore.QTimer.singleShot(update_time, self.plot_data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
