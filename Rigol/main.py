from PyQt5 import QtWidgets
from rigol_ui2 import Ui_MainWindow
import json


def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    func = config["config"]["type"]
    freq = config["config"]["frequency"]
    ampl = config["config"]["amplitude"]
    return func, freq, ampl


config = read_config()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(initial_type=config[0],
                       initial_freq=config[1],
                       initial_ampl=config[2])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
