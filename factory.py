from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car


class Factory:

    def create_calliope(self, last_service_date, last_service_mileage, current_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(self, last_service_date, last_service_mileage, current_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(self, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = Spindler(last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorscharch(self, last_service_date, last_service_mileage, current_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(self, last_service_date, last_service_mileage, current_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date)
        car = Car(engine, battery)
        return car
