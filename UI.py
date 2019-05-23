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
		edited = input('Has this book been stripped and edited (y / n)?\n')
		if(edited == 'y'):
			BookAnalyzer.analyzeBook(bookTitle)
		if(edited == 'n'):
			stripped = BookEditor.stripBook(bookTitle)
			BookAnalyzer.analyzeBook(stripped)
	elif(response == 'n'):
		response = input('Would you like to add a book to the database (y / n)?\n')
		if(response == 'y'):
			bookTitle = input('What is the name of the book?\n')
			timePeriod = input('Which time period is this from (middle english, renaissance, romantic, victorian)?\n')
			if(timePeriod == 'middle english'):
				if(BookCheck.middleEnglishCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'renaissance'):
				if(BookCheck.renaissanceCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'romantic'):
				if(BookCheck.romanticCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			if(timePeriod == 'victorian'):
				if(BookCheck.victorianCheck(bookTitle)):
					BookEditor.stripBook(bookTitle, timePeriod)
					print('Your book has been added to the database.\n')
				else:
					print('The database already has this book.')
			else:
				print('This time period doesn\'t match any of our time periods.')
		else:
			response = ' '
