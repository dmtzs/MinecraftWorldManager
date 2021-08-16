try:
    import os
    import time
    from Mets import metodos
except ImportError as errorimp:
    print(f"Ocurrió el siguiente error de importación: {errorimp}")

def main(accion, comm, pants):
    rutaOrigen= r"C:\Users\Diego\Downloads"
    rutaGuardar= r"C:\Users\Diego\OneDrive\Documentos\MundosMaincra"
    salir= True

    os.system(comm)
    while salir:
        pants.Menu()
        op= input("Ingresa la opción deseada: ")
        paso= accion.ValidarInt(op)
        if paso:
            if op== 1:
                resuls= os.walk(rutaOrigen)

                archivosMaincra= accion.ObtenerArchivos(resuls)
                accion.Guardar(rutaOrigen, rutaGuardar, archivosMaincra)
            elif op== 2:
                resuls= os.walk(rutaGuardar)
                archivosMaincra= accion.ObtenerArchivos(resuls)
                for i in archivosMaincra:
                    print(i)
                #Falta la parte de seleccionar el archivo y pasarlo a downloads

            elif op== 3:
                salir= False
        else:
            os.system(comm)
            print("Solo están permitidos números enteros")
            time.sleep(3)

if __name__== "__main__":
    try:
        accion= metodos.funciones()
        pants= metodos.Pantallas()

        comm= accion.LimpiarConsolaSO()
        
        main(accion, comm, pants)
        print("\n\n\n\t\t\tMundos de Minecraft movidos con éxito!!!")
    except Exception as e:
        os.system(accion.LimpiarConsolaSO())
        print(f"Ocurrió el siguiente error: {e}")
    except KeyboardInterrupt:
        print("Se presiono Ctrl+c terminando programa")
    finally:
        print("Programa finalizado")