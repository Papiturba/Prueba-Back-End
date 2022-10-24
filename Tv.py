from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje, precio, eficencia, marca,tamano):
        super().__init__(voltaje, precio, eficencia, marca)
        self.__tamano = tamano
        
    def get_tamano(self):
        return self.__tamano
    
    def set_tamanio(self,tamano):
        self.__tamanio = tamano
        
    def __str__(self):
        return f'{super().__str__()}\n Tamaño: {self.__tamano}'

    def calcular_descuento(self):
        return super().calcular_descuento()
    