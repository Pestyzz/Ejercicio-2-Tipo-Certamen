#Automotora Auto Seguro Programa Ingreso  de fichas
from os import system

fichas = []

menu = 1

def main_menu():
    print("Automotora Auto Seguro\n1.Grabar\n2.Buscar\n3.Imprimir Cotización\n4.Salir")

def user_option():
    while True:
        try:
            userOption = int(input(">Ingrese un dígito: "))
            
            if userOption == 1:
                return userOption
            elif userOption == 2:
                return userOption
            elif userOption == 3:
                return
            elif userOption == 4:
                return
            else:
                print("Digito inválido.")
                
        except ValueError:
            print("Caracter no válido")
            
def user_input(message):
    userInput = input(message)
    return userInput
            
def grabar_ficha():
    while True:
        multas = []
        
        patente = user_input("Ingrese Patente: ")
        tipo = user_input("Ingrese Tipo Vehículo (A = Auto, C = Camioneta): ")
        marca = user_input("Ingrese Marca: ")
        precio = user_input("Ingrese Precio: ")
        fechaReg = user_input("Ingrese Fecha de registro del vehículo (dd-mm-aa): ")
        nombreDueño = user_input("Ingrese Nombre del dueño: ")
        
        i = 0
        tieneMulta = user_input("¿Tiene multas? (Y,N):\n >")
        while True:
            
            if i > 0:
                tieneMulta = user_input("¿Tiene otra multa? (Y,N):\n >")
            
            if tieneMulta == "Y":
                montoMulta = user_input("Ingrese Monto de la multa: ")
                causaMulta = user_input("Ingrese Causa de la multa: ")
                print("Ingrese Fecha de la multa")
                diaMulta = user_input(">Día: ")
                mesMulta = user_input(">Mes: ")
                añoMulta = user_input(">Año: ")
                fechaMulta = str(f"{diaMulta}-{mesMulta}-{añoMulta}")
                multa = f"{montoMulta} {causaMulta} {fechaMulta}"
                multas.append(multa)
                i += 1
                continue
            elif tieneMulta== "N":
                if i > 0:
                    break
                multa = "El vehículo no posee multas."
                multas.append(multa)
                break
        break
    
    
    ficha = [patente, tipo, marca, precio, fechaReg, nombreDueño, multas]
    fichas.append(ficha)
    

while menu == 1:
    main_menu()
    userOption = user_option()
    
    match userOption:
        case 1:
            grabar_ficha()
            print(fichas)
            
    