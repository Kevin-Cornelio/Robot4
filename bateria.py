class Bateria:
    def __init__(self, capacidad=100):
        self.capacidad = capacidad
        self.nivel_actual = capacidad

    def consultar_estado(self):
        return f"Batería al {self.nivel_actual}%"

    def _controlar_descarga(self, cantidad):
        self.nivel_actual = max(0, self.nivel_actual - cantidad)
        if self.nivel_actual == 0:
            print("Batería agotada, el robot debe recargarse.")
        elif self.nivel_actual < 20:
            print("Nivel de batería bajo.")

    def cargar(self):
        self.nivel_actual = self.capacidad
        print("Batería cargada al 100%.")
