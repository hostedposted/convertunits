from convertunits.utils import is_none, Base

class Time(Base):
    def __init__(self, nanosecond = None, microsecond = None, millisecond = None, second = None, minute = None, hour = None, day = None, week = None, month = None, calendar_year = None, decade = None, century = None):
        if not is_none(nanosecond):
            self.nanosecond = nanosecond
            self.microsecond = nanosecond / 1000
            self.millisecond = nanosecond / 1e+6
            self.second = nanosecond / 1e+9
            self.minute = nanosecond / 6e+10
            self.hour = nanosecond / 3.6e+12
            self.day = nanosecond / 8.64e+13
            self.week = nanosecond / 6.048e+14
            self.month = nanosecond / 2.628e+15
            self.calendar_year = nanosecond / 3.154e+16
            self.decade = nanosecond / 3.154e+17
            self.century = nanosecond / 3.154e+18
        elif not is_none(microsecond):
            self.nanosecond = microsecond * 1000
            self.microsecond = microsecond
            self.millisecond = microsecond / 1000
            self.second = microsecond / 1e+6
            self.minute = microsecond / 6e+7
            self.hour = microsecond / 3.6e+9
            self.day = microsecond / 8.64e+10
            self.week = microsecond / 6.048e+11
            self.month = microsecond / 2.628e+12
            self.calendar_year = microsecond / 3.154e+13
            self.decade = microsecond / 3.154e+14
            self.century = microsecond / 3.154e+15
        elif not is_none(millisecond):
            self.nanosecond = millisecond * 1e+6
            self.microsecond = millisecond * 1000
            self.millisecond = millisecond
            self.second = millisecond / 1000
            self.minute = millisecond / 60000
            self.hour = millisecond / 3.6e+6
            self.day = millisecond / 8.64e+7
            self.week = millisecond / 6.048e+8
            self.month = millisecond / 2.628e+9
            self.calendar_year = millisecond / 3.154e+10
            self.decade = millisecond / 3.154e+11
            self.century = millisecond / 3.154e+12
        elif not is_none(second):
            self.nanosecond = second * 1e+9
            self.microsecond = second * 1e+6
            self.millisecond = second * 1000
            self.second = second
            self.minute = second / 60
            self.hour = second / 3600
            self.day = second / 86400
            self.week = second / 604800
            self.month = second / 2.628e+6
            self.calendar_year = second / 3.154e+7
            self.decade = second / 3.154e+8
            self.century = second / 3.154e+9
        elif not is_none(minute):
            self.nanosecond = minute * 6e+10
            self.microsecond = minute * 6e+7
            self.millisecond = minute * 60000
            self.second = minute * 60
            self.minute = minute
            self.hour = minute / 60
            self.day = minute / 1440
            self.week = minute / 10080
            self.month = minute / 43800
            self.calendar_year = minute / 525600
            self.decade = minute / 5.256e+6
            self.century = minute / 5.256e+7
        elif not is_none(hour):
            self.nanosecond = hour * 3.6e+12
            self.microsecond = hour * 3.6e+9
            self.millisecond = hour * 3.6e+6
            self.second = hour * 3600
            self.minute = hour * 60
            self.hour = hour
            self.day = hour / 24
            self.week = hour / 168
            self.month = hour / 730
            self.calendar_year = hour / 8760
            self.decade = hour / 87600
            self.century = hour / 876000
        elif not is_none(day):
            self.nanosecond = day * 8.64e+13
            self.microsecond = day * 8.64e+10
            self.millisecond = day * 8.64e+7
            self.second = day * 86400
            self.minute = day * 1440
            self.hour = day * 24
            self.day = day
            self.week = day / 7
            self.month = day / 30.417
            self.calendar_year = day / 365
            self.decade = day / 3650
            self.century = day / 36500
        elif not is_none(week):
            self.nanosecond = week * 6.048e+14
            self.microsecond = week * 6.048e+11
            self.millisecond = week * 6.048e+8
            self.second = week * 604800
            self.minute = week * 10080
            self.hour = week * 168
            self.day = week * 7
            self.week = week
            self.month = week / 4.345
            self.calendar_year = week / 52.143
            self.decade = week / 521
            self.century = week / 5214
        elif not is_none(month):
            self.nanosecond = month * 2.628e+15
            self.microsecond = month * 2.628e+12
            self.millisecond = month * 2.628e+9
            self.second = month * 2.628e+6
            self.minute = month * 43800
            self.hour = month * 730
            self.day = month * 30.417
            self.week = month * 4.345
            self.month = month
            self.calendar_year = month / 12
            self.decade = month / 120
            self.century = month / 1200
        elif not is_none(calendar_year):
            self.nanosecond = calendar_year * 3.154e+16
            self.microsecond = calendar_year * 3.154e+13
            self.millisecond = calendar_year * 3.154e+10
            self.second = calendar_year * 3.154e+7
            self.minute = calendar_year * 525600
            self.hour = calendar_year * 8760
            self.day = calendar_year * 365
            self.week = calendar_year * 52.143
            self.month = calendar_year * 12
            self.calendar_year = calendar_year
            self.decade = calendar_year / 10
            self.century = calendar_year / 100
        elif not is_none(decade):
            self.nanosecond = decade * 3.154e+17
            self.microsecond = decade * 3.154e+14
            self.millisecond = decade * 3.154e+11
            self.second = decade * 3.154e+8
            self.minute = decade * 5.256e+6
            self.hour = decade * 87600
            self.day = decade * 3650
            self.week = decade * 521
            self.month = decade * 120
            self.calendar_year = decade * 10
            self.decade = decade
            self.century = decade / 10
        elif not is_none(century):
            self.nanosecond = century * 3.154e+18
            self.microsecond = century * 3.154e+15
            self.millisecond = century * 3.154e+12
            self.second = century * 3.154e+9
            self.minute = century * 5.256e+7
            self.hour = century * 876000
            self.day = century * 36500
            self.week = century * 5214
            self.month = century * 1200
            self.calendar_year = century * 100
            self.decade = century * 10
            self.century = century
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    