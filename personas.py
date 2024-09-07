class Persona():

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def saluda(self):
        return f'"Hola soy {self.nombre}'
