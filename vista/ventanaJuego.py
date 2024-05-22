import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modelo'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'imagenes'))

from ambiente import Ambiente
from busqueda import obtener_mejor_movimiento

class VentanaJuego(QGraphicsView):
    def __init__(self, matriz, imagenes):
        super().__init__()
        self.matriz = matriz
        self.imagenes = imagenes
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.inicializar_escena()

        self.turno_yoshi_rojo = True  

    def inicializar_escena(self):
        self.scene.clear()
        for i, fila in enumerate(self.matriz):
            for j, valor in enumerate(fila):
                imagen = QPixmap(self.imagenes.get(valor, "Yoshi-s-World/imagenes/vacio.png"))
                item = QGraphicsPixmapItem(imagen)
                item.setPos(j * imagen.width(), i * imagen.height())
                self.scene.addItem(item)
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
        mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, 500)
        if mejor_movimiento_verde:
            ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
            self.actualizar_escena()
            self.turno_yoshi_rojo = True
        else:
            print("El Yoshi Verde no tiene movimientos disponibles. ¡El Yoshi Rojo gana!")
            print("Casillas pintadas por el verde:", ambiente.casillas_pintadas_verde, "No puede seguir jugando, no tiene movimientos")
            print("Casillas pintadas por el rojo:", ambiente.casillas_pintadas_rojo, "Puede seguir jugando" )

        if not ambiente.obtener_casillas_disponibles(ambiente.yoshi_rojo):
            print("El yoshi verde GANÓ")
            print("Casillas pintadas por el verde:", ambiente.casillas_pintadas_verde,"Puede seguir jugando")
            print("Casillas pintadas por el rojo:", ambiente.casillas_pintadas_rojo, "No puede seguir jugando, no tiene movimientos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ambiente = Ambiente()
    ambiente.inicializar_ambiente()
    matriz = ambiente.matriz
    imagenes = {
        0: "Yoshi-s-World/imagenes/vacio.png",
        1: "Yoshi-s-World/imagenes/yoshiVerde.png",
        2: "Yoshi-s-World/imagenes/yoshiRojo.png",
        3: "Yoshi-s-World/imagenes/verde.png",
        4: "Yoshi-s-World/imagenes/rojo.png"
    }
    ventana = VentanaJuego(matriz, imagenes)
    ventana.setWindowTitle("Juego de Yoshis")
    ventana.show()
    
    def primer_movimiento_yoshi_verde():
        mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, 2)
        ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
        ventana.actualizar_escena()
    
    QTimer.singleShot(1000, primer_movimiento_yoshi_verde)  # Espera 1 segundo antes del primer movimiento del Yoshi verde

    sys.exit(app.exec_())