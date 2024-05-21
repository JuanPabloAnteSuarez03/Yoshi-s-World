import unittest
from busqueda import *
from arbol import *
class TestObtenerMejorMovimiento(unittest.TestCase):

    def test_obtener_mejor_movimiento(self):
        # Crear un ambiente fijo para el test
        ambiente = Ambiente()
        ambiente.matriz = [
            ['1', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2']
        ]
        ambiente.yoshi_verde = Yoshi('verde', 0, 0)
        ambiente.yoshi_rojo = Yoshi('rojo', 7, 7)

        # Calcular el mejor movimiento
        mejor_movimiento = obtener_mejor_movimiento(ambiente, profundidad=3)

        # Verificar que el mejor movimiento es el esperado
        self.assertEqual(mejor_movimiento, (0, 1))

if __name__ == '__main__':
    unittest.main()
