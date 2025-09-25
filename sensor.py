import random

class Sensor:
    def __init__(self, proximidad=0, temporizador=0):
        self.proximidad = proximidad
        self.temporizador = temporizador

    def consultar_estado(self):
        self.proximidad = random.randint(0, 100)
        self.temporizador += 1
        return f"Proximidad: {self.proximidad}, Tiempo activo: {self.temporizador}s"

    def _calibrar(self):
        self.proximidad = 0
        self.temporizador = 0
        print("Sensor calibrado.")
