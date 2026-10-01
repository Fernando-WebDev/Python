import socket
import threading
import sys

def handle_incoming_client(client_socket, address):
    print(f"\n[+] Novo cliente conectado a você vindo de {address}")
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

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        # IMPORTANTE: '0.0.0.0' escuta em todas as placas de rede da máquina (aceita conexões externas)
        server.bind(('0.0.0.0', port))
        server.listen(5)
    except Exception as e:
        print(f"[Erro no Servidor] Não foi possível iniciar na porta {port}: {e}")
        return

    while True:
        try:
            client_socket, address = server.accept()
            thread = threading.Thread(target=handle_incoming_client, args=(client_socket, address))
            thread.daemon = True
            thread.start()
        except:
            break

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
    
    try:
        my_port = int(input("Informe a porta onde este nó deve escutar (ex: 5000): "))
    except ValueError:
        print("Porta inválida.")
        return

    # Inicia o servidor local em background
    server_thread = threading.Thread(target=start_server, args=(my_port,))
    server_thread.daemon = True
    server_thread.start()
    print(f"[*] Servidor rodando na porta {my_port} (aceitando conexões locais e da rede).")

    active_connections = {}
    conn_counter = 1

    while True:
        print("\n--- MENU ---")
        print("1. Conectar a um novo servidor (outra máquina ou local)")
        print("2. Enviar mensagem para um servidor conectado")
        print("3. Listar conexões ativas")
        print("4. Sair / Encerrar programa")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            target_ip = input("Informe o IP do servidor de destino (ex: 192.168.1.50 ou 127.0.0.1): ").strip()
            try:
                target_port = int(input("Informe a porta do servidor de destino: "))
                
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_sock.connect((target_ip, target_port))
                
                conn_id = conn_counter
                active_connections[conn_id] = client_sock
                conn_counter += 1

                t = threading.Thread(target=listen_to_remote_server, args=(client_sock, (target_ip, target_port)))
                t.daemon = True
                t.start()

                print(f"[+] Conectado com sucesso a {target_ip}:{target_port}! (ID da Conexão: {conn_id})")
            except Exception as e:
                print(f"[-] Erro ao conectar (Connection Refused provável): {e}")

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