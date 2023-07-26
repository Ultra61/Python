class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_desc_name(self):
        long_name = str(self.year) + " " + str(self.make) + " " + str(self.model)
        return long_name.title()

    def get_odometer(self):
        print("this car has " + str(self.odometer) + " miles")

    def set_odemeter(self, mileage):
        if mileage < self.odometer:
            print("cannot roll back odometer")
        else:
            self.odometer = mileage

class ElectricCar(Car): # Inherits all methods from previous class

    def __init__(self, make, model, year):
        super().__init__(make, model, year) # Inherits initialization from parent class
        self.battery_size = 75 # Add ElectricCar specific variable

    def desc_battery(self): # ElectricCar specific method
        print("this car has a " + str(self.battery_size) + "KWh battery")

my_tesla = ElectricCar("Tesla", "Model S", "2019")
print(my_tesla.get_desc_name())
my_tesla.desc_battery()

my_new_car = Car("Audi", "A4", "2004")
print(my_new_car.get_desc_name())

my_new_car.get_odometer()
my_new_car.set_odemeter(4000)
my_new_car.get_odometer()