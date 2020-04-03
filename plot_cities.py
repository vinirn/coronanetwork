import csv
import matplotlib.pyplot as plt

csvfilename = "./data/cities2.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    num=0
    for row in spamreader:
        num+=1
        #print(';\t'.join(row))
        
        citycode        = row[0]
        cityname        = row[1]
        citystate       = row[2]
        citypopulation  = row[3]
        citylong        = row[4]
        citylat         = row[5]
        
        print("("+str(num)+"/"+str(numlines)+") "+"Reading "+cityname)
        

        
