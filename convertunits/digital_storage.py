from convertunits.utils import is_none, Base

class Digital_storage(Base):
    def __init__(self, bit = None, kilobit = None, kibibit = None, megabit = None, mebibit = None, gigabit = None, gibibit = None, terabit = None, tebibit = None, petabit = None, pebibit = None, byte = None, kilobyte = None, kibibyte = None, megabyte = None, mebibyte = None, gigabyte = None, gibibyte = None, terabyte = None, tebibyte = None, petabyte = None, pebibyte = None):
        if not is_none(bit):
            self.bit = bit
            self.kilobit = bit / 1000
            self.kibibit = bit / 1024
            self.megabit = bit / 1e+6
            self.mebibit = bit / 1.049e+6
            self.gigabit = bit / 1e+9
            self.gibibit = bit / 1.074e+9
            self.terabit = bit / 1e+12
            self.tebibit = bit / 1.1e+12
            self.petabit = bit / 1e+15
            self.pebibit = bit / 1.126e+15
            self.byte = bit / 8
            self.kilobyte = bit / 8000
            self.kibibyte = bit / 8192
            self.megabyte = bit / 8e+6
            self.mebibyte = bit / 8.389e+6
            self.gigabyte = bit / 8e+9
            self.gibibyte = bit / 8.59e+9
            self.terabyte = bit / 8e+12
            self.tebibyte = bit / 8.796e+12
            self.petabyte = bit / 8e+15
            self.pebibyte = bit / 9.007e+15
        elif not is_none(kilobit):
            self.bit = kilobit * 1000
            self.kilobit = kilobit
            self.kibibit = kilobit / 1.024
            self.megabit = kilobit / 1000
            self.mebibit = kilobit / 1049
            self.gigabit = kilobit / 1e+6
            self.gibibit = kilobit / 1.074e+6
            self.terabit = kilobit / 1e+9
            self.tebibit = kilobit / 1.1e+9
            self.petabit = kilobit / 1e+12
            self.pebibit = kilobit / 1.126e+12
            self.byte = kilobit * 125
            self.kilobyte = kilobit / 8
            self.kibibyte = kilobit / 8.192
            self.megabyte = kilobit / 8000
            self.mebibyte = kilobit / 8389
            self.gigabyte = kilobit / 8e+6
            self.gibibyte = kilobit / 8.59e+6
            self.terabyte = kilobit / 8e+9
            self.tebibyte = kilobit / 8.796e+9
            self.petabyte = kilobit / 8e+12
            self.pebibyte = kilobit / 9.007e+12
        elif not is_none(kibibit):
            self.bit = kibibit * 1024
            self.kilobit = kibibit * 1.024
            self.kibibit = kibibit
            self.megabit = kibibit / 977
            self.mebibit = kibibit / 1024
            self.gigabit = kibibit / 976562
            self.gibibit = kibibit / 1.049e+6
            self.terabit = kibibit / 9.766e+8
            self.tebibit = kibibit / 1.074e+9
            self.petabit = kibibit / 9.766e+11
            self.pebibit = kibibit / 1.1e+12
            self.byte = kibibit * 128
            self.kilobyte = kibibit / 7.812
            self.kibibyte = kibibit / 8
            self.megabyte = kibibit / 7813
            self.mebibyte = kibibit / 8192
            self.gigabyte = kibibit / 7.812e+6
            self.gibibyte = kibibit / 8.389e+6
            self.terabyte = kibibit / 7.812e+9
            self.tebibyte = kibibit / 8.59e+9
            self.petabyte = kibibit / 7.812e+12
            self.pebibyte = kibibit / 8.796e+12
        elif not is_none(megabit):
            self.bit = megabit * 1e+6
            self.kilobit = megabit * 1000
            self.kibibit = megabit * 977
            self.megabit = megabit
            self.mebibit = megabit / 1.049
            self.gigabit = megabit / 1000
            self.gibibit = megabit / 1074
            self.terabit = megabit / 1e+6
            self.tebibit = megabit / 1.1e+6
            self.petabit = megabit / 1e+9
            self.pebibit = megabit / 1.126e+9
            self.byte = megabit * 125000
            self.kilobyte = megabit * 125
            self.kibibyte = megabit * 122
            self.megabyte = megabit / 8
            self.mebibyte = megabit / 8.389
            self.gigabyte = megabit / 8000
            self.gibibyte = megabit / 8590
            self.terabyte = megabit / 8e+6
            self.tebibyte = megabit / 8.796e+6
            self.petabyte = megabit / 8e+9
            self.pebibyte = megabit / 9.007e+9
        elif not is_none(mebibit):
            self.bit = mebibit * 1.049e+6
            self.kilobit = mebibit * 1049
            self.kibibit = mebibit * 1024
            self.megabit = mebibit * 1.049
            self.mebibit = mebibit
            self.gigabit = mebibit / 954
            self.gibibit = mebibit / 1024
            self.terabit = mebibit / 953674
            self.tebibit = mebibit / 1.049e+6
            self.petabit = mebibit / 9.537e+8
            self.pebibit = mebibit / 1.074e+9
            self.byte = mebibit * 131072
            self.kilobyte = mebibit * 131
            self.kibibyte = mebibit * 128
            self.megabyte = mebibit / 7.629
            self.mebibyte = mebibit / 8
            self.gigabyte = mebibit / 7629
            self.gibibyte = mebibit / 8192
            self.terabyte = mebibit / 7.629e+6
            self.tebibyte = mebibit / 8.389e+6
            self.petabyte = mebibit / 7.629e+9
            self.pebibyte = mebibit / 8.59e+9
        elif not is_none(gigabit):
            self.bit = gigabit * 1e+9
            self.kilobit = gigabit * 1e+6
            self.kibibit = gigabit * 976563
            self.megabit = gigabit * 1000
            self.mebibit = gigabit * 954
            self.gigabit = gigabit
            self.gibibit = gigabit / 1.074
            self.terabit = gigabit / 1000
            self.tebibit = gigabit / 1100
            self.petabit = gigabit / 1e+6
            self.pebibit = gigabit / 1.126e+6
            self.byte = gigabit * 1.25e+8
            self.kilobyte = gigabit * 125000
            self.kibibyte = gigabit * 122070
            self.megabyte = gigabit * 125
            self.mebibyte = gigabit * 119
            self.gigabyte = gigabit / 8
            self.gibibyte = gigabit / 8.59
            self.terabyte = gigabit / 8000
            self.tebibyte = gigabit / 8796
            self.petabyte = gigabit / 8e+6
            self.pebibyte = gigabit / 9.007e+6
        elif not is_none(gibibit):
            self.bit = gibibit * 1.074e+9
            self.kilobit = gibibit * 1.074e+6
            self.kibibit = gibibit * 1.049e+6
            self.megabit = gibibit * 1074
            self.mebibit = gibibit * 1024
            self.gigabit = gibibit * 1.074
            self.gibibit = gibibit
            self.terabit = gibibit / 931
            self.tebibit = gibibit / 1024
            self.petabit = gibibit / 931323
            self.pebibit = gibibit / 1.049e+6
            self.byte = gibibit * 1.342e+8
            self.kilobyte = gibibit * 134218
            self.kibibyte = gibibit * 131072
            self.megabyte = gibibit * 134
            self.mebibyte = gibibit * 128
            self.gigabyte = gibibit / 7.451
            self.gibibyte = gibibit / 8
            self.terabyte = gibibit / 7451
            self.tebibyte = gibibit / 8192
            self.petabyte = gibibit / 7.451e+6
            self.pebibyte = gibibit / 8.389e+6
        elif not is_none(terabit):
            self.bit = terabit * 1e+12
            self.kilobit = terabit * 1e+9
            self.kibibit = terabit * 9.766e+8
            self.megabit = terabit * 1e+6
            self.mebibit = terabit * 953674
            self.gigabit = terabit * 1000
            self.gibibit = terabit * 931
            self.terabit = terabit
            self.tebibit = terabit / 1.1
            self.petabit = terabit / 1000
            self.pebibit = terabit / 1126
            self.byte = terabit * 1.25e+11
            self.kilobyte = terabit * 1.25e+8
            self.kibibyte = terabit * 1.221e+8
            self.megabyte = terabit * 125000
            self.mebibyte = terabit * 119209
            self.gigabyte = terabit * 125
            self.gibibyte = terabit * 116
            self.terabyte = terabit / 8
            self.tebibyte = terabit / 8.796
            self.petabyte = terabit / 8000
            self.pebibyte = terabit / 9007
        elif not is_none(tebibit):
            self.bit = tebibit * 1.1e+12
            self.kilobit = tebibit * 1.1e+9
            self.kibibit = tebibit * 1.074e+9
            self.megabit = tebibit * 1.1e+6
            self.mebibit = tebibit * 1.049e+6
            self.gigabit = tebibit * 1100
            self.gibibit = tebibit * 1024
            self.terabit = tebibit * 1.1
            self.tebibit = tebibit
            self.petabit = tebibit / 909
            self.pebibit = tebibit / 1024
            self.byte = tebibit * 1.374e+11
            self.kilobyte = tebibit * 1.374e+8
            self.kibibyte = tebibit * 1.342e+8
            self.megabyte = tebibit * 137439
            self.mebibyte = tebibit * 131072
            self.gigabyte = tebibit * 137
            self.gibibyte = tebibit * 128
            self.terabyte = tebibit / 7.276
            self.tebibyte = tebibit / 8
            self.petabyte = tebibit / 7276
            self.pebibyte = tebibit / 8192
        elif not is_none(petabit):
            self.bit = petabit * 1e+15
            self.kilobit = petabit * 1e+12
            self.kibibit = petabit * 9.766e+11
            self.megabit = petabit * 1e+9
            self.mebibit = petabit * 9.537e+8
            self.gigabit = petabit * 1e+6
            self.gibibit = petabit * 931323
            self.terabit = petabit * 1000
            self.tebibit = petabit * 909
            self.petabit = petabit
            self.pebibit = petabit / 1.126
            self.byte = petabit * 1.25e+14
            self.kilobyte = petabit * 1.25e+11
            self.kibibyte = petabit * 1.221e+11
            self.megabyte = petabit * 1.25e+8
            self.mebibyte = petabit * 1.192e+8
            self.gigabyte = petabit * 125000
            self.gibibyte = petabit * 116415
            self.terabyte = petabit * 125
            self.tebibyte = petabit * 114
            self.petabyte = petabit / 8
            self.pebibyte = petabit / 9.007
        elif not is_none(pebibit):
            self.bit = pebibit * 1.126e+15
            self.kilobit = pebibit * 1.126e+12
            self.kibibit = pebibit * 1.1e+12
            self.megabit = pebibit * 1.126e+9
            self.mebibit = pebibit * 1.074e+9
            self.gigabit = pebibit * 1.126e+6
            self.gibibit = pebibit * 1.049e+6
            self.terabit = pebibit * 1126
            self.tebibit = pebibit * 1024
            self.petabit = pebibit * 1.126
            self.pebibit = pebibit
            self.byte = pebibit * 1.407e+14
            self.kilobyte = pebibit * 1.407e+11
            self.kibibyte = pebibit * 1.374e+11
            self.megabyte = pebibit * 1.407e+8
            self.mebibyte = pebibit * 1.342e+8
            self.gigabyte = pebibit * 140737
            self.gibibyte = pebibit * 131072
            self.terabyte = pebibit * 141
            self.tebibyte = pebibit * 128
            self.petabyte = pebibit / 7.105
            self.pebibyte = pebibit / 8
        elif not is_none(byte):
            self.bit = byte * 8
            self.kilobit = byte / 125
            self.kibibit = byte / 128
            self.megabit = byte / 125000
            self.mebibit = byte / 131072
            self.gigabit = byte / 1.25e+8
            self.gibibit = byte / 1.342e+8
            self.terabit = byte / 1.25e+11
            self.tebibit = byte / 1.374e+11
            self.petabit = byte / 1.25e+14
            self.pebibit = byte / 1.407e+14
            self.byte = byte
            self.kilobyte = byte / 1000
            self.kibibyte = byte / 1024
            self.megabyte = byte / 1e+6
            self.mebibyte = byte / 1.049e+6
            self.gigabyte = byte / 1e+9
            self.gibibyte = byte / 1.074e+9
            self.terabyte = byte / 1e+12
            self.tebibyte = byte / 1.1e+12
            self.petabyte = byte / 1e+15
            self.pebibyte = byte / 1.126e+15
        elif not is_none(kilobyte):
            self.bit = kilobyte * 8000
            self.kilobit = kilobyte * 8
            self.kibibit = kilobyte * 7.812
            self.megabit = kilobyte / 125
            self.mebibit = kilobyte / 131
            self.gigabit = kilobyte / 125000
            self.gibibit = kilobyte / 134218
            self.terabit = kilobyte / 1.25e+8
            self.tebibit = kilobyte / 1.374e+8
            self.petabit = kilobyte / 1.25e+11
            self.pebibit = kilobyte / 1.407e+11
            self.byte = kilobyte * 1000
            self.kilobyte = kilobyte
            self.kibibyte = kilobyte / 1.024
            self.megabyte = kilobyte / 1000
            self.mebibyte = kilobyte / 1049
            self.gigabyte = kilobyte / 1e+6
            self.gibibyte = kilobyte / 1.074e+6
            self.terabyte = kilobyte / 1e+9
            self.tebibyte = kilobyte / 1.1e+9
            self.petabyte = kilobyte / 1e+12
            self.pebibyte = kilobyte / 1.126e+12
        elif not is_none(kibibyte):
            self.bit = kibibyte * 8192
            self.kilobit = kibibyte * 8.192
            self.kibibit = kibibyte * 8
            self.megabit = kibibyte / 122
            self.mebibit = kibibyte / 128
            self.gigabit = kibibyte / 122070
            self.gibibit = kibibyte / 131072
            self.terabit = kibibyte / 1.221e+8
            self.tebibit = kibibyte / 1.342e+8
            self.petabit = kibibyte / 1.221e+11
            self.pebibit = kibibyte / 1.374e+11
            self.byte = kibibyte * 1024
            self.kilobyte = kibibyte * 1.024
            self.kibibyte = kibibyte
            self.megabyte = kibibyte / 977
            self.mebibyte = kibibyte / 1024
            self.gigabyte = kibibyte / 976562
            self.gibibyte = kibibyte / 1.049e+6
            self.terabyte = kibibyte / 9.766e+8
            self.tebibyte = kibibyte / 1.074e+9
            self.petabyte = kibibyte / 9.766e+11
            self.pebibyte = kibibyte / 1.1e+12
        elif not is_none(megabyte):
            self.bit = megabyte * 8e+6
            self.kilobit = megabyte * 8000
            self.kibibit = megabyte * 7813
            self.megabit = megabyte * 8
            self.mebibit = megabyte * 7.629
            self.gigabit = megabyte / 125
            self.gibibit = megabyte / 134
            self.terabit = megabyte / 125000
            self.tebibit = megabyte / 137439
            self.petabit = megabyte / 1.25e+8
            self.pebibit = megabyte / 1.407e+8
            self.byte = megabyte * 1e+6
            self.kilobyte = megabyte * 1000
            self.kibibyte = megabyte * 977
            self.megabyte = megabyte
            self.mebibyte = megabyte / 1.049
            self.gigabyte = megabyte / 1000
            self.gibibyte = megabyte / 1074
            self.terabyte = megabyte / 1e+6
            self.tebibyte = megabyte / 1.1e+6
            self.petabyte = megabyte / 1e+9
            self.pebibyte = megabyte / 1.126e+9
        elif not is_none(mebibyte):
            self.bit = mebibyte * 8.389e+6
            self.kilobit = mebibyte * 8389
            self.kibibit = mebibyte * 8192
            self.megabit = mebibyte * 8.389
            self.mebibit = mebibyte * 8
            self.gigabit = mebibyte / 119
            self.gibibit = mebibyte / 128
            self.terabit = mebibyte / 119209
            self.tebibit = mebibyte / 131072
            self.petabit = mebibyte / 1.192e+8
            self.pebibit = mebibyte / 1.342e+8
            self.byte = mebibyte * 1.049e+6
            self.kilobyte = mebibyte * 1049
            self.kibibyte = mebibyte * 1024
            self.megabyte = mebibyte * 1.049
            self.mebibyte = mebibyte
            self.gigabyte = mebibyte / 954
            self.gibibyte = mebibyte / 1024
            self.terabyte = mebibyte / 953674
            self.tebibyte = mebibyte / 1.049e+6
            self.petabyte = mebibyte / 9.537e+8
            self.pebibyte = mebibyte / 1.074e+9
        elif not is_none(gigabyte):
            self.bit = gigabyte * 8e+9
            self.kilobit = gigabyte * 8e+6
            self.kibibit = gigabyte * 7.812e+6
            self.megabit = gigabyte * 8000
            self.mebibit = gigabyte * 7629
            self.gigabit = gigabyte * 8
            self.gibibit = gigabyte * 7.451
            self.terabit = gigabyte / 125
            self.tebibit = gigabyte / 137
            self.petabit = gigabyte / 125000
            self.pebibit = gigabyte / 140737
            self.byte = gigabyte * 1e+9
            self.kilobyte = gigabyte * 1e+6
            self.kibibyte = gigabyte * 976563
            self.megabyte = gigabyte * 1000
            self.mebibyte = gigabyte * 954
            self.gigabyte = gigabyte
            self.gibibyte = gigabyte / 1.074
            self.terabyte = gigabyte / 1000
            self.tebibyte = gigabyte / 1100
            self.petabyte = gigabyte / 1e+6
            self.pebibyte = gigabyte / 1.126e+6
        elif not is_none(gibibyte):
            self.bit = gibibyte * 8.59e+9
            self.kilobit = gibibyte * 8.59e+6
            self.kibibit = gibibyte * 8.389e+6
            self.megabit = gibibyte * 8590
            self.mebibit = gibibyte * 8192
            self.gigabit = gibibyte * 8.59
            self.gibibit = gibibyte * 8
            self.terabit = gibibyte / 116
            self.tebibit = gibibyte / 128
            self.petabit = gibibyte / 116415
            self.pebibit = gibibyte / 131072
            self.byte = gibibyte * 1.074e+9
            self.kilobyte = gibibyte * 1.074e+6
            self.kibibyte = gibibyte * 1.049e+6
            self.megabyte = gibibyte * 1074
            self.mebibyte = gibibyte * 1024
            self.gigabyte = gibibyte * 1.074
            self.gibibyte = gibibyte
            self.terabyte = gibibyte / 931
            self.tebibyte = gibibyte / 1024
            self.petabyte = gibibyte / 931323
            self.pebibyte = gibibyte / 1.049e+6
        elif not is_none(terabyte):
            self.bit = terabyte * 8e+12
            self.kilobit = terabyte * 8e+9
            self.kibibit = terabyte * 7.812e+9
            self.megabit = terabyte * 8e+6
            self.mebibit = terabyte * 7.629e+6
            self.gigabit = terabyte * 8000
            self.gibibit = terabyte * 7451
            self.terabit = terabyte * 8
            self.tebibit = terabyte * 7.276
            self.petabit = terabyte / 125
            self.pebibit = terabyte / 141
            self.byte = terabyte * 1e+12
            self.kilobyte = terabyte * 1e+9
            self.kibibyte = terabyte * 9.766e+8
            self.megabyte = terabyte * 1e+6
            self.mebibyte = terabyte * 953674
            self.gigabyte = terabyte * 1000
            self.gibibyte = terabyte * 931
            self.terabyte = terabyte
            self.tebibyte = terabyte / 1.1
            self.petabyte = terabyte / 1000
            self.pebibyte = terabyte / 1126
        elif not is_none(tebibyte):
            self.bit = tebibyte * 8.796e+12
            self.kilobit = tebibyte * 8.796e+9
            self.kibibit = tebibyte * 8.59e+9
            self.megabit = tebibyte * 8.796e+6
            self.mebibit = tebibyte * 8.389e+6
            self.gigabit = tebibyte * 8796
            self.gibibit = tebibyte * 8192
            self.terabit = tebibyte * 8.796
            self.tebibit = tebibyte * 8
            self.petabit = tebibyte / 114
            self.pebibit = tebibyte / 128
            self.byte = tebibyte * 1.1e+12
            self.kilobyte = tebibyte * 1.1e+9
            self.kibibyte = tebibyte * 1.074e+9
            self.megabyte = tebibyte * 1.1e+6
            self.mebibyte = tebibyte * 1.049e+6
            self.gigabyte = tebibyte * 1100
            self.gibibyte = tebibyte * 1024
            self.terabyte = tebibyte * 1.1
            self.tebibyte = tebibyte
            self.petabyte = tebibyte / 909
            self.pebibyte = tebibyte / 1024
        elif not is_none(petabyte):
            self.bit = petabyte * 8e+15
            self.kilobit = petabyte * 8e+12
            self.kibibit = petabyte * 7.812e+12
            self.megabit = petabyte * 8e+9
            self.mebibit = petabyte * 7.629e+9
            self.gigabit = petabyte * 8e+6
            self.gibibit = petabyte * 7.451e+6
            self.terabit = petabyte * 8000
            self.tebibit = petabyte * 7276
            self.petabit = petabyte * 8
            self.pebibit = petabyte * 7.105
            self.byte = petabyte * 1e+15
            self.kilobyte = petabyte * 1e+12
            self.kibibyte = petabyte * 9.766e+11
            self.megabyte = petabyte * 1e+9
            self.mebibyte = petabyte * 9.537e+8
            self.gigabyte = petabyte * 1e+6
            self.gibibyte = petabyte * 931323
            self.terabyte = petabyte * 1000
            self.tebibyte = petabyte * 909
            self.petabyte = petabyte
            self.pebibyte = petabyte / 1.126
        elif not is_none(pebibyte):
            self.bit = pebibyte * 9.007e+15
            self.kilobit = pebibyte * 9.007e+12
            self.kibibit = pebibyte * 8.796e+12
            self.megabit = pebibyte * 9.007e+9
            self.mebibit = pebibyte * 8.59e+9
            self.gigabit = pebibyte * 9.007e+6
            self.gibibit = pebibyte * 8.389e+6
            self.terabit = pebibyte * 9007
            self.tebibit = pebibyte * 8192
            self.petabit = pebibyte * 9.007
            self.pebibit = pebibyte * 8
            self.byte = pebibyte * 1.126e+15
            self.kilobyte = pebibyte * 1.126e+12
            self.kibibyte = pebibyte * 1.1e+12
            self.megabyte = pebibyte * 1.126e+9
            self.mebibyte = pebibyte * 1.074e+9
            self.gigabyte = pebibyte * 1.126e+6
            self.gibibyte = pebibyte * 1.049e+6
            self.terabyte = pebibyte * 1126
            self.tebibyte = pebibyte * 1024
            self.petabyte = pebibyte * 1.126
            self.pebibyte = pebibyte
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    