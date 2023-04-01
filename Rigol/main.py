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

# Todos los tipos de función pueden estar en modo BURST/SWEEP

# Sweep solo SIN
# Continuo solo SIN y arb

# Rangos de frecuencia y amplitud
# Crear caja de retorno
# Crear lista de comandos por enviar y enviarlos con delay de x segs
