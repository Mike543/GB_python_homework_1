'''2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''




class Road:
    def __init__(self, _length, _width, thickness, mass):
        self._lnth = _length
        self._wdth = _width
        self.thick = thickness
        self.mas = mass
    def pavement(self, _length, _width, thickness, mass):
        print(f"Масса дорожного полотна равна {int(self._lnth*self._wdth*self.thick*self.mas/1000)} тонн")
                
road = Road(20, 5000, 25, 5)
road.pavement(20, 5000, 25, 5)

     