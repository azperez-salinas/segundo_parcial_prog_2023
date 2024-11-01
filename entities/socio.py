from abc import ABC, abstractmethod

class Socio(ABC):
    def __init__(self, cedula:int, edad:int, sexo:str):
        self.__cedula = cedula
        self.__edad = edad
        self.__sexo = sexo
        self.__sucursal = None
        
    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def sucursal(self):
        return self.__sucursal
    
    @sucursal.setter
    def sucursal(self, suc):
        self.__sucursal = suc
                
    def __eq__(self, ci):
        return self.__cedula == ci
    

class SocioDirecto(Socio):
    def __init__(self, cedula, edad, sexo):
        super().__init__(cedula, edad, sexo)
        self.__cedula = cedula
        self.__edad = edad
        self.__sexo = sexo
        self.__sucursal = None
        
class SocioTercero(Socio):
    def __init__(self, cedula:int, edad:int, sexo:str, app:str):
        super().__init__(cedula, edad, sexo)
        self.__cedula = cedula
        self.__edad = edad
        self.__sexo = sexo
        self.__sucursal = None
        self.__app = app
        
    