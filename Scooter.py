from Tecnologia import Tecnologia


class Scooter(Tecnologia):
        def __init__(self, voltaje, precio, eficiencia, marca, aro, velocidad, peso):
            super().__init__(voltaje,precio,eficiencia,marca)
            self.__aro = aro
            self.__peso = peso
            self.__velocidad = velocidad


        def get_aro(self):
            return self.__aro

        def set_aro(self,aro):
            self.__aro = aro

        def get_velocidad(self):
            return self.__velocidad

        def set_velocidad(self,velocidad):
            self.__velocidad = velocidad

        def get_peso(self):
            return self.__peso

        def set_peso(self,peso):
            self.__peso = peso
        

        def __str__(self):
            return f'{super().__str__()} Aro: {self.__aro}\n Peso: {self.__peso}\Velocidad: {self.__velocidad}\n Despacho:{self.calculo_scooter()}'
    

        def calculo_scooter(self):
         valorkg = 300
         costodespachobase = 4000
         totalkg = self.__peso * valorkg
         costo_total = costodespachobase+totalkg
         return f'El costo de despacho es: {costo_total} '

        def calcular_descuento(self):
            return super().calcular_descuento()

         

   
        

