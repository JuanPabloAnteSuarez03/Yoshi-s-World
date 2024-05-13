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

def minimax(nodo, profundidad, es_max, ambiente):
    if profundidad == 0:
        return heuristica(ambiente, nodo.estado)

    if es_max:
        mejor_valor = float("-inf")
        for hijo in nodo.hijos:
            valor = minimax(hijo, profundidad - 1, False, ambiente)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for hijo in nodo.hijos:
            valor = minimax(hijo, profundidad - 1, True, ambiente)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def obtener_mejor_movimiento(ambiente, profundidad):
    yoshi = ambiente.yoshi_verde
    mejor_movimiento = None
    mejor_valor = float("-inf")
    casillas_disponibles = ambiente.obtener_casillas_disponibles(yoshi)
    print(casillas_disponibles)
    
    for fila_destino, columna_destino in casillas_disponibles:
        ambiente_temporal = ambiente.copy()
        ambiente_temporal.realizar_movimiento(yoshi, fila_destino, columna_destino)
        nodo = Nodo(ambiente_temporal)
        valor = minimax(nodo, profundidad, False, ambiente_temporal)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = (fila_destino, columna_destino)
    
    return mejor_movimiento

# Uso:
ambiente = Ambiente()
ambiente.inicializar_ambiente()
profundidad = 3  # Profundidad de búsqueda del algoritmo minimax
mejor_movimiento = obtener_mejor_movimiento(ambiente, profundidad)
ambiente.mostrar_ambiente()
print("Mejor movimiento:", mejor_movimiento)
while mejor_movimiento is not None:
    yoshi_actual = ambiente.yoshi_verde  # Suponiendo que la máquina es el jugador verde
    profundidad = 3  # Profundidad de búsqueda del algoritmo minimax
    mejor_movimiento = obtener_mejor_movimiento(ambiente, profundidad)
    print("Mejor movimiento:", mejor_movimiento)
    ambiente.realizar_movimiento(yoshi_actual, *mejor_movimiento)
    ambiente.mostrar_ambiente()
    print()