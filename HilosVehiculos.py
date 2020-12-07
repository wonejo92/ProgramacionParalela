""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import json
import logging



LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

inicio=time.time()
#Path del archivo scv
path='Data_Vehiculo.json';

with open(path) as file:
    data = json.load(file)



class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        item=data
        self.queue.put(item)
        #time.sleep(2)

class Consumer(Thread):

    def __init__(self, queue, brand):
        Thread.__init__(self)
        self.queue = queue
        self.brand = brand

    def run(self):
        total = 0
        while True:
            item = self.queue.get()
            for datos in item:
                if datos["marca_vehiculo"] == self.brand:
                    costo = datos["costo_vehiculo"]
                    eliminarCaracter  = costo.replace("$", "")
                    costoF  = float(eliminarCaracter )
                    total = total + costoF
                    #print("Total por costo de los autos de " + self.brand + ": ${:,.2f}".format(total))
                else:
                   self.queue.put(item)

            self.queue.task_done()
            print("Total por costo de los autos de " + self.brand + ": ${:,.2f}".format(total))
            break



if __name__ =="__main__":
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue,brand='Hyundai')
    t3 = Consumer(queue,brand='Ford')
    t4 = Consumer(queue,brand='Chevrolet')
    t5 = Consumer(queue, brand='Toyota')

    t6 = Consumer(queue,brand='Dodge')
    t7 = Consumer(queue,brand='Volvo')
    t8 = Consumer(queue,brand='Audi')
    t9 = Consumer(queue, brand='Mazda')

    t10 = Consumer(queue,brand='Infiniti')
    t11 = Consumer(queue,brand='Buick')
    t12 = Consumer(queue,brand='Mitsubishi')
    t13 = Consumer(queue, brand='BMW')

    t14 = Consumer(queue,brand='Kia')
    t15 = Consumer(queue,brand='GMC')
    t16 = Consumer(queue,brand='Jeep')
    t17 = Consumer(queue, brand='Jaguar')




    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t6.start()
    t7.start()
    t8.start()
    t9.start()

    t10.start()
    t11.start()
    t12.start()
    t13.start()

    t14.start()
    t15.start()
    t16.start()
    t17.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    t6.join()
    t7.join()
    t8.join()
    t9.join()

    t10.join()
    t11.join()
    t12.join()
    t13.join()

    t14.join()
    t15.join()
    t16.join()
    t17.join()

    final=time.time()
    tiempo=(final-inicio)
    print("Tiempo empleado de Programacion con Hilos es: " + str(tiempo) + " Segundos")