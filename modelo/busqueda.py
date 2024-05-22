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
    return (casillas_pintadas_yoshi - casillas_pintadas_oponente) + (casillas_disponibles - mov_posibles_oponente)

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
        nodo = Nodo(copia_ambiente)
        generar_hijos(nodo, copia_ambiente.yoshi_rojo)  # Asegurarse de generar los hijos aquí
        valor = minimax(nodo, profundidad, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
    return mejor_movimiento

def generar_hijos(nodo, yoshi):
    ambiente = nodo.estado
    casillas_disponibles = ambiente.obtener_casillas_disponibles(yoshi)
    for fila_destino, columna_destino in casillas_disponibles:
        ambiente_temporal = copy.deepcopy(ambiente)  # Asegurarse de hacer una copia profunda aquí también
        ambiente_temporal.realizar_movimiento(yoshi, fila_destino, columna_destino)
        nodo_hijo = Nodo(ambiente_temporal)
        nodo.hijos.append(nodo_hijo)

# Inicializar el ambiente
ambiente = Ambiente()
ambiente.inicializar_ambiente()
ambiente.mostrar_ambiente()

# Bucle para jugar hasta que uno de los yoshis no tenga movimientos disponibles
while True:
    # Turno del yoshi verde (bot)
    print("Turno del Yoshi Verde:")
    mejor_movimiento_verde = obtener_mejor_movimiento(ambiente, 9)
    print("Lista de movimientos disponibles para el Yoshi Verde: ", ambiente.obtener_casillas_disponibles(ambiente.yoshi_verde))
    print("Mejor movimiento del Yoshi Verde: ", mejor_movimiento_verde)
    if mejor_movimiento_verde:
        ambiente.realizar_movimiento(ambiente.yoshi_verde, *mejor_movimiento_verde)
        ambiente.mostrar_ambiente()
    else:
        print("El Yoshi Verde no tiene movimientos disponibles. ¡El Yoshi Rojo gana!")
        break

    # Turno del usuario (Yoshi Rojo)
    print("Turno del Yoshi Rojo (Usuario):")
    movimientos_disponibles_rojo = ambiente.obtener_casillas_disponibles(ambiente.yoshi_rojo)
    print("Lista de movimientos disponibles para el Yoshi Rojo: ", movimientos_disponibles_rojo)
    if not movimientos_disponibles_rojo:
        print("El Yoshi Rojo no tiene movimientos disponibles. ¡El Yoshi Verde gana!")
        break

    # Solicitar movimiento del usuario
    fila_destino = int(input("Ingrese la fila del movimiento: "))
    columna_destino = int(input("Ingrese la columna del movimiento: "))
    if (fila_destino, columna_destino) in movimientos_disponibles_rojo:
        ambiente.realizar_movimiento(ambiente.yoshi_rojo, fila_destino, columna_destino)
        ambiente.mostrar_ambiente()
    else:
        print("Movimiento inválido. Intente nuevamente.")
