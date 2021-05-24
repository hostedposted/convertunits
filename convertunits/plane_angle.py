from convertunits.utils import is_none, Base

class Plane_angle(Base):
    def __init__(self, degree = None, gradian = None, milliradian = None, minute_of_arc = None, radian = None, second_of_arc = None):
        if not is_none(degree):
            self.degree = degree
            self.gradian = degree * 200/180
            self.milliradian = degree * 1000*pi/180
            self.minute_of_arc = degree * 60
            self.radian = degree * pi/180
            self.second_of_arc = degree * 3600
        elif not is_none(gradian):
            self.degree = gradian * 180/200
            self.gradian = gradian
            self.milliradian = gradian * 1000*pi/200
            self.minute_of_arc = gradian * 54
            self.radian = gradian * pi/200
            self.second_of_arc = gradian * 3240
        elif not is_none(milliradian):
            self.degree = milliradian * (3600 * 180)/1000*pi
            self.gradian = milliradian * 200/1000*pi
            self.milliradian = milliradian
            self.minute_of_arc = milliradian * (60 * 180)/1000*pi
            self.radian = milliradian / 1000
            self.second_of_arc = milliradian * (3600 * 180)/1000*pi
        elif not is_none(minute_of_arc):
            self.degree = minute_of_arc / 60
            self.gradian = minute_of_arc / 54
            self.milliradian = minute_of_arc * 1000*pi/(60 * 180)
            self.minute_of_arc = minute_of_arc
            self.radian = minute_of_arc * pi/(60 * 180)
            self.second_of_arc = minute_of_arc * 60
        elif not is_none(radian):
            self.degree = radian * 180/pi
            self.gradian = radian * 200/pi
            self.milliradian = radian * 1000
            self.minute_of_arc = radian * (60 * 180)/pi
            self.radian = radian
            self.second_of_arc = radian * (3600 * 180)/pi
        elif not is_none(second_of_arc):
            self.degree = second_of_arc / 3600
            self.gradian = second_of_arc / 3240
            self.milliradian = second_of_arc * 1000*pi/(180 * 3600)
            self.minute_of_arc = second_of_arc / 60
            self.radian = second_of_arc * pi/(180 * 3600)
            self.second_of_arc = second_of_arc
        else:
            raise TypeError(f"{self.__class__.__name__} expected 1 argument.")
    