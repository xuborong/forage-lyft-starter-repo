from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        if sum(self.tire_wear) >= 3:
            return True
        else:
            return False