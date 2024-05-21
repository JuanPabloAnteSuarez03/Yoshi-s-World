import unittest
from busqueda import *
from arbol import *
class TestMinimax(unittest.TestCase):

    def setUp(self):
        # Crear el ambiente inicial para la prueba
        self.ambiente = Ambiente()
        # Fijar las posiciones iniciales de los Yoshis para obtener resultados consistentes
        self.ambiente.yoshi_verde = Yoshi('verde', 0, 0)
        self.ambiente.yoshi_rojo = Yoshi('rojo', 7, 7)
        self.ambiente.matriz[0][0] = '1'
        self.ambiente.matriz[7][7] = '2'
    
    def test_minimax_heuristica(self):
        nodo = Nodo(self.ambiente)
        generar_hijos(nodo, self.ambiente.yoshi_verde)
        self.ambiente.mostrar_ambiente()
        print("Heuristica: ", heuristica(self.ambiente, self.ambiente.yoshi_verde))
        resultado = minimax(nodo, 1, True)
        # Se espera que el valor heurístico sea consistente con el ambiente inicial
        heuristica_esperada = heuristica(self.ambiente, self.ambiente.yoshi_verde)
        self.assertEqual(resultado, heuristica_esperada)
    
    def test_minimax_profundidad_2(self):
        nodo = Nodo(self.ambiente)
        generar_hijos(nodo, self.ambiente.yoshi_verde)
        for hijo in nodo.hijos:
            generar_hijos(hijo, self.ambiente.yoshi_rojo)
        
        resultado = minimax(nodo, 2, True)
        # No hay un valor esperado fijo, pero no debería ser infinito
        self.assertNotEqual(resultado, float("-inf"))
        self.assertNotEqual(resultado, float("inf"))
    
    def test_minimax_profundidad_0(self):
        nodo = Nodo(self.ambiente)
        
        resultado = minimax(nodo, 0, True)
        # Debería devolver la heurística del nodo inicial
        heuristica_esperada = heuristica(self.ambiente, self.ambiente.yoshi_verde)
        self.assertEqual(resultado, heuristica_esperada)

if __name__ == '__main__':
    unittest.main()
