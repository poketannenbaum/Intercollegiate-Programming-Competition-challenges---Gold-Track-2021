numbers = input("Enter count of words: ")
numbersarray = []
numbers = int(numbers)
while (numbers != 0):
	loopinput = input("Enter next word: ")
	numbersarray.append(loopinput)
	numbers -= 1
numbersarray = sorted(numbersarray, key=len)
print(numbersarray)