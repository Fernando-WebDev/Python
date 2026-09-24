
import socket
import threading
import time

def servidor(minha_porta):
    # Cria o servidor TCP para receber mensagens
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", minha_porta))
    s.listen(1)
    
    conn, _ = s.accept() # Fica travado aqui até o amigo conectar
    
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"\n[Amigo]: {msg}\nVocê: ", end="")

def cliente(ip_amigo, porta_amigo):
    # Cria o cliente TCP para enviar mensagens
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Fica tentando conectar até o servidor do amigo estar online
    while c.connect_ex((ip_amigo, porta_amigo)) != 0:
        time.sleep(0.5)
        
    print("\nConectado! Pode começar a digitar.")
    while True:
        c.send(input("Você: ").encode())

# 1. Configuração
minha_porta = int(input("Sua porta: "))
ip_amigo = input("IP do amigo (ex: 127.0.0.1): ")
porta_amigo = int(input("Porta do amigo: "))

# 2. Inicia o servidor em uma thread paralela
threading.Thread(target=servidor, args=(minha_porta,), daemon=True).start()

# 3. Inicia o cliente na thread principal
cliente(ip_amigo, porta_amigo)