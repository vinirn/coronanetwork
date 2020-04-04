import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from plot_cities import plot_cities

class City:
    code = ""
    name = ""
    state = ""
    population = 0
    long = 0.0
    lat = 0.0
    plotsize = 1.0
    plotfontsize = 10.0
    plotcolor = [0.0,0.0,0.0,1.0]
    showname = True


from plot_map import plot_brazil

state_sel = "mg"

bordercolor = .7*np.array([1.0,1.0,1.0])

plot_brazil(state_sel, bordercolor)

csvfilename = "./data/cities2.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    num=0
    names = []
    states=[]
    longs = []
    lats = []
    populations = []
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

        names.append(cityname)
        states.append(citystate)
        longs.append(float(citylong))
        lats.append(float(citylat))
        populations.append(float(citypopulation))

        print("("+str(num)+"/"+str(numlines)+") "+"Reading "+cityname)

ncities = len(cities)

maxpopulation = np.max(populations)

maxpopulation_state = 0
for city in cities:
    if (city.state==state_sel.upper()) or (state_sel.upper()=="ALL"):
        if city.population>maxpopulation_state:
            maxpopulation_state = city.population

text_population_threshold = maxpopulation_state * 0.05

sizes = np.log(np.array(populations))**1.0
sizesmin = np.min(sizes)

for icity in range(0,ncities):
    cities[icity].plotsize = np.log(cities[icity].population)**1.0
    cities[icity].plotsize += - sizesmin + 1.0
    cities[icity].plotfontsize = cities[icity].plotsize

crainbow = cm.rainbow(np.linspace(1, 0, ncities))
print(crainbow)
for icity in range(0,ncities):
    if (cities[icity].state==state_sel.upper()) or (state_sel.upper()=="ALL"):
        cexp = 0.2
        popul_factor = ((cities[icity].population-1)**cexp)/(maxpopulation_state**cexp)
        colorindex = ncities-int(np.floor(popul_factor*ncities))
        cities[icity].plotcolor = crainbow[colorindex]
        cities[icity].plotcolor[3] = popul_factor #alpha
        if cities[icity].population>text_population_threshold:
            cities[icity].showname = True
        else:
            cities[icity].showname = False

plot_cities(cities, state_sel)