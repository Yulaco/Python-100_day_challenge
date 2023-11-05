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
