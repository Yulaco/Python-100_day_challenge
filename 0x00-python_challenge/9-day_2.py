# Program identifies what generation you belong to.

print("GENERATION IDENTIFIER")
print()
print("=========================================")
print()

year = int(input("Please enter what year you were born: "))

if (year > 1883 and year <= 1900):
    print("Lost generation, the diesel engine was invented in your time period!")
elif (year > 1901 and year <= 1927):
    print("Greatest generation, the world got laminated glass from your generation.")
elif (year > 1925 and year <= 1946):
    print("Silent Generation, you are wise! You went through the Great Depression and WWII.")
elif (year > 1947 and year <= 1964):
    print("Baby Boomer you were born in the period the hard disk was invented!")
elif (year > 1965 and year <= 1981):
    print("You belong to Generation X! You were born in the period where the laptop was invented.")
elif (year > 1982 and year <= 1995):
    print("You are Millenials! You were born in the period when the laptop was invented.")
elif (year > 1996 and Generation <= 2015):
    print("Hi, Generation Z! You came around the time of the Xbox, Youtube, Netflix.")
else:
    print("Please, enter the correct year you were born")
