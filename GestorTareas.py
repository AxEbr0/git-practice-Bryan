import Tarea
class GestorTareas:
    
    def __init__(self):
        self.listaTareas = []

    def addTarea(self, nomb, est):
        if nomb == "":
            print("Ingrese un nombre")
        elif not est == "Pendiente" or not est == "Realizada":
            print("Ingrese un estado correcto")
        else:
            nuevaTarea = Tarea(nomb, est)
            self.listaTareas.append(nuevaTarea)

    def mostrarTareas(self):
        if self.listaTareas == []:
            print("Esta lista de tareas esta vacía")
        else:
            print("Tareas:")
            i = 0
            for tarea in self.listaTareas:
                print(i++ +": " + tarea.getNombre + ", Estado: " + tarea.getEstado)


    def mostrarTareasPendientes(self):
        if self.listaTareas == []:
            print("Esta lista de tareas esta vacía")
        else:
            print("Tareas sin realizar:")
            i = 0
            for tarea in self.listaTareas:
                if tarea.getEstado == "Pendiente":
                    print(i++ +": " + tarea.getNombre)

    def marcarRealizada(self, pos):
        cont = 0
        if pos>len(self.listaTareas):
            print("Fuera de rango")
        else:
            for a in range(0,len(self.listaTareas), 1):
                if self.listaTareas.getEstado(pos) == "Pendiente":
                    cont+=1
                if cont == pos:
                    self.listaTareas.setEstado(pos) == "Realizada"
                    print("Tarea realizada con exito")
                    break
    def eliminarTarea(self, pos):
         self.listaTareas.remove(pos)



            
            
        






            
            
