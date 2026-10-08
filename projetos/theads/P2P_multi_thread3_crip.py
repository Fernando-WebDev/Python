import socket
import threading
import os

def gerar_tabela_cifra(caminho_chave):
    """Lê o arquivo de chaves e gera a tabela de tradução para criptografia/decriptografia."""
    if not os.path.exists(caminho_chave):
        # Caso o arquivo de chave não exista, retorna uma tabela neutra (sem alteração)
        return str.maketrans("", "")
    
    try:
        with open(caminho_chave, "r", encoding="utf-8") as arquivo:
            chaves = arquivo.read().strip()
        
        lista_chaves = chaves.split(",")
        antes = ""
        depois = ""
        
        for chave in lista_chaves:
            if len(chave) >= 2:
                c1, c2 = chave[0], chave[1]
                if c1 in antes or c2 in antes:
                    continue
                antes += c1 + c2
                depois += c2 + c1
                
        return str.maketrans(antes, depois)
    except Exception as e:
        print(f"[Aviso] Erro ao carregar chaves de '{caminho_chave}': {e}. Usando texto plano.")
        return str.maketrans("", "")

# Tabela de cifra padrão (busca o arquivo 'chave.txt' no mesmo diretório do script)
CAMINHO_CHAVE = "chave.txt"
tabela_chaves = gerador_tabela_cifra(CAMINHO_CHAVE) if os.path.exists(CAMINHO_CHAVE) else str.maketrans("", "")

def cifrar_mensagem(mensagem):
    """Cifra a mensagem usando a tabela atbash modificada."""
    return mensagem.translate(tabela_chaves)

def decifrar_mensagem(mensagem_cifrada):
    """Decifra a mensagem usando a mesma tabela (simétrica)."""
    return mensagem_cifrada.translate(tabela_chaves)

def handle_incoming_client(client_socket, address):
    print(f"\n[+] Novo cliente conectado a você vindo de {address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            mensagem_cifrada = data.decode('utf-8')
            mensagem_original = decifrar_mensagem(mensagem_cifrada)
            print(f"\n[Mensagem Recebida de {address}]: {mensagem_original} (Cifrada: {mensagem_cifrada})")
    except ConnectionResetError:
        pass
    finally:
        client_socket.close()
        print(f"\n[-] Conexão com {address} foi encerrada.")

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
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
            mensagem_cifrada = data.decode('utf-8')
            mensagem_original = decifrar_mensagem(mensagem_cifrada)
            print(f"\n[Resposta de {remote_address}]: {mensagem_original} (Cifrada: {mensagem_cifrada})")
    except:
        pass

def main():
    print("=== NÓ DE REDE MULTI-THREADING COM CRIPTOGRAFIA ===")
    
    global tabela_chaves
    if os.path.exists(CAMINHO_CHAVE):
        print(f"[*] Arquivo '{CAMINHO_CHAVE}' encontrado. Criptografia ativada!")
    else:
        print(f"[*] Aviso: '{CAMINHO_CHAVE}' não encontrado no diretório atual. As mensagens irão sem cifra.")

    try:
        my_port = int(input("Informe a porta onde este nó deve escutar (ex: 5000): "))
    except ValueError:
        print("Porta inválida.")
        return

    # Inicia o servidor local em background
    server_thread = threading.Thread(target=start_server, args=(my_port,))
    server_thread.daemon = True
    server_thread.start()
    print(f"[*] Servidor rodando na porta {my_port}.")

    active_connections = {}
    conn_counter = 1

    while True:
        print("\n--- MENU ---")
        print("1. Conectar a um novo servidor")
        print("2. Enviar mensagem criptografada para um servidor conectado")
        print("3. Listar conexões ativas")
        print("4. Sair / Encerrar programa")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            target_ip = input("Informe o IP do servidor de destino: ").strip()
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
                print(f"[-] Erro ao conectar: {e}")

        elif opcao == "2":
            if not active_connections:
                print("[-] Você não está conectado a nenhum servidor no momento.")
                continue

            print("\nConexões ativas:")
            for cid in active_connections:
                print(f" - ID: {cid}")

            try:
                cid_escolhido = int(input("Digite o ID da conexão: "))
                if cid_escolhido in active_connections:
                    mensagem = input("Digite a mensagem: ")
                    
                    # Aplica a criptografia antes de enviar via socket
                    mensagem_cifrada = cifrar_mensagem(mensagem)
                    
                    active_connections[cid_escolhido].sendall(mensagem_cifrada.encode('utf-8'))
                    print(f"[✓] Mensagem enviada e criptografada: {mensagem_cifrada}")
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