from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modelo'))

from ambiente import *
from yoshi import *

import subprocess

ambiente = Ambiente() # Inicia el ambiente

class Ui_ventanaCuadricula(object):
    def setupUi(self, ventanaCuadricula):
        ventanaCuadricula.setObjectName("ventanaCuadricula") # Establece el nombre del objeto de la ventana principal como "ventanaCuadricula".
        ventanaCuadricula.resize(1000, 1000) # Establece el tamaño de la ventana principal como 1000x1000 píxeles.
        ventanaCuadricula.setMinimumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño mínimo de la ventana principal como 1000x1000 píxeles.
        ventanaCuadricula.setMaximumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño máximo de la ventana principal como 1000x1000 píxeles.
        font = QtGui.QFont() # Crea una instancia de QFont para establecer la fuente de texto de la ventana.
        font.setFamily("Cooper Black") # Establece la familia de fuentes de texto como "Cooper Black".
        font.setPointSize(10) # Establece el tamaño de la fuente de texto como 10 puntos.
        ventanaCuadricula.setFont(font) # Aplica la configuración de fuente de texto a la ventana principal.
        ventanaCuadricula.setStyleSheet(".btnVolver {\n" # Define el estilo CSS de la ventana, incluyendo estilos para el botón "Volver" y sus estados de hover y presionado.
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
        self.centralwidget = QtWidgets.QWidget(ventanaCuadricula) # Crea un widget central dentro de la ventana principal.
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño mínimo del widget central como 1000x1000 píxeles.
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño máximo del widget central como 1000x1000 píxeles.
        self.centralwidget.setObjectName("centralwidget") # Establece el nombre del widget central como "centralwidget".
        self.frame = QtWidgets.QFrame(self.centralwidget) # Crea un marco dentro del widget central.
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 1000)) # Establece la geometría (posición y tamaño) del marco como 0,0 y 1000x1000 píxeles respectivamente.
        self.frame.setMinimumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño mínimo del marco como 1000x1000 píxeles.
        self.frame.setMaximumSize(QtCore.QSize(1000, 1000)) # Establece el tamaño máximo del marco como 1000x1000 píxeles.
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel) # Establece la forma del marco como un panel estilizado.
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised) # Establece la sombra del marco como elevada.
        self.frame.setObjectName("frame") # Establece el nombre del marco como "frame".

        self.background_image = QtGui.QPixmap("imagenes/fondoCuadricula.png").scaled(self.frame.size()) # Carga fondoCuadricula como fondo para el marco y la escala para que se ajuste al tamaño del marco.
        self.background_label = QtWidgets.QLabel(self.frame) # Crea una etiqueta para mostrar la imagen de fondo dentro del marco.
        self.background_label.setPixmap(self.background_image) # Establece la imagen de fondo en la etiqueta.
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1000, 1000)) # Establece la geometría de la etiqueta para que ocupe todo el tamaño del marco.

        icon = QtGui.QIcon("imagenes/iconoHuevo.png") # Crea un icono para la ventana principal utilizando la imagen iconoHuevo.
        ventanaCuadricula.setWindowIcon(icon) # Establece el icono de la ventana principal

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame) # Crea un widget de cuadrícula dentro del marco para organizar los elementos de la interfaz gráfica.
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 891)) # Establece la geometría del widget de cuadrícula.
        self.gridLayoutWidget.setObjectName("gridLayoutWidget") # Establece el nombre del widget de cuadrícula.
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget) # Crea un diseño de cuadrícula dentro del widget de cuadrícula.
        self.gridLayout.setContentsMargins(0, 0, 0, 0) # Establece los márgenes del diseño de cuadrícula a 0.
        self.gridLayout.setSpacing(8) # Establece el espacio entre los elementos de la cuadrícula como 8 píxeles.
        self.gridLayout.setObjectName("gridLayout") # Establece el nombre del diseño de cuadrícula.
        
        ambiente.inicializar_ambiente() # Llama al método inicializar_ambiente() del objeto ambiente, que se encarga de inicializar el entorno del juego.
        ambiente.mostrar_ambiente() # Llama al método mostrar_ambiente() del objeto ambiente, que muestra el entorno del juego en su estado actual.

        self.graphicsViews = [] #  Inicializa una lista vacía llamada graphicsViews que se utilizará para almacenar los widgets de QGraphicsView

        for i, fila in enumerate(ambiente.matriz): # Itera sobre las filas de la matriz del ambiente.
            for j, columna in enumerate(fila): # Itera sobre las columnas de cada fila de la matriz del ambiente.
                graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget) # Crea un nuevo widget de QGraphicsView dentro del gridLayoutWidget
                graphicsView.setObjectName(f"graphicsView_{i * 8 + j}") # Establece el nombre del widget QGraphicsView utilizando la posición en la cuadrícula.
                self.gridLayout.addWidget(graphicsView, i, j) # Agrega el widget QGraphicsView al diseño de cuadrícula en la posición i, j.
                self.graphicsViews.append(graphicsView) # Agrega el widget QGraphicsView a la lista graphicsViews.

                scene = QtWidgets.QGraphicsScene() # Crea una nueva escena de QGraphicsScene para cada QGraphicsView.
                graphicsView.setScene(scene) # Establece la escena recién creada como la escena del QGraphicsView.

                graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) # Desactiva la barra de desplazamiento horizontal del QGraphicsView.
                graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) # Desactiva la barra de desplazamiento vertical del QGraphicsView
                graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag) # Establece el modo de arrastre del QGraphicsView como NoDrag, lo que significa que los elementos dentro del QGraphicsView no se pueden arrastrar.

                graphicsView.mousePressEvent = lambda event, i=i, j=j: self.on_graphicsView_clicked(i, j) #  Sobrescribe el método mousePressEvent del QGraphicsView para manejar los clics del mouse, pasando las coordenadas i y j.

        # Crear items de QGraphicsPixmapItem directamente
        self.yoshi_rojo_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap("imagenes/yoshiRojo.png")) # Crea un elemento de QGraphicsPixmapItem para representar al personaje Yoshi rojo utilizando la imagen yoshiRojo.
        self.yoshi_verde_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap("imagenes/yoshiVerde.png")) # Crea un elemento de QGraphicsPixmapItem para representar al personaje Yoshi verde utilizando la imagen yoshiVerde.

        # Crear objetos Yoshi sin incluir QGraphicsPixmapItem
        self.yoshi_rojo = Yoshi('rojo', ambiente.yoshi_rojo.fila, ambiente.yoshi_rojo.columna) # Crea un objeto de la clase Yoshi con el color "rojo" y las coordenadas correspondientes a la fila y columna del Yoshi rojo en el ambiente.
        self.yoshi_verde = Yoshi('verde', ambiente.yoshi_verde.fila, ambiente.yoshi_verde.columna) # Crea un objeto de la clase Yoshi con el color "verde" y las coordenadas correspondientes a la fila y columna del Yoshi verde en el ambiente.

        self.yoshi_seleccionado = None # Inicializa la variable yoshi_seleccionado como None, que se utilizará para almacenar el elemento Yoshi seleccionado por el usuario en la interfaz gráfica.

        # Usar items de QGraphicsPixmapItem en set_yoshi
        self.set_yoshi(self.yoshi_rojo_item, self.yoshi_rojo.fila, self.yoshi_rojo.columna) # Llama al método set_yoshi() con el elemento de Yoshi rojo, su fila y columna correspondiente, para posicionarlo en la interfaz gráfica.
        self.set_yoshi(self.yoshi_verde_item, self.yoshi_verde.fila, self.yoshi_verde.columna) #  Llama al método set_yoshi() con el elemento de Yoshi verde, su fila y columna correspondiente, para posicionarlo en la interfaz gráfica. 

        self.btnVolver = QtWidgets.QPushButton(self.frame) # Crea un botón de tipo QPushButton y lo coloca en el marco frame.
        self.btnVolver.setGeometry(QtCore.QRect(770, 920, 171, 51)) # Establece la geometría (posición y tamaño) del botón en el marco.
        self.btnVolver.setStyleSheet("font: 14pt \"Cooper Black\";") # Establece el estilo de la fuente del botón.
        self.btnVolver.setObjectName("btnVolver") # Establece el nombre del objeto del botón.
        self.btnVolver.clicked.connect(self.abrir_niveles) # Conecta la señal clicked del botón a la función abrir_niveles().
        ventanaCuadricula.setCentralWidget(self.centralwidget) # Establece el widget central de la ventana principal como centralwidget.

        self.retranslateUi(ventanaCuadricula) # Llama al método retranslateUi() para traducir los textos de la interfaz gráfica.
        QtCore.QMetaObject.connectSlotsByName(ventanaCuadricula) # Conecta los slots (métodos) de la ventana principal mediante su nombre.

    def retranslateUi(self, ventanaCuadricula): # Define el método retranslateUi() para traducir los textos de la interfaz gráfica.
        _translate = QtCore.QCoreApplication.translate # Asigna a una función la traducción que se utiliza para traducir cadenas de texto en la interfaz de usuario.
        ventanaCuadricula.setWindowTitle(_translate("Cuadricula", "CUADRICULA")) #  Establece el título de la ventana principal.
        self.btnVolver.setText(_translate("Cuadricula", "VOLVER")) # Establece el texto del botón "Volver".
        self.btnVolver.setProperty("class", _translate("Cuadricula",  # Establece algunas propiedades de estilo del botón utilizando hojas de estilo.
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

    def abrir_niveles(self): # Define el método abrir_niveles() que se ejecutará cuando se haga clic en el botón "Volver".
        subprocess.Popen(["python", "vista/ventanaInicio.py"]) # Abre una nueva instancia de Python para ejecutar el script ventanaInicio.py.
        app = QApplication.instance() # Obtiene la instancia existente de la aplicación.
        app.activeWindow().hide() # Oculta la ventana activa actualmente en la aplicación.

    def on_graphicsView_clicked(self, i, j):# Define el método on_graphicsView_clicked() que se ejecutará cuando se haga clic en un QGraphicsView.
        clicked_graphicsView = self.graphicsViews[i * 8 + j] #  Obtiene el QGraphicsView que se ha clicado utilizando sus índices i y j.
        if not clicked_graphicsView.scene().items(): # Verifica si no hay elementos en la escena asociada al QGraphicsView que se ha clicado.
            if self.yoshi_seleccionado is not None: # Verifica si hay un elemento Yoshi seleccionado.
                # Obtener el objeto Yoshi correspondiente
                yoshi = self.get_yoshi_by_item(self.yoshi_seleccionado) # Obtiene el objeto Yoshi correspondiente al elemento Yoshi seleccionado.
                if yoshi is not None: # Verifica si se ha encontrado un objeto Yoshi correspondiente al elemento seleccionado.
                    ambiente.realizar_movimiento(yoshi, i, j) # Llama al método realizar_movimiento() del objeto ambiente para realizar el movimiento del Yoshi.
                self.set_yoshi(self.yoshi_seleccionado, i, j) # Actualiza la posición del elemento Yoshi seleccionado en la interfaz gráfica.
                self.yoshi_seleccionado = None # Reinicia la selección del elemento Yoshi.
                ambiente.mostrar_ambiente() # Actualiza la visualización del ambiente después de realizar el movimiento del Yoshi.
        else:
            clicked_items = clicked_graphicsView.scene().items() # Obtiene todos los elementos presentes en la escena asociada al QGraphicsView clicado.
            if self.yoshi_rojo_item in clicked_items: # Verifica si el elemento Yoshi rojo está entre los elementos clicados.
                self.yoshi_seleccionado = self.yoshi_rojo_item # Establece el elemento Yoshi rojo como el elemento seleccionado si ha sido clicado.
            elif self.yoshi_verde_item in clicked_items: # Verifica si el elemento Yoshi verde está entre los elementos clicados.
                self.yoshi_seleccionado = self.yoshi_verde_item # Establece el elemento Yoshi verde como el elemento seleccionado si ha sido clicado.

    def get_yoshi_by_item(self, yoshi_item): # Define una función para obtener el objeto Yoshi correspondiente al elemento gráfico de Yoshi.
        if yoshi_item == self.yoshi_rojo_item: # Verifica si el elemento de Yoshi dado es igual al elemento de Yoshi rojo.
            return self.yoshi_rojo # Retorna el objeto Yoshi rojo si el elemento de Yoshi coincide con el elemento de Yoshi rojo.
        elif yoshi_item == self.yoshi_verde_item: # Verifica si el elemento de Yoshi dado es igual al elemento de Yoshi verde.
            return self.yoshi_verde # Retorna el objeto Yoshi verde si el elemento de Yoshi coincide con el elemento de Yoshi verde.
        return None # Retorna None si el elemento de Yoshi no coincide con ningún elemento de Yoshi conocido.

    def set_yoshi(self, yoshi_item, i, j): # Define una función para establecer la posición del elemento de Yoshi en la cuadrícula.
        if yoshi_item.scene() is not None: # Verifica si el elemento de Yoshi pertenece a una escena.
            yoshi_item.scene().removeItem(yoshi_item) # Remueve el elemento de Yoshi de la escena actual si ya está presente.

        cell_width = self.graphicsViews[0].width() # Obtiene el ancho de una celda en la cuadrícula.
        cell_height = self.graphicsViews[0].height() # Obtiene el alto de una celda en la cuadrícula.
        yoshi_width = yoshi_item.pixmap().width() # Obtiene el ancho del pixmap (imagen) del Yoshi.
        yoshi_height = yoshi_item.pixmap().height() # Obtiene el alto del pixmap del Yoshi.
        x_pos = (cell_width - yoshi_width) / 2 # Calcula la posición x para centrar el Yoshi en la celda.
        y_pos = (cell_height - yoshi_height) / 2 # Calcula la posición y para centrar el Yoshi en la celda.

        scene = self.graphicsViews[i * 8 + j].scene() # Obtiene la escena asociada al QGraphicsView en la posición especificada en la cuadrícula.
        
        # Verificar si el yoshi rojo está inicializado en el ambiente
        if ambiente.yoshi_rojo is not None: # Verifica si el objeto Yoshi rojo está inicializado en el ambiente.
            scene.addItem(yoshi_item) # Agrega el elemento de Yoshi a la escena.
            yoshi_item.setPos(ambiente.yoshi_rojo.fila, ambiente.yoshi_rojo.columna) # Establece la posición del elemento de Yoshi en la posición actual del Yoshi rojo en la cuadrícula.

        # Verificar si el yoshi verde está inicializado en el ambiente
        if ambiente.yoshi_verde is not None: # Verifica si el objeto Yoshi verde está inicializado en el ambiente.
            scene.addItem(yoshi_item) # Agrega el elemento de Yoshi a la escena.
            yoshi_item.setPos(ambiente.yoshi_verde.fila, ambiente.yoshi_verde.columna) # Establece la posición del elemento de Yoshi en la posición actual del Yoshi verde en la cuadrícula si está inicializado.

        # Si ninguno de los Yoshis está inicializado, colocar el yoshi en la posición calculada
        if ambiente.yoshi_rojo is None and ambiente.yoshi_verde is None: # Verifica si ninguno de los Yoshis está inicializado en el ambiente.
            scene.addItem(yoshi_item) # Agrega el elemento de Yoshi a la escena.
            yoshi_item.setPos(j * cell_width + x_pos, i * cell_height + y_pos) # Establece la posición del elemento de Yoshi en la posición calculada basada en la fila y columna en la cuadrícula.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaCuadricula = QtWidgets.QMainWindow()
    ui = Ui_ventanaCuadricula()
    ui.setupUi(ventanaCuadricula)
    ventanaCuadricula.show()
    sys.exit(app.exec_())
