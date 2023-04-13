# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rigol2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.period_stop_input = QtWidgets.QLineEdit(self.mode_group)
        self.period_stop_input.setGeometry(QtCore.QRect(230, 30, 91, 20))
        self.period_stop_input.setObjectName("period_stop_input")
        self.period_stop_label = QtWidgets.QLabel(self.mode_group)
        self.period_stop_label.setGeometry(QtCore.QRect(230, 10, 91, 16))
        self.period_stop_label.setObjectName("period_stop_label")
        self.cycle_start_label = QtWidgets.QLabel(self.mode_group)
        self.cycle_start_label.setGeometry(QtCore.QRect(120, 10, 91, 16))
        self.cycle_start_label.setObjectName("cycle_start_label")
        self.cycle_start_input = QtWidgets.QLineEdit(self.mode_group)
        self.cycle_start_input.setGeometry(QtCore.QRect(120, 30, 91, 20))
        self.cycle_start_input.setObjectName("cycle_start_input")

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
        self.load_combo.addItem("")

        # Create an empty item and then add an item
        # for each .json file in the configs folder
        self.load_combo.addItem("")
        for file in self.list_saved_configs():
            self.load_combo.addItem(file)

        self.load_button = QtWidgets.QPushButton(self.load_group)
        self.load_button.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.load_button.setObjectName("load_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(10, 230, 91, 23))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.save_exit)

        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(370, 230, 91, 23))
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(self.get_parameters)

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
            self.cycle_start_label.setText)  # type: ignore
        self.mode_combo.currentTextChanged['QString'].connect(
            self.period_stop_label.setText)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rigol DG1022"))
        self.config_group.setTitle(_translate("MainWindow", "Configuración"))
        self.type_combo.setItemText(0, _translate("MainWindow", "Sine"))
        self.type_combo.setItemText(1, _translate("MainWindow", "Pulse"))
        self.type_combo.setItemText(2, _translate("MainWindow", "Arbitrary"))

        self.type_combo.setCurrentText(self.__initial_type)
        self.freq_input.setText(str(self.__initial_freq))
        self.ampl_input.setText(str(self.__initial_ampl))

        self.type_label.setText(_translate("MainWindow", "Tipo"))
        self.freq_label.setText(_translate("MainWindow", "Frecuencia [Hz]"))
        self.ampl_label.setText(_translate("MainWindow", "Amplitud [V]"))
        self.period_stop_label.setText(_translate("MainWindow", "Período"))
        self.cycle_start_label.setText(_translate("MainWindow", "Ciclos"))
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
        self.return_field.setText(_translate("MainWindow", "CONSOLE RETURN"))
        self.query_button.setText(_translate("MainWindow", "Consultar"))
        self.action_Cargar.setText(_translate("MainWindow", "&Cargar"))
        self.action_Local.setText(_translate("MainWindow", "&Local"))
        self.action_Memoria.setText(_translate("MainWindow", "&Memoria"))