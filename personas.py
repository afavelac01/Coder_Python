class Persona():

    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def saluda(self):
        return f'"Hola soy {self.nombre}'
