import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modelo'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'imagenes'))
from ambiente import Ambiente


class VentanaJuego(QGraphicsView):
    def __init__(self, matriz, imagenes):
        super().__init__()
        self.matriz = matriz
        self.imagenes = imagenes
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.inicializar_escena()

    def inicializar_escena(self):
        for i, fila in enumerate(self.matriz):
            for j, valor in enumerate(fila):
                imagen = QPixmap(self.imagenes[valor])
                item = QGraphicsPixmapItem(imagen)
                item.setPos(j * imagen.width(), i * imagen.height())
                self.scene.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Inicializa el ambiente
    ambiente = Ambiente()
    ambiente.inicializar_ambiente()

    # Obtén la matriz del ambiente
    matriz = ambiente.matriz

    imagenes = {
        0: "imagenes/vacio.png",
        1: "imagenes/yoshiVerde.png",
        2: "imagenes/yoshiRojo.png",
        3: "imagenes/verde.png",
        4: "imagenes/rojo.png"
    }

    ventana = VentanaJuego(matriz, imagenes)
    ventana.setWindowTitle("Juego de Yoshis")
    ventana.show()

    sys.exit(app.exec_())
