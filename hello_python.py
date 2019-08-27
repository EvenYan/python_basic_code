class Clock:
    def __init__(self, hour=10, minute=10, second=10):
        self.hour = hour
        self.minute = minute
        self.second = second
    
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
        
    def __str__(self):
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)


class Calendar:
    def __init__(self, year=1990, month=10, day=10):
        self.year = year
        self.month = month
        self.day = day

    def next_day(self):
        self.day += 1
        if self.day == 31:
            self.day = 1
            self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        
    def __str__(self):
        return "%d-%02d-%02d" % (self.year, self.month, self.day)
    
    
class ClockCalendar(Clock, Calendar):
    def __init__(self, year, month, day, hour, minute, second):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, year, month, day)
        print("*"*50)
        print(self.year, self.month, self.day)
    
    def __str__(self):
        print("当前时间是：")
        return Calendar.__str__(self) + " " + \
                Clock.__str__(self)
    
    def tick(self):
        Clock.tick(self)
        if self.hour == 0 and self.minute==0 and self.second==0:
            Calendar.next_day(self)
    
    
if __name__ == "__main__":
    clock = Clock(12, 59, 59)
    print(clock)
    clock.tick()
    print(clock)
    calendar = Calendar()
    calendar.next_day()
    calendar.next_day()
    print(calendar)
    calendar_clock = ClockCalendar(1998, 12, 30, 23, 59, 59)
    print(calendar_clock)
    calendar_clock.tick()
    print(calendar_clock)
