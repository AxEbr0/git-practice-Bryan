import json
import os
from Tarea import Tarea

class GestorTareas:
    lista_tareas : list
    ARCHIVO_DB = "data.json"
    
    def __init__(self):
        self.lista_tareas = []
        self.cargar_datos()

    def add_tarea(self, nomb : str, est :str):
        if nomb == "":
            print("Ingrese un nombre")
        elif est not in ("Realizada","Pendiente"):
            print("Ingrese un estado correcto")
        else:
            self.lista_tareas.append(Tarea(nomb, est))
            self.guardar_datos()
            

    def mostrar_tareas(self):
        if self.lista_tareas == []:
            print("No hay tareas registradas")
        else:
            print("Tareas:")
            i = 0
            for tarea in self.lista_tareas:
                i+=1
                print(i, ":", tarea.get_nombre(), ", Estado:", tarea.get_estado())

    def obtener_tareas_pendientes(self)-> list:
      return [n for n in self.lista_tareas if n.get_estado()=="Pendiente"]
    
    def mostrar_tareas_lista(self):
        if self.lista_tareas == []:
            print("No hay tareas registradas")
            return
        tareas_pendientes = self.obtener_tareas_pendientes()
        if tareas_pendientes == []:
            print("No hay tareas pendientes")
        else:
            print("Tareas pendientes:")
            i = 0
            for tarea in tareas_pendientes:
                    i+=1
                    print(i ,":" , tarea.get_nombre())

    def marcar_realizada(self, pos):
        pos-=1
        cont = -1
        if (pos>=len(self.obtener_tareas_pendientes())) or (pos < 0):
            print("La tarea seleccionada no existe")
        else:
            for a in range(len(self.lista_tareas)):
                if self.lista_tareas[a].get_estado() == "Pendiente":
                    cont+=1
                if cont == pos:
                    self.lista_tareas[a].set_estado("Realizada")
                    self.guardar_datos()
                    print("Tarea realizada con exito")
                    return
                  
    def eliminar_tarea(self, pos):
        pos-=1
        if (pos>=len(self.lista_tareas)) or (pos<0):
          print("La tarea seleccionada no existe")
          return
         
        self.lista_tareas.pop(pos)
        self.guardar_datos()
        print("Tarea eliminada con exito")
        
    def guardar_datos(self):
        datos_para_guardar = []
        for tarea in self.lista_tareas:
            datos_para_guardar.append({
                "nombre": tarea.get_nombre(),
                "estado": tarea.get_estado()
            })
            
        try:
            with open(self.ARCHIVO_DB, "w") as archivo:
                json.dump(datos_para_guardar, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self):
        if not os.path.exists(self.ARCHIVO_DB):
            return

        try:
            with open(self.ARCHIVO_DB, "r") as archivo:
                datos_cargados = json.load(archivo)
                
                self.lista_tareas = []
                for dato in datos_cargados:
                    nueva_tarea = Tarea(dato["nombre"], dato["estado"])
                    self.lista_tareas.append(nueva_tarea)
        except Exception as e:
            print(f"Error al cargar datos o archivo corrupto: {e}")
    