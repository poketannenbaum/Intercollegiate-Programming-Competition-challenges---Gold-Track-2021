import re
number = input("Enter the number: ")
numberarray = list(map(int, number))
newarray = []
while(True):
	numberarray = list(map(int, number))
	try:
		testaroon = numberarray[1]
	except:
		break
	numberarraysize = len(numberarray)
	numberpointer = 0
	counter = 0
	for num in numberarray:
		placeholderval = abs(num - numberarray [counter + 1])
		newarray.append(placeholderval)
		if (counter + 1 == numberarraysize - 1):
			number = ""
			for numb in newarray:
				number =number + str(numb)
			newarray = []
			break
		counter += 1
print(number)
