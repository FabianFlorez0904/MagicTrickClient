import socket
import sys
from menuClass import tiempo, clear

def isConected(ipservidor):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"isconected"
        # Send data
        #print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)
        # Receive response
        #print('waiting to receive')
        data, server = sock.recvfrom(4096)
        if data == b"conected":
            #print('received {!r}'.format(data))
            return True
        else:
            return False
    except NameError:
        return False
    #except Exception as e:
    #        print(type(e).__name__)
    #
    #         return False    
    finally:
        #print('closing socket')
        sock.close()
def enviar(ipservidor, dato):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        if dato == '1':
            message = b"dato1"
            # Send data
            #print('sending {!r}'.format(message))
            sent = sock.sendto(message, server_address)
            # Receive response
            #print('waiting to receive')
            data, server = sock.recvfrom(4096)
            if data == b"saved":
                #print('received {!r}'.format(data))
                return
            else:
                enviar(ipservidor, dato)
                return
        if dato == '0':
            message = b"dato0"
            # Send data
            #print('sending {!r}'.format(message))
            sent = sock.sendto(message, server_address)
            # Receive response
            #print('waiting to receive')
            data, server = sock.recvfrom(4096)
            if data == b"saved":
                #print('received {!r}'.format(data))
                return
            else:
                enviar(ipservidor, dato)
                return
                
    except NameError:
        return False
    except Exception as e:
            print(type(e).__name__)
    #         return False    
    finally:
        #print('closing socket')
        sock.close()

def recibirNumeroMagico(ipservidor):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"pleaseSendTheNumber"
        # Send data
        #print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)
        # Receive response
        #print('waiting to receive')
        data, server = sock.recvfrom(4096)
        return data.decode()
    except NameError:
        return False
    except Exception as e:
            print(type(e).__name__)
    
    #         return False    
    finally:
        #print('closing socket')
        sock.close()
    

def cerrarConexion():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ipservidor, 5000 )
    try:
        message = b"close"
        # Send data
        #print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)
        # Receive response
        #print('waiting to receive'
    except NameError:
        return False
    except Exception as e:
            print(type(e).__name__)
    
    #         return False    
    finally:
        #print('closing socket')
        sock.close()
# try:
    
#     # Send data
#     print('sending {!r}'.format(message))
#     sent = sock.sendto(message, server_address)

#     # Receive response
#     print('waiting to receive')
#     data, server = sock.recvfrom(4096)
#     print('received {!r}'.format(data))
# finally:
#     print('closing socket')
#     sock.close()