
class Persona:
    def __init__(self, _nombre, _edad, _altura, _sexo):
        self._nombre = _nombre
        self._edad = _edad
        self._altura =_altura
        self._sexo = _sexo

    def get_Nombre(self):
        return self._nombre

    def set_Nombre(self,nombre):
        self._nombre = nombre

    def get_Edad(self):
        return self._edad

    def set_Edad(self,edad):
        self._edad = edad

    def get_Altura(self):
        return self._altura

    def set_Altura(self, altura):
        self._altura = altura

    def get_Sexo(self):
        self._sexo

    def set_Sexo(self, sexo):
        self._sexo = sexo
