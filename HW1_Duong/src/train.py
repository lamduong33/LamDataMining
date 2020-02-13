import numpy # for arrrays
import nltk  # for stemming and tokenizing
import re    # for regular expressions

# Function: readData
# -------------------------------------------------
# fileName: name of the file as a string
# trainingData: the training data as a NumPy array
# 
# Return data as a numpy array
def readData(fileName):
    trainingDataFile = open(fileName, "r")
    trainingData = numpy.array([], dtype=object)
    for eachLine in trainingDataFile:
        trainingData = numpy.insert(trainingData, trainingData.size, eachLine)
    return trainingData

# Function: printData
# -------------------------------------------------
# dataList: the data as a NumPy Array
#
# Simply print each element of the numpy array
def printData(dataList):
    for eachLine in dataList:
        print(eachLine)
        print("\n")

# Function: train
# ---------------------

#def trainData(trainingData)

def main():
    trainingData = readData("1580506710_9392152_train_file.dat")
    print(trainingData.size)
main()

