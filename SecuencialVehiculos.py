import time
import json
path='Data_Vehiculo.json';
BrantoTittle="";

inicio= time.time()

with open(path) as file:
    data = json.load(file)

def classifyVehicles(brand):
    valores = [];
    Total=0;
    print(" Marca: ",brand)
    BrantoTittle = brand;
    for datas in data:
        if datas["marca_vehiculo"] == brand:
            costo = datas["costo_vehiculo"]
            valores.append(costo)
            eliminarCaracter = costo.replace("$", "")
            costoF = float(eliminarCaracter)
            Total = Total + costoF;
    print("Total de costos : ${:,.2f}".format(Total))



if __name__ == "__main__":
    print(" PROCESAMIENTO SECUENCIAL DE VEHICULOS. ")
    classifyVehicles("Hyundai")
    classifyVehicles("Ford")
    classifyVehicles("Chevrolet")
    classifyVehicles("Toyota")

    classifyVehicles("Dodge")
    classifyVehicles("Volvo")
    classifyVehicles("Audi")
    classifyVehicles("Mazda")

    classifyVehicles("Infiniti")
    classifyVehicles("Buick")
    classifyVehicles("Mitsubishi")
    classifyVehicles("BMW")

    classifyVehicles("Kia")
    classifyVehicles("GMC")
    classifyVehicles("Jeep")
    classifyVehicles("Jaguar")



    final = time.time()
    TiempoFinal=(final-inicio)
    print('Tiempo empleado en Programacion Secuencia es :' , str(TiempoFinal) , " Segundos ")