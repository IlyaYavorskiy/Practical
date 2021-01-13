class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.speed

    def go(self):
        print('start key')

    def stop(self):
        print('stop it now')

    def turn(self):
        print('turn!!!')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('over speed!')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('over speed!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


class SportCar(Car):
    pass


town = TownCar(120, 'white', 'bmw')
print(town.color, town.speed, town.name, town.is_police)
town.go()
town.turn()
town.stop()
town.show_speed()

police = PoliceCar(90, 'black', '911')
print(police.color, police.speed, police.name, police.is_police)
police.go()
police.turn()
police.stop()
police.show_speed()