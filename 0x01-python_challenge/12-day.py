#Debug the code

print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")

ans1 = input("What language are we writting in? : ")

if ans1 == "python":
    print("Correct")
else:
    print("Nope")

answ2 = int(input("Which lesson number is this? : "))
if (ans2 > 12):
    print("We're not quite that far yet!")
elif (ans2 == 12):
    print("That's right!")
else:
    print("We've gone well past that!")
