from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)

titles = [("MiddleEnglishBookTitles.txt", "Middle English"), ("RenaissanceBookTitles.txt", "Renaissance"), ("RomanticBookTitles.txt", "Romantic"), ("VictorianBookTitles.txt", "Victorian")]
X = []
Y = []


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




