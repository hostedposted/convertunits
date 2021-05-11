from convertunits.utils import is_none, Base

class Speed(Base):
    def __init__(self, miles_per_hour = None, foot_per_second = None, meter_per_second = None, kilometer_per_hour = None, knot = None):
        if not is_none(miles_per_hour):
            self.miles_per_hour = miles_per_hour
            self.foot_per_second = miles_per_hour * 1.467
            self.meter_per_second = miles_per_hour / 2.237
            self.kilometer_per_hour = miles_per_hour * 1.609
            self.knot = miles_per_hour / 1.151
        elif not is_none(foot_per_second):
            self.miles_per_hour = foot_per_second / 1.467
            self.foot_per_second = foot_per_second
            self.meter_per_second = foot_per_second / 1.467
            self.kilometer_per_hour = foot_per_second / 3.281
            self.knot = foot_per_second / 1.688
        elif not is_none(meter_per_second):
            self.miles_per_hour = meter_per_second * 2.237
            self.foot_per_second = meter_per_second * 3.281
            self.meter_per_second = meter_per_second
            self.kilometer_per_hour = meter_per_second * 3.281
            self.knot = meter_per_second * 1.944
        elif not is_none(kilometer_per_hour):
            self.miles_per_hour = kilometer_per_hour / 1.609
            self.foot_per_second = kilometer_per_hour / 1.097
            self.meter_per_second = kilometer_per_hour / 3.6
            self.kilometer_per_hour = kilometer_per_hour
            self.knot = kilometer_per_hour / 1.852
        elif not is_none(knot):
            self.miles_per_hour = knot * 1.151
            self.foot_per_second = knot * 1.151
            self.meter_per_second = knot * 1.688
            self.kilometer_per_hour = knot * 1.852
            self.knot = knot
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    