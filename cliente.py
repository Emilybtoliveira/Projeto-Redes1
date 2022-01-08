import socket
from threading import Thread

def receiveMessages():
    while True:
        msg_servidor = tcp.recv(1024)
        if not msg_servidor: break
        print("Servidor disse: ", msg_servidor.decode("utf-8"))
    tcp.close()

def sendMessage():
    print ('Para sair pressione Enter')

    msg = ''

    while (msg != b''):        
        msg = bytes(input(), 'iso_8859_1')
        tcp.sendall(msg) 
    
    print("Fechando conexão...")
    tcp.close()
    return


HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

Thread(target=receiveMessages, args=()).start() 

sendMessage()