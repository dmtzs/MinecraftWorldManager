try:
    import os
    import shutil
    import platform
except ImportError as errorimp2:
    print(f"Ocurrió el siguiente error de importación: {errorimp2}")

class funciones():
    exten= ".mcworld"

    def ObtenerArchivos(self, resuls):
        lstFiles= []
        
        for _, _, files in resuls:
            for fichero in files:
                (nombreFichero, extension)= os.path.splitext(fichero)
                if (extension== self.exten):
                    lstFiles.append(nombreFichero+self.exten)
        return lstFiles
    
    def Guardar(self, rutaOrigen, rutaMover, arregloArchivos):
        for mundo in arregloArchivos:
            shutil.move(f"{rutaOrigen}\\{mundo}", f"{rutaMover}\\{mundo}")

    def Descargas(self, rutaOrigen, rutaMover, Arch):
        shutil.move(f"{rutaOrigen}\\{Arch}", f"{rutaMover}\\{Arch}")

    def LimpiarConsolaSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls"
        else:
            return "clear"

    def ValidarInt(self, opcion):
        try:
            _= int(opcion)
            return True

        except Exception:
            return False

class Pantallas():
    def Menu(self):
        print("\n\n\n\t\t\t\t**Menú**\n")
        print("\t\t\t1. Guardar mundo.")
        print("\t\t\t2. Traer mundo.")
        print("\t\t\t3. Salir")
    
    def SoloEnteros(self, comm):
        import time

        os.system(comm)
        print("Solo están permitidos números enteros")
        time.sleep(3)
        os.system(comm)

    def NoArchivos(self, comm):
        import time

        os.system(comm)
        print("No hay mundos de minecraft guardados en la ruta")
        time.sleep(3)
        os.system(comm)

    def MensajeFinalOpciones(self, comm, bandera):
        import time
        
        if bandera== 0:
            print("\n\n\n\t\t\tMundos de Minecraft movidos con éxito!!!")
            time.sleep(3)
            os.system(comm)

        elif bandera== 1:
            print("\n\n\n\t\t\tArchivos pasados a descargas con éxito!!!")
            time.sleep(3)
            os.system(comm)