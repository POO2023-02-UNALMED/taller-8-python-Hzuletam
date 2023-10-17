from persona.py import Persona
from futbolista.py import Futbolista

class Futbolista(Persona,Deportista):
    listaFutbolistas = []
    def __init__(self,_nombre, _edad, _altura, _sexo, deporte, anosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        
        Persona.__init__(self, _nombre, _edad, _altura, _sexo)
        Deportista.__init__(self,deporte, anosPracticando)
        self._golesMarcados = golesMarcados 
        self._tarjetasRojas = tarjetasRojas 
        self._piernaHabil = piernaHabil
        listaFutbolistas.append(self)
    
    def get_GolesMarcados(self):
        return self._golesMarcados

    def set_GolesMarcados(self, goles):
        self._golesMarcados = goles

    def get_TarjetasRojas(self):
        return self._tarjetasRojas

    def set_TarjetasRojas(self,tarjetas):
        self._tarjetasRojas = tarjetas
    
    def get_PiernaHabil(self):
        return self._piernaHabil

    def set_PiernaHabil(self, pierna):
        self._piernaHabil = pierna

    @staticmethod
    def get_ListaFutbolistas(self):
        return self.listaFutbolistas

    @staticmethod
    def set_ListaFutbolistas(self, futbolistas):
        self.listaFutbolistas = futbolistas

    def __str__(self):
        return f"Mi nombre es {self.get_Nombre()} so profesional en el deporte {self.get_Deporte()} Tengo {self.get_Edad()} años de edad y llevo {self.get_AnosPracticando()} anos en el deporte"