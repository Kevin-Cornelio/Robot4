from pilas import Pilas

class ControlRemoto:
    def __init__(self, robot, pilas=None):
        self.robot = robot
        self.controlador = "default"
        self.pilas = pilas or Pilas()
        print(f"📱 Control remoto conectado al robot {robot.nombre}")

    def conectado_a_robot(self):
        print(f"✅ Control remoto conectado al robot {self.robot.nombre}")

    def enviar_comando(self, comando):
        print(f"📡 Enviando comando '{comando}' al robot {self.robot.nombre}")
