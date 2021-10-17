#region Librerias
from collections import namedtuple
import re
import os
import datetime
import sys
#endregion

# region Declaracion de variables
LimpiarPantalla = lambda: os.system('cls')
Producto = namedtuple("Producto", ("descripcion", "cantidad", "precio"))
monto_total = 0
diccionario_ventas = {}
diccionario_productos = {}
diccionario_montos = {}
regexLetras = "^[a-zA-Z ]+$"
#endregion

#region Metodos
def opcion_uno():
    global monto_total
    # Se pregunta la clave, luego de ello se busca en el diccionario.
    clave = input("Ingrese la clave de la venta: ")
    if clave in diccionario_ventas.keys():
        print("Esa clave ya está registrada, intente de nuevo. ")
        input("Pulse enter para continuar... ")
    else:
        # Si la clave no se encuentra, se capturan el resto de los datos
        while True:
            folio = input("Ingrese el folio del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                except Exception:
                    print(f"Ocurrió un problema, debe ingresar un dato numérico entero: {sys.exc_info()[0]}")
                    input("Pulse enter para continuar... ")
                else:
                    while True:
                        try:
                            precio = float(input("Ingrese el precio del producto: "))
                        except Exception:
                            print(f"Ocurrió un problema, debe ingresar un dato numérico de tipo entero o float: {sys.exc_info()[0]}")
                            input("Pulse enter para continuar... ")
                        else:
                            break
                    break

            # Luego de capturar, se realiza la instancia, se almacena en un diccionario
            # y se actualiza la variable monto.
            producto_registrado = Producto(descripcion, cantidad, precio)
            diccionario_productos[folio] = producto_registrado
            monto = (cantidad * precio)
            monto_total = monto_total + monto

        # Se pregunta al usuario si desea seguir capturando otro producto
            respuesta = input("¿Desea agregar otro producto? [S/N]: ")
            if respuesta.upper() == "S":
                LimpiarPantalla()
            elif respuesta.upper() == "N":
                # Si ya no desea capturar, se imprimee el calculo del monto e IVA
                LimpiarPantalla()
                fecha = datetime.datetime.now()
                momento = fecha.strftime("%d/%m/%Y")
                IVA = (monto_total * 0.16)
                print(f'El monto total a pagar es: {"${:,.2f}".format((monto_total + IVA))}')
                print(f'El IVA aplicable del 16% es: {"${:,.2f}".format((IVA))}')
                diccionario_copia = diccionario_productos.copy()
                diccionario_ventas[clave] = diccionario_copia,momento
                diccionario_productos.clear()
                diccionario_montos[clave] = monto_total+IVA
                monto_total = 0
                input("Pulse enter para continuar... ")
                break
            else:
                print("Error. Opcion no válida!")


def opcion_dos():
    LimpiarPantalla()
    monto_total_consulta = 0
    busqueda = input("Ingrese la clave de venta a buscar: ")
    if busqueda in diccionario_ventas.keys():
        for producto in diccionario_ventas[busqueda][0]:
            print(f"La descripción del producto es: {diccionario_ventas[busqueda][0][producto].descripcion}")
            print(f"La cantidad del producto: {diccionario_ventas[busqueda][0][producto].cantidad}")
            print(f"El precio unitario del producto es: {'${:,.2f}'.format(diccionario_ventas[busqueda][0][producto].precio)}")
        print(f"La fecha de venta fue: {diccionario_ventas[busqueda][1]}")
        print(f"El monto total de la venta fue: {'${:,.2f}'.format(diccionario_montos[busqueda])}")
        input("Pulse enter para continuar... ")
    else:
        print("Clave no registrada. ")
        input("Pulse enter para continuar... ")

def opcion_tres():
    LimpiarPantalla()
    print("Saldrás del sistema!")

def main(): 
    while True:
        LimpiarPantalla()
        print("***MENU VENTA***")
        print("¿Qué desea hacer?")
        print("1: Registrar Venta")
        print("2: Consultar Venta")
        print("3: Salir")
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                opcion_uno()
            elif opcion == 2:
                opcion_dos()
            elif opcion == 3:
                opcion_tres()
                break
            else:
                print("Opcion no valida")
                input("Pulse enter para continuar... ")
        except ValueError:
            print('Ingrese un dato numérico entero. ')
            input("Pulse enter para continuar... ")
#endregion

# Se manda a llamar el metodo Main
main()