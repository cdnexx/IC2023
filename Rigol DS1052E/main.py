import sys
from osc_ui import *
from PyQt5 import QtCore
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


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

        self.plot_data()

    def plot_data(self):
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

        plt.plot(time, data)
        plt.title('Osciloscopio CH1')
        plt.ylabel('Volateje (V)')
        plt.xlabel("Tiempo (" + tUnit + ")")
        plt.xlim(time[0], time[-1])

        self.draw()

        QtCore.QTimer.singleShot(1000, self.plot_data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
