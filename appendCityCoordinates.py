import csv
import urllib.request, urllib.error, urllib.parse
import shutil

outdatapath = "/home/osboxes/Documents/data/wikicities"

csvfilename = "./data/cities.csv"
csvfilename_out = "./data/cities2.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    with open(csvfilename_out, 'w', newline='\n') as csvfile_out:
        spamwriter_out = csv.writer(csvfile_out, delimiter=';',quoting=csv.QUOTE_NONE)
        num=0
        numCitiesNotFound = 0
        for row in spamreader:
            num+=1
            #print(';\t'.join(row))
            
            citycode        = row[1]
            cityname        = row[2]
            citystate       = row[3]
            citypopulation  = row[4]
            citywiki        = row[5]


            print("("+str(num)+"/"+str(numlines)+") "+"Searching coordinates for "+cityname)
            
            csvfilename_coords = "./data/coordinates.csv"
            with open(csvfilename_coords, newline='\n') as csvfile_coords:
                spamreader_coords = csv.reader(csvfile_coords, delimiter=';')
                found = False
                for row_coords in spamreader_coords:
                    citycode_coords = row_coords[0]
                    cityname_coords = row_coords[1]
                    citylong_coords = row_coords[2]
                    citylat_coords  = row_coords[3]

                    if citycode_coords == citycode:
                        print("Achou! Longitude = "+citylong_coords+", Latitude = "+citylat_coords)
                        found = True
                        spamwriter_out.writerow([citycode,cityname,citystate,citypopulation,citylong_coords,citylat_coords,citywiki])
                if (not found):
                    print("Not found coordinates of "+cityname+" !")
                    numCitiesNotFound += 1
    print("Number of Cities Not Found: "+ str(numCitiesNotFound))
        