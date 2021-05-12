from convertunits.utils import is_none, Base

class Fuel_economy(Base):
    def __init__(self, miles_per_gallon = None, miles_per_gallon_imperial = None, kilometer_per_liter = None, liter_per_100_kilometers = None):
        if not is_none(miles_per_gallon):
            self.miles_per_gallon = miles_per_gallon
            self.miles_per_gallon_imperial = miles_per_gallon * 1.201
            self.kilometer_per_liter = miles_per_gallon / 2.352
            self.liter_per_100_kilometers = 235.215/(1)
        elif not is_none(miles_per_gallon_imperial):
            self.miles_per_gallon = miles_per_gallon_imperial / 1.201
            self.miles_per_gallon_imperial = miles_per_gallon_imperial
            self.kilometer_per_liter = miles_per_gallon_imperial / 2.825
            self.liter_per_100_kilometers = 282.481/(miles_per_gallon_imperial)
        elif not is_none(kilometer_per_liter):
            self.miles_per_gallon = 100/(kilometer_per_liter)
            self.miles_per_gallon_imperial = kilometer_per_liter * 2.825
            self.kilometer_per_liter = kilometer_per_liter
            self.liter_per_100_kilometers = 100/(kilometer_per_liter)
        elif not is_none(liter_per_100_kilometers):
            self.miles_per_gallon = 100/(liter_per_100_kilometers)
            self.miles_per_gallon_imperial = 282.481/(liter_per_100_kilometers)
            self.kilometer_per_liter = 100/(liter_per_100_kilometers)
            self.liter_per_100_kilometers = liter_per_100_kilometers
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    