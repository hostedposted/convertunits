from convertunits.utils import is_none, Base

class Frequency(Base):
    def __init__(self, hertz = None, kilohertz = None, megahertz = None, gigahertz = None):
        if not is_none(hertz):
            self.hertz = hertz
            self.kilohertz = hertz / 1000
            self.megahertz = hertz / 1e+6
            self.gigahertz = hertz / 1e+9
        elif not is_none(kilohertz):
            self.hertz = kilohertz * 1000
            self.kilohertz = kilohertz
            self.megahertz = kilohertz / 1000
            self.gigahertz = kilohertz / 1e+6
        elif not is_none(megahertz):
            self.hertz = megahertz * 1e+6
            self.kilohertz = megahertz * 1000
            self.megahertz = megahertz
            self.gigahertz = megahertz / 1000
        elif not is_none(gigahertz):
            self.hertz = gigahertz * 1e+9
            self.kilohertz = gigahertz * 1e+6
            self.megahertz = gigahertz * 1000
            self.gigahertz = gigahertz
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    