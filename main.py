from GestorTareas import GestorTareas
import os
def main() :
  salir = False
  gestor = GestorTareas()
  #gestor.add_tarea("Arreglar ventilador", "Pendiente")
  #gestor.add_tarea("Arreglar mesa", "Pendiente")
  #gestor.add_tarea("Arreglar silla", "Pendiente")
  #gestor.add_tarea("Arreglar refrigerador", "Realizada")
  #gestor.add_tarea("Arreglar PC", "Pendiente")
  #gestor.add_tarea("Arreglar puerta", "Realizada")
  #gestor.add_tarea("Arreglar a la vecina", "Pendiente")
  
  while salir==False:
    print("Gestor de tareas programadas")
    print("1-Mostrar lista de tareas")
    print("2-Añadir tarea nueva")
    print("3-Marcar tarea como realizada")
    print("4-Eliminar tarea")
    print("5-Salir")
    eleccion = int(input("Eliga una opcion: "))
    os.system('cls')
    if eleccion == 1:
      gestor.mostrar_tareas()
      input("Volver...")
      os.system('cls')
    elif eleccion == 2:
      nom = input("Ingrese nombre de tarea: ")
      est = input("Ingrese estado de la tarea: ")
      gestor.add_tarea( nom , est)
      print("Tarea añadida con exito")
      input("Volver...")
      os.system('cls')
    elif eleccion == 3:
      gestor.mostrar_tareas_lista()
      marcar = int(input("Eliga la tarea a realizar: "))
      gestor.marcar_realizada(marcar)
      input("Volver...")
      os.system('cls')
    elif eleccion == 4:
      gestor.mostrar_tareas()
      eliminar = int(input("Eliga la tarea a eliminar: "))
      gestor.eliminar_tarea(eliminar)
      input("Volver...")
      os.system('cls')
    elif eleccion == 5:
      print("Cerrando programa...")
      print("Programa cerrado con exito")
      salir = True
    else:
      print("Opcion no valida, vuelva a intentar")
      input("Volver...")
      os.system('cls')
      
      
      
    
  
  
  

if __name__ == "__main__":
  main()