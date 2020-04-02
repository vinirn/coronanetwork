import csv
import urllib.request, urllib.error, urllib.parse
import shutil

outdatapath = "/home/osboxes/Documents/data/wikicities"

csvfilename = "./data/cities.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    num=0
    for row in spamreader:
        num+=1
        #print(';\t'.join(row))
        
        citycode = row[1]
        cityname = row[2]
        wikiurl = "https://pt.wikipedia.org/"+row[5]
        #if (num<3):
        print("("+str(num)+"/"+str(numlines)+") "+"Reading wiki for "+cityname)
        
        outfilename = outdatapath + "/" + citycode + ".html"
        urllib.request.urlretrieve(wikiurl, outfilename) 
        
