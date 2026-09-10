from threading import Thread
from time import sleep

def threaded_function(id, num):
    for i in range(num):
        print('Thread', id, 'contando', i)
        sleep(0.5)

threads_list = []

for i in [1, 2]:
    thread = Thread(target=threaded_function, args=(i, 10))
    thread.start()
    # Armazena as threads em uma lista de Threads
    threads_list.append(thread)


# Cria uma operaçõa bloqueante que impede a finalização
# da thread principal antes das outras
for t in threads_list:
    t.join()

print("Threads finalizadas :)")