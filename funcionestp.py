from datetime import datetime
from tabulate import tabulate as tb
from typing import List, Tuple

def leer_archivo()-> List[str]:
    """
    Lee el archivo 'Productos_Elie.csv' 
    Pre: No recibe parametros.
    Post: retorna una lista con las líneas del archivo.
    """
    try:
        with open("Productos_Elie.csv","rt", encoding="utf-8-sig") as arch:
            return [lineas for lineas in arch]
    except:
        return []
   
def parsear(archivo: List[str]) -> Tuple[List[str]]:
    """
    Separa los datos de un archivo CSV en 'Encabezado' y 'Datos'.
    Pre: Lista de strings con datos de un archivo CSV.
    Post: Retorna una tupla con encabezado y datos.
    """
    arch =  [lineas.strip().split(";") for lineas in archivo]
    return arch[0], arch[1:]

def cargar_dia()->str:
    """
    Obtiene el día actual
    Pre: No recibe parametros.
    Post: Retorna el nombre del día actual.
    """
    fecha_actual = datetime.now()
    nombre_dia = fecha_actual.strftime("%A")
    return nombre_dia

def mostrar_menu() ->None:
    """
    Muestra las opciones del menú.
    Pre: No recibe parametros.
    Post: Retorna None
    """
    opc=["1. Procesar Venta", "0. Cerrar Programa"]
    for _ in opc:
        print(_)
        
        
def extraer_productos(productos: List[List[str]]) ->List[str]:
    """
    Extrae todos los productos de una matriz 
    Pre: Matriz de las líneas del archivo CSV
    Post: Retorna una lista con el nombre de los productos.
    """
    return [prod[1].lower() for prod in productos]

def calcular_precio(productos: List[str] ,producto: str, cantidad: int)->float:
    """
    Calcula el precio total de un producto.
    Pre: Recibe una lista con los datos de los productos, el nombre del producto elegido y la cantidad comprada.
    Post: Retorna el precio total de la cantidad del producto elegido.
    """
    for elem in productos:
        if producto.lower() == elem[1].lower():
            return float(elem[2]) * cantidad
            
def calcular_total(lista_productos: List[Tuple[str, int, float]]) ->float :
    """
    Suma todos los precios totales de los productos cargados.
    Pre: Recibe una lista de tuplas con: 'nombre_del_producto', 'cantidad' y 'precio_total'
    Post: Retorna la suma de todos los 'precio_total'.
    """
    return sum(elem[2] for elem in lista_productos)


def calcular_descuento(dia:str) ->float:
    """
    Calcula el descuento de los productos dependiendo del dia.
    Pre:  Recibe el día actual
    Post: Retorna un flotante que simboliza el descuento dependiendo del día. 
    """
    dias_descuento = {"monday": 0.15,
                       "tuesday": 0.05,
                       "wednesday": 0.1,
                       "thursday": 0.05,
                       "friday": 0.2,
                       "saturday": 0.1
                       }
     return dias_descuento.get(dia.lower(), 0)
    
def aplicar_descuento(total:float, descuento:float) -> float:
    """
    Calcula el precio precio final con el descuento del día.
    Pre: Recibe el precio total de los productos y el flotante que simboliza el descuento
    Post: Retorna el precio total aplicando el descuento (total - total * descuento).
    """
    return total - total * descuento

def cargar_productos(productos: List[List[str]]) -> List[Tuple[str, int, float]]: 
    """
    La funcion permite la carga de productos. 
    En un bucle, solicita al usuario que ingrese el nombre de un producto. Si este se encuentra en la lista, se le solicita la cantidad del mismo; de lo contrario, se muestra un error.
    Si el usuario ingresa un valor inferior a 1 como cantidad, se le pide que ingrese el número nuevamente; de lo contrario, se muestra un error y se solicita el nombre del producto nuevamente.
    El bucle termina cuando el usuario presiona 'ENTER' al ingresar el nombre del producto. 
    Pre: Recibe la matriz con los datos de los productos del archivo CSV.
    Post: Retorna una lista de tuplas que contienen el nombre del producto, la cantidad y el precio total de la cantidad del producto.
    """
    lista_prod=[]
    while True:
        producto=input("Ingrese el Nombre del producto(Enter terminar carga): ").strip()
        if not producto:
            return lista_prod 
        if producto.lower() in extraer_productos(productos):
            try:
                cantidad=int(input("Ingrese la cantidad de productos: "))
                while cantidad < 1:
                    print("Se ingreso un numero menor a 1")
                    cantidad = int(input("Ingrese la cantidad de productos:"))
                actuales=( producto.lower(), cantidad, calcular_precio(productos,producto,cantidad) )
                lista_prod.append(actuales)         
            except:
                print("Se ingreso un valor invalido, Elija el producto nuevamente:")
        else:
            print("El producto ingresado es invalido o no esta en registrado en la base de datos")
            
def generar_ticket(productos_cargados: List[Tuple[str, int, float]]) -> str:
    """
    Genera un ticket de compra; Calcula el precio total, el descuento del día y el precio final con el descuento aplicado. 
    Pre: Recibe una lista de tuplas con 'nombre_del_producto', 'cantidad' y 'precio_total'.
    Post: Retorna un string que simula ser un ticket de compra con 'Producto', 'Cantidad' y 'Precio', además del subtotal y el precio final con descuento.
    """
    encabezado = ["Producto","Cantidad","Precio"]
    
    lineas = [(prod[0], prod[1], f"${prod[2]:.2f}") for prod in productos_cargados]
    
    tabla = tb(lineas, headers=encabezado, tablefmt="fancy_grid")
    
    total = calcular_total(productos_cargados)
    
    descuento = calcular_descuento(cargar_dia())
    precio_final = aplicar_descuento(total, descuento)
    
    ticket = f"\n{tabla}\n\nMonto Total: ${total:.2f}\nMonto Final con Descuento: ${precio_final:.2f}\n"
    
    return ticket
    
if __name__ == "__main__":
    print()
            
    
