def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day == 30:
        return year, month + 1, 1
        if month == 12:
            return year +1,1,1
    else:
        return year,month,day + 1

print nextDay(2012, 9, 30)
