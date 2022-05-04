from queue import Queue

from threading import Thread

import time

# Crear cola
q = Queue(10)

def producer(name, numero):

    """Productor"""

    count = 1 #mostrador

    while (numero!=count):

        q.join()

        q.put(count)

        print(f"{name} esta produciendo el bollo {count}")

        count+=1


def customer(name, numero):

    """consumidor"""

    count = 1

    while (numero!=count):

        #baozi = q.get()

        print(f"El consumidor- {name} está comiendo el bollo {count}")

        count+=1

        q.task_done() # Envía una señal después de comer

        time.sleep(1)



if __name__ == '__main__':

    numero=input('Introduce el número de bollos que se quiere realizar: ')

    t1 = Thread(target=producer,args=("Maestro Zhang",numero))

    t2 = Thread(target=customer,args=("Xiaoming",numero))

    t1.start()

    t2.start()

