import socket
import threading

clientes = [] # Lista para armazenar as conexões ativas

def tratar_cliente(conn):
    # Fica escutando as mensagens de um cliente específico
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: 
                break
            # Retransmite a mensagem para todos os OUTROS clientes conectados
            for c in clientes:
                if c != conn:
                    c.send(msg)
        except:
            break
    
    # Se der erro ou desconectar, remove da lista
    clientes.remove(conn)
    conn.close()

def iniciar_servidor(porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", porta))
    s.listen()
    print(f"Servidor aberto. Aguardando conexões na porta {porta}...")
    
    # O loop principal do servidor apenas aceita novas conexões
    while True:
        conn, addr = s.accept()
        clientes.append(conn)
        print(f"\n[+] Alguém conectou de {addr}")
        
        # Cria uma thread independente para ouvir este novo cliente
        threading.Thread(target=tratar_cliente, args=(conn,), daemon=True).start()

def iniciar_cliente(ip, porta, nome):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((ip, porta))
    
    # Função interna para o cliente ouvir mensagens do servidor em paralelo
    def receber():
        while True:
            try:
                print("\n" + c.recv(1024).decode() + "\nVocê: ", end="")
            except:
                break
                
    threading.Thread(target=receber, daemon=True).start()
    
    print("\nConectado! Pode começar a digitar.")
    while True:
        msg = input("Você: ")
        c.send(f"[{nome}]: {msg}".encode())

# --- Menu Principal ---
modo = input("Você quer hospedar a sala (S) ou entrar em uma (C)? ").strip().upper()

if modo == 'S':
    porta = int(input("Qual porta usar para o servidor? "))
    iniciar_servidor(porta)
else:
    nome = input("Qual o seu nome? ")
    ip = input("IP do servidor (ex: 127.0.0.1): ")
    porta = int(input("Porta do servidor: "))
    iniciar_cliente(ip, porta, nome)