'''4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f"{self.color} {self.name} поехал"

    def stop(self):
        return f"{self.name} остановился"

    def turn_left(self):
        return f"{self.name} повернул направо"

    def turn_rigt(self):
        return f"{self.name} повернул налево"

    def show_speed(self):
        return f"{self.name} едет со скростью {self.speed}"

    def police(self):
        if self.is_police == True:
            return f"Автомобиль {self.name} - служебная машина полиции. Разбегаемся!!!"
        else:
            return f"Все тихо, похоже {self.name} - не полицейский автомобиль. Можно поднажать)"

class WorkCar(Car):

    def show_speed(self):
        print(f"{self.name} едет со скростью {self.speed}")
        if self.speed > 40:
            return f"Автомобиль {self.name} превысил скорость. Полиция уже в пути!"
        else:
            return "Это нормальная скорость для грузового автомобиля"



work = WorkCar(40, "gray", "Kamaz", False)
print(work.go())
print(work.police())
print(work.turn_left())
print(work.turn_rigt())
print(work.turn_rigt())
print(work.turn_left())
print(work.show_speed())
print(work.stop())


class TownCar(Car):

    def show_speed(self):
        print(f"{self.name} едет со скростью {self.speed}")
        if self.speed > 60:
            return f"Автомобиль {self.name} превысил скорость. Полиция уже в пути!"
        else:
            return "Это нормальная скорость для городского автомобиля"



town = TownCar(70, "green", "Жигуль", False)
print(town.go())
print(town.police())
print(town.turn_left())
print(town.turn_rigt())
print(town.show_speed())
print(town.stop())

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

sport = SportCar(200, "red", "Lamborgini", False)
print(sport.go())
print(sport.police())
print(sport.turn_left())
print(sport.turn_rigt())
print(sport.stop())

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

police = PoliceCar(200, "черный", "Уазик", True)
print(police.go())
print(police.police())
print(police.turn_left())
print(police.turn_rigt())
print(police.stop())