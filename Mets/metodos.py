try:
    import os, shutil, platform
except ImportError as errorimp2:
    print(f"Ocurrió el siguiente error de importación: {errorimp2}")

class funciones():
    exten= ".mcworld"
    rutaGuardar= r"C:\Users\Diego\OneDrive\Documentos\MundosMaincra"

    def ObtenerArchivos(self, resuls):
        lstFiles= []
        
        for _, _, files in resuls:
            for fichero in files:
                (nombreFichero, extension)= os.path.splitext(fichero)
                if (extension== self.exten):
                    lstFiles.append(nombreFichero+self.exten)
        return lstFiles
    
    def Guardar(self, rutaOrigen, arregloArchivos):
        for mundo in arregloArchivos:
            shutil.move(f"{rutaOrigen}\\{mundo}", f"{self.rutaGuardar}\\{mundo}")

    def LimpiarConsolaSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls"
        else:
            return "clear"

    def ValidarInt(self, opcion):
        try:
            aux= int(opcion)
            return True

        except Exception:
            return False

    def TraerArchs(self):
        pass

class Pantallas():
    def Menu(self):
        print("\n\n\n\t\t\t\t**Menú**\n")
        print("\t\t\t1. Guardar mundo.")
        print("\t\t\t2. Traer mundo.")
        print("\t\t\t3. Salir")