from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import subprocess

class Ui_Bienvenida(object):
    def setupUi(self, Bienvenida):
        Bienvenida.setObjectName("Bienvenida")
        Bienvenida.resize(700, 700)
        Bienvenida.setMinimumSize(QtCore.QSize(700, 700))
        Bienvenida.setMaximumSize(QtCore.QSize(700, 700))
        Bienvenida.setStyleSheet(".btnContinuar {"
                            "font: 12pt \"Cooper Black\";"
                            "background: #D30000;"
                            "border-radius: 20px;"
                            "border: none;"  # Elimina el borde predeterminado del botón
                            "color: white;"  # Color de texto blanco
                            "}"
                            ".btnContinuar:hover {"
                            "background-color: rgb(150, 0, 0);"
                            "}"
                            ".btnContinuar:pressed {"
                            "background-color: rgb(100, 0, 0);"
                            "}")
        self.centralwidget = QtWidgets.QWidget(Bienvenida)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setMinimumSize(QtCore.QSize(700, 700))
        self.frame.setMaximumSize(QtCore.QSize(700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Cargar la imagen de fondo y ajustar al tamaño del frame
        self.background_image = QtGui.QPixmap("imagenes/fondoYoshi.png").scaled(self.frame.size())  # Ajustar tamaño
        self.background_label = QtWidgets.QLabel(self.frame)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 700, 700))

        # Directorio de la imagen del icono
        icon = QtGui.QIcon("imagenes/iconoHuevo.png")  # Crear QIcon desde el archivo de imagen
        Bienvenida.setWindowIcon(icon)  # Establecer el icono de la ventana

        self.label_titulo_bienvenida = QtWidgets.QLabel(self.frame)
        self.label_titulo_bienvenida.setGeometry(QtCore.QRect(0, 0, 700, 80))
        self.label_titulo_bienvenida.setMinimumSize(QtCore.QSize(700, 80))
        self.label_titulo_bienvenida.setMaximumSize(QtCore.QSize(700, 80))
        self.label_titulo_bienvenida.setStyleSheet("font: 20pt \"Cooper Black\";")
        self.label_titulo_bienvenida.setObjectName("label_titulo_bienvenida")
        self.label_miembros = QtWidgets.QLabel(self.frame)
        self.label_miembros.setGeometry(QtCore.QRect(0, 160, 700, 230))
        self.label_miembros.setMinimumSize(QtCore.QSize(700, 230))
        self.label_miembros.setMaximumSize(QtCore.QSize(700, 230))
        self.label_miembros.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.label_miembros.setObjectName("label_miembros")
        self.btnContinuar = QtWidgets.QPushButton(self.frame)
        self.btnContinuar.setGeometry(QtCore.QRect(260, 480, 171, 51))
        self.btnContinuar.setMinimumSize(QtCore.QSize(171, 51))
        self.btnContinuar.setMaximumSize(QtCore.QSize(171, 51))
        self.btnContinuar.setStyleSheet("font: 12pt \"Cooper Black\";")
        self.btnContinuar.setObjectName("btnContinuar")
        self.btnContinuar.clicked.connect(self.abrir_continuar)
        Bienvenida.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bienvenida)
        QtCore.QMetaObject.connectSlotsByName(Bienvenida)

    def retranslateUi(self, Bienvenida):
        _translate = QtCore.QCoreApplication.translate
        Bienvenida.setWindowTitle(_translate("Bienvenida", "BIENVENIDA"))
        self.label_titulo_bienvenida.setText(_translate("Bienvenida", "<html><head/><body><p align=\"center\"><span style=\" color:#d30000;\">YOSHI\'S WORLD</span></p></body></html>"))
        self.label_miembros.setText(_translate("Bienvenida", "<html><head/><body><p align=\"center\"><span style=\" color:#d30000;\">Juan Pablo Ante - 2140132</span></p><p align=\"center\"><span style=\" color:#d30000;\">Nicolás Garcés - 2180066</span></p><p align=\"center\"><span style=\" color:#d30000;\">Alejandro Guerrero - 2179652</span></p><p align=\"center\"><span style=\" color:#d30000;\">Alejandro Zambrano - 1941088</span></p></body></html>"))
        self.btnContinuar.setText(_translate("Bienvenida", "CONTINUAR"))
        self.btnContinuar.setProperty("class", _translate("Bienvenida", 
        "btnContinuar {"
        "font: 12pt \"Cooper Black\";"
        "background: #D30000;"
        "border-radius: 20px;"
        "border: none;"  # Elimina el borde predeterminado del botón
        "color: white;"  # Color de texto blanco
        "}"
        ".btnContinuar:hover {"
        "background-color: rgb(150, 0, 0);"
        "}"
        "btnContinuar:pressed {"
        "background-color: rgb(100, 0, 0);"
        "}"))
    
    def abrir_continuar(self):
        # Ejecutar "ventanaInicio.py" usando subprocess
        subprocess.Popen(["python", "vista/ventanaInicio.py"])
         # Ocultar la ventana actual
        app = QApplication.instance()
        app.activeWindow().hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bienvenida = QtWidgets.QMainWindow()
    ui = Ui_Bienvenida()
    ui.setupUi(Bienvenida)
    Bienvenida.show()
    sys.exit(app.exec_())
