"""Rigol dg1022 control UI."""

import time
import os
import json
import pyvisa
from PyQt5 import QtCore, QtGui, QtWidgets
from save_dialog import Ui_Dialog as SaveDialog


class Ui_MainWindow(object):

    def __init__(self) -> None:
        super().__init__()
        self.dg1022 = None
        self.green_alert = "#90ee90"
        self.yellow_alert = "#FFEA8B"
        self.orange_alert = "#FFA964"
        self.red_alert = "#E5584F"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(470, 280)
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
        self.mode_group.setGeometry(QtCore.QRect(10, 100, 331, 71))
        self.mode_group.setTitle("")
        self.mode_group.setObjectName("mode_group")
        self.param2 = QtWidgets.QLineEdit(self.mode_group)
        self.param2.setGeometry(QtCore.QRect(230, 30, 91, 20))
        self.param2.setObjectName("param2")
        self.param2_label = QtWidgets.QLabel(self.mode_group)
        self.param2_label.setGeometry(QtCore.QRect(230, 10, 91, 16))
        self.param2_label.setObjectName("param2_label")
        self.param1_label = QtWidgets.QLabel(self.mode_group)
        self.param1_label.setGeometry(QtCore.QRect(120, 10, 91, 16))
        self.param1_label.setObjectName("param1_label")
        self.param1 = QtWidgets.QLineEdit(self.mode_group)
        self.param1.setGeometry(QtCore.QRect(120, 30, 91, 20))
        self.param1.setObjectName("param1")

        self.mode_combo = QtWidgets.QComboBox(self.mode_group)
        self.mode_combo.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.mode_combo.setObjectName("mode_combo")
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_label = QtWidgets.QLabel(self.mode_group)
        self.mode_label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.mode_label.setObjectName("mode_label")

        self.save_group = QtWidgets.QGroupBox(self.centralwidget)
        self.save_group.setGeometry(QtCore.QRect(350, 90, 111, 81))
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
        self.load_button.clicked.connect(
            lambda: self.load_config(self.load_combo.currentText()))

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(10, 230, 91, 23))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.save_exit)

        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(370, 230, 91, 23))
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(self.send_configs)

        self.return_group = QtWidgets.QGroupBox(self.centralwidget)
        self.return_group.setGeometry(QtCore.QRect(10, 170, 451, 51))
        self.return_group.setObjectName("return_group")
        self.return_field = QtWidgets.QLineEdit(self.return_group)
        self.return_field.setEnabled(True)
        self.return_field.setGeometry(QtCore.QRect(10, 20, 431, 22))
        self.return_field.setReadOnly(True)
        self.return_field.setPlaceholderText("")
        self.return_field.setObjectName("return_field")
        self.query_button = QtWidgets.QPushButton(self.centralwidget)
        self.query_button.setGeometry(QtCore.QRect(270, 230, 91, 23))
        self.query_button.setObjectName("query_button")
        self.query_button.clicked.connect(self.query_params)

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
        self.action_Cargar = QtWidgets.QAction(MainWindow)
        self.action_Cargar.setObjectName("action_Cargar")
        self.action_Local = QtWidgets.QAction(MainWindow)
        self.action_Local.setObjectName("action_Local")
        self.action_Memoria = QtWidgets.QAction(MainWindow)
        self.action_Memoria.setObjectName("action_Memoria")

        self.retranslateUi(MainWindow)
        self.mode_combo.currentTextChanged['QString'].connect(
            self.update_param_labels)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rigol DG1022"))
        self.config_group.setTitle(_translate("MainWindow", "Configuración"))
        self.type_combo.setItemText(0, _translate("MainWindow", "Sine"))
        self.type_combo.setItemText(1, _translate("MainWindow", "Pulse"))
        self.type_combo.setItemText(2, _translate("MainWindow", "Arbitrary"))
        self.type_label.setText(_translate("MainWindow", "Tipo"))
        self.freq_label.setText(_translate("MainWindow", "Frecuencia [Hz]"))
        self.ampl_label.setText(_translate("MainWindow", "Amplitud [V]"))
        self.param2_label.setText(_translate("MainWindow", "Período"))
        self.param1_label.setText(_translate("MainWindow", "Ciclos"))
        self.mode_combo.setItemText(0, _translate("MainWindow", "Continuo"))
        self.mode_combo.setItemText(1, _translate("MainWindow", "Sweep"))
        self.mode_combo.setItemText(2, _translate("MainWindow", "Burst"))
        self.mode_label.setText(_translate("MainWindow", "Modo"))
        self.save_group.setTitle(_translate("MainWindow", "Guardar"))
        self.local_button.setText(_translate("MainWindow", "Local"))
        self.memory_button.setText(_translate("MainWindow", "Memoria"))
        self.load_group.setTitle(_translate(
            "MainWindow", "Cargar configuración"))
        self.load_combo.setItemText(0, _translate("MainWindow", "-"))
        self.load_button.setText(_translate("MainWindow", "Cargar"))
        self.exit_button.setText(_translate("MainWindow", "Salir"))
        self.send_button.setText(_translate("MainWindow", "Enviar"))
        self.return_group.setTitle(_translate("MainWindow", "Retorno"))
        self.query_button.setText(_translate("MainWindow", "Consultar"))
        self.action_Cargar.setText(_translate("MainWindow", "&Cargar"))
        self.action_Local.setText(_translate("MainWindow", "&Local"))
        self.action_Memoria.setText(_translate("MainWindow", "&Memoria"))

        # Load last config values
        self.load_config("last_config")
        self.update_param_labels()

        # Connect device
        self.connect_device()

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

    def get_type(self) -> str:
        return self.type_combo.currentText()

    def get_freq(self) -> float:
        return float(self.freq_input.text())

    def get_ampl(self) -> float:
        return float(self.ampl_input.text())

    def get_mode(self) -> str:
        return self.mode_combo.currentText()

    def get_param1(self) -> float:
        return float(self.param1.text())

    def get_param2(self) -> float:
        return float(self.param2.text())

    # ------------------ Methods ------------------

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

    def send_command(self, cmd):
        self.dg1022.write(cmd)
        delay = 0.001 * len(cmd)
        time.sleep(delay)
        if cmd[-1] == '?':
            return self.dg1022.read()

    def send_configs(self):
        wave = {
            "Sine": "SIN",
            "Pulse": "PULS",
            "Arbitrary": "USER"
        }
        mode = {
            "Continuo": "",
            "Sweep": "SWE",
            "Burst": "BURS"
        }

        commands = []
        # Set wave type, frequency and amplitude
        commands.append(
            f"APPL:{wave[self.get_type()]} {self.get_freq()},{self.get_ampl()}")
        # Set the selected mode
        if self.get_mode() == "Continuo":
            commands.append("SWE:STAT OFF")
            commands.append("BURS:STAT OFF")
        else:
            commands.append(f"{mode[self.get_mode()]}:STAT ON")

        # Config sweep and burst
        if self.get_mode() == "Sweep":
            commands.append(" ")
        elif self.get_mode() == "Burst":
            # Set cycle number. min=1 max=50000 || infinite=INF
            commands.append(f"BURS:NCYC {self.get_param1()}")
            # Set the period of burst. min=0.000001 max=500
            commands.append(f"BURS:INT:PER {self.get_param2()}")

        print(commands)

    def get_parameters(self):
        func_type = self.type_combo.currentText().upper()
        frequency = self.verify_input(self.freq_input)
        amplitude = self.verify_input(self.ampl_input)

        self.dg1022.write(f'APPLY:{func_type}')
        time.sleep(0.5)
        self.dg1022.write(f'FREQ {frequency}')
        time.sleep(0.5)
        self.dg1022.write(f'VOLT {amplitude}')
        time.sleep(0.5)

        self.query_params()

    def message_return(self, msg, color='white'):
        self.return_field.setText(msg)
        self.return_field.setStyleSheet(f"background: {color};")

    def format_query(self, apply, sweep, burst):
        props = apply.split(',')
        func = props[0][5:]
        freq = float(props[1])
        ampl = float(props[2])
        mode = ''
        if 'OFF' in sweep and 'OFF' in burst:
            mode = 'Continuo'
        elif 'ON' in sweep:
            mode = 'Sweep'
        elif 'ON' in burst:
            mode = 'Burst'

        return f'Tipo: {func}, Frecuencia: {freq} Hz, Amplitud: {ampl} V, Modo: {mode}'

    def query_params(self):
        try:
            apply = self.send_command('APPL?')
            sweep = self.send_command('SWE:STAT?')
            burst = self.send_command('BURS:STAT?')
            self.message_return(self.format_query(
                apply, sweep, burst), self.green_alert)
        except AttributeError:
            self.message_return(
                "Error al realizar la consulta.", self.red_alert)

    def load_config(self, config_name):
        """Load selected config"""
        if config_name != "-":
            with open(f"configs/{config_name}.json", encoding="utf-8") as config_file:
                config = json.load(config_file)
            self.type_combo.setCurrentText(config["config"]["type"])
            self.freq_input.setText(str(config["config"]["frequency"]))
            self.ampl_input.setText(str(config["config"]["amplitude"]))
            self.mode_combo.setCurrentText(config["mode"]["activeMode"])
            self.param1.setText(str(config["mode"]["param1"]))
            self.param2.setText(str(config["mode"]["param2"]))

            # Set load combo on default value
            self.load_combo.setCurrentText("-")

            self.message_return(
                f"Se ha cargado la configuración: {config_name}", color=self.green_alert)

    def save(self, filename: str):
        file_route = f"configs/{filename}.json"
        with open(file_route, "r") as config_file:
            config = json.load(config_file)
        config["config"]["type"] = self.get_type()
        config["config"]["frequency"] = self.get_freq()
        config["config"]["amplitude"] = self.get_ampl()
        config["mode"]["activeMode"] = self.get_mode()
        if self.get_mode() == "Continuo":
            config["mode"]["param1"] = 0
            config["mode"]["param2"] = 0
        else:
            config["mode"]["param1"] = self.get_param1()
            config["mode"]["param2"] = self.get_param2()

        with open(file_route, "w") as config_file:
            json.dump(config, config_file, indent=2)

    # Save last config and exit.
    def save_exit(self):
        self.save("last_config")
        exit()

    def update_saved_list(self, pre, post):
        if pre != post:
            counter = 0
            for file in post:
                try:
                    if file == pre[counter]:
                        counter += 1
                    else:
                        self.load_combo.addItem(file)
                        self.message_return(
                            f'Se ha guardado: {file}', color=self.green_alert)
                except IndexError:
                    self.load_combo.addItem(file)
                    self.message_return(
                        f'Se ha guardado: {file}', color=self.green_alert)

    def list_saved_configs(self):
        directory = os.listdir('configs')
        files = []
        for file in directory:
            if '.json' in file:
                # Append the filename to files list without file extension.
                files.append(file[:file.find('.')])
        return files

    def update_param_labels(self):
        if self.mode_combo.currentText() == "Continuo":
            self.param1_label.setText("")
            self.param2_label.setText("")
            self.param1.setEnabled(False)
            self.param2.setEnabled(False)
            self.param1.setVisible(False)
            self.param2.setVisible(False)
        if self.mode_combo.currentText() == "Sweep":
            self.param1_label.setText("Start")
            self.param2_label.setText("Stop")
            self.param1.setEnabled(True)
            self.param2.setEnabled(True)
            self.param1.setVisible(True)
            self.param2.setVisible(True)
        if self.mode_combo.currentText() == "Burst":
            self.param1_label.setText("Ciclos")
            self.param2_label.setText("Período [s]")
            self.param1.setEnabled(True)
            self.param2.setEnabled(True)
            self.param1.setVisible(True)
            self.param2.setVisible(True)

    def connect_device(self, device='USB0::0x0400::0x09C4::DG1D200200107::INSTR'):
        """Connect the device"""
        try:
            rm = pyvisa.ResourceManager()
            self.dg1022 = rm.open_resource(device)
            self.message_return(f"Conectado a: {device}", self.green_alert)
        except pyvisa.errors.VisaIOError:
            self.message_return(
                "Error al conectar con el dispositivo.", self.red_alert)
        except ValueError:
            self.message_return(
                "Error al conectar con el dispositivo.", self.red_alert)
