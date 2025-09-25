class RobotLimpieza:
    def __init__(self):
        self.limpiando = False
        self.modo_limpieza = "Normal"
        self.temporizador = 0

    def iniciar_limpieza(self):
        self.limpiando = True
        print("Empezando la limpieza")

    def detener_limpieza(self):
        self.limpiando = False
        print("Limpieza detenida.")

    def seleccionar_modo(self, modo):
        self.modo_limpieza = modo
        print(f"Modo de limpieza seleccionado: {modo}")

    def _autodiagnostico(self):
        print(" Haciendo autodiagnóstico del módulo de limpieza")
