import sys
import BookEditor
import BookCheck
import BookAnalyzer

print('Welcome!')
print('q to quit')
response = ' '
while(response != 'q'):
	response = input('Would you like to analyze a book (y / n)?\n')
	if(response == 'y'):
		bookTitle = input('What is the name of the file?\n')
		if bookTitle[:-4] == ".txt":
			print(BookAnalyzer.heuristicBook(bookTitle))
		else:
			print(BookAnalyzer.heuristicBook(bookTitle + ".txt"))
	elif(response == 'n'):
		response = input('Would you like to add a book to the database (y / n)?\n')
		if(response == 'y'):
			bookTitle = input('What is the name of the book?\n')
			timePeriod = input('Which time period is this from (middle english, renaissance, romantic, victorian)?\n')
			if(timePeriod == 'middle english'):
				if(BookCheck.middleEnglishCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					BookCheck.addBookToDatabase(bookTitle, "MiddleEnglish")
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'renaissance'):
				if(BookCheck.renaissanceCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					BookCheck.addBookToDatabase(bookTitle, "Renaissance")
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'romantic'):
				if(BookCheck.romanticCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					BookCheck.addBookToDatabase(bookTitle, "Romantic")
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'victorian'):
				if(BookCheck.victorianCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					BookAnalyzer.addBookToDatabase(bookTitle, "Victorian")
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			else:
				print('This time period doesn\'t match any of our time periods.')
		else:
			response = ' '
