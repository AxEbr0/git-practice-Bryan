import Tarea
class GestorTareas:
    
    def __init__(self):
        self.listaTareas = []

    def addTarea(self, nomb, est):
        if nomb == "":
            print("Ingrese un nombre")
        else:
            nuevaTarea = Tarea(nomb, est)
            self.listaTareas.append(nuevaTarea)