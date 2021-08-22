try:
    import os
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
            op= int(op)
            if op== 1:
                resuls= os.walk(rutaOrigen)

                archivosMaincra= accion.ObtenerArchivos(resuls)
                accion.Guardar(rutaOrigen, rutaGuardar, archivosMaincra)
                pants.MensajeFinalOpciones(comm, 0)
            elif op== 2:
                os.system(comm)
                resuls= os.walk(rutaGuardar)
                archivosMaincra= accion.ObtenerArchivos(resuls)
                if len(archivosMaincra) > 0:
                    for i in range(len(archivosMaincra)):
                        print(f"\n\t\t{i+1}. {archivosMaincra[i]}")
                    op2= input("Ingresa el número correspondiente al número del mundo que deseas pasar a descargas: ")
                    paso2= accion.ValidarInt(op2)
                    if paso2:
                        op2= int(op2)
                        accion.Descargas(rutaGuardar, rutaOrigen, archivosMaincra[op2-1])
                        pants.MensajeFinalOpciones(comm, 1)
                    else:
                        pants.SoloEnteros(comm)
                else:
                    pants.NoArchivos(comm)

            elif op== 3:
                salir= False
        else:
            pants.SoloEnteros(comm)

if __name__== "__main__":
    try:
        accion= metodos.funciones()
        pants= metodos.Pantallas()

        comm= accion.LimpiarConsolaSO()
        
        main(accion, comm, pants)

    except Exception as e:
        os.system(accion.LimpiarConsolaSO())
        print(f"Ocurrió el siguiente error: {e}")

    except KeyboardInterrupt:
        print("Se presiono Ctrl+c terminando programa")

    finally:
        print("Finalizando programa")