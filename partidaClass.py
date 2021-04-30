from cartaClass import *
from menuClass import *
from socketClass import *
def seleccionNumeroUsuario():
    while True:
        try:
            clear()
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

def buscarCarta(numCarta):
    listaCartas = [cartaUno, cartaDos, cartaTres, cartaCuatro, cartaCinco, cartaSeis, cartaSiete]
    for carta in listaCartas:
        if carta.getNumCarta() == numCarta:
            return carta

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
def mostrarCartas(ip):
    for i in range(1,8):
        carta = buscarCarta(i)
        carta.imprimirCarta()
        resultado = pregunta()
        enviar(ip, resultado)
        clear()
    return recibirNumeroMagico(ip)
    
def iniciarPartida():
    resultado = ''
    clear()
    ipservidor = input("Ingresa la ip del servidor\n-->")
    if isConected(ipservidor):
        mensajeServidorEncontrado()
        mensajeNumeroUsuario()
        numeroRecibido = mostrarCartas(ipservidor)
        mostrarCartaUsuario(numeroRecibido)
        return ipservidor    
    elif not isConected(ipservidor):
        mensajeServidorNoEncontrado()
        return 

