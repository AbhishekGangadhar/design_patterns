from abc import ABC, abstractmethod
from behavioral.observer.observer import IObserver
from behavioral.observer.weather_station import WeatherStation


class IDisplay(ABC):
    @abstractmethod
    def display(self) -> str:
        pass


class PhoneDisplay(IObserver, IDisplay):
    def __init__(self, weather_station: WeatherStation):
        self.weather_station = weather_station
        self.weather_station.register_observer(self)
        self.__temp = self.weather_station.get_current_temperature()

    def __del__(self):
        self.weather_station.unregister_observer(self)

    def update(self):
        self.__temp = self.weather_station.get_current_temperature()

    def display(self) -> str:
        return f"Phone Display: Current Temperature: {self.__temp}"


class TVDisplay(IObserver, IDisplay):
    def __init__(self, weather_station):
        self.weather_station = weather_station
        self.weather_station.register_observer(self)
        self.__temperature = self.weather_station.get_current_temperature()

    def __del__(self):
        self.weather_station.unregister_observer(self)

    def update(self):
        self.__temperature = self.weather_station.get_current_temperature()

    def display(self) -> str:
        return f"TV Display: Current Temperature: {self.__temperature}"
