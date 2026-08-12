import socket
# Sockets permitem a comunicação entre processos - na mesma máquina ou não -
# através da criação de conexões entre os processos.

# Define o endereço como a própria máquina e a portas como: 3210
IP = '127.0.1.1'
Server_Port = 9090

# Cria o socket padrão: IPv4 - UDP
# socket.AF_INET -> ipv4 - Internet Protocol version 4
# SOCK_DGRAM -> UDP
# Gerente de Contextos
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # Define o IPVA, o metodo usado (SOCK_STREAM) e garante que feche o servidor caso saia do bloco de comandos

    # Mostra que o cliente foi iniciado
    print('Cliente Inicializado ...\n\n')

    # Conecta ao servidor
    sock.connect((IP, Server_Port))

    print('Cliente Conectado ao servidor ...\n\n') # Mensagem que mostra quando o cliente se conecta

    while True: # Enquanto o cliente não digitar 'sair'
        mensagem = input('Digite um valor [digite "sair" para encerrar]:') # Solicita a mensagem ao cliente

        # Codifica a string para enviar ao cliente
        mensagem = mensagem.encode()

        # Envia a mensagem para o Servidor
        sock.sendall(mensagem)

        print(f'Mensagem: {mensagem.decode()} \n  - enviada para IP {IP} : Porta {Server_Port}\n') # Mostra a mensagem codificada e pra qual endereço ela foi enviada

        if mensagem.decode() == 'sair': # Quebra o loop caso o cliente queira encerrar
            break

        # Aguarda/Recebe a mensagem de resposta do servidor
        data = sock.recv(1024)

        # decodifica a mensagem retornando apenas a string referente à mensagem
        mensagem = data.decode()

        # Mostra a mensagem decodificada e de onde veio
        print(f'Mensagem: {mensagem} \n  - recebida do IP {IP} : Porta {Server_Port}\n')

# Mensagem de encerramento
print('\nCliente Finalizado.\n')
