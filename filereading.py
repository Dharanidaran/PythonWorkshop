import os

filepath = os.path.join( os.getcwd(),'Dataset','roskilde.csv')
print(filepath)


filepointer = open(filepath ,'r')

fileData = []


for line in filepointer:
	fileData.append(line)


for line in fileData:
	columns = line.split(sep=",")
	# print(columns[-4:])
	print(columns[-1])