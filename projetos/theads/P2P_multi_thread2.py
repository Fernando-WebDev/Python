import socket
import threading
import sys

# Função executada em uma thread separada para lidar com um cliente conectado ao nosso servidor local
def handle_incoming_client(client_socket, address):
    print(f"\n[+] Novo cliente conectado a você vindo de {address}")
    print("Digite algo a qualquer momento ou pressione Enter para voltar ao menu...")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            mensagem = data.decode('utf-8')
            print(f"\n[Mensagem Recebida de {address}]: {mensagem}")
    except ConnectionResetError:
        pass
    finally:
        client_socket.close()
        print(f"\n[-] Conexão com {address} foi encerrada.")

# Função que inicia o socket do servidor em background (escutando conexões)
def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(('127.0.0.1', port))
        server.listen(5)
    except Exception as e:
        print(f"[Erro no Servidor] Não foi possível iniciar na porta {port}: {e}")
        return

    while True:
        try:
            client_socket, address = server.accept()
            # Cada cliente que chega ganha uma thread dedicada
            thread = threading.Thread(target=handle_incoming_client, args=(client_socket, address))
            thread.daemon = True
            thread.start()
        except:
            break

# Função executada em thread para escutar respostas de um servidor ao qual nos conectamos
def listen_to_remote_server(sock, remote_address):
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print(f"\n[-] O servidor {remote_address} encerrou a conexão.")
                break
            print(f"\n[Resposta de {remote_address}]: {data.decode('utf-8')}")
    except:
        pass

def main():
    print("=== NÓ DE REDE MULTI-THREADING (Servidor & Cliente) ===")
    
    # Configura a porta onde ESTA instância vai escutar conexões
    try:
        my_port = int(input("Informe a porta onde este nó deve escutar (ex: 5000): "))
    except ValueError:
        print("Porta inválida.")
        return

    # Inicia o servidor local em uma thread em background
    server_thread = threading.Thread(target=start_server, args=(my_port,))
    server_thread.daemon = True
    server_thread.start()
    print(f"[*] Servidor interno rodando na porta {my_port}. Pronto para aceitar conexões!")

    # Dicionário para armazenar as conexões ativas de cliente: {id_conexao: socket}
    active_connections = {}
    conn_counter = 1

    while True:
        print("\n--- MENU ---")
        print("1. Conectar a um novo servidor")
        print("2. Enviar mensagem para um servidor conectado")
        print("3. Listar conexões ativas")
        print("4. Sair / Encerrar programa")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                target_port = int(input("Informe a porta do servidor de destino (localhost): "))
                
                # Cria um socket de cliente e conecta
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_sock.connect(('127.0.0.1', target_port))
                
                # Guarda no dicionário de conexões ativas
                conn_id = conn_counter
                active_connections[conn_id] = client_sock
                conn_counter += 1

                # Dispara uma thread para escutar as respostas desse servidor específico
                t = threading.Thread(target=listen_to_remote_server, args=(client_sock, ('127.0.0.1', target_port)))
                t.daemon = True
                t.start()

                print(f"[+] Conectado com sucesso ao servidor na porta {target_port}! (ID da Conexão: {conn_id})")
            except Exception as e:
                print(f"[-] Erro ao conectar: {e}")

        elif opcao == "2":
            if not active_connections:
                print("[-] Você não está conectado a nenhum servidor no momento.")
                continue

            print("\nConexões ativas:")
            for cid in active_connections:
                print(f" - ID: {cid}")

            try:
                cid_escolhido = int(input("Digite o ID da conexão para a qual deseja enviar mensagem: "))
                if cid_escolhido in active_connections:
                    mensagem = input("Digite a mensagem: ")
                    active_connections[cid_escolhido].sendall(mensagem.encode('utf-8'))
                    print("[✓] Mensagem enviada!")
                else:
                    print("[-] ID de conexão inválido.")
            except ValueError:
                print("[-] Entrada inválida.")

        elif opcao == "3":
            if not active_connections:
                print("[-] Nenhuma conexão ativa no momento.")
            else:
                print("\nServidores conectados por você:")
                for cid, sock in active_connections.items():
                    print(f" - ID {cid} (Destino: {sock.getpeername()})")

        elif opcao == "4":
            print("[*] Encerrando todas as conexões e saindo...")
            for sock in active_connections.values():
                sock.close()
            break
        else:
            print("[-] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()