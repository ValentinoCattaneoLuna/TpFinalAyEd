import funcionestp as fn

def main() ->None:
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
