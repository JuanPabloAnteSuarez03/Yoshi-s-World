from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from ventanaJuego import *



class Ui_ventanaEmergente(object):
    def setupUi(self, ventanaEmergente, mensaje):
        ventanaEmergente.setObjectName("ventanaEmergente")
        ventanaEmergente.resize(700, 300)
        ventanaEmergente.setMinimumSize(QtCore.QSize(700, 300))
        ventanaEmergente.setMaximumSize(QtCore.QSize(700, 300))
        ventanaEmergente.setStyleSheet(".btnOk {\n"
        "    background: #d30000;\n"
        "    border-radius: 20px;\n"
        "    border: nonepx;\n"
        "    color: white;\n"
        "}\n"
        ".btnOk:hover{\n"
        "    background-color: rgb(150, 0, 0);\n"
        "}\n"
        ".btnOk:pressed {\n"
        "    background-color: rgb(100, 0, 0);\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(ventanaEmergente)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 300))
        self.frame.setMinimumSize(QtCore.QSize(700, 300))
        self.frame.setMaximumSize(QtCore.QSize(700, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Cargar la imagen de fondo y ajustar al tamaño del frame
        self.background_image = QtGui.QPixmap("imagenes/fondoResultados.png").scaled(self.frame.size())  # Ajustar tamaño
        self.background_label = QtWidgets.QLabel(self.frame)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 700, 300))

        # Directorio de la imagen del icono
        icon = QtGui.QIcon("imagenes/iconoHuevo.png")  # Crear QIcon desde el archivo de imagen
        ventanaEmergente.setWindowIcon(icon)  # Establecer el icono de la ventana

        self.label_mensaje = QtWidgets.QLabel(self.frame)
        self.label_mensaje.setGeometry(QtCore.QRect(150, 20, 511, 201))
        self.label_mensaje.setStyleSheet("font: 10pt \"Cooper Black\";")
        self.label_mensaje.setObjectName("label_mensaje")
        self.label_mensaje.setWordWrap(True)
        self.label_mensaje.setText(mensaje)
        self.label_imagen = QtWidgets.QLabel(self.frame)
        self.label_imagen.setGeometry(QtCore.QRect(20, 50, 100, 100))
        self.label_imagen.setText("")
        self.label_imagen.setObjectName("label_imagen")

        # Cargar la imagen
        ruta_imagen = "imagenes/yoshiResultados.png"
        imagen = QtGui.QPixmap(ruta_imagen)

        # Establecer la imagen en el QLabel
        self.label_imagen.setPixmap(imagen)

        self.btnOk = QtWidgets.QPushButton(self.frame)
        self.btnOk.setGeometry(QtCore.QRect(590, 250, 81, 41))
        self.btnOk.setMinimumSize(QtCore.QSize(81, 41))
        self.btnOk.setMaximumSize(QtCore.QSize(81, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(ventanaEmergente.close)
        #app.activeWindow().hide()
        ventanaEmergente.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventanaEmergente, mensaje)
        QtCore.QMetaObject.connectSlotsByName(ventanaEmergente)

    def retranslateUi(self, ventanaEmergente, mensaje):
        _translate = QtCore.QCoreApplication.translate
        ventanaEmergente.setWindowTitle(_translate("ventanaEmergente", "Resultados"))
        self.label_mensaje.setText(_translate("ventanaEmergente", f"<html><head/><body><p><span style=\" font-size:12pt;\">{mensaje}<br/></span></p></body></html>"))
        self.btnOk.setText(_translate("ventanaEmergente", "OK"))
        self.btnOk.setProperty("class", _translate("ventanaEmergente", 
        "btnOk {\n"
        "    background: #d30000;\n"
        "    border-radius: 20px;\n"
        "    border: nonepx;\n"
        "    color: white;\n"
        "}\n"
        "btnOk:hover{\n"
        "    background-color: rgb(200, 0, 0);\n"
        "}\n"
        "btnOk:pressed {\n"
        "    background-color: rgb(150, 0, 0);\n"
        "}"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaEmergente = QtWidgets.QMainWindow()
    ui = Ui_ventanaEmergente()
    mensaje = ("¡El Yoshi Rojo Gana!<br>Casillas pintadas por el verde: 20, No puede seguir jugando.<br>Casillas pintadas por el rojo: 21, Puede seguir jugando.")
    ui.setupUi(ventanaEmergente,mensaje)
    ventanaEmergente.show()
    sys.exit(app.exec_())
