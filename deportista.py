class Deportista:
    
    def __init__(self, deporte, anosPracticando):
        self._deporte = deporte
        self._anosPracticando = anosPracticando

    def get_Deporte(self):
        return self._deporte

    def set_Deporte(self, deporte):
        self._deporte = deporte

    def get_AnosPracticando(self):
        return self._anosPracticando

    def set_AnosPracticando(self,anos):
        self._anosPracticando = anos
    