def leapyear( year):
    if year % 4 == 0:
        return 0
    else:
        return 1

def daysinmonth(year,month):
    nor_year = (31,28,31,30,31,30,31,31,30,31,30,31)
    leap_year = (31,29,31,30,31,30,31,31,30,31,30,31)
    if leapyear(year) == 0:
        return leap_year[month-1]
    else:
        return nor_year[month-1]





print daysinmonth(2012,2)