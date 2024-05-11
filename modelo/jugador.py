class Jugador:
    def __init__(self, color, es_maquina=False):
        self.color = color
        self.movimientos_realizados = 0
        self.es_maquina = es_maquina
    
    def __str__(self):
        return f"{'Máquina' if self.es_maquina else 'Jugador'} {self.color.capitalize()}"
    
    def realizar_movimiento(self):
        if self.es_maquina:
            # Aquí puedes implementar la lógica para que la máquina realice un movimiento automáticamente
            pass
        else:
            # Aquí puedes solicitar la entrada del usuario para que el jugador humano realice un movimiento
            pass
