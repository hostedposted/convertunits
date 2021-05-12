from convertunits.utils import is_none, Base

class Data_transfer_rate(Base):
    def __init__(self, bit_per_second = None, kilobit_per_second = None, kilobyte_per_second = None, kibibit_per_second = None, megabit_per_second = None, megabyte_per_second = None, mebibit_per_second = None, gigabit_per_second = None, gigabyte_per_second = None, gibibit_per_second = None, terabit_per_second = None, terabyte_per_second = None, tebibit_per_second = None):
        if not is_none(bit_per_second):
            self.bit_per_second = bit_per_second
            self.kilobit_per_second = bit_per_second / 1000
            self.kilobyte_per_second = bit_per_second / 8000
            self.kibibit_per_second = bit_per_second / 1024
            self.megabit_per_second = bit_per_second / 1e+6
            self.megabyte_per_second = bit_per_second / 8e+6
            self.mebibit_per_second = bit_per_second / 1.049e+6
            self.gigabit_per_second = bit_per_second / 1e+9
            self.gigabyte_per_second = bit_per_second / 8e+9
            self.gibibit_per_second = bit_per_second / 1.074e+9
            self.terabit_per_second = bit_per_second / 1e+12
            self.terabyte_per_second = bit_per_second / 8e+12
            self.tebibit_per_second = bit_per_second / 1.1e+12
        elif not is_none(kilobit_per_second):
            self.bit_per_second = kilobit_per_second * 1000
            self.kilobit_per_second = kilobit_per_second
            self.kilobyte_per_second = kilobit_per_second / 8
            self.kibibit_per_second = kilobit_per_second / 1.024
            self.megabit_per_second = kilobit_per_second / 1000
            self.megabyte_per_second = kilobit_per_second / 8000
            self.mebibit_per_second = kilobit_per_second / 1049
            self.gigabit_per_second = kilobit_per_second / 1e+6
            self.gigabyte_per_second = kilobit_per_second / 8e+6
            self.gibibit_per_second = kilobit_per_second / 1.074e+6
            self.terabit_per_second = kilobit_per_second / 1e+9
            self.terabyte_per_second = kilobit_per_second / 8e+9
            self.tebibit_per_second = kilobit_per_second / 1.1e+9
        elif not is_none(kilobyte_per_second):
            self.bit_per_second = kilobyte_per_second * 8000
            self.kilobit_per_second = kilobyte_per_second * 8
            self.kilobyte_per_second = kilobyte_per_second
            self.kibibit_per_second = kilobyte_per_second * 7.812
            self.megabit_per_second = kilobyte_per_second / 125
            self.megabyte_per_second = kilobyte_per_second / 1000
            self.mebibit_per_second = kilobyte_per_second / 131
            self.gigabit_per_second = kilobyte_per_second / 125000
            self.gigabyte_per_second = kilobyte_per_second / 1e+6
            self.gibibit_per_second = kilobyte_per_second / 134218
            self.terabit_per_second = kilobyte_per_second / 1.25e+8
            self.terabyte_per_second = kilobyte_per_second / 1e+9
            self.tebibit_per_second = kilobyte_per_second / 1.374e+8
        elif not is_none(kibibit_per_second):
            self.bit_per_second = kibibit_per_second * 1024
            self.kilobit_per_second = kibibit_per_second * 1.024
            self.kilobyte_per_second = kibibit_per_second / 7.812
            self.kibibit_per_second = kibibit_per_second
            self.megabit_per_second = kibibit_per_second / 977
            self.megabyte_per_second = kibibit_per_second / 7813
            self.mebibit_per_second = kibibit_per_second / 1024
            self.gigabit_per_second = kibibit_per_second / 976562
            self.gigabyte_per_second = kibibit_per_second / 7.812e+6
            self.gibibit_per_second = kibibit_per_second / 1.049e+6
            self.terabit_per_second = kibibit_per_second / 9.766e+8
            self.terabyte_per_second = kibibit_per_second / 7.812e+9
            self.tebibit_per_second = kibibit_per_second / 1.074e+9
        elif not is_none(megabit_per_second):
            self.bit_per_second = megabit_per_second * 1e+6
            self.kilobit_per_second = megabit_per_second * 1000
            self.kilobyte_per_second = megabit_per_second * 125
            self.kibibit_per_second = megabit_per_second * 977
            self.megabit_per_second = megabit_per_second
            self.megabyte_per_second = megabit_per_second / 8
            self.mebibit_per_second = megabit_per_second / 1.049
            self.gigabit_per_second = megabit_per_second / 1000
            self.gigabyte_per_second = megabit_per_second / 8000
            self.gibibit_per_second = megabit_per_second / 1074
            self.terabit_per_second = megabit_per_second / 1e+6
            self.terabyte_per_second = megabit_per_second / 8e+6
            self.tebibit_per_second = megabit_per_second / 1.1e+6
        elif not is_none(megabyte_per_second):
            self.bit_per_second = megabyte_per_second * 8e+6
            self.kilobit_per_second = megabyte_per_second * 8000
            self.kilobyte_per_second = megabyte_per_second * 1000
            self.kibibit_per_second = megabyte_per_second * 7813
            self.megabit_per_second = megabyte_per_second * 8
            self.megabyte_per_second = megabyte_per_second
            self.mebibit_per_second = megabyte_per_second * 7.629
            self.gigabit_per_second = megabyte_per_second / 125
            self.gigabyte_per_second = megabyte_per_second / 1000
            self.gibibit_per_second = megabyte_per_second / 134
            self.terabit_per_second = megabyte_per_second / 125000
            self.terabyte_per_second = megabyte_per_second / 1e+6
            self.tebibit_per_second = megabyte_per_second / 137439
        elif not is_none(mebibit_per_second):
            self.bit_per_second = mebibit_per_second * 1.049e+6
            self.kilobit_per_second = mebibit_per_second * 1049
            self.kilobyte_per_second = mebibit_per_second * 131
            self.kibibit_per_second = mebibit_per_second * 1024
            self.megabit_per_second = mebibit_per_second * 1.049
            self.megabyte_per_second = mebibit_per_second / 7.629
            self.mebibit_per_second = mebibit_per_second
            self.gigabit_per_second = mebibit_per_second / 954
            self.gigabyte_per_second = mebibit_per_second / 7629
            self.gibibit_per_second = mebibit_per_second / 1024
            self.terabit_per_second = mebibit_per_second / 953674
            self.terabyte_per_second = mebibit_per_second / 7.629e+6
            self.tebibit_per_second = mebibit_per_second / 1.049e+6
        elif not is_none(gigabit_per_second):
            self.bit_per_second = gigabit_per_second / 1100
            self.kilobit_per_second = gigabit_per_second * 1e+6
            self.kilobyte_per_second = gigabit_per_second * 125000
            self.kibibit_per_second = gigabit_per_second * 976563
            self.megabit_per_second = gigabit_per_second * 1000
            self.megabyte_per_second = gigabit_per_second * 125
            self.mebibit_per_second = gigabit_per_second * 954
            self.gigabit_per_second = gigabit_per_second
            self.gigabyte_per_second = gigabit_per_second / 8
            self.gibibit_per_second = gigabit_per_second / 1.074
            self.terabit_per_second = gigabit_per_second / 1000
            self.terabyte_per_second = gigabit_per_second / 8000
            self.tebibit_per_second = gigabit_per_second / 1100
        elif not is_none(gigabyte_per_second):
            self.bit_per_second = gigabyte_per_second * 8e+9
            self.kilobit_per_second = gigabyte_per_second * 8e+6
            self.kilobyte_per_second = gigabyte_per_second * 1e+6
            self.kibibit_per_second = gigabyte_per_second * 7.812e+6
            self.megabit_per_second = gigabyte_per_second * 8000
            self.megabyte_per_second = gigabyte_per_second * 1000
            self.mebibit_per_second = gigabyte_per_second * 7629
            self.gigabit_per_second = gigabyte_per_second * 8
            self.gigabyte_per_second = gigabyte_per_second
            self.gibibit_per_second = gigabyte_per_second * 7.451
            self.terabit_per_second = gigabyte_per_second / 125
            self.terabyte_per_second = gigabyte_per_second / 1000
            self.tebibit_per_second = gigabyte_per_second / 137
        elif not is_none(gibibit_per_second):
            self.bit_per_second = gibibit_per_second * 1.074e+9
            self.kilobit_per_second = gibibit_per_second * 1.074e+6
            self.kilobyte_per_second = gibibit_per_second * 134218
            self.kibibit_per_second = gibibit_per_second * 1.049e+6
            self.megabit_per_second = gibibit_per_second * 1074
            self.megabyte_per_second = gibibit_per_second * 134
            self.mebibit_per_second = gibibit_per_second * 1024
            self.gigabit_per_second = gibibit_per_second * 1.074
            self.gigabyte_per_second = gibibit_per_second / 7.451
            self.gibibit_per_second = gibibit_per_second
            self.terabit_per_second = gibibit_per_second / 931
            self.terabyte_per_second = gibibit_per_second / 7451
            self.tebibit_per_second = gibibit_per_second / 1024
        elif not is_none(terabit_per_second):
            self.bit_per_second = terabit_per_second * 1e+12
            self.kilobit_per_second = terabit_per_second * 1e+9
            self.kilobyte_per_second = terabit_per_second * 1.25e+8
            self.kibibit_per_second = terabit_per_second * 9.766e+8
            self.megabit_per_second = terabit_per_second * 1e+6
            self.megabyte_per_second = terabit_per_second * 125000
            self.mebibit_per_second = terabit_per_second * 953674
            self.gigabit_per_second = terabit_per_second * 1000
            self.gigabyte_per_second = terabit_per_second * 125
            self.gibibit_per_second = terabit_per_second * 931
            self.terabit_per_second = terabit_per_second
            self.terabyte_per_second = terabit_per_second / 8
            self.tebibit_per_second = terabit_per_second / 1.1
        elif not is_none(terabyte_per_second):
            self.bit_per_second = terabyte_per_second * 8e+12
            self.kilobit_per_second = terabyte_per_second * 8e+9
            self.kilobyte_per_second = terabyte_per_second * 1e+9
            self.kibibit_per_second = terabyte_per_second * 7.812e+9
            self.megabit_per_second = terabyte_per_second * 8e+6
            self.megabyte_per_second = terabyte_per_second * 1e+6
            self.mebibit_per_second = terabyte_per_second * 7.629e+6
            self.gigabit_per_second = terabyte_per_second * 8000
            self.gigabyte_per_second = terabyte_per_second * 1000
            self.gibibit_per_second = terabyte_per_second * 7451
            self.terabit_per_second = terabyte_per_second * 8
            self.terabyte_per_second = terabyte_per_second
            self.tebibit_per_second = terabyte_per_second * 7.276
        elif not is_none(tebibit_per_second):
            self.bit_per_second = tebibit_per_second * 1.1e+12
            self.kilobit_per_second = tebibit_per_second * 1.1e+9
            self.kilobyte_per_second = tebibit_per_second * 1.374e+8
            self.kibibit_per_second = tebibit_per_second * 1.074e+9
            self.megabit_per_second = tebibit_per_second * 1.1e+6
            self.megabyte_per_second = tebibit_per_second * 137439
            self.mebibit_per_second = tebibit_per_second * 1.049e+6
            self.gigabit_per_second = tebibit_per_second * 1100
            self.gigabyte_per_second = tebibit_per_second * 137
            self.gibibit_per_second = tebibit_per_second * 1024
            self.terabit_per_second = tebibit_per_second * 1.1
            self.terabyte_per_second = tebibit_per_second / 7.276
            self.tebibit_per_second = tebibit_per_second
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    