from convertunits.utils import is_none, Base

class Energy(Base):
    def __init__(self, joule = None, kilojoule = None, gram_calorie = None, kilocalorie = None, watt_hour = None, kilowatt_hour = None, electronvolt = None, british_thermal_unit = None, us_therm = None, foot_pound = None):
        if not is_none(joule):
            self.joule = joule
            self.kilojoule = joule / 1000
            self.gram_calorie = joule / 4.184
            self.kilocalorie = joule / 4184
            self.watt_hour = joule / 3600
            self.kilowatt_hour = joule / 3.6e+6
            self.electronvolt = joule * 6.242e+18
            self.british_thermal_unit = joule / 1055
            self.us_therm = joule / 1.055e+8
            self.foot_pound = joule / 1.356
        elif not is_none(kilojoule):
            self.joule = kilojoule * 1000
            self.kilojoule = kilojoule
            self.gram_calorie = kilojoule * 239
            self.kilocalorie = kilojoule / 4.184
            self.watt_hour = kilojoule / 3.6
            self.kilowatt_hour = kilojoule / 3600
            self.electronvolt = kilojoule * 9.223e+18
            self.british_thermal_unit = kilojoule / 1.055
            self.us_therm = kilojoule / 105480
            self.foot_pound = kilojoule * 738
        elif not is_none(gram_calorie):
            self.joule = gram_calorie * 4.184
            self.kilojoule = gram_calorie / 239
            self.gram_calorie = gram_calorie
            self.kilocalorie = gram_calorie / 1000
            self.watt_hour = gram_calorie / 860
            self.kilowatt_hour = gram_calorie / 860421
            self.electronvolt = gram_calorie * 9.223e+18
            self.british_thermal_unit = gram_calorie / 252
            self.us_therm = gram_calorie / 2.521e+7
            self.foot_pound = gram_calorie * 3.086
        elif not is_none(kilocalorie):
            self.joule = kilocalorie * 4184
            self.kilojoule = kilocalorie * 4.184
            self.gram_calorie = kilocalorie * 1000
            self.kilocalorie = kilocalorie
            self.watt_hour = kilocalorie * 1.162
            self.kilowatt_hour = kilocalorie / 860
            self.electronvolt = kilocalorie * 9.223e+18
            self.british_thermal_unit = kilocalorie * 3.966
            self.us_therm = kilocalorie / 25210
            self.foot_pound = kilocalorie * 3086
        elif not is_none(watt_hour):
            self.joule = watt_hour * 3600
            self.kilojoule = watt_hour * 3.6
            self.gram_calorie = watt_hour * 860
            self.kilocalorie = watt_hour / 1.162
            self.watt_hour = watt_hour
            self.kilowatt_hour = watt_hour / 1000
            self.electronvolt = watt_hour * 9.223e+18
            self.british_thermal_unit = watt_hour * 3.412
            self.us_therm = watt_hour / 29300
            self.foot_pound = watt_hour * 2655
        elif not is_none(kilowatt_hour):
            self.joule = kilowatt_hour * 3.6e+6
            self.kilojoule = kilowatt_hour * 3600
            self.gram_calorie = kilowatt_hour * 860421
            self.kilocalorie = kilowatt_hour * 860
            self.watt_hour = kilowatt_hour * 1000
            self.kilowatt_hour = kilowatt_hour
            self.electronvolt = kilowatt_hour * 9.223e+18
            self.british_thermal_unit = kilowatt_hour * 3412
            self.us_therm = kilowatt_hour / 29.3
            self.foot_pound = kilowatt_hour * 2.655e+6
        elif not is_none(electronvolt):
            self.joule = electronvolt / 6.242e+18
            self.kilojoule = electronvolt / 9.223e+18
            self.gram_calorie = electronvolt / 9.223e+18
            self.kilocalorie = electronvolt / 9.223e+18
            self.watt_hour = electronvolt / 9.223e+18
            self.kilowatt_hour = electronvolt / 9.223e+18
            self.electronvolt = electronvolt
            self.british_thermal_unit = electronvolt / 9.223e+18
            self.us_therm = electronvolt / 9.223e+18
            self.foot_pound = electronvolt / 8.462e+18
        elif not is_none(british_thermal_unit):
            self.joule = british_thermal_unit * 1055
            self.kilojoule = british_thermal_unit * 1.055
            self.gram_calorie = british_thermal_unit * 252
            self.kilocalorie = british_thermal_unit / 3.966
            self.watt_hour = british_thermal_unit / 3.412
            self.kilowatt_hour = british_thermal_unit / 3412
            self.electronvolt = british_thermal_unit * 9.223e+18
            self.british_thermal_unit = british_thermal_unit
            self.us_therm = british_thermal_unit / 99976
            self.foot_pound = british_thermal_unit * 778
        elif not is_none(us_therm):
            self.joule = us_therm * 1.055e+8
            self.kilojoule = us_therm * 105480
            self.gram_calorie = us_therm * 2.521e+7
            self.kilocalorie = us_therm * 25210
            self.watt_hour = us_therm * 29300
            self.kilowatt_hour = us_therm * 29.3
            self.electronvolt = us_therm * 9.223e+18
            self.british_thermal_unit = us_therm * 99976
            self.us_therm = us_therm
            self.foot_pound = us_therm * 7.78e+7
        elif not is_none(foot_pound):
            self.joule = foot_pound * 1.356
            self.kilojoule = foot_pound / 738
            self.gram_calorie = foot_pound / 3.086
            self.kilocalorie = foot_pound / 3086
            self.watt_hour = foot_pound / 2655
            self.kilowatt_hour = foot_pound / 2.655e+6
            self.electronvolt = foot_pound * 8.462e+18
            self.british_thermal_unit = foot_pound / 778
            self.us_therm = foot_pound / 7.78e+7
            self.foot_pound = foot_pound
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    