# Program that splits the bill
# round function (what rounding, how many decimal places)

myBill = float(input("What was the bill? : "))
numberOfPeople = int(input("How many people? : "))

answer = myBill / numberOfPeople
print("You all owe", answer)

answer = round(answer, 2)
print("You all owe", answer)
