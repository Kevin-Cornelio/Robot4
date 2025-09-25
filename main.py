from robotcito import Robot
from control_remoto import ControlRemoto

mi_robot = Robot("Robotito")

control = ControlRemoto(mi_robot)

mi_robot.encender()

mi_robot.iniciar_limpieza()

mi_robot.consultar_estado()

mi_robot.detener_limpieza()

mi_robot.apagar()

mi_robot.bateria.cargar()
mi_robot.encender()
mi_robot.iniciar_limpieza()

from robotcito import Robot
from control_remoto import ControlRemoto

mi_robot = Robot("Robotito")
control = ControlRemoto(mi_robot)

def menu():
    print("\n--- MENÚ DEL ROBOT ---")
    print("1. Prender robot")
    print("2. Apagar robot")
    print("3. Empezar limpieza")
    print("4. Detener limpieza")
    print("5. Chequear estado")
    print("6. Elegir modo de limpieza")
    print("7. Cargar batería")
    print("8. Usar control remoto para enviar comando")
    print("9. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_robot.encender()
    elif opcion == "2":
        mi_robot.apagar()
    elif opcion == "3":
        mi_robot.iniciar_limpieza()
    elif opcion == "4":
        mi_robot.detener_limpieza()
    elif opcion == "5":
        mi_robot.consultar_estado()
    elif opcion == "6":
        modo = input("Elegí el modo (Normal, Turbo, Silencioso): ")
        mi_robot.modulo_limpieza.seleccionar_modo(modo)
    elif opcion == "7":
        mi_robot.bateria.cargar()
    elif opcion == "8":
        comando = input("Escribe el comando para el robot: ")
        control.enviar_comando(comando)
    elif opcion == "9":
        print("Cerrando del programa")
        break
    else:
        print("Opción inválida, intentalo de nuevo.")
