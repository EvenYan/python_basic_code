class Clock:
    def __init__(self, hour=10, minute=10, second=10):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        print("打印当前时间：")
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)
    
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
            
            
class Calendar:
    def __init__(self, year=1980, month=10, day=10):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print("打印当前日历：")
        return "%d-%02d-%02d" % (self.year, self.month, self.day)
    
    def next_day(self):
        self.day += 1
        if self.day == 31:
            self.day = 1
            self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
            
class CalendarClock(Calendar, Clock):
    def __init__(self, year, month, day, hour, minute, second):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hour, minute, second)
    
    def __str__(self):
        return Calendar.__str__(self) + " " + Clock.__str__(self)
    
    def tick(self):
        Clock.tick(self)
        if self.hour == 0:
            Calendar.next_day(self)
            
canlendar_clock = CalendarClock(2019, 12, 30, 23, 59, 59)
print(canlendar_clock)
canlendar_clock.tick()
print(canlendar_clock)
