import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from vista.ventanaBienvenida import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Bienvenida = QtWidgets.QMainWindow()
    ui = Ui_Bienvenida()
    ui.setupUi(Bienvenida)
    Bienvenida.show()
    sys.exit(app.exec_())