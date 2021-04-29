#
#   Cliente
#
from menuClass import *

from partidaClass import *

def main():
    bienvenida()
    while True:
        try:
            
            ##clear()
            imprimirMenu()
            opcion = int(input("Opcion aqui -->"))
            if opcion == 1:
                iniciarPartida()
                continue
            elif opcion == 2:
                creditos()
                continue
            elif opcion == 3:
                terminar()
                break
            else:
                opcionNoEncontrada()
        except ValueError:
            opcionNoEncontrada()
        except Exception as e:
             print(type(e).__name__)
#   Llamado del main
main()
