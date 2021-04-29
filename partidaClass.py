from cartaClass import *
from menuClass import *
from socketClass import *
def seleccionNumeroUsuario():
    while True:
        try:
            ##clear()
            numero = input("Escoje una carta entre el 0 al 100 y escribela\n-->")
            numero = int(numero)
            if numero >= 0 and numero <= 100:
                #print(type(numero))
                return numero 
            else:
                mensajeCartaFueraRango()
                continue
        except Exception as e:
            print(type(e).__name__)

def pregunta():
    while True:
        print(
            "-------------------------------------------------\n",
            "{: ^50}\n".format("¿Tu carta esta en esta carta?")
        )
        respuesta = input("{: >25}".format("[y/n]-->"))
        if respuesta == 'y' or respuesta == 'Y':
            return '1'
        elif respuesta == 'n' or respuesta == 'N':
            return '0'
        else:
            continue


def iniciarPartida():
    resultado = ''
    ##clear()
    ipservidor = input("Ingresa la ip del servidor\n-->")
    print(isConected(ipservidor))
    if isConected(ipservidor):
        mensajeServidorEncontrado()
        numeroUsuario = seleccionNumeroUsuario()
        ##clear()
        mensajeNumeroUsuario(numeroUsuario)
        cartaUno.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaDos.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaTres.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaCuatro.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaCinco.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaSeis.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        cartaSiete.imprimirCarta()
        resultado = pregunta()
        enviar(ipservidor, resultado)
        numeroRecibido = recibirNumeroMagico(ipservidor)
        print('Tu carta es: ', numeroRecibido)
    elif not isConected(ipservidor):
        ###clear()
        mensajeServidorNoEncontrado()
        tiempo(3)
        return

