import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from ventanaEmergente import *
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modelo'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'imagenes'))

from ambiente import Ambiente
from busqueda import obtener_mejor_movimiento

import subprocess

class VentanaJuego(QGraphicsView):
    def __init__(self, matriz, imagenes, dificultad):
        super().__init__()
        self.matriz = matriz
        self.imagenes = imagenes
        self.dificultad = dificultad
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.inicializar_escena()
        # Directorio de la imagen del icono


        self.turno_yoshi_rojo = True  

        self.ventana_emergente = None

        # Crear el botón Volver
        self.btnVolver = QPushButton("Volver")
        #self.btnVolver.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.btnVolver.clicked.connect(self.volver)
        self.btnVolver.setVisible(False)  # Establecer la visibilidad inicial del botón
        self.btnVolver.setStyleSheet(
            "QPushButton {"
            "background: #2C3CFF;"
            "border-radius: 20px;"
            "border: none;"  
            "color: white;" 
            "font: 16pt Cooper Black ;" 
            "}"
            "QPushButton:hover {"
            "background-color: rgb(30, 41, 176);"
            "}"
            "QPushButton:pressed {"
            "background-color: rgb(19, 26, 112);"
            "}"
        )
        
        # Layout de la ventana
        self.layout = QHBoxLayout()  # Cambiar a un layout horizontal
        self.layout.addWidget(self.btnVolver, alignment=Qt.AlignBottom | Qt.AlignRight)  # Alineación del botón
        self.setLayout(self.layout)
    

    def inicializar_escena(self):
        self.scene.clear()
        for i, fila in enumerate(self.matriz):
            for j, valor in enumerate(fila):
                imagen = QPixmap(self.imagenes.get(valor, "imagenes/vacio.png"))
                item = QGraphicsPixmapItem(imagen)
                item.setPos(j * imagen.width(), i * imagen.height())
                self.scene.addItem(item)
                # Agregar líneas negras para los bordes de las celdas
                self.scene.addLine(j * imagen.width(), i * imagen.height(), (j+1) * imagen.width(), i * imagen.height(), Qt.black)  # Borde superior
                self.scene.addLine((j+1) * imagen.width(), i * imagen.height(), (j+1) * imagen.width(), (i+1) * imagen.height(), Qt.black)  # Borde derecho
                self.scene.addLine((j+1) * imagen.width(), (i+1) * imagen.height(), j * imagen.width(), (i+1) * imagen.height(), Qt.black)  # Borde inferior
                self.scene.addLine(j * imagen.width(), (i+1) * imagen.height(), j * imagen.width(), i * imagen.height(), Qt.black)  # Borde izquierdo
        self.adjust_size()

    def realizar_movimiento(self, x, y):
        ambiente.realizar_movimiento(ambiente.yoshi_rojo, x, y)
        self.matriz = ambiente.matriz
        self.actualizar_escena()

    def actualizar_escena(self):
        self.inicializar_escena()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.turno_yoshi_rojo:
            scene_pos = self.mapToScene(event.pos())
            first_image = QPixmap(list(self.imagenes.values())[0])
            cell_width = first_image.width()
            cell_height = first_image.height()
            x = int(scene_pos.y() // cell_height)
            y = int(scene_pos.x() // cell_width)

            if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]):
                casillas_disponibles = ambiente.obtener_casillas_disponibles(ambiente.yoshi_rojo)
                if (x, y) in casillas_disponibles:
                    self.realizar_movimiento(x, y)
                    self.turno_yoshi_rojo = False
                    QTimer.singleShot(1000, self.turno_yoshi_verde)  # Espera 1 segundo antes de mover el bot verde

    def adjust_size(self):
        if self.matriz and self.imagenes:
            first_image = QPixmap(list(self.imagenes.values())[0])
            cell_width = first_image.width()
            cell_height = first_image.height()
            scene_width = cell_width * len(self.matriz[0])
            scene_height = cell_height * len(self.matriz)
            self.scene.setSceneRect(0, 0, scene_width, scene_height)
            self.setFixedSize(scene_width + 2, scene_height + 2)

    def turno_yoshi_verde(self):
        mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, self.dificultad)
        if mejor_movimiento_verde:
            ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
            self.actualizar_escena()
            self.turno_yoshi_rojo = True
        else:
            print("El Yoshi Verde no tiene movimientos disponibles. ¡El Yoshi Rojo gana!")
            print("Casillas pintadas por el verde:", ambiente.casillas_pintadas_verde, "No puede seguir jugando, no tiene movimientos")
            print("Casillas pintadas por el rojo:", ambiente.casillas_pintadas_rojo, "Puede seguir jugando" )
            resultado = (
                "El Yoshi Verde no tiene movimientos disponibles. ¡El Yoshi Rojo gana!<br>"
                f"Casillas pintadas por el verde: {ambiente.casillas_pintadas_verde}, No puede seguir<br>jugando<br>"
                f"Casillas pintadas por el rojo: {ambiente.casillas_pintadas_rojo}, Puede seguir jugando"
            )
            self.mostrar_resultado(resultado)
            self.btnVolver.setFixedSize(120, 50)  # Ajustar tamaño horizontal y vertical
            self.btnVolver.setVisible(True)  # Establecer la visibilidad del botón "Volver" como True

        if not ambiente.obtener_casillas_disponibles(ambiente.yoshi_rojo):
            print("El yoshi verde GANÓ")
            print("Casillas pintadas por el verde:", ambiente.casillas_pintadas_verde,"Puede seguir jugando")
            print("Casillas pintadas por el rojo:", ambiente.casillas_pintadas_rojo, "No puede seguir jugando, no tiene movimientos")
            resultado = (
                "El yoshi verde GANÓ<br>"
                f"Casillas pintadas por el verde: {ambiente.casillas_pintadas_verde}, Puede seguir jugando<br>"
                f"Casillas pintadas por el rojo: {ambiente.casillas_pintadas_rojo}, No puede seguir jugando"
            )
            self.mostrar_resultado(resultado)
            self.btnVolver.setFixedSize(120, 50)  # Ajustar tamaño horizontal y vertical
            self.btnVolver.setVisible(True)  # Establecer la visibilidad del botón "Volver" como True
    
    def mostrar_resultado(self, mensaje):
        if not self.ventana_emergente:
            self.ventana_emergente = QtWidgets.QMainWindow()
            ui_ventana_emergente = Ui_ventanaEmergente()
            ui_ventana_emergente.setupUi(self.ventana_emergente, mensaje)
            self.ventana_emergente.show()

    def volver(self):
        # Ejecutar "ventanaInicio.py" usando subprocess
        subprocess.Popen(["python", "vista/ventanaInicio.py"])
        # Ocultar la ventana actual
        app = QApplication.instance()
        app.activeWindow().hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dificultad = int(sys.argv[1]) if len(sys.argv) > 1 else 2  # Recibir la dificultad como argumento
    ambiente = Ambiente()
    ambiente.inicializar_ambiente()
    matriz = ambiente.matriz
    imagenes = {
        0: "imagenes/vacio.png",
        1: "imagenes/yoshiVerde.png",
        2: "imagenes/yoshiRojo.png",
        3: "imagenes/verde.png",
        4: "imagenes/rojo.png"
    }
    ventana = VentanaJuego(matriz, imagenes, dificultad)
    icon = QtGui.QIcon("imagenes/iconoHuevo.png")  # Crear QIcon desde el archivo de imagen
    ventana.setWindowIcon(icon)  # Establecer el icono de la ventana
    ventana.setWindowTitle("Juego de Yoshis")
    ventana.show()
    
    def primer_movimiento_yoshi_verde():
        mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, 2)
        ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
        ventana.actualizar_escena()
    
    QTimer.singleShot(1000, primer_movimiento_yoshi_verde)  # Espera 1 segundo antes del primer movimiento del Yoshi verde

    sys.exit(app.exec_())