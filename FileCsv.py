import csv
import os


filepath = os.path.join( os.getcwd(),'Dataset','roskilde.csv')

outputPath = os.path.join( os.getcwd(),'Dataset','light.csv')


fileobject = open(filepath,'r')
writeobject = open(outputPath,'w')

csvReader = csv.reader(fileobject,delimiter=",")
csvWriter = csv.writer(writeobject,delimiter=",")
Content = []

# for line in csvReader:
# 	Content.append(line)

# for column in Content:
# 	print(column[-1])



for line in csvReader:
	csvWriter.writerow([line[-1],line[-2]])