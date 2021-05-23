try:
    import metodos, os
except ImportError as errorimp:
    print(f"Ocurrió el siguiente error de importación: {errorimp}")

def main(accion):
    rutaOrigen= r"C:\Users\Diego\Downloads"
    resuls= os.walk(rutaOrigen)

    archivosMaincra= accion.ObtenerArchivos(resuls)
    accion.Guardar(rutaOrigen, archivosMaincra)

if __name__== "__main__":
    try:
        accion= metodos.funciones()

        os.system(accion.LimpiarConsolaSO())
        main(accion)
        print("\n\n\n\t\t\tMundos de Minecraft movidos con éxito!!!")
    except Exception as e:
        os.system(accion.LimpiarConsolaSO())
        print(f"Ocurrió el siguiente error: {e}")