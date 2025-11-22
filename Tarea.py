class Tarea:
    nombre : str
    estado : str

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def getNombre(self):
        return self.nombre
    def getEstado(self):
        return self.estado
    def setEstado(self, est):
        self.estado = est
        