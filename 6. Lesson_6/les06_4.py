# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
#  - speed, color, name, is_police (булево).
# А также методы:
#  - go, stop, turn(direction)
# , которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

# Опишите несколько дочерних классов:
#  - TownCar, SportCar, WorkCar, PoliceCar.

# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    __start_speed = 1
    __directions = {'forward': 'прямо', 'back': 'назад', 'left': 'налево', 'right': 'направо'}

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.direction = 'forward'

    def go(self):
        if not self.speed:
            self.speed = self.__start_speed
        print(f'Машина поехала. Скорость машины: {self.speed}')

    def stop(self):
        if self.speed:
            self.speed = 0
        print('Машина остановилась')

    def turn(self, direction='forward'):
        self.direction = direction
        print(f'Машина едет {self.__directions.get(direction)}')

    def turn_forward(self):
        self.turn('forward')

    def turn_back(self):
        self.turn('back')

    def turn_left(self):
        self.turn('left')

    def turn_right(self):
        self.turn('right')

    def speed_up(self, speed=10):
        self.speed += speed
        self.show_speed()

    def speed_down(self, speed=10):
        self.speed = (self.speed - speed) if self.speed > speed else 0
        self.show_speed()

    def show_speed(self):
        if not self.speed:
            self.stop()
            return
        print(f'Скорость машины: {self.speed}')


class TownCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name='town-car', is_police=False)
        self._max_speed = 60

    def show_speed(self):
        if not self.speed:
            self.stop()
            return
        if self.speed > self._max_speed:
            print(f'Вы превысили max возможную скорость ({self._max_speed}). ', end='')
        print(f'Скорость машины: {self.speed}')


class WorkCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name='work-car', is_police=False)
        self._max_speed = 40

    def show_speed(self):
        if not self.speed:
            self.stop()
            return
        if self.speed > self._max_speed:
            print(f'Вы превысили max возможную скорость ({self._max_speed}). ', end='')
        print(f'Скорость машины: {self.speed}')


class SportCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name='sport-car', is_police=False)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name='police-car', is_police=True)


t_car = TownCar(0, 'blue')
print('Это полицейская машина') if t_car.is_police else print(f'Это {t_car.name}')
print(f'Цвет машины: {t_car.color}')

t_car.go()

t_car.speed_up()
t_car.speed_up(50)
t_car.speed_down(1)

t_car.turn()
t_car.turn('right')
t_car.turn()
t_car.turn('left')

t_car.stop()
