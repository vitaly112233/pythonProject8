# #1. Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
#
# class Auto:
#     def __init__(self, brand, age, color="", mark="", weight=0):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#
#     def move(self):
#         print("move")
#
#     def birthday(self):
#         self.age += 1
#
#     def stop(self):
#         print("stop")
#
#
# car = Auto("Volkswagen", 7, "Blue", "jetta", 1700)
#
#
# print(car.brand)
# print(car.age)
# print(car.color)
# print(car.mark)
# print(car.weight)
# car.move()
# car.birthday()
# print(car.age)
# car.stop()


# /---------------------------------------------------

#2. Создать 2 класса truck и car, которые являются наследниками класса auto.
#
# import time
#
#
# class Auto:
#     def __init__(self, brand, age, color="", mark="", weight=0):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#
#
# class Truck(Auto):
#     def __init__(self, max_load):
#         self.max_load = max_load
#
# def move(self):
#     print("attention")
#     super().move()
#
#
# def load(self):
#     time.sleep(1)
#     print("load")
#     time.sleep(1)
#
#
# class Car(Auto):
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print('max speed is:',self.max_speed)
#
#
# truck1 = Truck(10000, "Scania", 5, "Red", "R420", 8000)
# truck2 = Truck(12000, "Mercedes", 2, "Silver", "Actros", 9000)
# car1 = Car(260, "Volkswagen", 3, "Blue", "jetta", 1700)
# car2 = Car(250, "Audi", 1, "Black", "A6", 1800)
#
# print(truck1.brand, truck1.age, truck1.max_load)
# truck1.load()
# truck1.move()
# print(truck2.brand, truck2.age, truck2.max_load)
# truck2.load()
# truck2.move()
# print(car1.brand, car1.age, car1.max_speed)
# car1.move()
# print(car2.brand, car2.age, car2.max_speed)
# car2.move()

#-----------------------------------------------
# #3Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     if area == 0:
#         print('Они равны')
#
# cir1 = Circle(3)
# cir2 = Circle(2)
# print(cir1.area(), cir2.area())
#
