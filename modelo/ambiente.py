import random
from yoshi import *
class Ambiente:
    def __init__(self):
        self.matriz = [[0] * 8 for _ in range(8)]
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
        self.matriz[fila_verde][columna_verde] = 'V'
        self.matriz[fila_rojo][columna_rojo] = 'R'
    
    def obtener_casillas_disponibles(self, yoshi):
        fila_actual, columna_actual = yoshi.fila, yoshi.columna
        movimientos = [(fila_actual + 1, columna_actual + 2), (fila_actual + 1, columna_actual - 2),
                       (fila_actual - 1, columna_actual + 2), (fila_actual - 1, columna_actual - 2),
                       (fila_actual + 2, columna_actual + 1), (fila_actual + 2, columna_actual - 1),
                       (fila_actual - 2, columna_actual + 1), (fila_actual - 2, columna_actual - 1)]
        casillas_disponibles = []
        for fila, columna in movimientos:
            if 0 <= fila < 8 and 0 <= columna < 8 and self.matriz[fila][columna] == 0:
                casillas_disponibles.append((fila, columna))
        return casillas_disponibles
    
    def realizar_movimiento(self, yoshi, fila_destino, columna_destino):
        fila_actual, columna_actual = yoshi.fila, yoshi.columna
        if (fila_destino, columna_destino) in self.obtener_casillas_disponibles(yoshi):
            self.matriz[fila_actual][columna_actual] = yoshi.color[0].upper()
            self.matriz[fila_destino][columna_destino] = yoshi.color[0].upper()
            yoshi.fila, yoshi.columna = fila_destino, columna_destino
            self.actualizar_casillas_pintadas(yoshi)
            return True
        else:
            return False
    
    def actualizar_casillas_pintadas(self, yoshi):
        if yoshi.color == 'verde':
            self.casillas_pintadas_verde += 1
        elif yoshi.color == 'rojo':
            self.casillas_pintadas_rojo += 1
    
    def mostrar_ambiente(self):
        for fila in self.matriz:
            print(' '.join(map(str, fila)))

# Ejemplo de uso:
ambiente = Ambiente()
ambiente.inicializar_ambiente()
ambiente.mostrar_ambiente()
print()
ambiente.realizar_movimiento(ambiente.yoshi_verde, 2, 3)
ambiente.mostrar_ambiente()