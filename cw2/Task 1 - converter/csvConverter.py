import csv
import sys

inputFile = sys.argv[1] #input file
outputFile = sys.argv[2] # output file

with open(inputFile, 'rb') as csvFile:
    writeToFile = [] #list
    myReader = csv.reader(csvFile, delimiter=',')#read from csv file
    for row in myReader:
        if row[len(row) - 1]== '1': # check character at end of line
            newLine = "+" + row[len(row)- 1] # add new line with '+1' at front
        else:
            newLine = "" + row[len(row) - 1]# add new line with '-1' at front
        del row[len(row) - 1]# delete it
        count = 1
        for v in row:
            newLine = newLine + " " + str(count) + ":" + v # add contents to send line
            count += 1
        newLine = newLine + "\n"
        writeToFile.append(newLine)
csvFile.close()# close input file

del writeToFile[0]# delete title

newFile = open(outputFile, "w")# create new file
for w in writeToFile:
    newFile.write(w)#add contents of the list to the new file

newFile.close()# close output file