from ambiente import *
from arbol import *
from yoshi import *
from jugador import *

def heuristica(ambiente, yoshi):
    # Contar la cantidad de casillas pintadas por el yoshi y su oponente
    casillas_pintadas_yoshi = ambiente.casillas_pintadas_verde
    casillas_pintadas_oponente = ambiente.casillas_pintadas_rojo
    
    # Calcular la cantidad de casillas disponibles para el yoshi
    casillas_disponibles = len(ambiente.obtener_casillas_disponibles(yoshi))
    
    oponente = ambiente.yoshi_rojo
    mov_posibles_oponente = len(ambiente.obtener_casillas_disponibles(oponente))
    
    # Calcular la heurística combinando los aspectos anteriores
    heuristica = (casillas_pintadas_yoshi - casillas_pintadas_oponente) + casillas_disponibles + mov_posibles_oponente
    
    return heuristica

def minimax(nodo, profundidad, es_max):
    if profundidad == 0 or not nodo.hijos:
        return heuristica(nodo.estado, nodo.estado.yoshi_verde if es_max else nodo.estado.yoshi_rojo)

    if es_max:
        mejor_valor = float("-inf")
        for hijo in nodo.hijos:
            valor = minimax(hijo, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for hijo in nodo.hijos:
            valor = minimax(hijo, profundidad - 1, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor
    
def generar_hijos(nodo, yoshi):
    ambiente = nodo.estado
    casillas_disponibles = ambiente.obtener_casillas_disponibles(yoshi)
    for fila_destino, columna_destino in casillas_disponibles:
        ambiente_temporal = ambiente.copy()
        ambiente_temporal.realizar_movimiento(yoshi, fila_destino, columna_destino)
        nodo_hijo = Nodo(ambiente_temporal)
        nodo.hijos.append(nodo_hijo)

def obtener_mejor_movimiento(ambiente, profundidad):
    yoshi = ambiente.yoshi_verde
    mejor_movimiento = None
    mejor_heuristica = float("-inf")
    casillas_disponibles = ambiente.obtener_casillas_disponibles(yoshi)
    print("Casillas disponibles:", casillas_disponibles)
    
    for fila_destino, columna_destino in casillas_disponibles:
        ambiente_temporal = ambiente.copy()
        ambiente_temporal.realizar_movimiento(yoshi, fila_destino, columna_destino)
        nodo = Nodo(ambiente_temporal)
        generar_hijos(nodo, ambiente_temporal.yoshi_rojo)
        heuristica_actual = minimax(nodo, profundidad, False)
        print(ambiente_temporal.yoshi_verde.fila, ambiente_temporal.yoshi_verde.columna)
        print(heuristica_actual)
        if heuristica_actual > mejor_heuristica:
            mejor_heuristica = heuristica_actual
            mejor_movimiento = (fila_destino, columna_destino)
    
    return mejor_movimiento

# Uso:
ambiente = Ambiente()
ambiente.inicializar_ambiente()
profundidad = 3  # Profundidad de búsqueda del algoritmo minimax
mejor_movimiento = obtener_mejor_movimiento(ambiente, profundidad)
ambiente.mostrar_ambiente()
print("Posicion Yoshi:", (ambiente.yoshi_verde.fila, ambiente.yoshi_verde.columna))
print("Mejor movimiento:", mejor_movimiento)
print(mejor_movimiento[0])
print(mejor_movimiento[1])
ambiente.realizar_movimiento(ambiente.yoshi_verde, mejor_movimiento[0], mejor_movimiento[1])
ambiente.mostrar_ambiente()
print()
# while mejor_movimiento is not None:
#     yoshi_actual = ambiente.yoshi_verde  # Suponiendo que la máquina es el jugador verde
#     profundidad = 3  # Profundidad de búsqueda del algoritmo minimax
#     mejor_movimiento = obtener_mejor_movimiento(ambiente, profundidad)
#     print("Mejor movimiento:", mejor_movimiento)
#     ambiente.realizar_movimiento(yoshi_actual, *mejor_movimiento)
#     ambiente.mostrar_ambiente()
#     print()