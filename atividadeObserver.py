from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Sensor(ABC):
    def __init__(self):
        self.observers = []
        self.estado = 20.0

    def attach(self, o: Observer):
        self.observers.append(o)

    def detach(self, o: Observer):
        self.observers.remove(o)

    def notify(self):
        for o in self.observers:
            o.update(self)

    def set_estado(self, novo_estado):
        self.estado = novo_estado
        print(f"\n[Sensor] Novo estado: {self.estado}°C")
        self.notify()

class Display(Observer):
    def update(self, subject):
        temp = subject.estado
        print(f"[Display] Mostrando: {temp}°C")

class Logger(Observer):
    def update(self, subject):
        temp = subject.estado
        print(f"[Logger] Registrado: {temp}°C")

if __name__ == "__main__":
    sensor = Sensor()
    display = Display()
    logger = Logger()

    sensor.attach(display)
    sensor.attach(logger)

    sensor.set_estado(31.5)

    sensor.detach(display)
    print("[Sensor] Display desinscrito.")

    sensor.set_estado(18.2)