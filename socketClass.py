import socket
import sys
from menuClass import tiempo, clear

def isConected(ipservidor):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"isconected"
        sent = sock.sendto(message, server_address)
        data, server = sock.recvfrom(4096)
        if data == b"conected":
            return True
        else:
            return False
    except NameError:
        print('NameError')
        return False
    except Exception as e:
        print(type(e).__name__)
        return False    
    finally:
        sock.close()
def enviar(ipservidor, dato):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        if dato == '1' or dato == '0':
            if dato == '1':
                message = b"dato1"
            else:
                message = b"dato0"
            sent = sock.sendto(message, server_address)
            data, server = sock.recvfrom(4096)
            if data == b"saved":
                return
            else:
                enviar(ipservidor, dato)
                return
    except NameError:
        print('NameError')
    except Exception as e:
            print(type(e).__name__)
    finally:
        sock.close()

def recibirNumeroMagico(ipservidor):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"pleaseSendTheNumber"
        sent = sock.sendto(message, server_address)
        data, server = sock.recvfrom(4096)
        return data.decode()
    except NameError:
        print('NameError')
    except Exception as e:
            print(type(e).__name__)
    finally:
        sock.close()
    

def cerrarConexion(ipservidor='localhost'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"close"
        sent = sock.sendto(message, server_address)
    except NameError:
        print('NameError')
    except Exception as e:
            print(type(e).__name__)    
    finally:
        sock.close()
