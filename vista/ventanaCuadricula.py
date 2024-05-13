from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import subprocess

class Ui_ventanaCuadricula(object):
    def setupUi(self, ventanaCuadricula):
        ventanaCuadricula.setObjectName("ventanaCuadricula")
        ventanaCuadricula.resize(1000, 1000)
        ventanaCuadricula.setMinimumSize(QtCore.QSize(1000, 1000))
        ventanaCuadricula.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        ventanaCuadricula.setFont(font)
        ventanaCuadricula.setStyleSheet(".btnVolver {\n"
                                "   background: #d30000;\n"
                                "   border-radius: 20px;\n"
                                "   border: nonepx;\n"
                                "   color: white;\n"
                                "}\n"
                                ".btnVolver:hover {\n"
                                "   background-color: rgb(150, 0, 0);\n"
                                "}\n"
                                ".btnVolver:pressed{\n"
                                "   background-color: rgb(100, 0, 0)\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(ventanaCuadricula)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.frame.setMinimumSize(QtCore.QSize(1000, 1000))
        self.frame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Cargar la imagen de fondo y ajustar al tamaño del frame
        self.background_image = QtGui.QPixmap("imagenes/fondoCuadricula.png").scaled(self.frame.size())  # Ajustar tamaño
        self.background_label = QtWidgets.QLabel(self.frame)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1000, 1000))

        # Directorio de la imagen del icono
        icon = QtGui.QIcon("imagenes/iconoHuevo.png")  # Crear QIcon desde el archivo de imagen
        ventanaCuadricula.setWindowIcon(icon)  # Establecer el icono de la ventana

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 891))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")

        self.graphicsViews = []

        # Crear widgets de QGraphicsView
        for i in range(8):
            for j in range(8):
                graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
                graphicsView.setObjectName(f"graphicsView_{i * 8 + j}")
                self.gridLayout.addWidget(graphicsView, i, j)
                self.graphicsViews.append(graphicsView)

                # Configurar la escena
                scene = QtWidgets.QGraphicsScene()
                graphicsView.setScene(scene)

                # Establecer propiedades para desactivar el desplazamiento automático y el modo de arrastre
                graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

                # Conectar el evento de clic del mouse a un slot
                graphicsView.mousePressEvent = lambda event, i=i, j=j: self.on_graphicsView_clicked(i, j)

        # Cargar yoshis rojos y verdes
        self.yoshi_rojo = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap("imagenes/yoshiRojo.png"))
        self.yoshi_verde = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap("imagenes/yoshiVerde.png"))

        self.yoshi_seleccionado = None  # Variable para el yoshi seleccionado

        self.set_yoshi(self.yoshi_rojo, 0, 0)
        self.set_yoshi(self.yoshi_verde, 0, 1)

        self.btnVolver = QtWidgets.QPushButton(self.frame)
        self.btnVolver.setGeometry(QtCore.QRect(770, 920, 171, 51))
        self.btnVolver.setStyleSheet("font: 14pt \"Cooper Black\";")
        self.btnVolver.setObjectName("btnVolver")
        #self.btnVolver.clicked.connect(self.abrir_niveles)
        ventanaCuadricula.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventanaCuadricula)
        QtCore.QMetaObject.connectSlotsByName(ventanaCuadricula)

    def retranslateUi(self, ventanaCuadricula):
        _translate = QtCore.QCoreApplication.translate
        ventanaCuadricula.setWindowTitle(_translate("Cuadricula", "CUADRICULA"))
        self.btnVolver.setText(_translate("Cuadricula", "VOLVER"))
        self.btnVolver.setProperty("class", _translate("Cuadricula", 
        "btnVolver {\n"
        "   background: #d30000;\n"
        "   border-radius: 20px;\n"
        "   border: nonepx;\n"
        "   color: white;\n"
        "}\n"
        "btnVolver:hover {\n"
        "   background-color: rgb(150, 0, 0);\n"
        "}\n"
        "btnVolver:pressed{\n"
        "   background-color: rgb(100, 0, 0)\n"
        "}"))
    
    """def abrir_niveles(self):
        # Ejecutar "Mando y Grogu.py" usando subprocess
        subprocess.Popen(["python", "vista/ventanaInicio.py"])
         # Ocultar la ventana actual
        app = QApplication.instance()
        app.activeWindow().hide()"""    

    def on_graphicsView_clicked(self, i, j):
        # Obtener el QGraphicsView clicado
        clicked_graphicsView = self.graphicsViews[i * 8 + j]

        # Comprobar si la celda clicada está vacía
        if not clicked_graphicsView.scene().items():
            if self.yoshi_seleccionado is not None:
                # Mover el yoshi seleccionado a la celda vacía
                self.set_yoshi(self.yoshi_seleccionado, i, j)
                self.yoshi_seleccionado = None
        else:
            # Comprobar si el elemento clicado es un yoshi
            clicked_items = clicked_graphicsView.scene().items()
            if self.yoshi_rojo in clicked_items:
                self.yoshi_seleccionado = self.yoshi_rojo
            elif self.yoshi_verde in clicked_items:
                self.yoshi_seleccionado = self.yoshi_verde

    def set_yoshi(self, yoshi_item, i, j):
        # Eliminar el yoshi de su escena actual
        if yoshi_item.scene() is not None:
            yoshi_item.scene().removeItem(yoshi_item)

        # Calcular la posición para centrar el yoshi en la celda
        cell_width = self.graphicsViews[0].width()
        cell_height = self.graphicsViews[0].height()
        yoshi_width = yoshi_item.pixmap().width()
        yoshi_height = yoshi_item.pixmap().height()
        x_pos = (cell_width - yoshi_width) / 2
        y_pos = (cell_height - yoshi_height) / 2

        # Establecer el yoshi en la nueva celda
        scene = self.graphicsViews[i * 8 + j].scene()

        # Si el yoshi está colocado en la posición inicial o en una posición en la que ha estado antes, 
        # centrarlo, de lo contrario, establecerlo en la posición especificada
        if i == 0 and j == 0:
            scene.addItem(yoshi_item)
            yoshi_item.setPos(0, 0)
        elif i == 0 and j == 1:
            scene.addItem(yoshi_item)
            yoshi_item.setPos(0, 1)  
        else:
            scene.addItem(yoshi_item)
            yoshi_item.setPos(j * cell_width + x_pos, i * cell_height + y_pos)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaCuadricula = QtWidgets.QMainWindow()
    ui = Ui_ventanaCuadricula()
    ui.setupUi(ventanaCuadricula)
    ventanaCuadricula.show()
    sys.exit(app.exec_())
