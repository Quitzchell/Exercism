MINUTES_PER_DAY = 24 * 60

class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (hour * 60 + minute ) % MINUTES_PER_DAY

    @property
    def hours(self):
        return self.total_minutes // 60

    @property
    def minutes(self):
        return self.total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)
