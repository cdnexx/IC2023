# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rigol DS1052E/qtdesigner/osc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 370)
        MainWindow.setWindowTitle("Rigol DS1052e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(20, 10, 441, 281))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_time = QtWidgets.QWidget()
        self.tab_time.setObjectName("tab_time")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_time)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.time_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.time_layout.setContentsMargins(0, 0, 0, 0)
        self.time_layout.setObjectName("time_layout")
        self.tab_widget.addTab(self.tab_time, "Tiempo")
        self.tab_frequency = QtWidgets.QWidget()
        self.tab_frequency.setObjectName("tab_frequency")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_frequency)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 431, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.freq_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.freq_layout.setContentsMargins(0, 0, 0, 0)
        self.freq_layout.setObjectName("freq_layout")
        self.tab_widget.addTab(self.tab_frequency, "Frecuencia")
        self.save_group = QtWidgets.QGroupBox(self.centralwidget)
        self.save_group.setGeometry(QtCore.QRect(480, 260, 151, 91))
        self.save_group.setTitle("Guardar")
        self.save_group.setObjectName("save_group")
        self.fft_button = QtWidgets.QPushButton(self.save_group)
        self.fft_button.setGeometry(QtCore.QRect(10, 20, 131, 28))
        self.fft_button.setText("FFT")
        self.fft_button.setObjectName("fft_button")
        self.temp_button = QtWidgets.QPushButton(self.save_group)
        self.temp_button.setGeometry(QtCore.QRect(10, 50, 131, 28))
        self.temp_button.setText("Temporal")
        self.temp_button.setObjectName("temp_button")
        self.settings_group = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_group.setGeometry(QtCore.QRect(480, 20, 141, 231))
        self.settings_group.setTitle("Ajustes")
        self.settings_group.setObjectName("settings_group")
        self.ch1_slider = QtWidgets.QSlider(self.settings_group)
        self.ch1_slider.setGeometry(QtCore.QRect(10, 40, 22, 161))
        self.ch1_slider.setMinimum(1)
        self.ch1_slider.setMaximum(12)
        self.ch1_slider.setPageStep(1)
        self.ch1_slider.setOrientation(QtCore.Qt.Vertical)
        self.ch1_slider.setObjectName("ch1_slider")
        self.ch2_slider = QtWidgets.QSlider(self.settings_group)
        self.ch2_slider.setGeometry(QtCore.QRect(60, 40, 22, 161))
        self.ch2_slider.setMinimum(1)
        self.ch2_slider.setMaximum(12)
        self.ch2_slider.setPageStep(1)
        self.ch2_slider.setOrientation(QtCore.Qt.Vertical)
        self.ch2_slider.setObjectName("ch2_slider")
        self.trigger_slider = QtWidgets.QSlider(self.settings_group)
        self.trigger_slider.setGeometry(QtCore.QRect(110, 40, 22, 161))
        self.trigger_slider.setOrientation(QtCore.Qt.Vertical)
        self.trigger_slider.setObjectName("trigger_slider")
        self.ch1_label = QtWidgets.QLabel(self.settings_group)
        self.ch1_label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.ch1_label.setText("CH1")
        self.ch1_label.setObjectName("ch1_label")
        self.ch2_label = QtWidgets.QLabel(self.settings_group)
        self.ch2_label.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.ch2_label.setText("CH2")
        self.ch2_label.setObjectName("ch2_label")
        self.trigger_label = QtWidgets.QLabel(self.settings_group)
        self.trigger_label.setGeometry(QtCore.QRect(100, 20, 41, 16))
        self.trigger_label.setText("Trigger")
        self.trigger_label.setObjectName("trigger_label")
        self.ch1_state = QtWidgets.QLabel(self.settings_group)
        self.ch1_state.setGeometry(QtCore.QRect(10, 210, 41, 16))
        self.ch1_state.setText("200 mV")
        self.ch1_state.setObjectName("ch1_state")
        self.ch2_state = QtWidgets.QLabel(self.settings_group)
        self.ch2_state.setGeometry(QtCore.QRect(60, 210, 41, 16))
        self.ch2_state.setText("500 mV")
        self.ch2_state.setObjectName("ch2_state")
        self.time_group = QtWidgets.QGroupBox(self.centralwidget)
        self.time_group.setGeometry(QtCore.QRect(20, 300, 441, 51))
        self.time_group.setTitle("Tiempo")
        self.time_group.setObjectName("time_group")
        self.time_slider = QtWidgets.QSlider(self.time_group)
        self.time_slider.setGeometry(QtCore.QRect(10, 20, 381, 22))
        self.time_slider.setMinimum(1)
        self.time_slider.setMaximum(31)
        self.time_slider.setPageStep(1)
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.time_state = QtWidgets.QLabel(self.time_group)
        self.time_state.setGeometry(QtCore.QRect(400, 20, 41, 16))
        self.time_state.setText("500 us")
        self.time_state.setObjectName("time_state")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass
