from convertunits.utils import is_none, Base

class Length(Base):
    def __init__(self, kilometer = None, meter = None, centimeter = None, millimeter = None, micrometer = None, nanometer = None, mile = None, yard = None, foot = None, inch = None, nautical_mile = None):
        if not is_none(kilometer):
            self.kilometer = kilometer
            self.meter = kilometer * 1000
            self.centimeter = kilometer * 100000
            self.millimeter = kilometer * 1e+6
            self.micrometer = kilometer * 1e+9
            self.nanometer = kilometer * 1e+12
            self.mile = kilometer / 1.609
            self.yard = kilometer * 1094
            self.foot = kilometer * 3281
            self.inch = kilometer * 39370
            self.nautical_mile = kilometer / 1.852
        elif not is_none(meter):
            self.kilometer = meter / 1000
            self.meter = meter
            self.centimeter = meter * 100
            self.millimeter = meter * 1000
            self.micrometer = meter * 1e+6
            self.nanometer = meter * 1e+9
            self.mile = meter / 1609
            self.yard = meter * 1.094
            self.foot = meter * 3.281
            self.inch = meter * 39.37
            self.nautical_mile = meter / 1852
        elif not is_none(centimeter):
            self.kilometer = centimeter / 100000
            self.meter = centimeter / 100
            self.centimeter = centimeter
            self.millimeter = centimeter * 10
            self.micrometer = centimeter * 10000
            self.nanometer = centimeter * 1e+7
            self.mile = centimeter / 160934
            self.yard = centimeter / 91.44
            self.foot = centimeter / 30.48
            self.inch = centimeter / 2.54
            self.nautical_mile = centimeter / 185200
        elif not is_none(millimeter):
            self.kilometer = millimeter / 1e+6
            self.meter = millimeter / 1000
            self.centimeter = millimeter / 10
            self.millimeter = millimeter
            self.micrometer = millimeter * 1000
            self.nanometer = millimeter * 1e+6
            self.mile = millimeter / 1.609e+6
            self.yard = millimeter / 914
            self.foot = millimeter / 305
            self.inch = millimeter / 25.4
            self.nautical_mile = millimeter / 1.852e+6
        elif not is_none(micrometer):
            self.kilometer = micrometer / 1e+9
            self.meter = micrometer / 1e+6
            self.centimeter = micrometer / 10000
            self.millimeter = micrometer / 1000
            self.micrometer = micrometer
            self.nanometer = micrometer * 1000
            self.mile = micrometer / 1.609e+9
            self.yard = micrometer / 914400
            self.foot = micrometer / 304800
            self.inch = micrometer / 25400
            self.nautical_mile = micrometer / 1.852e+9
        elif not is_none(nanometer):
            self.kilometer = nanometer / 1e+12
            self.meter = nanometer / 1e+9
            self.centimeter = nanometer / 1e+7
            self.millimeter = nanometer / 1e+6
            self.micrometer = nanometer / 1000
            self.nanometer = nanometer
            self.mile = nanometer / 1.609e+12
            self.yard = nanometer / 9.144e+8
            self.foot = nanometer / 3.048e+8
            self.inch = nanometer / 2.54e+7
            self.nautical_mile = nanometer / 1.852e+12
        elif not is_none(mile):
            self.kilometer = mile * 1.609
            self.meter = mile * 1609
            self.centimeter = mile * 160934
            self.millimeter = mile * 1.609e+6
            self.micrometer = mile * 1.609e+9
            self.nanometer = mile * 1.609e+12
            self.mile = mile
            self.yard = mile * 1760
            self.foot = mile * 5280
            self.inch = mile * 63360
            self.nautical_mile = mile / 1.151
        elif not is_none(yard):
            self.kilometer = yard / 1094
            self.meter = yard / 1.094
            self.centimeter = yard * 91.44
            self.millimeter = yard * 914
            self.micrometer = yard * 914400
            self.nanometer = yard * 9.144e+8
            self.mile = yard / 1760
            self.yard = yard
            self.foot = yard * 3
            self.inch = yard * 36
            self.nautical_mile = yard / 2025
        elif not is_none(foot):
            self.kilometer = foot / 3281
            self.meter = foot / 3.281
            self.centimeter = foot * 30.48
            self.millimeter = foot * 305
            self.micrometer = foot * 304800
            self.nanometer = foot * 3.048e+8
            self.mile = foot / 5280
            self.yard = foot / 3
            self.foot = foot
            self.inch = foot * 12
            self.nautical_mile = foot / 6076
        elif not is_none(inch):
            self.kilometer = inch / 39370
            self.meter = inch / 39.37
            self.centimeter = inch * 2.54
            self.millimeter = inch * 25.4
            self.micrometer = inch * 25400
            self.nanometer = inch * 2.54e+7
            self.mile = inch / 63360
            self.yard = inch / 36
            self.foot = inch / 12
            self.inch = inch
            self.nautical_mile = inch / 72913
        elif not is_none(nautical_mile):
            self.kilometer = nautical_mile * 1.852
            self.meter = nautical_mile * 1852
            self.centimeter = nautical_mile * 185200
            self.millimeter = nautical_mile * 1.852e+6
            self.micrometer = nautical_mile * 1.852e+9
            self.nanometer = nautical_mile * 1.852e+12
            self.mile = nautical_mile * 1.151
            self.yard = nautical_mile * 2025
            self.foot = nautical_mile * 6076
            self.inch = nautical_mile * 72913
            self.nautical_mile = nautical_mile
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    