from TimeType import *
# Lukas Graig
# A class to set and get calender days

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Clock(TimeType):
    def __init__(self):
        super().__init__()
        self.__years = 1980
        self.__months = 1
        self.__days = 1

    def leapyear(self, leapyear): # A function to check if a year is a leapyear
        if leapyear % 400 == 0 or leapyear % 4 == 0 and leapyear % 100 == 0:
            month[1] = 29
            return True
        else:
            month[1] = 28
            return False

    def setClock(self, hour, minute, second, years, months, days):
        self.leapyear(years)
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
            if 1900 <= years <= 2100 and 1 <= months <= 12 and 1 <= days <= month[months-1]:
                super().set_time(hour, minute, second)
                self.__years = years
                self.__months = months
                self.__days = days
                return True
            else:
                return False
        else:
            return False

    def increaseDay(self):
        self.leapyear(self.__years)
        self.__days += 1
        if self.__days == month[self.__months - 1] + 1:
            self.__days = 1
            self.__months += 1
            if self.__months == 13:
                self.__months = 1
                self.__years += 1
                if self.__years == 2101:
                    self.__years = 1900

    def decreaseDay(self):
        self.leapyear(self.__years)
        self.__days -= 1
        if self.__days == 0:
            self.__days = month[self.__months - 1]
            self.__months -= 1
            if self.__months == 0:
                self.__months = 12
                self.__years -= 1
                if self.__years == 1899:
                    self.__years = 2100

    def increaseSecond(self):
        self.leapyear(self.__years)
        super().increase_second()
        if super().get_hours() == 0 and super().get_minutes() == 0 and super().get_seconds() == 0:
            self.__days += 1
            if self.__days == month[self.__months - 1] + 1:
                self.__days = 1
                self.__months += 1
                if self.__months == 13:
                    self.__months = 1
                    self.__years += 1
                    if self.__years == 2101:
                        self.__years = 1900

    def decreaseSecond(self):
        self.leapyear(self.__years)
        super().decrease_second()
        if super().get_hours() == 23 and super().get_minutes() == 59 and super().get_seconds() == 59:
            self.__days -= 1
            if self.__days == 0:
                self.__days = month[self.__months - 1]
                self.__months -= 1
                if self.__months == 0:
                    self.__months = 12
                    self.__years -= 1
                    if self.__years == 1899:
                        self.__years = 2100

    def __str__(self):
        return (f"The time is {super().__str__()} and it is {self.__months:02d}/{self.__days:02d}/{self.__years}")
