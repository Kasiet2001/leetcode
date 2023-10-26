from datetime import datetime
def daysBetweenDates(date1, date2):
    x = datetime.strptime(date1, '%Y-%m-%d')
    y = datetime.strptime(date2, '%Y-%m-%d')
    return abs((y - x).days)
print(daysBetweenDates("2019-06-29", "2019-06-30"))