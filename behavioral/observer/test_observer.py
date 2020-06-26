import unittest
from unittest import TestCase
from behavioral.observer.weather_station import WeatherStation
from behavioral.observer.displays import TVDisplay, PhoneDisplay


class TestObserverPatter(TestCase):
    def test(self):
        weather_station = WeatherStation(28)
        self.assertEqual(0, len(weather_station.observers))

        tv_display_1 = TVDisplay(weather_station)
        self.assertEqual("TV Display: Current Temperature: 28", tv_display_1.display())

        phone_display_1 = PhoneDisplay(weather_station)
        self.assertEqual("Phone Display: Current Temperature: 28", phone_display_1.display())

        self.assertEqual(2, len(weather_station.observers))

        weather_station.set_current_temperature(29)

        self.assertEqual("TV Display: Current Temperature: 29", tv_display_1.display())
        self.assertEqual("Phone Display: Current Temperature: 29", phone_display_1.display())

        tv_display_2 = TVDisplay(weather_station)
        self.assertEqual("TV Display: Current Temperature: 29", tv_display_1.display())

        self.assertEqual(3, len(weather_station.observers))

        weather_station.unregister_observer(tv_display_2)
        self.assertEqual(2, len(weather_station.observers))

        weather_station.unregister_observer(tv_display_1)
        weather_station.unregister_observer(phone_display_1)
        self.assertEqual(0, len(weather_station.observers))


if __name__ == '__main__':
    unittest.main()
