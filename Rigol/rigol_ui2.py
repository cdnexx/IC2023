"""Rigol DG1022 control UI."""

from PyQt5 import QtCore, QtGui, QtWidgets
from save_dialog import Ui_Dialog as SaveDialog
import pyvisa
import time
import os
import json


class Ui_MainWindow(object):

    def __init__(self, initial_type: str, initial_freq: float, initial_ampl: float) -> None:
        super().__init__()
        self.__initial_type = initial_type
        self.__initial_freq = initial_freq
        self.__initial_ampl = initial_ampl

    def setupUi(self, MainWindow):
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
        self.type_combo.setObjectName("type_combo")
        self.type_combo.addItem("")
        self.type_combo.addItem("")
        self.type_combo.addItem("")

        self.freq_input = QtWidgets.QLineEdit(self.config_group)
        self.freq_input.setGeometry(QtCore.QRect(120, 40, 91, 20))
        self.freq_input.setObjectName("freq_input")

        self.ampl_input = QtWidgets.QLineEdit(self.config_group)
        self.ampl_input.setGeometry(QtCore.QRect(230, 40, 91, 20))
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
        self.local_button.clicked.connect(self.open_save_dialog)

        self.memory_button = QtWidgets.QPushButton(self.save_group)
        self.memory_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.memory_button.setObjectName("memory_button")

        self.load_group = QtWidgets.QGroupBox(self.centralwidget)
        self.load_group.setGeometry(QtCore.QRect(350, 10, 111, 80))
        self.load_group.setObjectName("load_group")

        self.load_combo = QtWidgets.QComboBox(self.load_group)
        self.load_combo.setGeometry(QtCore.QRect(10, 20, 91, 22))
        self.load_combo.setObjectName("load_combo")

        # Create an empty item and then add an item
        # for each .json file in the configs folder
        self.load_combo.addItem("")
        for file in self.list_saved_configs():
            self.load_combo.addItem(file)

        self.load_button = QtWidgets.QPushButton(self.load_group)
        self.load_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.load_button.setObjectName("load_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(20, 190, 91, 23))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.save_exit)

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

        # Set config values
        self.type_combo.setCurrentText(self.__initial_type)
        self.freq_input.setText(str(self.__initial_freq))
        self.ampl_input.setText(str(self.__initial_ampl))

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

        # # Set text value for the default option and then
        # # set the remaining text values as the filename.
        # self.load_combo.setItemText(0, _translate("MainWindow", "-"))
        # counter = 1
        # for file in self.list_saved_configs():
        #     self.load_combo.setItemText(
        #         counter, _translate("MainWindow", file))
        #     counter += 1

        self.load_button.setText(_translate("MainWindow", "Cargar"))
        self.exit_button.setText(_translate("MainWindow", "Salir"))
        self.send_button.setText(_translate("MainWindow", "Enviar"))

    # ------------------ Windows ------------------

    def open_save_dialog(self):
        pre_file_list = self.list_saved_configs()
        dialog = QtWidgets.QDialog()
        dialog.ui = SaveDialog(self.save)
        dialog.ui.setupUi(dialog)
        dialog.exec_()

        # Once the dialog window is closed, config list is updated
        post_file_list = self.list_saved_configs()
        self.update_saved_list(pre_file_list, post_file_list)

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

        self.query_params()

    def query_params(self):
        self.DG1022.write('APPL?')
        time.sleep(0.5)
        print(self.DG1022.read())

    def load_config(self):
        return

    def save(self, filename: str):
        file_route = f"configs/{filename}.json"
        with open(file_route, "r") as config_file:
            config = json.load(config_file)
        config["config"]["type"] = self.get_type()
        config["config"]["frequency"] = self.get_freq()
        config["config"]["amplitude"] = self.get_ampl()
        with open(file_route, "w") as config_file:
            json.dump(config, config_file, indent=2)

    # Save last config and exit.
    def save_exit(self):
        self.save("last_config")
        exit()

    def update_saved_list(self, pre, post):
        counter = 0
        for file in post:
            try:
                if file == pre[counter]:
                    counter += 1
                else:
                    self.load_combo.addItem(file)
                    print(f"nuevo archivo {file}")
            except IndexError:
                self.load_combo.addItem(file)

    def list_saved_configs(self):
        directory = os.listdir('configs')
        files = []
        for file in directory:
            if '.json' in file:
                # Append the filename to files list without file extension.
                files.append(file[:file.find('.')])
        return files

    # rm = pyvisa.ResourceManager()
    # DG1022 = rm.open_resource(
    #     'USB0::0x0400::0x09C4::DG1D200200107::INSTR')  # Rigol DG1022
