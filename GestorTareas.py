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

    def mostrarTareas(self):
        if self.listaTareas == []:
            print("Esta lista de tareas esta vacía")
        else:
            print("Tareas:")
            i = 0
            a = 2
            for tarea in self.listaTareas:
                print(i++ +": " + tarea.getNombre + ", Estado: " + tarea.getEstado)
            
            
