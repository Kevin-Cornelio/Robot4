from bateria import Bateria
from sensor import Sensor
from robot_limpieza import RobotLimpieza

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = Bateria()
        self.sensor = Sensor()
        self.modulo_limpieza = RobotLimpieza()
        self.encendido = False

    def encender(self):
        if self.bateria.nivel_actual > 0:
            self.encendido = True
            print(f" {self.nombre} encendido.")
        else:
            print(" No se puede encender. La batería está agotada.")

    def apagar(self):
        self.encendido = False
        print(f" {self.nombre} apagado.")

    def iniciar_limpieza(self):
        if self.encendido:
            self.modulo_limpieza.iniciar_limpieza()
            # Cada limpieza consume un 10% de batería
            self.bateria._controlar_descarga(10)
        else:
            print(" Primero enciende el robot.")

    def detener_limpieza(self):
        self.modulo_limpieza.detener_limpieza()

    def consultar_estado(self):
        # Muestra estado de batería y sensores
        print(self.bateria.consultar_estado())
        print(self.sensor.consultar_estado())

    def _calcular_ruta_limpieza(self):
        print(" Calculando la ruta de limpieza")

    def _procesar_datos_sensor(self):
        print(" Procesando los datos del sensor")
        print(self.sensor.consultar_estado())

    def _gestionar_bateria(self):
        print(" Gestionando la batería")
