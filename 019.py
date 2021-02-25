# Counting Sundays

# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# https://projecteuler.net/problem=19

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 1
sunday_count = 0
for year in range(1900, 2001):
    if year % 4 == 0 and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0))):
        months[1] = 29
    else:
        months[1] = 28
    for month in months:
        day_of_manth = 1
        while day_of_manth <= month:
            if (year > 1900) and (i % 7 == 0) and (day_of_manth == 1):
                sunday_count += 1
            i += 1
            day_of_manth += 1
print(i)
print(sunday_count)
