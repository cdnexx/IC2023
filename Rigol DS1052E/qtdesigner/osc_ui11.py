import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
import pyvisa


class OscilloscopeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OscilloscopeWidget).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


class UpdateThread(QtCore.QThread):
    dataReady = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, oscilloscope):
        super(UpdateThread, self).__init__()
        self.oscilloscope = oscilloscope
        self.running = False

    def run(self) -> None:
        self.running = True
        self.oscilloscope.write(":RUN")
        while self.running:
            # Leer datos desde el osciloscopio
            self.oscilloscope.write(":WAV:DATA?")
            raw_data = self.oscilloscope.read_raw()
            # Decodificar y procesar datos
            data = np.frombuffer(raw_data, dtype=np.uint8)
            data = (data - 128) * self.oscilloscope.query_ascii_values(":WAV:YINC?")[
                0] + self.oscilloscope.query_ascii_values(":WAV:YOR?")[0]
            self.dataReady.emit(data)
            self.msleep(100)  # Actualizar cada 100 ms

    def stop(self):
        self.running = False
        self.wait()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 370)

        self.rm = pyvisa.ResourceManager()
        self.oscilloscope = self.rm.open_resource(
            'USB0::0x1AB1::0x0588::DS1ET200601265::INSTR', timeout=20, chunk_size=1024000)

        self.oscilloscope.write(":STOP")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(20, 10, 441, 281))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_time = QtWidgets.QWidget()
        self.tab_time.setObjectName("tab_time")

        self.time_osc_widget = QtWidgets.QWidget(self.tab_time)
        self.time_osc_widget.setGeometry(QtCore.QRect(0, 0, 441, 261))
        self.time_osc_widget.setStyleSheet("")
        self.time_osc_widget.setObjectName("time_osc_widget")
        self.osc_widget = OscilloscopeWidget()
        self.time_osc_widget.layout().addWidget(self.osc_widget)

        self.tab_widget.addTab(self.tab_time, "")
        self.tab_frequency = QtWidgets.QWidget()
        self.tab_frequency.setObjectName("tab_frequency")
        self.freq_osc_widget = QtWidgets.QWidget(self.tab_frequency)
        self.freq_osc_widget.setGeometry(QtCore.QRect(0, 0, 441, 261))
        self.freq_osc_widget.setStyleSheet("")
        self.freq_osc_widget.setObjectName("freq_osc_widget")
        self.tab_widget.addTab(self.tab_frequency, "")
        self.save_group = QtWidgets.QGroupBox(self.centralwidget)
        self.save_group.setGeometry(QtCore.QRect(480, 260, 151, 91))
        self.save_group.setObjectName("save_group")
        self.fft_button = QtWidgets.QPushButton(self.save_group)
        self.fft_button.setGeometry(QtCore.QRect(10, 20, 131, 28))
        self.fft_button.setObjectName("fft_button")
        self.temp_button = QtWidgets.QPushButton(self.save_group)
        self.temp_button.setGeometry(QtCore.QRect(10, 50, 131, 28))
        self.temp_button.setObjectName("temp_button")
        self.settings_group = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_group.setGeometry(QtCore.QRect(480, 20, 141, 231))
        self.settings_group.setObjectName("settings_group")
        self.ch1_slider = QtWidgets.QSlider(self.settings_group)
        self.ch1_slider.setGeometry(QtCore.QRect(10, 40, 22, 171))
        self.ch1_slider.setOrientation(QtCore.Qt.Vertical)
        self.ch1_slider.setObjectName("ch1_slider")
        self.ch2_slider = QtWidgets.QSlider(self.settings_group)
        self.ch2_slider.setGeometry(QtCore.QRect(60, 40, 22, 171))
        self.ch2_slider.setOrientation(QtCore.Qt.Vertical)
        self.ch2_slider.setObjectName("ch2_slider")
        self.trigger_slider = QtWidgets.QSlider(self.settings_group)
        self.trigger_slider.setGeometry(QtCore.QRect(110, 40, 22, 171))
        self.trigger_slider.setOrientation(QtCore.Qt.Vertical)
        self.trigger_slider.setObjectName("trigger_slider")
        self.ch1_label = QtWidgets.QLabel(self.settings_group)
        self.ch1_label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.ch1_label.setObjectName("ch1_label")
        self.ch2_label = QtWidgets.QLabel(self.settings_group)
        self.ch2_label.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.ch2_label.setObjectName("ch2_label")
        self.trigger_label = QtWidgets.QLabel(self.settings_group)
        self.trigger_label.setGeometry(QtCore.QRect(100, 20, 41, 16))
        self.trigger_label.setObjectName("trigger_label")
        self.time_group = QtWidgets.QGroupBox(self.centralwidget)
        self.time_group.setGeometry(QtCore.QRect(20, 300, 441, 51))
        self.time_group.setObjectName("time_group")
        self.time_slider = QtWidgets.QSlider(self.time_group)
        self.time_slider.setGeometry(QtCore.QRect(10, 20, 421, 22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rigol DS1052e"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.tab_time), _translate("MainWindow", "Tiempo"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.tab_frequency), _translate("MainWindow", "Frecuencia"))
        self.save_group.setTitle(_translate("MainWindow", "Guardar"))
        self.fft_button.setText(_translate("MainWindow", "FFT"))
        self.temp_button.setText(_translate("MainWindow", "Temporal"))
        self.settings_group.setTitle(_translate("MainWindow", "Ajustes"))
        self.ch1_label.setText(_translate("MainWindow", "CH1"))
        self.ch2_label.setText(_translate("MainWindow", "CH2"))
        self.trigger_label.setText(_translate("MainWindow", "Trigger"))
        self.time_group.setTitle(_translate("MainWindow", "Tiempo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
