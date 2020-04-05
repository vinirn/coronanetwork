import csv
from City import City

def get_cities_from_csv(csvfilename):

    with open(csvfilename, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        numlines = len(list(spamreader))


    with open(csvfilename, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        num=0
        cities = []
        for row in spamreader:
            num+=1
            #print(';\t'.join(row))
            
            citycode        = row[0]
            cityname        = row[1]
            citystate       = row[2]
            citypopulation  = row[3]
            citylong        = row[4]
            citylat         = row[5]
            
            city = City()
            city.code = citycode
            city.name = cityname
            city.state = citystate
            city.population = float(citypopulation)
            city.long = float(citylong)
            city.lat = float(citylat)
            cities.append(city)

            print("("+str(num)+"/"+str(numlines)+") "+"Reading "+cityname)

    return(cities)