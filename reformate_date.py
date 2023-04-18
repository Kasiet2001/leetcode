def reformatDate(date):
    date = date.split()
    monthd ={'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
            'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    day = date[0][:-2]
    month = date[1]
    year = date[2]
    if len(day) < 2:
        day = '0' + day
    return f'{year}-{monthd[month]}-{day}'
print(reformatDate("26th May 1960"))