n = input("Enter N: ")
n = int(n)
oddnums = []
counter = 1
while (counter != 20001):
    oddnums.append(counter)
    counter += 2
counter3 = 2
counter3placeholder = 2
nplaceholder = 2
while(True):
	numstoremove = []
	counter3 = oddnums[nplaceholder - 1]
	counter3placeholder = counter3
	while(True):
		try:
			oddnums[counter3]
		except:
			break
		numstoremove.append(oddnums[counter3 - 1])
		counter3 += counter3placeholder
	nplaceholder += 1
	tempset1 = set(oddnums)
	tempset2 = set(numstoremove)
	answer = list(tempset1 - tempset2)
	oddnums = answer
	oddnums.sort()
	if (nplaceholder > n - 1):
		oddnums.sort()
		break
print (oddnums[n - 1])