from exceptions.capacidadMaximaAlcanzada import CapacidadMaximaAlcanzada
from exceptions.entidadNoExiste import EntidadNoExiste
from exceptions.entidadYaExiste import EntidadYaExiste
from exceptions.datosInvalidos import DatosInvalidos
from entities.sucursal import Sucursal
from entities.socio import SocioDirecto, SocioTercero
from gimnasio import Gimnasio

if __name__ == "__main__":
    # Initialize the gym management system
    gimnasio = Gimnasio()
    
    # Test registering a new branch (sucursal)
    try:
        gimnasio.registrar_sucursal("Centro", 2)
        print("Sucursal 'Centro' registrada correctamente.")
    except (DatosInvalidos, EntidadYaExiste) as e:
        print(e)

    # Test registering a new user (socio) in the branch
    try:
        gimnasio.registrar_usuario("Centro", 12345678, 25, 'M', 0)  # SocioDirecto
        print("Usuario 12345678 registrado correctamente en 'Centro'.")
    except (DatosInvalidos, EntidadYaExiste, CapacidadMaximaAlcanzada) as e:
        print(e)

    # Test registering a second user
    try:
        gimnasio.registrar_usuario("Centro", 87654321, 30, 'H', 1)  # SocioTercero - Pase Libre
        print("Usuario 87654321 registrado correctamente en 'Centro'.")
    except (DatosInvalidos, EntidadYaExiste, CapacidadMaximaAlcanzada) as e:
        print(e)

    # Test branch capacity limit
    try:
        gimnasio.registrar_usuario("Centro", 11223344, 28, 'H', 2)  # Should raise CapacidadMaximaAlcanzada
    except CapacidadMaximaAlcanzada as e:
        print(e)

    # Test transferring a user to a new branch
    try:
        gimnasio.registrar_sucursal("Norte", 3)
        gimnasio.traspasar_usuario("Norte", 12345678)
        print("Usuario 12345678 transferido correctamente a 'Norte'.")
    except (EntidadNoExiste, EntidadYaExiste) as e:
        print(e)

    # Test getting the branch a user belongs to
    try:
        barrio = gimnasio.obtener_sucursal(12345678)
        print(f"Usuario 12345678 pertenece a la sucursal: {barrio}")
    except DatosInvalidos as e:
        print(e)

    # Test obtaining the number of users by type
    try:
        total_directos = gimnasio.obtener_nro_usuarios(1)
        total_terceros = gimnasio.obtener_nro_usuarios(2)
        print(f"Total socios directos: {total_directos}")
        print(f"Total socios por app de terceros: {total_terceros}")
    except DatosInvalidos as e:
        print(e)    
