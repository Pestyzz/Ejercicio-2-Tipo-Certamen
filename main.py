#Automotora Auto Seguro Programa Ingreso de fichas
from os import system

fichas = []

menu = 1

""" FUNCIONES DEL PROGRAMA """
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
                return userOption
            elif userOption == 4:
                return userOption
            else:
                print("Dígito inválido.")
        except ValueError:
            print("Caracter no válido")
            
def user_input(message, patente=False, tipo=False, marca=False, precio=False, multas=False, fecha=False, nombre=False, causa=False):
    while True:
        try:
            userInput = input(message)
            #Se valida el ingreso de la patente
            if patente == True:
                userInput = userInput.upper()
                if len(userInput) < 1:
                    print("Debe ingresar una patente.")
                    continue
                elif userInput.isalnum() == False:
                    raise ValueError
                elif len(userInput) != 6:
                    print("La patente debe contener 6 caracteres.")
                    continue
            #---------------------------------------
            #Se valida el ingreso del tipo de vehículo
            if tipo == True:
                userInput = userInput.upper()
                if len(userInput) != 1:
                    print("Debe ingresar un tipo de vehículo.")
                    continue
                elif userInput not in ["A", "C"]:
                    print("Tipo de vehículo no válido.")
                    continue
                match userInput:
                    case "A":
                        userInput = "Auto"
                    case "C":
                        userInput = "Camioneta"
            #---------------------------------------
            #Se valida el ingreso de la marca
            if marca == True:
                userInput = userInput.capitalize()
                if len(userInput) < 1:
                    print("Debe ingresar una marca.")
                    continue
                elif userInput.isalpha() == False:
                    raise ValueError
            #---------------------------------------
            #Se valida el ingreso del precio
            if precio == True:
                if len(userInput) < 1:
                    print("Debe ingresar un valor válido.")
                    continue
                elif userInput.isdigit() == False:
                    raise ValueError
                elif userInput.isdigit() <= 0:
                    print("Valor inválido.")
                    continue
            #---------------------------------------
            #Se valida el ingreso del nombre del dueño
            if nombre == True:
                userInput = userInput.capitalize()
                
                txt = userInput.replace(" ", "") 
                #Si se ingresa un apellido o más nombres, lo que se hace es reemplazar el espacio por ninguno, y validar el nombre entero sin espacios.
                
                if len(txt) < 1:
                    print("Debe ingresar el nombre del dueño del vehículo.")
                    continue
                elif txt.isalpha() == False:
                    raise ValueError
            #---------------------------------------
            #Se validan los datos de la fecha registro/fecha multa
            if fecha == True:   
                if len(userInput) != 10:
                    print("Ingrese el formato correcto por favor. (dd-mm-aaaa)")
                    continue
                elif userInput[2] != "-" or userInput[5] != "-": #Se valida que en esas posiciones se encuentre "-" para que sea correcto el formato pedido dd-mm-aaaa.
                    print("Ingrese el formato correcto por favor. (dd-mm-aaaa)")
                    continue
                    
                dia, mes, anio = userInput.split("-") # ['día', 'mes', 'año']
                dia = int(dia)
                mes = int(mes)
                anio = int(anio)
                if dia < 1 or dia > 31:
                    print("Día inválido")
                    continue
                elif mes < 1 or mes > 12:
                    print("Mes inválido.")
                    continue
                elif anio <= 1800 or anio > 2023:
                    print("Año inválido.")
                    continue 
            #---------------------------------------
            #Se valida el ingreso de si posee multas
            if multas == True:
                userInput = userInput.upper()
                if len(userInput) != 1:
                    print("Debe ingresar una de las 2 opciones.")
                    continue
                elif userInput not in ["Y", "N"]:
                    print("Respuesta inválida.")
                    continue
                
            #---------------------------------------
            #Se valida el ingreso de la causa de la multa
            if causa == True:
                userInput = userInput.capitalize()
                
                txt = userInput.replace(" ", "")
                
                if len(txt) < 1:
                    print("Debe ingresar la causa de la multa.")
                elif txt.isalpha() == False:
                    raise ValueError
            #---------------------------------------
            
            return userInput
        except ValueError:
            print("Caracter no válido.")
            
