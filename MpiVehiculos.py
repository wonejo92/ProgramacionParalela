#Para ejecutar un script con mip se utiliza el siguiente comando
#mpiexec -n 5 python "nombre del script"
from mpi4py import MPI
import time
import json
import logging

ListaVehiculos=[];
ListaFiltrada=[];

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

inicio=time.time()
#Path del archivo scv
path='Data_Vehiculo.json';

#lectura del archivo Json
with open(path) as file:
    info = json.load(file)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2


def Filtrado():
    for datas in info:
        ListaVehiculos.append(datas["marca_vehiculo"])
        #print(ListaVehiculos)

    for n in ListaVehiculos:
        if n not in ListaFiltrada:
            ListaFiltrada.append(n)
    print("Lista Filtrada")
    #print(ListaFiltrada)

data = comm.gather(data, root=0)
if rank == 0:
    Filtrado()
else:
    Filtrado()
    for i in range(0,size):
        total = 0
        for datas in info:
            if datas["marca_vehiculo"] == ListaFiltrada[i]:
                costo = datas["costo_vehiculo"]
                eliminarCaracter = costo.replace("$", "")
                costoF = float(eliminarCaracter)
                total = total + costoF
        print("Total por costo de los autos de " + ListaFiltrada[i] + ": ${:,.2f}".format(total))
final=time.time()
tiempo=(final-inicio)
print("Tiempo empleado de Programacion con Hilos es: " + str(tiempo) + " Segundos")