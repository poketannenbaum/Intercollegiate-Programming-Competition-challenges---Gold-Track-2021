order = input("Enter weight of rock order: ")
order = int(order)
number = order
totalrocks = []
totalrocks.append(order)
answer = []
answercounter = 0
answertallycounter = 0
while (order != 0):
	order -= 1
	totalrocks.append(order)
totalrocks.reverse()
totalrocks.pop(0)
counter2 = 0 
counter3 = 0
iterator = 0
while(iterator < number - 1):
	answer = []
	counter = 0
	counter2 = 0
	if (totalrocks[counter3] == number):
		break
	while(counter2 < number):
		counter2 += totalrocks[counter3]
		if (counter2 == number):
			while(True):
				if (counter2 == 0):
					answertallycounter += answer[len(answer) - 1]
					answercounter += 1
					break
				answer.append(totalrocks[counter3])
				counter2 -= totalrocks[counter3]
				counter3 -= 1
			if(counter2 == 0):
				break
		counter3 += 1
		counter += 1
	iterator += 1
	counter3 = iterator
print(answercounter, " ", answertallycounter)