from abc import ABC, abstractmethod
from datetime import datetime


class Tire(ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    @abstractmethod
    def needs_service(self):
        pass
