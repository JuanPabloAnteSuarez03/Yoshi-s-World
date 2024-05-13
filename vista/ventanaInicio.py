from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaInicio(object):
    def setupUi(self, ventanaInicio):
        ventanaInicio.setObjectName("ventanaInicio")
        ventanaInicio.resize(1000, 700)
        ventanaInicio.setMinimumSize(QtCore.QSize(1000, 700))
        ventanaInicio.setMaximumSize(QtCore.QSize(1000, 700))
        ventanaInicio.setStyleSheet(
        ".btnFacil {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        ".btnFacil:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        ".btnFacil:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}\n"
        ".btnMedio {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        ".btnMedio:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        ".btnMedio:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}\n"
        ".btnDificil {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        ".btnDificil:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        ".btnDificil:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(ventanaInicio)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.frame.setMinimumSize(QtCore.QSize(1000, 700))
        self.frame.setMaximumSize(QtCore.QSize(1000, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Cargar la imagen de fondo y ajustar al tamaño del frame
        self.background_image = QtGui.QPixmap("imagenes/fondoNiveles.png").scaled(self.frame.size())  # Ajustar tamaño
        self.background_label = QtWidgets.QLabel(self.frame)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1000, 700))

        # Directorio de la imagen del icono
        icon = QtGui.QIcon("imagenes/iconoHuevo.png")  # Crear QIcon desde el archivo de imagen
        ventanaInicio.setWindowIcon(icon)  # Establecer el icono de la ventana

        self.label_titulo_nivel = QtWidgets.QLabel(self.frame)
        self.label_titulo_nivel.setGeometry(QtCore.QRect(0, 40, 1000, 80))
        self.label_titulo_nivel.setMinimumSize(QtCore.QSize(1000, 80))
        self.label_titulo_nivel.setMaximumSize(QtCore.QSize(1000, 80))
        self.label_titulo_nivel.setStyleSheet("font: 20pt \"Cooper Black\";")
        self.label_titulo_nivel.setObjectName("label_titulo_nivel")
        self.btnFacil = QtWidgets.QPushButton(self.frame)
        self.btnFacil.setGeometry(QtCore.QRect(190, 230, 140, 60))
        self.btnFacil.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.btnFacil.setObjectName("btnFacil")
        self.btnMedio = QtWidgets.QPushButton(self.frame)
        self.btnMedio.setGeometry(QtCore.QRect(430, 230, 140, 60))
        self.btnMedio.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.btnMedio.setObjectName("btnMedio")
        self.btnDificil = QtWidgets.QPushButton(self.frame)
        self.btnDificil.setGeometry(QtCore.QRect(670, 230, 140, 60))
        self.btnDificil.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.btnDificil.setObjectName("btnDificil")
        ventanaInicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventanaInicio)
        QtCore.QMetaObject.connectSlotsByName(ventanaInicio)

    def retranslateUi(self, ventanaInicio):
        _translate = QtCore.QCoreApplication.translate
        ventanaInicio.setWindowTitle(_translate("ventanaInicio", "NIVELES"))
        self.label_titulo_nivel.setText(_translate("ventanaInicio", "<html><head/><body><p align=\"center\"><span style=\" color:#d30000;\">NIVELES</span></p></body></html>"))
        self.btnFacil.setText(_translate("ventanaInicio", "FACIL"))
        self.btnFacil.setProperty("class", _translate("ventanaInicio", 
        "btnFacil {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        "btnFacil:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        "btnFacil:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}"))
        self.btnMedio.setText(_translate("ventanaInicio", "MEDIO"))
        self.btnMedio.setProperty("class", _translate("ventanaInicio", 
        "btnMedio {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        "btnMedio:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        "btnMedio:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}"))
        self.btnDificil.setText(_translate("ventanaInicio", "DIFICIL"))
        self.btnDificil.setProperty("class", _translate("ventanaInicio", 
        "btnDificil {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        "btnDificil:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        "btnDificil:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaInicio = QtWidgets.QMainWindow()
    ui = Ui_ventanaInicio()
    ui.setupUi(ventanaInicio)
    ventanaInicio.show()
    sys.exit(app.exec_())
