# Calculate how many seconds in a year
# 31, 536, 000 seconds
# 60 seconds in a minute
# 60 minutes in a hour
# 24 hour in a day
# 30 days 
# 12 months
# leap year +1
# if leap year has 366 days

print("START")
print("How many seconds are in a year?")
print()
print("==================================================")
print()

# Converting 60 min to sec
hourToseconds = 60 * 60
print(f"There are {hourToSeconds} seconds in 60 minutes.")

# Converting 24 hrs to sec
dayToSeconds = hourToSeconds * 24
print(f"There are {dayToSeconds} seconds in 24 hours.")

# Converting 30 days to sec
thirtyToSeconds = dayToSeconds * 30
print(f"There are {thirtydaysToSeconds} seconds in 30 days.")

# Converting 11 mon to sec
monthsToSecons = thirtydaysToSeconds * 11
print(f"There are {monthsToSeconds} seconds in 11 months plus the 7 days of months with 31 days.")

# Converting 7 days of the mon with 31 days to sec
yearToSecond = (dayToSeconds * 7) + monthsToSeconds
print(f"There are {yearToSecond} seconds in 11 months plus 7 days of months with 31 days.")

# Converting mon of february to sec
fullYearToSeconds = (dayToSeconds * 28) + yearToSecond
print(f"There are {fullYearToSeconds} seconds in 12 months.")

# Converting leap year to sec
leapYear = int(29)
if leapYear:
    leapYearToSeconds = (leapYear * dayToSeconds) + yearToSecond
print(f"There are {leapYearToSeconds} seconds in a leap year.")
