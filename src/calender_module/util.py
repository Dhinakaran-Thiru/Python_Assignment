from datetime import datetime
import calendar
def calendar_module(s):
    date=datetime.strptime(s,"%m %d %Y")
    weekday=date.weekday()
    day=calendar.day_name[weekday]
    return day.upper()
