tvShow = input("What is your favorite tv show? ")

if tvShow == "Suits":
    print("That is nice")

    faveCharacter = input("Who is your favorite character?")
    
    if faveCharacter == "Harvey Specter":
        print("Right answer")

    else:
        print("Nah, Mike Ross is the greatest")

elif tvShow == "The Apprentice":
    print("You have a business mindset!")

else:
    print("Yes, that's cool but please try again")
