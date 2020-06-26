from behavioral.observer.observable import IObservable


class WeatherStation(IObservable):
    def __init__(self, current_temperature: float):
        super().__init__()
        self.__current_temperature = current_temperature

    def get_current_temperature(self):
        return self.__current_temperature

    def set_current_temperature(self, temperature: float):
        self.__current_temperature = temperature
        self.notify()
