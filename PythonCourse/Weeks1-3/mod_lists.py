cars = ['honda', 'toyota', 'chevrolet', 'dodge', 'lotus']
#change value of 'honda' to 'ford'
print(cars[0])
cars[0] = 'ford'
print(cars[0])
#append value of 'ferrari' to cars
cars.append('ferrari')
print(cars)
#insert jeep into [1] position in cars
cars.insert(1, 'jeep')
print(cars)
#remove jeep using del
del cars[1]
print(cars)
#using the pop method
pop_car = cars.pop()
print(pop_car)
print(cars)
#using index in pop method
pop_car = cars.pop(0)
print(pop_car)
print(cars)
#using remove to remove a specified value
remove_car = 'chevrolet'
cars.remove(remove_car)
print(cars)