def is_leap(year):
    """
    Docstring: it checks if a year
    is leap or not
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                retrn = True
            else:
                retrn = False
        else:
            retrn = True
    else:
        retrn = False

def days_in_month(year, month):
    """
    Docstring: it returns the number
    of days in a year
    """
    if len(str(year)) != 4:
        return "Invalid Year"
    if month > 12 or month < 0:
        return "Invalid month input"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        month_days[1] += 1
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month {eg: 1 for janury}: "))
days = days_in_month(year, month)
print(days)