
from threading import Thread
from time import sleep

# Função que será executada nas threads
def threaded_function(id, num):
    for i in range(num):
        print('Thread', id, 'contando', i)
        sleep(1)

    print ('Thread', id, 'finalizando')

# Lança as três threads e inicia sua execução (start)
for i in [1, 2, 3]:
    thread = Thread(target=threaded_function, args=(i, 3))
    thread.start()

# A linha principal de execução encerra antes das threads
print("Threads finalizadas :)")