"""Rigol DG1022 control UI."""

from PyQt5 import QtCore, QtGui, QtWidgets
import pyvisa
import time


class Ui_MainWindow(object):

    def __init__(self, initial_type: str, initial_freq: float, initial_ampl: float) -> None:
        super().__init__()
        print(initial_type)
        self.__initial_type = initial_type
        self.__initial_freq = initial_freq
        self.__initial_ampl = initial_ampl

    def setupUi(self, MainWindow):
        print(self.__initial_ampl)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(470, 240)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.config_group = QtWidgets.QGroupBox(self.centralwidget)
        self.config_group.setGeometry(QtCore.QRect(10, 10, 331, 81))
        self.config_group.setObjectName("config_group")

        self.type_combo = QtWidgets.QComboBox(self.config_group)
        self.type_combo.setGeometry(QtCore.QRect(10, 40, 91, 22))
        self.type_combo.setObjectName("trype_combo")
        self.type_combo.addItem("")
        self.type_combo.addItem("")
        self.type_combo.addItem("")

        self.freq_input = QtWidgets.QLineEdit(self.config_group)
        self.freq_input.setGeometry(QtCore.QRect(120, 40, 91, 20))
        self.freq_input.setProperty("value", self.__initial_freq)
        self.freq_input.setObjectName("freq_input")

        self.ampl_input = QtWidgets.QLineEdit(self.config_group)
        self.ampl_input.setGeometry(QtCore.QRect(230, 40, 91, 20))
        self.ampl_input.setProperty("value", self.__initial_ampl)
        self.ampl_input.setObjectName("ampl_input")

        self.type_label = QtWidgets.QLabel(self.config_group)
        self.type_label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.type_label.setObjectName("type_label")
        self.freq_label = QtWidgets.QLabel(self.config_group)
        self.freq_label.setGeometry(QtCore.QRect(120, 20, 91, 16))
        self.freq_label.setObjectName("freq_label")
        self.ampl_label = QtWidgets.QLabel(self.config_group)
        self.ampl_label.setGeometry(QtCore.QRect(230, 20, 91, 16))
        self.ampl_label.setObjectName("ampl_label")
        self.mode_group = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_group.setGeometry(QtCore.QRect(10, 100, 331, 81))
        self.mode_group.setObjectName("mode_group")
        self.period_stop_input = QtWidgets.QLineEdit(self.mode_group)
        self.period_stop_input.setGeometry(QtCore.QRect(230, 40, 91, 20))
        self.period_stop_input.setObjectName("period_stop_input")
        self.period_stop_label = QtWidgets.QLabel(self.mode_group)
        self.period_stop_label.setGeometry(QtCore.QRect(230, 20, 91, 16))
        self.period_stop_label.setObjectName("period_stop_label")
        self.cycle_start_label = QtWidgets.QLabel(self.mode_group)
        self.cycle_start_label.setGeometry(QtCore.QRect(120, 20, 91, 16))
        self.cycle_start_label.setObjectName("cycle_start_label")
        self.cycle_start_input = QtWidgets.QLineEdit(self.mode_group)
        self.cycle_start_input.setGeometry(QtCore.QRect(120, 40, 91, 20))
        self.cycle_start_input.setObjectName("cycle_start_input")

        self.burst_button = QtWidgets.QPushButton(self.mode_group)
        self.burst_button.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.burst_button.setObjectName("burst_button")

        self.sweep_button = QtWidgets.QPushButton(self.mode_group)
        self.sweep_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.sweep_button.setObjectName("sweep_button")

        self.save_group = QtWidgets.QGroupBox(self.centralwidget)
        self.save_group.setGeometry(QtCore.QRect(350, 100, 111, 81))
        self.save_group.setObjectName("save_group")

        self.local_button = QtWidgets.QPushButton(self.save_group)
        self.local_button.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.local_button.setObjectName("local_button")
        self.local_button.clicked.connect(self.save_config)

        self.memory_button = QtWidgets.QPushButton(self.save_group)
        self.memory_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.memory_button.setObjectName("memory_button")

        self.load_group = QtWidgets.QGroupBox(self.centralwidget)
        self.load_group.setGeometry(QtCore.QRect(350, 10, 111, 80))
        self.load_group.setObjectName("load_group")

        self.load_combo = QtWidgets.QComboBox(self.load_group)
        self.load_combo.setGeometry(QtCore.QRect(10, 20, 91, 22))
        self.load_combo.setObjectName("load_combo")
        self.load_combo.addItem("")
        self.load_combo.addItem("")

        self.load_button = QtWidgets.QPushButton(self.load_group)
        self.load_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.load_button.setObjectName("load_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(20, 190, 91, 23))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.query_params)

        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(370, 190, 91, 23))
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(self.get_parameters)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rigol DG1022"))
        self.config_group.setTitle(_translate("MainWindow", "Configuración"))
        self.type_combo.setItemText(0, _translate("MainWindow", "SIN"))
        self.type_combo.setItemText(1, _translate("MainWindow", "PULSE"))
        self.type_combo.setItemText(2, _translate("MainWindow", "ARB"))
        self.type_label.setText(_translate("MainWindow", "Tipo"))
        self.freq_label.setText(_translate("MainWindow", "Frecuencia [Hz]"))
        self.ampl_label.setText(_translate("MainWindow", "Amplitud [V]"))
        self.mode_group.setTitle(_translate("MainWindow", "Modo: ---"))
        self.period_stop_label.setText(_translate("MainWindow", "Período"))
        self.cycle_start_label.setText(_translate("MainWindow", "Ciclos"))
        self.burst_button.setText(_translate("MainWindow", "Burst"))
        self.sweep_button.setText(_translate("MainWindow", "Sweep"))
        self.save_group.setTitle(_translate("MainWindow", "Guardar"))
        self.local_button.setText(_translate("MainWindow", "Local"))
        self.memory_button.setText(_translate("MainWindow", "Memoria"))
        self.load_group.setTitle(_translate(
            "MainWindow", "Cargar configuración"))

        self.load_combo.setItemText(0, _translate("MainWindow", "-"))

        self.load_button.setText(_translate("MainWindow", "Cargar"))
        self.exit_button.setText(_translate("MainWindow", "Salir"))
        self.send_button.setText(_translate("MainWindow", "Enviar"))

    # ------------------ Getters ------------------
    def get_type(self) -> float:
        return self.type_combo.currentText().upper()
    
    def get_freq(self) -> float:
        return float(self.freq_input.text())
    
    def get_ampl(self) -> float:
        return float(self.ampl_input.text())

    def verify_input(self, element) -> float | None:
        """Return the value if it's a number
           Otherwise, clears the input and return None 
        """
        try:
            return float(element.text())
        except ValueError:
            element.clear()
            print('Debes ingresar un número válido')
            return None
            # Ventana de error

    def get_parameters(self):
        func_type = self.type_combo.currentText().upper()
        frequency = self.verify_input(self.freq_input)
        amplitude = self.verify_input(self.ampl_input)

        self.DG1022.write(f'APPLY:{func_type}')
        time.sleep(0.5)
        self.DG1022.write(f'FREQ {frequency}')
        time.sleep(0.5)
        self.DG1022.write(f'VOLT {amplitude}')
        time.sleep(0.5)

    def query_params(self):
        self.DG1022.write('APPL?')
        time.sleep(0.5)
        print(self.DG1022.read())

    def load_config(self):
        return
    
    def save_config(self):
        import json
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        config["config"]["type"] = self.get_type()
        config["config"]["frequency"] = self.get_freq()
        config["config"]["amplitude"] = self.get_ampl()
        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=2)

    # rm = pyvisa.ResourceManager()
    # DG1022 = rm.open_resource(
    #     'USB0::0x0400::0x09C4::DG1D200200107::INSTR')  # Rigol DG1022


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
