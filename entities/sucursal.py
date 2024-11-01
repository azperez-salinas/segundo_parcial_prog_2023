from exceptions.entidadYaExiste import EntidadYaExiste

class Sucursal:
    def __init__(self, barrio:str, capacidad:int):
        self.__barrio = barrio
        self.__capacidad = capacidad
        self.__socios_registrados = {}

    def tiene_capacidad(self):
        return len(self.__socios_registrados) < self.__capacidad

    def agregar_socio(self, socio):
        if socio.cedula in self.__socios_registrados:
            raise EntidadYaExiste('[ERROR] Socio ya registrado')
        self.__socios_registrados[socio.cedula] = socio
        socio.sucursal = self
        
    def desasociar_socio(self, cedula):
        socio = self.__socios_registrados[cedula] ##self.__socios_registrados.get(cedula) 
        if socio:
            socio.sucursal = None
            return self.__socios_registrados.pop(cedula)
        return None
        
    
    @property
    def socios_registrados(self):
        return self.__socios_registrados
    
    @property
    def barrio(self):
        return self.__barrio
    
    def __eq__(self, otro_barrio):
        return self.__barrio == otro_barrio
    