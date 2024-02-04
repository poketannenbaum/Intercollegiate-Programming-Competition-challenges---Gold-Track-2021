import re
numbers = input("Enter two numbers separated by a space: ")
numberarray = re.split(" ", numbers)
numberarray = list(map(int, numberarray))
number1 = numberarray[0]
number2 = numberarray [1]
placeholdernumber1 = 0
placeholdernumber2 = 0
result = 0
number1result = 0
number2result = 0
number1divisors = []
number2divisors = []
while (placeholdernumber1 != number1 - 1):
	placeholdernumber1 += 1
	result = number1 / placeholdernumber1
	if (result.is_integer()):
		number1divisors.append(placeholdernumber1)
while (placeholdernumber2 != number2 - 1):
	placeholdernumber2 += 1
	result = number2 / placeholdernumber2
	if (result.is_integer()):
		number2divisors.append(placeholdernumber2)
for num in number1divisors:
	number1result = number1result + num
for num in number2divisors:
	number2result = number2result + num
if (number2result == number1 and number1result == number2):
	print("Agreeable numbers")
else:
	print("Non-agreeable numbers")