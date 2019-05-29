import sys

middleEnglishBooks = 'MiddleEnglishBookTitles.txt'
renaissanceBooks = 'RenaissanceBookTitles.txt'
romanticBooks = 'RomanticBookTitles.txt'
victorianBooks = 'VictorianBookTitles.txt'

def middleEnglishCheck(booktitle):
	f = open(middleEnglishBooks, 'r')
	titles = f.readlines()
	for title in titles:
		if(title[-1] == '\n'):
			newtitle = title[:-1]
		else:
			newtitle = title
		if(newtitle == booktitle):
			return True
	return False


def renaissanceCheck(booktitle):
	f = open(renaissanceBooks, 'r')
	titles = f.readlines()
	for title in titles:
		if(title[-1] == '\n'):
			newtitle = title[:-1]
		else:
			newtitle = title
		if(newtitle == booktitle):
			return True
	return False


def romanticCheck(booktitle):
	f = open(romanticBooks, 'r')
	titles = f.readlines()
	for title in titles:
		if(title[-1] == '\n'):
			newtitle = title[:-1]
		else:
			newtitle = title
		if(newtitle == booktitle):
			return True
	return False

def victorianCheck(booktitle):
	f = open(victorianBooks, 'r')
	titles = f.readlines()
	#print(titles)
	for title in titles:
		if(title[-1] == '\n'):
			newtitle = title[:-1]
		else:
			newtitle = title
		if(newtitle == booktitle):
			return True
	return False

def addBookToDatabase(bookTitle, timePeriod):
	f = open(timePeriod + "BookTitles.txt", 'r')
	bookTitles = f.readlines()
	f.close()
	f = open(timePeriod + "BookTitles.txt", 'w+')
	for title in bookTitles:
		temp = title
		if temp[-1] == "\n":
			temp = title[:-1]
		f.write(temp + "\n")
	f.write(bookTitle + "\n")
	f.close()