def grabar_ficha():
    multas = [] #La lista multas la defino en la función, ya que si está afuera todas las fichas tendrán las mismas multas y no distintas.
    
    while True:
        patente = user_input("Ingrese Patente: ", patente=True)
        tipo = user_input("Ingrese Tipo Vehículo (A = Auto, C = Camioneta): ", tipo=True)
        marca = user_input("Ingrese Marca: ", marca=True)
        precio = user_input("Ingrese Precio: $", precio=True)
        fechaReg = user_input("Ingrese Fecha de registro del vehículo (dd-mm-aaaa): ", fecha=True)
        nombreDueño = user_input("Ingrese Nombre del dueño: ", nombre=True)
        
        #Ingreso de las multas a la respectiva lista de estas
        i = 0 #La variable i la utilizo solamente para verificar si ya ha ingresado al menos una multa.
        tieneMulta = user_input("¿Tiene multas? (Y,N):\n >", multas=True)
        while True:
            if i > 0: #Esta parte solamente va cuando ya hay al menos una multa ingresada
                tieneMulta = user_input("¿Tiene otra multa? (Y,N):\n >", multas=True)
            
            if tieneMulta == "Y":
                montoMulta = user_input("Ingrese Monto de la multa: $", precio=True)
                causaMulta = user_input("Ingrese Causa de la multa: ", causa=True)
                fechaMulta = user_input("Ingrese Fecha de la multa: ", fecha=True)
                multa = f"${montoMulta} {causaMulta} {fechaMulta}"
                multas.append(multa)
                i += 1
                continue
            elif tieneMulta== "N":
                if i > 0:
                    break
                multa = "No posee multas."
                multas.append(multa)
                break
            
        break
    
    ficha = [tipo, patente, marca, precio, fechaReg, nombreDueño, multas]
    fichas.append(ficha)
    
def buscar_ficha():
    buscado = user_input("Ingrese Patente: ", patente=True)
    
    for ficha in fichas:
        if ficha[1] == buscado:
            print("Datos Ficha Vehículo: ")
            print(f"Tipo: {ficha[0]}")
            print(f"Patente: {ficha[1]}")
            print(f"Marca: {ficha[2]}")
            print(f"Precio: {ficha[3]}")
            print(f"Fecha de registro del vehículo: {ficha[4]}")
            break
    else:
        print("Patente no registrada.")

def impr_certifi():
    buscado = user_input("Ingrese Patente: ", patente=True)
    
    for ficha in fichas:
        if ficha[1] == buscado:
            print("\t                    COTIZACIÓN AUTOMOTORA AUTO SEGURO                                  ")
            print("\tSe otorga la presente cotización que indica los datos actuales del vehículo a la venta:")
            print(f"Tipo: {ficha[0]}")
            print(f"Patente: {ficha[1]}")
            print(f"Marca: {ficha[2]}")
            print(f"Precio: {ficha[3]}")
            print(f"Fecha de registro del vehículo: {ficha[4]}")
            print(f"Nombre del dueño: {ficha[5]}")
            multas = "\n".join(ficha[6])
            print(f"Multas:\n{multas}")
            print("""\n\tSe otorga esta cotización a la persona que lo solicitó para los fines que estime pertinente.\n
                                Sin otro particular.\n
                                Santiago,30-junio-2022
                                AUTOMOTORA AUTO SEGURO""")
            break
    else:
        print("Patente no registrada.")
        
def salir():
    print("Saliendo...\nBastián Ñiripil.\nversión 1.1")
    menu = 0
    return menu

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""" PROGRAMA PRINCIPAL """""""""""""""""""""""""""""""""""""""

while menu == 1:
    main_menu()
    userOption = user_option()
    
    match userOption:
        case 1:
            grabar_ficha()
            print(fichas)
        case 2:
            buscar_ficha()
        case 3:
            impr_certifi()
        case 4:
            menu = salir()