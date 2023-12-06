from datetime import datetime
from tabulate import tabulate as tb
def leer_archivo():
    try:
        with open("Productos_Elie.csv","rt", encoding="utf-8-sig") as arch:
            return [lineas for lineas in arch]
    except:
        return []
    
def parsear(archivo):
    arch =  [lineas.strip().split(";") for lineas in archivo]
    return arch[0], arch[1:]

def cargar_dia():
    fecha_actual = datetime.now()
    nombre_dia = fecha_actual.strftime("%A")
    return nombre_dia

def mostrar_menu():
    opc=["1. Procesar Venta", "0. Cerrar Programa"]
    for _ in opc:
        print(_)
        
        
def extraer_productos(productos):
    return [prod[1].lower() for prod in productos]

def calcular_precio(productos,producto, cantidad):
    for elem in productos:
        if producto.lower() == elem[1].lower():
            return float(elem[2]) * cantidad
            
def calcular_total(lista_productos):
    return sum(elem[2] for elem in lista_productos)


def calcular_descuento(dia):
     dias_descuento = {"monday": 0.15,
                       "tuesday": 0.05,
                       "wednesday": 0.1,
                       "thursday": 0.05,
                       "friday": 0.2,
                       "saturday": 0.1
                       }
     return dias_descuento.get(dia.lower(), 0)
    
def aplicar_descuento(total, descuento):
    return total - total * descuento

def cargar_productos(productos):
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
            
def generar_ticket(productos_cargados):
    encabezado = ["Producto","Cantidad","Precio"]
    
    lineas = [(prod[0], prod[1], f"${prod[2]:.2f}") for prod in productos_cargados]
    
    tabla = tb(lineas, headers=encabezado, tablefmt="fancy_grid")
    
    total = calcular_total(productos_cargados)
    
    descuento = calcular_descuento(cargar_dia())
    precio_final = aplicar_descuento(total, descuento)
    
    ticket = f"\n{tabla}\n\nMonto Total: ${total:.2f}\nMonto Final con Descuento: ${precio_final:.2f}\n"
    
    return ticket

#<>             
if __name__ == "__main__":
    print()
            
    
