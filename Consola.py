from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self,voltaje,precio,eficiencia,marca,nombre,version):
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__nombre = nombre
        self.__version = version
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_version(self):
        return self.__version
    
    def set_version(self,version):
        self.__version = version
        
    def __str__(self):
        return f'{super().__str__()}\n Nombre:{self.__nombre}\n Versión:{self.__version}'
        

    def calcular_descuento(self):
        return super().calcular_descuento()
