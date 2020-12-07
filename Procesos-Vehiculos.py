#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from multiprocessing import pool
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

def classifyVehicles(brand):
    Valores=[];
    Total=0;
    if(data!=0):
        for datas in data:
            if datas["marca_vehiculo"] == brand:
                costo = datas["costo_vehiculo"]
                Valores.append(costo)
                eliminarCaracter = costo.replace("$", "")
                costoF = float(eliminarCaracter)
                Total = Total + costoF
        print("Total de costos por marca:",brand,"${:,.2f}".format(Total))



if __name__=="__main__":
    #Se crea una instancia de la clase POOL
    pool = multiprocessing.Pool(processes=16)
    pool.map(classifyVehicles,["Hyundai","Ford","Chevrolet","Toyota","Dodge","Volvo","Audi","Mazda","Infiniti","Buick","Mitsubishi","BMW","Kia","GMC","Jeep","Jaguar"])

    pool.close()
    pool.join()
    
    final = time.time()
    TiempoFinal=(final-inicio)
    print('Tiempo empleado en Programacion Secuencia es :' , str(TiempoFinal) , " Segundos ")
