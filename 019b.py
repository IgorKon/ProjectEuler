months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 1
sunday_count = 0
for year in range(1900, 2001):
    if year % 4 == 0 and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0))):
        months[1] = 29
    else:
        months[1] = 28
    
    for m in range(0, 12):
        month_day_count = months[m]
        day_of_manth = 1
        while day_of_manth <= month_day_count:
            if (year > 1900) and (i % 7 == 0) and (day_of_manth == 1):
                print(year, m + 1)
                sunday_count += 1
            i += 1
            day_of_manth += 1
print(i)
print(sunday_count)
