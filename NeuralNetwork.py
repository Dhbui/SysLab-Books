from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)

titles = [("MiddleEnglishBookTitles.txt", "Middle English"), ("RenaissanceBookTitles.txt", "Renaissance"), ("RomanticBookTitles.txt", "Romantic"), ("VictorianBookTitles.txt", "Victorian")]
X = []
Y = []

def runNeuralNet():
    for titleTuple in titles:
        f = open(titleTuple[0], 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            temp = line
            if temp[-1] == "\n":
                temp = line[:-1]
            f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\" + titleTuple[1] + "\\" + temp + ".txt", 'r')
            X.append(" ".join(f.readlines()))
            Y.append(titleTuple[1])


def createIndexing():
    toKeep = "abcdefghijklmnopqrstuvwxyz1234567890"
    indexMap = dict()
    index = 0
    for title in titles:
        f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\" + title[0], 'r')
        books = f.readlines()
        f.close()
        for book in books:
            book1 = book
            if book[-1] == "\n":
                book1 = book[:-1]
            f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\" + title[1] + "\\" + book1 + ".txt", 'r')
            text = f.readlines()
            toRemove = ""
            for line in text:
                for char in line:
                    if char not in toKeep:
                        toRemove = toRemove + char
                temp = line
                for char in toRemove:
                    temp.replace(char, " ")
                temp = temp.split(" ")
                if "" in temp:
                    temp.remove("")
                for word in temp:
                    temp2 = word
                    print(temp2)
                    if temp2[-1] == '\n':
                        temp2 = word[:-1]
                    if temp2 not in indexMap:
                        indexMap[word] = index
                        index += 1
    f = open("C:\\Users\\Dylan\\Documents\\SysLab Books\\Data\\indexMapping.txt", 'w+')
    for key in indexMap:
        f.write(str(indexMap[key]) + " " + key + "\n")
    f.close()

def getIndexing():
    indexMap = dict()
    f = open("indexMapping.txt", 'r')
    mapping = f.readlines()
    f.close()
    for pair in mapping:
        line = pair
        if pair == "":
            break
        if pair[-1] == "\n":
            line = pair[:-1]
        item = line.split(" ")
        indexMap[line[1]] = int(line[0])
    return indexMap

createIndexing()

