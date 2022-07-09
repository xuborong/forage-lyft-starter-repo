from abc import ABC
from engine.engine import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__(last_service_mileage, current_mileage)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
