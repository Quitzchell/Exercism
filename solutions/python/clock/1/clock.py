from datetime import datetime, timedelta


class Clock:
    def __init__(self, hour, minute):
        if minute >= 60:
            plus_hours = minute // 60
            minute = minute % 60
            hour += plus_hours

        if minute < 0:
            minus_hours = minute // 60
            minute = minute % 60
            hour += minus_hours
            
        hour = hour % 24
        
        self.time = datetime.now().replace(hour=hour, minute=minute)

    def __repr__(self):
        hour = self.time.hour
        minute = self.time.minute
        return f"Clock({hour}, {minute})"

    def __str__(self):
        return self.time.strftime('%H:%M')

    def __eq__(self, other):
        return self.time.strftime('%H:%M') == other.time.strftime('%H:%M')

    def __add__(self, minutes):
        res = self.time + timedelta(minutes=minutes)
        return res.strftime('%H:%M')

    def __sub__(self, minutes):
        res = self.time - timedelta(minutes=minutes)
        return res.strftime('%H:%M')