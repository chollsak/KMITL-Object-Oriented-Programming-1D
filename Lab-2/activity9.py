def day_of_year(day,month,year):
    count = 0
    month_list = is_leap(year)
    count = sum(month_list[:month-1])
    count += day
    return count

def is_leap(year):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    if year%400 == 0 and year%100 == 0:
        return leap_month_list
    elif year%4 == 0:
        return leap_month_list
    else:
        return month_list

def day_in_year(year):
    if year%400 == 0 and year%100 == 0:
        return 366
    elif year%4 == 0:
        return 366
    else:
        return 365

def date_diff(date_1, date_2):
    day_diff = 0
    date_1 = list(map(int,date_1.split('-')))
    date_2 = list(map(int,date_2.split('-')))

    if date_1[1] <= 12 and date_1[1] >= 1 and date_2[1] <= 12 and date_2[1] >= 1 and date_1[0] <= is_leap(date_1[2])[date_1[1]-1] and date_1[0] >= 1 and date_2[0] <= is_leap(date_2[2])[date_2[1]-1] and date_2[0] >= 1:
        if date_2[2] - date_1[2] != 0:
            for i in range(1,date_2[2]-date_1[2]):
                day_diff += day_in_year(date_1[2]+i)
        
        day_diff += day_in_year(date_1[2]) - (day_of_year(date_1[0],date_1[1],date_1[2]))
        day_diff += (day_of_year(date_2[0],date_2[1],date_2[2])) + 1

        return day_diff
    else:
        return -1

print(date_diff('25-12-1999','9-3-2000'))