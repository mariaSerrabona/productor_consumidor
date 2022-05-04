from queue import Queue

from threading import Thread

import time

# Crear cola
q = Queue(10)

def producer(name, numero):

    """Productor"""

    count = 0 #mostrador

    while (count<numero):

        q.join()

        q.put(count)

        print(f"{name} esta produciendo el bollo {count+1}")

        count+=1


def customer(name, numero):

    """consumidor"""

    count = 0

    while (count<numero):

        baozi = q.get()

        print(f"El consumidor- {name} está comiendo el bollo {count+1}")

        count+=1

        q.task_done() # Envía una señal después de comer

        time.sleep(1)



if __name__ == '__main__':

    numero=input('Introduce el número de bollos que se quiere realizar: ')
    numero=int(numero)

    t1 = Thread(target=producer,args=("Maestro Zhang",numero))

    t2 = Thread(target=customer,args=("Xiaoming",numero))

    t1.start()

    t2.start()

