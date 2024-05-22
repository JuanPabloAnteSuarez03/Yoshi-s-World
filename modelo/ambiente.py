import random
from yoshi import *
class Ambiente:
    def __init__(self):
        self.matriz = [['0'] * 8 for _ in range(8)]
        self.yoshi_verde = None
        self.yoshi_rojo = None
        self.casillas_pintadas_verde = 0
        self.casillas_pintadas_rojo = 0

    def inicializar_ambiente(self):
        # Inicializar las posiciones aleatorias de los Yoshis
        fila_verde, columna_verde = random.randint(0, 7), random.randint(0, 7)
        fila_rojo, columna_rojo = random.randint(0, 7), random.randint(0, 7)
        while fila_verde == fila_rojo and columna_verde == columna_rojo:
            fila_rojo, columna_rojo = random.randint(0, 7), random.randint(0, 7)
        
        self.yoshi_verde = Yoshi('verde', fila_verde, columna_verde)
        self.yoshi_rojo = Yoshi('rojo', fila_rojo, columna_rojo)
        # Marcar las posiciones iniciales de los Yoshis en el tablero
        self.matriz[fila_verde][columna_verde] = 1
        self.matriz[fila_rojo][columna_rojo] = 2
    
    def realizar_movimiento(self, yoshi, fila_destino, columna_destino):
        fila_actual, columna_actual = yoshi.fila, yoshi.columna
        # Marcar la posición anterior como pintada
        if yoshi.color == 'verde':
            self.matriz[fila_actual][columna_actual] = 3
        elif yoshi.color == 'rojo':
            self.matriz[fila_actual][columna_actual] = 4
        # Actualizar la posición del Yoshi
        yoshi.fila, yoshi.columna = fila_destino, columna_destino
        # Actualizar la matriz y las casillas pintadas
        self.actualizar_casillas_pintadas(yoshi)
    
    def actualizar_casillas_pintadas(self, yoshi):
        fila, columna = yoshi.fila, yoshi.columna
        if yoshi.color == 'verde':
            self.casillas_pintadas_verde += 1
            self.matriz[fila][columna] = 1
        elif yoshi.color == 'rojo':
            self.casillas_pintadas_rojo += 1
            self.matriz[fila][columna] = 2

    def obtener_casillas_disponibles(self, yoshi):
        fila_actual, columna_actual = yoshi.fila, yoshi.columna
        movimientos = [(fila_actual + 1, columna_actual + 2), (fila_actual + 1, columna_actual - 2),
                       (fila_actual - 1, columna_actual + 2), (fila_actual - 1, columna_actual - 2),
                       (fila_actual + 2, columna_actual + 1), (fila_actual + 2, columna_actual - 1),
                       (fila_actual - 2, columna_actual + 1), (fila_actual - 2, columna_actual - 1)]
        casillas_disponibles = []
        for fila, columna in movimientos:
            if 0 <= fila < 8 and 0 <= columna < 8 and self.matriz[fila][columna] == '0':
                casillas_disponibles.append((fila, columna))
        return casillas_disponibles

    def mostrar_ambiente(self):
        for fila in self.matriz:
            print(' '.join(map(str, fila)))

    def copy(self):
        copia = Ambiente()
        copia.matriz = [fila[:] for fila in self.matriz]
        copia.yoshi_verde = Yoshi(self.yoshi_verde.color, self.yoshi_verde.fila, self.yoshi_verde.columna) if self.yoshi_verde else None
        copia.yoshi_rojo = Yoshi(self.yoshi_rojo.color, self.yoshi_rojo.fila, self.yoshi_rojo.columna) if self.yoshi_rojo else None
        copia.casillas_pintadas_verde = self.casillas_pintadas_verde
        copia.casillas_pintadas_rojo = self.casillas_pintadas_rojo
        return copia

# Ejemplo de uso:
# ambiente = Ambiente()
# ambiente.inicializar_ambiente()
# ambiente.mostrar_ambiente()
# print()
# print(ambiente.yoshi_verde.fila, ambiente.yoshi_verde.columna)
# print(ambiente.obtener_casillas_disponibles(ambiente.yoshi_verde))
# ambiente.realizar_movimiento(ambiente.yoshi_verde, 2, 3)
# ambiente.realizar_movimiento(ambiente.yoshi_verde, 5, 4)
# ambiente.realizar_movimiento(ambiente.yoshi_verde, 3, 2)
# ambiente.realizar_movimiento(ambiente.yoshi_verde, 1, 6)
# ambiente.realizar_movimiento(ambiente.yoshi_rojo, 4, 5)
# ambiente.realizar_movimiento(ambiente.yoshi_rojo, 6, 1)
# ambiente.realizar_movimiento(ambiente.yoshi_rojo, 7, 3)
# ambiente.realizar_movimiento(ambiente.yoshi_rojo, 5, 7)
# ambiente.mostrar_ambiente()
# print(ambiente.casillas_pintadas_verde, ambiente.casillas_pintadas_rojo)