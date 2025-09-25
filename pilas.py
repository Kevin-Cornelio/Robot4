class Pilas:
    def __init__(self, tipo="AAA", desechable=True):
        self.tipo = tipo
        self.desechable = desechable

    def conectado_a_control_remoto(self):
        print("Pilas conectadas al control remoto.")
