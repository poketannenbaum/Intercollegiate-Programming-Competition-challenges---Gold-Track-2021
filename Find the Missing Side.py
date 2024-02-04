import re
import math
firstseg = input("Enter first segment: ")
firstlength = input("Enter first length: ")
secondseg = input("Enter second segment: ")
secondlength = input("Enter second length: ")
firstlength = int(firstlength)
secondlength = int(secondlength)
seglist = []
seglist.extend(firstseg)
seglist.extend(secondseg)
seen = set()
duplicates = ""
for element in seglist:
	if element in seen:
		duplicates = element
	else:
		seen.add(element)
if (duplicates == "A" or duplicates == "C"):
	if (firstseg == "AC" or firstseg == "CA"):
		Answer = firstlength * firstlength - secondlength * secondlength
		Answer = math.sqrt(Answer)
	else:
		Answer = secondlength * secondlength - firstlength * firstlength
		Answer = math.sqrt(Answer)
if (duplicates == "B"):
	Answer = firstlength * firstlength + secondlength * secondlength
	Answer = math.sqrt(Answer)
	Answer = round(Answer)
	print(f"AC ", Answer)
if (duplicates == "A"):
	Answer = round(Answer)
	print("BC ", Answer)
if (duplicates == "C"):
	Answer = round(Answer)
	print("AB ", Answer)


