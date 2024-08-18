# car is  object to have objects use class method
from car import car

car1 = car('BMW','M4', '2023', 'White')
car2 = car('BENZ','Z1', '2024', 'Black')
car3 = car('JEEP','XP', '2023', 'Red')
car4 = car('MINI', 'COPPER', '2023', 'White')
print(car1 , end = "")
print(car2 , end = "")
print(car3 , end = "")
print(car4 , end = "")
car1.stop()
car2.drive()


