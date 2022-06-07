# Lukas Graig
# A class to set and get time

class TimeType:
    def __init__(self):
        self.__hours = 0            # Private variables
        self.__minutes = 0
        self.__seconds = 0

    def get_hours(self):
        return self.__hours

    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds

    def set_hours(self, hour):
        if 0 <= hour <= 23:         # Check to make sure time is valid
            self.__hours = hour
            return True
        else:
            return False

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self.__minutes = minute
            return True
        else:
            return False

    def set_seconds(self, second):
        if 0 <= second <= 59:
            self.__seconds = second
            return True
        else:
            return False

    def set_time(self, hour, minute, second):
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
            self.__hours = hour
            self.__minutes = minute
            self.__seconds = second
            return True
        else:
            return False

    def increase_second(self):
        self.__seconds += 1 # Nested ifs to check if time needs to be changed
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def decrease_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

    def __str__(self): #Print function
        if 13 <= self.__hours < 24:
            return (f"{(self.__hours - 12):02d}:{self.__minutes:02d}:{self.__seconds:02} PM")
        elif self.__hours == 12:
            return (f"{(self.__hours):02d}:{self.__minutes:02d}:{self.__seconds:02} PM")
        elif self.__hours == 0:
            return (f"{(self.__hours + 12):02d}:{self.__minutes:02d}:{self.__seconds:02} AM")
        else:
            return (f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02} AM")

