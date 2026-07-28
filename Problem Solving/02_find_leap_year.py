# find leap year
# import calendar
#
# year = int(input("Enter a year: "))
# if calendar.isleap(year):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# find leap year
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")