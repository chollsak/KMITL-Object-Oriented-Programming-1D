def day_of_year(day,month,year):
    count = 0
    month_list = is_leap(year)
    count = sum(month_list[:month-1])
    count += day
    return count

def is_leap(year):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month_list = [31,29,31,30,31,30,31,31,30,31,30,31]

    if year % 400 == 0 and year % 100 == 0:
        return leap_month_list
    elif year%4 == 0:
        return leap_month_list
    else:
        return month_list

print(day_of_year(1, 4, 2022))
    
    