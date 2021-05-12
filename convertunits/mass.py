from convertunits.utils import is_none, Base

class Mass(Base):
    def __init__(self, metric_ton = None, kilogram = None, gram = None, milligram = None, microgram = None, imperial_ton = None, us_ton = None, stone = None, pound = None, ounce = None):
        if not is_none(metric_ton):
            self.metric_ton = metric_ton
            self.kilogram = metric_ton * 1000
            self.gram = metric_ton * 1e+6
            self.milligram = metric_ton * 1e+9
            self.microgram = metric_ton * 1e+12
            self.imperial_ton = metric_ton / 1.016
            self.us_ton = metric_ton * 1.102
            self.stone = metric_ton * 157
            self.pound = metric_ton * 2205
            self.ounce = metric_ton * 35274
        elif not is_none(kilogram):
            self.metric_ton = kilogram / 1000
            self.kilogram = kilogram
            self.gram = kilogram * 1000
            self.milligram = kilogram * 1e+6
            self.microgram = kilogram * 1e+9
            self.imperial_ton = kilogram / 1016
            self.us_ton = kilogram / 907
            self.stone = kilogram / 6.35
            self.pound = kilogram * 2.205
            self.ounce = kilogram * 35.274
        elif not is_none(gram):
            self.metric_ton = gram / 1e+6
            self.kilogram = gram / 1000
            self.gram = gram
            self.milligram = gram * 1000
            self.microgram = gram * 1e+6
            self.imperial_ton = gram / 1.016e+6
            self.us_ton = gram / 907185
            self.stone = gram / 6350
            self.pound = gram / 454
            self.ounce = gram / 28.35
        elif not is_none(milligram):
            self.metric_ton = milligram / 1e+9
            self.kilogram = milligram / 1e+6
            self.gram = milligram / 1000
            self.milligram = milligram
            self.microgram = milligram * 1000
            self.imperial_ton = milligram / 1.016e+9
            self.us_ton = milligram / 9.072e+8
            self.stone = milligram / 6.35e+6
            self.pound = milligram / 453592
            self.ounce = milligram / 28350
        elif not is_none(microgram):
            self.metric_ton = microgram / 1e+12
            self.kilogram = microgram / 1e+9
            self.gram = microgram / 1e+6
            self.milligram = microgram / 1000
            self.microgram = microgram
            self.imperial_ton = microgram / 1.016e+12
            self.us_ton = microgram / 9.072e+11
            self.stone = microgram / 6.35e+9
            self.pound = microgram / 4.536e+8
            self.ounce = microgram / 2.835e+7
        elif not is_none(imperial_ton):
            self.metric_ton = imperial_ton * 1.016
            self.kilogram = imperial_ton * 1016
            self.gram = imperial_ton * 1.016e+6
            self.milligram = imperial_ton * 1.016e+9
            self.microgram = imperial_ton * 1.016e+12
            self.imperial_ton = imperial_ton
            self.us_ton = imperial_ton * 1.12
            self.stone = imperial_ton * 160
            self.pound = imperial_ton * 2240
            self.ounce = imperial_ton * 35840
        elif not is_none(us_ton):
            self.metric_ton = us_ton / 1.102
            self.kilogram = us_ton * 907
            self.gram = us_ton * 907185
            self.milligram = us_ton * 9.072e+8
            self.microgram = us_ton * 9.072e+11
            self.imperial_ton = us_ton / 1.12
            self.us_ton = us_ton
            self.stone = us_ton * 143
            self.pound = us_ton * 2000
            self.ounce = us_ton * 32000
        elif not is_none(stone):
            self.metric_ton = stone / 157
            self.kilogram = stone * 6.35
            self.gram = stone * 6350
            self.milligram = stone * 6.35e+6
            self.microgram = stone * 6.35e+9
            self.imperial_ton = stone / 160
            self.us_ton = stone / 143
            self.stone = stone
            self.pound = stone * 14
            self.ounce = stone * 224
        elif not is_none(pound):
            self.metric_ton = pound / 2205
            self.kilogram = pound / 2.205
            self.gram = pound * 454
            self.milligram = pound * 453592
            self.microgram = pound * 4.536e+8
            self.imperial_ton = pound / 2240
            self.us_ton = pound / 2000
            self.stone = pound / 14
            self.pound = pound
            self.ounce = pound * 16
        elif not is_none(ounce):
            self.metric_ton = ounce / 35274
            self.kilogram = ounce / 35.274
            self.gram = ounce * 28.35
            self.milligram = ounce * 28350
            self.microgram = ounce * 2.835e+7
            self.imperial_ton = ounce / 35840
            self.us_ton = ounce / 32000
            self.stone = ounce / 224
            self.pound = ounce / 16
            self.ounce = ounce
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    