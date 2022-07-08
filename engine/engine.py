from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    @abstractmethod
    def needs_service(self):
        pass
