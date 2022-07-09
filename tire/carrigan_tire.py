from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        count = 0
        for i in self.tire_wear:
            if i >= 0.9:
                count += 1
        if count >= 1:
            return True
        else:
            return False
