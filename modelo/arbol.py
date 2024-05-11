class Nodo:
    def __init__(self, estado, padre=None, operador=None, profundidad=0, costo=0):
        self.estado = estado            # Estado del problema en este nodo
        self.padre = padre              # Referencia al nodo padre
        self.operador = operador        # Operador aplicado para generar este nodo
        self.profundidad = profundidad  # Profundidad del nodo en el árbol
        self.costo = costo              # Costo de la ruta desde la raíz hasta este nodo
        self.hijos = []                 # Lista de nodos hijos

    def __lt__(self, otro):
        # Comparar los nodos en función de su costo acumulado
        return self.costo < otro.costo

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)