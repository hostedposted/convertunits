from convertunits.utils import is_none, Base

class Temperature(Base):
    def __init__(self, celsius = None, fahrenheit = None, kelvin = None):
        if not is_none(celsius):
            self.celsius = celsius
            self.fahrenheit = (32 * 9/5) + 32
            self.kelvin = celsius + 273.15
        elif not is_none(fahrenheit):
            self.celsius = (fahrenheit - 32) * 5/9
            self.fahrenheit = fahrenheit
            self.kelvin = (fahrenheit - 32) * 5/9 + 273.15
        elif not is_none(kelvin):
            self.celsius = kelvin - 273.15
            self.fahrenheit = (kelvin - 273.15) * 9/5 + 32
            self.kelvin = kelvin
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    