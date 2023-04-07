"""Main module"""
import json
from PyQt5 import QtWidgets
from rigol_ui2 import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# Sweep solo SIN
# Continuo solo SIN y arb

# Rangos de frecuencia y amplitud
# boton enviar y aplicar (run)

# Start y stop del sweep? -> FREQ
# SWEEP TIME, SPACING
