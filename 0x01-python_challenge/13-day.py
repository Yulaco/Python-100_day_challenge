# Grade Generator

print('GRADE GENERATOR')
print()

testName = input('Please type in the name of a test: ')
print(testName)

maximumScore = int(input('Please type the maximum score you can receive: '))
print(maximumScore)

pointReceived = int(input('Please type the number of points received: '))
print(pointReceived)

percentage = round(float((pointReceived / maximumScore) * 100), 2)
print(percentage)

print('You got', percentage, '%')

if percentage >= 90:
    print('A+')
elif percentage >= 80 and percentage <= 89:
    print('A')
elif percentage >= 70 and percentage <= 79:
    print('B')
elif percentage >= 60 and percentage <= 69:
    print('C')
elif percentage >= 50 and percentage <= 59:
    print('D')
elif percentage < 50:
    print('Under 50')
else:
    print('Please try again')
