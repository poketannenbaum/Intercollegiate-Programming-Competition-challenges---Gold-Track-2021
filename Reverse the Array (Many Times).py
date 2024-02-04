import re
numbers = input("Enter Count, integers separated by a space: ")
numbersarray = re.split(" ", numbers)
numbersarray = list(map(int, numbersarray))
count = numbersarray[0]
numbersarray.pop(0)
revcount = 0
answer = []
while (revcount != count):
	answer.append(numbersarray[revcount])
	originallist = answer
	internalcounter = len(answer) - 1
	internalcounter2 = 0
	answer.reverse()
	revcount += 1
realanswer = ""
answer = list(map(str, answer))
for num in answer:
	realanswer += num
	realanswer += " "
print(realanswer)
