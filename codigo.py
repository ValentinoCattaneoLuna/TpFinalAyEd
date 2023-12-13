import funcionestp as fn

def main() ->None:
    """
    Función principal que ejecuta el programa de procesamiento de ventas.
    1. Lee el archivo 'Productos_Elie.csv'.
    2. Muestra un menú con opciones al usuario.
    3. Permite al usuario procesar una venta, cargando productos y generando un ticket de compra.
    4. Permite al usuario cerrar el programa.
    El programa solo se ejecuta si no hay errores al leer el archivo. En caso contrario, se muestra un error.
    """
    arch=fn.leer_archivo()
    if arch:
        encabezado,datos = fn.parsear(arch)
        while True:
            fn.mostrar_menu()
            try:
                elegir=int(input("Ingrese una opcion: "))
                if elegir==1:
                    carga=fn.cargar_productos(datos)
                    print(fn.generar_ticket(carga))
                    
                elif elegir==0:
                    print("Saliendo...")
                    break
                else:
                    print("Se ingreso una funcion invalida")
            except:
                print("Se ingreso un caracter invalido")
    else:
        print("No se pudo conectar a la base de datos")

if __name__ == "__main__":
    main() 
