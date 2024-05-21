import copy
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
    heuristica = (casillas_pintadas_yoshi - casillas_pintadas_oponente) + casillas_disponibles - mov_posibles_oponente
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

def obtener_mejor_movimiento(ambiente, profundidad):
    mejor_valor = float("-inf")
    mejor_movimiento = None
    for movimiento in ambiente.obtener_casillas_disponibles(ambiente.yoshi_verde):
        copia_ambiente = copy.deepcopy(ambiente)
        copia_ambiente.realizar_movimiento(copia_ambiente.yoshi_verde, *movimiento)
        valor = minimax(Nodo(copia_ambiente), profundidad, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
    return mejor_movimiento

ambiente = Ambiente()
ambiente.inicializar_ambiente()
ambiente.mostrar_ambiente()

# Bucle para jugar hasta que uno de los yoshis no tenga movimientos disponibles
while True:
    # Turno del yoshi verde
    print("Turno del Yoshi Verde:")
    mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, 3)
    if mejor_movimiento_verde:
        ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
        ambiente.mostrar_ambiente()
    else:
        print("El Yoshi Verde no tiene movimientos disponibles. ¡El Yoshi Rojo gana!")
        break

