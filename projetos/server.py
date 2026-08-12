import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 3220

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    