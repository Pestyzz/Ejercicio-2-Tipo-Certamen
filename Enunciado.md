Enunciado
-----------------------------------------------------------------------------------------------------------------------------------------------------
La automotora “Auto Seguro” necesita registrar todos los datos de los vehículos (ficha) que en este periodo tienen a la venta. 
El registro de vehículos debe almacenar las fichas de acuerdo a los siguientes datos y sus validaciones correspondientes:
Tipo (solo una letra, A = Auto, C= Camioneta)
Patente (ejemplo LJPB14, 6 caracteres)
Marca (entre 2 y 15 caracteres)
Precio (mayor a $5.000.000)
Fecha de registro del vehículo (ejemplo dd-mm-aaaa, no vacía)
Nombre del dueño (no vacío)
Multas (monto, causa y fecha). Por ejemplo ($50.000 Mal estacionado 01-03-2019 / $100.000 Exceso velocidad 15-09-2021)

En el registro de vehículos que pertenece a la región metropolitana de Santiago de Chile, requiere construir un programa con un menú que contenga las siguientes opciones, las que pueden ser utilizadas más de una vez:

Opción 1
●	Grabar: Corresponde a guardar los datos de un vehículo, indicados en la ficha. Realizando previamente las validaciones correspondientes, si un dato no es adecuado debe volver a solicitarlo. 

Opción 2
●	Buscar: Corresponde buscar un auto por su patente y mostrar la ficha excluyendo nombre y multas. Si no se encuentra indicar un mensaje adecuado y volver al menú.

Opción 3
•	Imprimir cotización: Esta opción permite imprimir una cotización, para una patente específica. En caso de no encontrar la patente, debe mostrar un mensaje adecuado y volver al menú. El formato de la cotización es el siguiente:

COTIZACION AUTOMOTORA  AUTO SEGURO

Se otorga la presente cotización que indica los datos actuales del vehículo a la venta:
Tipo:  Camioneta
Patente: LJPB14, 6 caracteres
Marca: Chevrolet
Precio: $25.000.000
Fecha de registro: 24-09-2018
Nombre del dueño: Juan Pérez Serón
Multas:
  $50.000 Mal estacionado   01-03-2019
$100.000 Exceso velocidad 15-09-2021

Se otorga esta cotización a la persona que lo solicito para los fines que estime pertinente.

Sin otro particular.

Santiago, 30-junio-2022
AUTOMOTORA AUTO SEGURO

Opción 4 
●	Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y la versión del programa.
