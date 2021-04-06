class Clock:
    def __init__(self, hour, minute):
        self.m = minute % 60
        self.h = (hour+minute//60)%24

    def __repr__(self):
        return '{:0>2d}:{:0>2d}'.format(self.h, self.m)

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        temp_m = self.m + minutes + (self.h * 60)
        self.m = temp_m % 60
        self.h = (temp_m // 60) % 24
        return self

    def __sub__(self, minutes):
        temp_m = self.m - minutes + (self.h * 60)
        self.m = temp_m % 60
        self.h = (temp_m // 60) % 24
        return self
        
        
if __name__ == '__main__':

    print(str(Clock(8, 0)))