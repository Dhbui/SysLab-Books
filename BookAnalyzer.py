import BookEditor

def getData(timePeriod):
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Data\\" + timePeriod + "Data.txt", 'r')
	lines = f.readlines()
	f.close()
	data = dict()
	index = 0
	while index < len(lines):
		if lines[index][-1] == "\n":
			data[lines[index][:-1]] = int(lines[index + 1])
		else:
			data[lines[index]] = int(lines[index + 1])
		index += 2

	return data

def createData(timePeriod):
	f = open(timePeriod + "BookTitles.txt", 'r')
	bookTitles = f.readlines()
	#print(bookTitles)
	f.close()
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Data\\" + timePeriod + "Data.txt", 'w+')
	data = dict()
	for title in bookTitles:
		if(title[-1] == "\n"):
			title = title[:-1]
		book = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Edited Books\\" + title + "Edited.txt", 'r')
		for line in book:
			temp = line.split(" ")
			for word in temp:
				tempword = word
				if tempword != '':
					if word[-1] == '\n':
						tempword = word[:-1]
					if tempword not in data:
						data[tempword] = 1
					elif tempword in data:
						data[tempword] += 1
		book.close()
	data.pop("", None)
	#print(data)
	for key in data:
		f.write(key + '\n')
		f.write(str(data[key]) + '\n')
	f.close()

def updateData(bookname, timePeriod):
	data = getData(timePeriod)
	book = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Edited Books\\" + bookname + "Edited.txt", 'r')
	for line in book:
		temp = line.split(" ")
		for word in temp:
			tempword = word
			if tempword != '':
				if word[-1] == '\n':
					tempword = word[:-1]
				if tempword not in data:
					data[tempword] = 1
				elif tempword in data:
					data[tempword] += 1
	book.close()
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Data\\" + timePeriod + "Data.txt", 'w')
	data.pop("", None)
	#print(data)
	for key in data:
		f.write(key + '\n')
		f.write(str(data[key]) + '\n')
	f.close()

def bookData(filename):
	data = dict()
	book = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Edited Books\\" + filename + ".txt", 'r')
	for line in book:
		temp = line.split(" ")
		for word in temp:
			tempword = word
			if tempword != '':
				if word[-1] == '\n':
					tempword = word[:-1]
				if tempword not in data:
					data[tempword] = 1
				elif tempword in data:
					data[tempword] += 1
	book.close()
	data.pop("", None)
	#print(data)
	return data

def wordPercentageErrorTimePeriod(word, bookData, sum, periodData, periodSum):
	percentage = float(periodData[word] / (periodSum * 1.0))
	#print(word, ' ', percentage)
	if word not in bookData:
		return percentage
	else:
		difference = float(bookData[word] / (sum * 1.0))
		return float(abs(percentage - difference))

def wordPercentageErrorBook(word, bookData, sum, periodData):
	percentage = float(bookData[word] / (sum * 1.0))
	#print(word, ' ', percentage)
	if word not in periodData:
		return percentage
	else:
		return 0

def totalPercentageError(bookData, sum, periodData, periodSum):
	totalDifference = float(0.0)
	for word in periodData:
		totalDifference += wordPercentageErrorTimePeriod(word, bookData, sum, periodData, periodSum)
	for word in bookData:
		totalDifference += wordPercentageErrorBook(word, bookData, sum, periodData)
	#print('Total Error: ', totalDifference)
	return totalDifference

def heuristicBook(filename):
	newBook = BookEditor.stripBookToAnalyze(filename)
	data = bookData(newBook)
	middleEnglishData = getData("MiddleEnglish")
	romanticData = getData("Romantic")
	renaissanceData = getData("Renaissance")
	victorianData = getData("Victorian")
	dataSum = 0
	middleEnglishSum = 0
	romanticSum = 0
	renaissanceSum = 0
	victorianSum = 0
	#print(middleEnglishData)
	for key in data:
		dataSum += data[key]
	for key in middleEnglishData:
		middleEnglishSum += middleEnglishData[key]
	for key in romanticData:
		romanticSum += romanticData[key]
	for key in renaissanceData:
		renaissanceSum += renaissanceData[key]
	for key in victorianData:
		victorianSum += victorianData[key]
	# print(dataSum)
	# print(middleEnglishSum)
	# print(romanticSum)
	# print(renaissanceSum)
	# print(victorianSum)
	middleEnglishTuple = (totalPercentageError(data, dataSum, middleEnglishData, middleEnglishSum), "Middle English")
	romanticTuple = (totalPercentageError(data, dataSum, romanticData, romanticSum), "Romantic")
	renaissanceTuple = (totalPercentageError(data, dataSum, renaissanceData, renaissanceSum), "Renaissance")
	victorianTuple = (totalPercentageError(data, dataSum, victorianData, victorianSum), "Victorian")
	minimumError = min(middleEnglishTuple, romanticTuple, renaissanceTuple, victorianTuple)
	# print(middleEnglishTuple)
	# print(romanticTuple)
	# print(renaissanceTuple)
	# print(victorianTuple)
	# print(minimumError)
	return minimumError[1]


f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\TestingSetBookTitles.txt", 'r')
titles = f.readlines()
f.close()
for title in titles:
	temp = title
	if title[-1] == "\n":
		temp = title[:-1]
	print(temp, ": ", heuristicBook(temp))
