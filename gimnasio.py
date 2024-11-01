from exceptions.capacidadMaximaAlcanzada    import CapacidadMaximaAlcanzada
from exceptions.entidadNoExiste             import EntidadNoExiste
from exceptions.entidadYaExiste             import EntidadYaExiste
from exceptions.datosInvalidos              import DatosInvalidos 
from entities.sucursal                      import Sucursal
from entities.socio                         import Socio, SocioDirecto, SocioTercero

class Gimnasio:
    def __init__(self):
        self.__sucursales = {}
        self.__socios = {}
        
    def registrar_sucursal(self, barrio, capacidad):
        if not barrio or not capacidad:
            raise DatosInvalidos('[ERROR] Datos ingresados invalidos')
        
        if barrio in self.__sucursales:
            raise EntidadYaExiste('[ERROR] Sucursal ya existe')
        
        suc = Sucursal(barrio, capacidad)
        self.__sucursales[barrio] = suc
        
        
    def registrar_usuario(self, barrio, cedula, edad, sexo, tipo_socio):
        if not barrio or not cedula or not edad or not sexo or tipo_socio not in [0, 1, 2]:
            raise DatosInvalidos('[ERROR] Datos ingresados invalidos')
        
        sexo = sexo.upper()
        if sexo not in ['H','M']:
            raise DatosInvalidos('[ERROR] Datos ingresados invalidos')
        
        if barrio not in self.__sucursales:
            raise DatosInvalidos('[ERROR] Sucursal no encontrada')
        
        suc = self.__sucursales[barrio]

        if not suc.tiene_capacidad():
            raise CapacidadMaximaAlcanzada('[ERROR] Capacidad máxima alcanzada en la sucursal')
        
        if tipo_socio == 0:
            nuevo_socio = SocioDirecto(cedula, edad, sexo)
        else:
            app = 'Pase Libre' if tipo_socio == 1 else "Tu Pase"
            nuevo_socio = SocioTercero(cedula, edad, sexo, app)
    
        suc.agregar_socio(nuevo_socio)
        self.__socios[cedula] = nuevo_socio
        
        
    def traspasar_usuario(self,	barrio,	cedula):
        if cedula not in self.__socios:
            raise EntidadNoExiste('[ERROR] Socio no existe')
        
        if barrio not in self.__sucursales:
            raise EntidadNoExiste('[ERROR] Sucursal no existe')
        
        socio = self.__socios[cedula]
        suc_antigua = self.__sucursales[socio.sucursal.barrio] 
        
        if barrio == suc_antigua.barrio:
            raise EntidadYaExiste('[ERROR] Socio ya asociado a la sucursal ingresada')
        
        suc_nueva = self.__sucursales[barrio]
        
        suc_antigua.desasociar_socio(cedula)
        suc_nueva.agregar_socio(socio)
        
    def	obtener_sucursal(self, cedula):
        socio = self.__socios[cedula]
        return socio.sucursal.barrio
    
    
    def	obtener_nro_usuarios(self, tipo_usuario):
        if tipo_usuario not in [1, 2]:
            raise DatosInvalidos('[ERROR] Datos ingresados invalidos')
        
        cantidad_usuarios_sucursal = 0
        for sucursal in self.__sucursales.values():
            for socio in sucursal.socios_registrados.values():
                if tipo_usuario == 1 and isinstance(socio, SocioDirecto):
                    cantidad_usuarios_sucursal += 1
                elif tipo_usuario == 2 and isinstance(socio, SocioTercero):
                    cantidad_usuarios_sucursal += 1
                    
        return cantidad_usuarios_sucursal