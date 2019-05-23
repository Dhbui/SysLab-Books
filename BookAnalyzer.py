import sys
import BookEditor

def getData(timePeriod):
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Data\\" + timePeriod + "Data.txt", 'r')
	lines = f.readlines()
	f.close()
	data = dict()
	index = 0
	while index < len(lines):
		data[lines[index]] = int(lines[index + 1])
		index += 2

	return data

def createData(timePeriod):
	f = open(timePeriod + "BookTitles.txt", 'r')
	bookTitles = f.readlines()
	print(bookTitles)
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
	print(data)
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
	print(data)
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
	print(data)
	return data

def wordPercentageError(word, bookData, sum, periodData, periodSum):
	percentage = bookData[word] / (sum * 1.0)
	if word not in periodData:
		print(percentage)
		return percentage
	else:
		periodPercent = periodData[word] / (periodSum * 1.0)
		return abs((periodPercent - percentage) / periodPercent)

def totalPercentageError(bookData, sum, periodData, periodSum):
	totalError = 0.0
	for word in bookData:
		totalError += wordPercentageError(word, bookData, sum, periodData, periodSum)
	print('Total Error: ', totalError)
	return totalError

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
	print(dataSum)
	print(middleEnglishSum)
	print(romanticSum)
	print(renaissanceSum)
	print(victorianSum)
	middleEnglishTuple = (totalPercentageError(data, dataSum, middleEnglishData, middleEnglishSum), "Middle English")
	romanticTuple = (totalPercentageError(data, dataSum, romanticData, romanticSum), "Romantic")
	renaissanceTuple = (totalPercentageError(data, dataSum, renaissanceData, renaissanceSum), "Renaissance")
	victorianTuple = (totalPercentageError(data, dataSum, victorianData, victorianSum), "Victorian")
	minimumError = min(middleEnglishTuple, romanticTuple, renaissanceTuple, victorianTuple)
	print(middleEnglishTuple)
	print(romanticTuple)
	print(renaissanceTuple)
	print(victorianTuple)
	print(minimumError)
	return minimumError[1]

print(heuristicBook("Castle Rackrent"))
