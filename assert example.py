# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#
def leapyear( year,month,date):
    if year % 100 == 0 and year % 400 != 0:
        return 1
    elif year % 4:
        return 0

def daysinmonth(year,month,date):
    nor_year = (31,28,31,30,31,30,31,31,30,31,30,31)
    leap_year = (31,29,31,30,31,30,31,31,30,31,30,31)
    if leapyear(year,month,date) == 0:
        return leap_year[month-1]
    else:
        return nor_year[month-1]




def nextDay(year1, month1, day1):
    if month1 == 12 and day1 == 31:
        return year1 + 1, 1, 1
    elif day1 == daysinmonth(year1, month1, day1):
        return year1, month1 + 1, 1
    else:
        return year1,month1,day1 + 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    new_year = year1
    new_month = month1
    new_day = day1
    i = 0
    while True:
        if new_year == year2 and new_month == month2 and new_day == day2:
            break
        new_year, new_month, new_day = nextDay(new_year, new_month, new_day)
        i = i + 1
    return i


