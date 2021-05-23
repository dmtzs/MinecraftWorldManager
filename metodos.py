try:
    import os, shutil, platform
except ImportError as errorimp2:
    print(f"Ocurrió el siguiente error de importación: {errorimp2}")

class funciones():
    exten= ".mcworld"
    rutaGuardar= r"C:\Users\Diego\OneDrive\Documentos\MundosMaincra"

    def ObtenerArchivos(self, resuls):
        lstFiles= []
        
        for root, dirs, files in resuls:
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