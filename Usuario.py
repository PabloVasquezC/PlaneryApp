class Usuario:
    def __init__(self, nombre_de_usuario, contrasena):   
        self.nombre_der_usuario = nombre_de_usuario
        self.__contrasena = contrasena

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

usuario1 = Usuario("Pablo Vasquez", "CATA.7531")
usuario2 = Usuario("Nicolas Riquelme", "1234")
usuario3 = Usuario("Ester Godoy","1234")
