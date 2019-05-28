import sys

toKeep = '1234567890abcdefghijklmnopqrstuvwxyz.;,—:?!" '


def stripBook(bookName, timeperiod):
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\" + timeperiod + "\\" + bookName + ".txt", 'r')
	lines = [line.rstrip('\n') for line in f]
	f.close()
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Edited Books\\" + bookName + "Edited.txt", 'w+')
	for line in lines:
		toRemove = list()
		temp = line.lower()
		temp = temp + " , "
		for char in temp:
			if(char not in toKeep):
				toRemove.append(char) 
		for char in toRemove:
			temp = temp.replace(char, " ")
		temp = temp.replace(".", '\n ')
		temp = temp.replace(",", '\n ')
		temp = temp.replace(";", '\n ')
		temp = temp.replace(":", '\n ')
		temp = temp.replace("—", '\n ')
		temp = temp.replace("?", '\n ')
		temp = temp.replace("!", '\n ')
		temp = temp.replace("\"", '\n ')
		f.write(temp)
	f.close()
	return bookName + "Edited"

def stripBookToAnalyze(bookName):
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\To Analyze\\" + bookName + ".txt", 'r')
	# print([line for line in f])
	lines = [line.rstrip('\n') for line in f]
	f.close()
	f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Edited Books\\" + bookName + "Edited.txt", 'w+')
	for line in lines:
		toRemove = list()
		temp = line.lower()
		temp = temp + " , "
		for char in temp:
			if(char not in toKeep):
				toRemove.append(char) 
		for char in toRemove:
			temp = temp.replace(char, " ")
		temp = temp.replace(".", '\n ')
		temp = temp.replace(",", '\n ')
		temp = temp.replace(";", '\n ')
		temp = temp.replace(":", '\n ')
		temp = temp.replace("—", '\n ')
		temp = temp.replace("?", '\n ')
		temp = temp.replace("!", '\n ')
		temp = temp.replace("\"", '\n ')
		f.write(temp)
	f.close()
	return bookName + "Edited"

f = open("RenaissanceBookTitles.txt", 'r')
for line in f:
	temp = line
	if line[-1] == '\n':
		temp = line[:-1]
	print(line)
	stripBook(temp, "Renaissance")