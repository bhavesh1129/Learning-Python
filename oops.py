class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fullname(self):
        return f"{self.__brand} -> {self.__model}"

    def get_brand(self):
        return self.__brand + "!"
    
    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model + "!"

    @staticmethod
    def general_description():
        return "Cars are amazing means of transportation"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    

car1 = Car("Maruti", "Brezza")
# print(car1.model)
# print(car1.fullname())

electricCar1 = ElectricCar("Kia", "Seltos", "24kWH")
# print(electricCar1.fullname())
print(car1)

print(car1.get_brand())

car1.set_model("Swift")
print(car1.get_model())

print(car1.general_description())

print(isinstance(car1, Car))
print(isinstance(car1, ElectricCar))

