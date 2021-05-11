from convertunits.utils import is_none, Base

class Area(Base):
    def __init__(self, square_kilometer = None, square_meter = None, square_mile = None, square_yard = None, square_foot = None, square_inch = None, hectare = None, acre = None):
        if not is_none(square_kilometer):
            self.square_kilometer = square_kilometer
            self.square_meter = square_kilometer * 1e+6
            self.square_mile = square_kilometer / 2.59
            self.square_yard = square_kilometer * 1.196e+6
            self.square_foot = square_kilometer * 1.076e+7
            self.square_inch = square_kilometer * 1.55e+9
            self.hectare = square_kilometer * 1.55e+9
            self.acre = square_kilometer * 100
        elif not is_none(square_meter):
            self.square_kilometer = square_meter / 1e+6
            self.square_meter = square_meter
            self.square_mile = square_meter / 2.59e+6
            self.square_yard = square_meter * 1.196
            self.square_foot = square_meter * 10.764
            self.square_inch = square_meter * 1550
            self.hectare = square_meter / 10000
            self.acre = square_meter / 4047
        elif not is_none(square_mile):
            self.square_kilometer = square_mile * 2.59
            self.square_meter = square_mile * 2.59e+6
            self.square_mile = square_mile
            self.square_yard = square_mile * 3.098e+6
            self.square_foot = square_mile * 2.788e+7
            self.square_inch = square_mile * 2.788e+7
            self.hectare = square_mile * 4.014e+9
            self.acre = square_mile * 640
        elif not is_none(square_yard):
            self.square_kilometer = square_yard / 1.196e+6
            self.square_meter = square_yard / 1.196
            self.square_mile = square_yard / 3.098e+6
            self.square_yard = square_yard
            self.square_foot = square_yard * 9
            self.square_inch = square_yard * 1296
            self.hectare = square_yard / 11960
            self.acre = square_yard / 4840
        elif not is_none(square_foot):
            self.square_kilometer = square_foot / 1.076e+7
            self.square_meter = square_foot / 10.764
            self.square_mile = square_foot / 2.788e+7
            self.square_yard = square_foot / 9
            self.square_foot = square_foot
            self.square_inch = square_foot * 144
            self.hectare = square_foot / 107639
            self.acre = square_foot / 43560
        elif not is_none(square_inch):
            self.square_kilometer = square_inch / 1.55e+9
            self.square_meter = square_inch / 1550
            self.square_mile = square_inch / 4.014e+9
            self.square_yard = square_inch / 1296
            self.square_foot = square_inch / 144
            self.square_inch = square_inch
            self.hectare = square_inch / 1.55e+7
            self.acre = square_inch / 6.273e+6
        elif not is_none(hectare):
            self.square_kilometer = hectare / 100
            self.square_meter = hectare * 10000
            self.square_mile = hectare / 259
            self.square_yard = hectare * 11960
            self.square_foot = hectare * 107639
            self.square_inch = hectare * 1.55e+7
            self.hectare = hectare
            self.acre = hectare * 2.471
        elif not is_none(acre):
            self.square_kilometer = acre / 247
            self.square_meter = acre * 4047
            self.square_mile = acre / 640
            self.square_yard = acre * 4840
            self.square_foot = acre * 43560
            self.square_inch = acre * 6.273e+6
            self.hectare = acre / 2.471
            self.acre = acre
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    