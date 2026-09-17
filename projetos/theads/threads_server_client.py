import socket
import threading


TCP_IP = '0.0.0.0'
CLIENT_IP = '127.0.0.1'
TCP_PORT = 3232


def server():
    """Executa o servidor TCP."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Permite reutilizar a porta rapidamente após o encerramento
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((TCP_IP, TCP_PORT))
        sock.listen(1)

        print('Servidor inicializado ...')
        print(f'Aguardando conexão na porta {TCP_PORT}...\n')

        conn, addr = sock.accept()

        with conn:
            print(f'Servidor conectado por: {addr}\n')

            mensagem = ''

            while True:
                data = conn.recv(1024)

                # Cliente desconectou
                if not data:
                    break

                mensagem = data.decode().strip()

                print(f'Mensagem recebida: {mensagem}')

                # Cliente solicitou encerramento
                if mensagem == 'sair':
                    break
                else:
                    conn.sendall(mensagem.encode())

    print('\nServidor finalizado.')


def client():
    """Executa o cliente TCP."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        print('Cliente inicializado ...')

        # O servidor pode levar alguns milissegundos para
        # começar a escutar. Faz algumas tentativas de conexão.
        while True:
            try:
                sock.connect((CLIENT_IP, TCP_PORT))
                break

            except ConnectionRefusedError:
                # Aguarda o servidor iniciar
                import time
                time.sleep(0.1)

        print('Cliente conectado ao servidor!\n')

        while True:

            mensagem = input(
                'Digite uma mensagem [ou "sair" para encerrar]: '
            )

            sock.sendall(mensagem.encode())

            # Cliente solicitou encerramento
            if mensagem == 'sair':
                break

            # Recebe resposta do servidor
            data = sock.recv(1024)

            if not data:
                print('Servidor desconectado.')
                break

            resposta = data.decode()

            print(f'msg do servidor: {resposta}\n')

    print('Cliente finalizado.')


def main():
    # Thread responsável pelo servidor
    server_thread = threading.Thread(
        target=server,
        name='Servidor'
    )

    # Thread responsável pelo cliente
    client_thread = threading.Thread(
        target=client,
        name='Cliente'
    )

    # Inicia primeiro o servidor
    server_thread.start()

    # Inicia o cliente imediatamente depois
    client_thread.start()

    # Aguarda as duas threads terminarem
    server_thread.join()
    client_thread.join()

    print('\nPrograma finalizado.')


if __name__ == '__main__':
    main()
