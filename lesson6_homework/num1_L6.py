import time


class TrafficLight:
    __color = None

    def running(self):
        while True:
            TrafficLight.__color = 'red'
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'green'
            print(TrafficLight.__color)
            time.sleep(5)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
            time.sleep(2)


tl = TrafficLight()
tl.running()
