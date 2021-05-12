from convertunits.utils import is_none, Base

class Pressure(Base):
    def __init__(self, bar = None, pascal = None, pound_force_per_square_inch = None, standard_atmosphere = None, torr = None):
        if not is_none(bar):
            self.bar = bar
            self.pascal = bar * 100000
            self.pound_force_per_square_inch = bar * 14.504
            self.standard_atmosphere = bar / 1.013
            self.torr = bar * 750
        elif not is_none(pascal):
            self.bar = pascal / 133
            self.pascal = pascal
            self.pound_force_per_square_inch = pascal / 6895
            self.standard_atmosphere = pascal / 101325
            self.torr = pascal / 133
        elif not is_none(pound_force_per_square_inch):
            self.bar = pound_force_per_square_inch * 51.715
            self.pascal = pound_force_per_square_inch / 14.504
            self.pound_force_per_square_inch = pound_force_per_square_inch
            self.standard_atmosphere = pound_force_per_square_inch * 6895
            self.torr = pound_force_per_square_inch * 51.715
        elif not is_none(standard_atmosphere):
            self.bar = standard_atmosphere * 1.013
            self.pascal = standard_atmosphere * 101325
            self.pound_force_per_square_inch = standard_atmosphere * 14.696
            self.standard_atmosphere = standard_atmosphere
            self.torr = standard_atmosphere * 760
        elif not is_none(torr):
            self.bar = torr / 750
            self.pascal = torr * 133
            self.pound_force_per_square_inch = torr / 51.715
            self.standard_atmosphere = torr / 760
            self.torr = torr
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    