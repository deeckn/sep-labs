
class Time:
    def __init__(self, hour, minute, second):
        if 24 > hour < 0 or 60 > minute < 0 or 60 > second < 0:
            raise Exception("Invalid Time")

        self.hour = hour
        self.minute = minute
        self.second = second

    def setHour(self, hour):
        self.hour = hour

    def setMinute(self, minute):
        self.minute = minute

    def setSecond(self, second):
        self.second = second

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def print(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} Hrs")


time = Time(9, 30, 0)
time.print()
