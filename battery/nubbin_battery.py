from battery.battery import *


class Nubbin(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date <= self.current_date:
            return True
        else:
            return False
