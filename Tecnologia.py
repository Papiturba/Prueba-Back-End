


class Tecnologia:
    def __init__(self,voltaje,precio,eficiencia,marca):
        self.__voltaje = voltaje 
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
        
    def get_voltaje(self):
        return self.__voltaje
    
    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
        
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio
        
    def get_eficiencia(self):
        return self.__eficiencia
    
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia
        
    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        self.__marca = marca
        
        
    def __str__(self):
        return f'Marca: {self.__marca}\n Voltaje: {self.__voltaje}\n Precio:{self.__precio}\n Eficiencia:{self.__eficiencia} Descuento: {self.calcular_descuento()}'
    
    
    def calcular_descuento(self):

       if self.__eficiencia == "A" or self.__eficiencia == "B":
            descuento = self.__precio*0.5
            total = self.__precio-descuento
            self.set_precio(total)
            return f'El descuento es de {descuento} y el precio total de: {total}'
       elif self.__eficiencia == "C" or  self.__eficiencia == "D":
            descuento = self.__precio*0.3
            total = self.__precio-descuento
            self.set_precio(total)
            return f'El descuento es de {descuento} y el precio total de: {total}'
       elif self.__eficiencia == "E" or self.__eficiencia == "F":
            descuento = self.__precio*0.1
            total = self.__precio-descuento
            self.set_precio(total)
            return f'El descuento es de {descuento} y el precio total de: {total}'
       else :   
            descuento = 0
            total = self.__precio-descuento
            return f'No se aplica descuento, el precio es de: {self.__precio}'
            
        
 
    









        