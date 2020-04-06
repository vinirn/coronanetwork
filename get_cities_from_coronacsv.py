import csv
from City import City
from Cities import Cities

def get_cities_from_coronacsv(day):

    csvcoronafilename = "./data/corona/" + day + ".csv"

    cities = Cities()

    with open(csvcoronafilename, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        numlines = len(list(spamreader))


    with open(csvcoronafilename, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        num=0
        for row in spamreader:
            num+=1
            if len(row)==3:
                city = City()
                city.name        = row[0]
                city.state       = row[1]
                city.fields["coronacases"+day] = row[2]
                cities.append(city)

    for city in cities.cities:
        print("("+str(num)+"/"+str(numlines)+") "
                +city.name+ " " + city.state + " " 
                + city.fields["coronacases"+day])

    return(cities)
