class Yoshi:
    def __init__(self, color, fila, columna):
        self.color = color
        self.fila = fila
        self.columna = columna

    def obtener_casillas_disponibles(self, matriz_ambiente):
        fila_actual, columna_actual = self.fila, self.columna
        movimientos = [(fila_actual + 1, columna_actual + 2), (fila_actual + 1, columna_actual - 2),
                       (fila_actual - 1, columna_actual + 2), (fila_actual - 1, columna_actual - 2),
                       (fila_actual + 2, columna_actual + 1), (fila_actual + 2, columna_actual - 1),
                       (fila_actual - 2, columna_actual + 1), (fila_actual - 2, columna_actual - 1)]
        casillas_disponibles = []
        for fila, columna in movimientos:
            if 0 <= fila < 8 and 0 <= columna < 8 and matriz_ambiente[fila][columna] == 0:
                casillas_disponibles.append((fila, columna))
        return casillas_disponibles

