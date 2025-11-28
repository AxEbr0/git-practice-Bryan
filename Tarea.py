class Tarea:
    nombre: str
    estado: str

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def get_nombre(self):
        return self.nombre
    def get_estado(self):
        return self.estado
    def set_estado(self, est):
        self.estado = est
        