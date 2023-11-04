# Tip calculator

print("TIP CALCULATOR")
print()
print("=============================================")
print()

totalBill = float(input("What is the total bill? : $"))
percentageBill = int(input("What is the tip you want to give? : "))
answer = (totalBill * percentageBill) / 100
print("The total amount is", answer)

total2 = answer + totalBill
splitBill = int(input("How many people will split the bill? : "))
answer2 = total2 / splitBill
totalBill1 = round(answer2, 2)
print("The total amount per person is $", totalBill1)
