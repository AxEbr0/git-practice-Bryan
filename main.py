from GestorTareas import GestorTareas
def main() :
  g = GestorTareas()
  g.addTarea("Comprar el pan", "Pendiente")
  g.mostrarTareas()

if __name__ == "__main__":
  main()