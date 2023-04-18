def daysBetweenDates(date1, date2):
    days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    date1 = date1.split('-')
    date2 = date2.split('-')
    if  date1[0] % 4 == 0 and (date1[0] % 400 == 0 or date1[0] % 100 != 0):
        d =
