import re
rsnclms = input("Enter number of rows then columns: ")
start = input("Enter starting room (Row then column): ")
instructions = input("Enter instructions: ")
sizearr = re.split(" ", rsnclms)
startarr = re.split(" ", start)
instructionsarr = re.split(" ", instructions)
sizearr = list(map(int, sizearr))
startarr = list(map(int, startarr))
instructionsarr = list(map(int, instructionsarr))
count = 0
visitedrooms = []
leftflag = 0
rightflag = 0
orientation = 0
successflag = ""
strofpos = str(startarr[0]) + " " + str(startarr[1])
visitedrooms.append(strofpos)
if(startarr[0] == 0):
	orientation = 0
elif(startarr[0] > 0 and startarr[1] > 0):
	orientation = 1
elif(startarr[0] > 0 and startarr[1] == 0):
	orientation = 3
else:
	orientation = 2
while(True):
	if(instructionsarr[count] == 9):
		if (successflag == ""):
			successflag = "tour ended before leaving building"
		break
	if(instructionsarr[count] == 1):
		orientation += 1
		if (orientation == 4):
			orientation = 0
	if(instructionsarr[count] == 2):
		orientation -= 1
		if (orientation == -1):
			orientation = 3
	if(orientation == 0):
		startarr[0] = startarr[0] + 1
	if(orientation == 1):
		startarr[1] = startarr[1] - 1
	if(orientation == 2):
		startarr[0] = startarr[0] - 1
	if(orientation == 3):
		startarr[1] = startarr[1] + 1
	strofpos = str(startarr[0]) + " " + str(startarr[1])
	if(strofpos in visitedrooms):
		successflag = "Visited same room more than once"
		break
	if(startarr[0] < 0 or startarr[1]  < 0 or startarr[0] > sizearr[0] or startarr[1] > sizearr[1]):
		try:
			instructionsarr[count + 1]
			successflag = "left building before tour was over"
			break
		except:
			successflag = "Successful Tour"
			break
	try:
		instructionsarr[count]
	except:
		successflag = "tour ended before leaving building"
		break
	visitedrooms.append(strofpos)
	count += 1
print(successflag)