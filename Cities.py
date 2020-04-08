import csv
import numpy as np
import matplotlib.cm as cm
from City import City

class Cities:
    cities = []
    sumfields = {}
    maxfields = {}
    minfields = {}
    state_sel = ""
    fieldsdescriptions = {}

    def __init__(self):
        self.cities = []
        self.sumfields={}
        self.maxfields={}
        self.minfields={}
        self.fieldsdescriptions = {}
    
    def update_sum(self,city):
        if self.test_state(city.state):
            for key in city.fields:
                if key in self.sumfields:
                    self.sumfields[key]+=city.fields[key]
                else:
                    self.sumfields[key]=city.fields[key]

    def update_info(self,city):
        if self.test_state(city.state):
            for key in city.fields:
                if key in self.maxfields:
                    if city.fields[key]>self.maxfields[key]:
                        self.maxfields[key]=city.fields[key]
                    if city.fields[key]<self.minfields[key]:
                        self.minfields[key]=city.fields[key]
                else:
                    self.maxfields[key]=city.fields[key]
                    self.minfields[key]=city.fields[key]

    def print_info(self):
        for key in self.sumfields:
            print("sum " + key+": " + str(self.sumfields[key]))
        for key in self.minfields:
            print("min " + key+": " + str(self.minfields[key]))
        for key in self.maxfields:
            print("max " + key+": " + str(self.maxfields[key]))

    def test_state(self,state):
        if (state.upper()==self.state_sel.upper()) or (self.state_sel.upper()=="ALL"):
            return(True)
        else:
            return(False)

    def append(self,city):

        city.unify_ambiguous_names()

        self.cities.append(city)
        self.update_info(city)
        self.update_sum(city)

    def ncities(self):
        return(len(self.cities))

    def range(self):
        return(range(0,self.ncities()))

    def populations(self):
        pops = []
        for city in self.cities:
            pops.append(float(city.population))
        return(pops)

    def maxpopulation(self):
        maxp = 0
        for city in self.cities:
            if city.population > maxp:
                maxp = city.population
        return(maxp)
    
    def maxpopulation_state(self, state_sel = "ALL"):
        maxp_state = 0
        for city in self.cities:
            if (city.state==state_sel.upper()) or (state_sel.upper()=="ALL"):
                if city.population>maxp_state:
                    maxp_state = city.population
        return(maxp_state)

    def print(self):
        for city in self.cities:
            print(city.name + "," + city.state,end=" ")
            for key in city.fields:
                print(key + ":"+str(city.fields[key])+",",end=" ")
            print(" ")

    def config_plot_from_field(self, plotexp = 1.0, text_threshold_factor=0.1, fieldname="population"):
        ncities = self.ncities()

        text_threshold = self.maxfields[fieldname] * text_threshold_factor
        for icity in self.range():
            if fieldname in self.cities[icity].fields:
                self.cities[icity].plotsize = np.log(100.0*float(self.cities[icity].fields[fieldname]))**plotexp
                self.cities[icity].plotfontsize = self.cities[icity].plotsize
                self.cities[icity].plottext = self.cities[icity].name + ":" + str(self.cities[icity].fields[fieldname])
            else:
                self.cities[icity].plotsize = 0
                self.cities[icity].plotfontsize = 0

        crainbow = cm.rainbow(np.linspace(1, 0, ncities))

        for icity in self.range():
            if (self.cities[icity].state==self.state_sel.upper()) or (self.state_sel.upper()=="ALL"):
                cexp = 0.2
                popul_factor = ((self.cities[icity].population-1)**cexp)/(self.maxpopulation_state(self.state_sel)**cexp)
                colorindex = ncities-int(np.floor(popul_factor*ncities))
                self.cities[icity].plotcolor = crainbow[colorindex]
                self.cities[icity].plotcolor[3] = popul_factor #alpha
                if fieldname in self.cities[icity].fields:
                    if self.cities[icity].fields[fieldname]>text_threshold:
                        self.cities[icity].showname = True
                    else:
                        self.cities[icity].showname = False
                else:
                    self.cities[icity].showname = False
    
    def config_plot(self, plotexp = 1.0, text_population_threshold=10000):
        ncities = self.ncities()

        sizes = np.log(np.array(self.populations()))**1.0
        sizesmin = np.min(sizes)
        for icity in self.range():
            self.cities[icity].plotsize = np.log(self.cities[icity].population)**plotexp
            self.cities[icity].plotsize += - sizesmin + 1.0
            self.cities[icity].plotfontsize = self.cities[icity].plotsize
            self.cities[icity].plottext = self.cities[icity].name

        crainbow = cm.rainbow(np.linspace(1, 0, ncities))

        for icity in self.range():
            if (self.cities[icity].state==self.state_sel.upper()) or (self.state_sel.upper()=="ALL"):
                cexp = 0.2
                popul_factor = ((self.cities[icity].population-1)**cexp)/(self.maxpopulation_state(state_sel)**cexp)
                colorindex = ncities-int(np.floor(popul_factor*ncities))
                self.cities[icity].plotcolor = crainbow[colorindex]
                self.cities[icity].plotcolor[3] = popul_factor #alpha
                if self.cities[icity].population>text_population_threshold:
                    self.cities[icity].showname = True
                else:
                    self.cities[icity].showname = False

    def get_cities_from_csv(self,csvfilename):

        with open(csvfilename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            numlines = len(list(spamreader))

        with open(csvfilename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            num=0
            for row in spamreader:
                num+=1

                city = City()
                city.code = row[0]
                city.name = row[1]
                city.state = row[2]
                city.population = int(row[3])
                city.fields["population"] = int(city.population)
                city.long = float(row[4])
                city.lat = float(row[5])

                if self.test_state(city.state):
                    self.append(city)

                print("("+str(num)+"/"+str(numlines)+") "+"Reading "+city.name)

    def include_int_field_from_csv(self,csvfilename,fieldname):
        for icity in self.range():
            with open(csvfilename, newline='\n') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';')
                for row in spamreader:
                    if len(row)==3:
                        name = row[0]
                        state = row[1]
                        if self.test_state(state):
                            if (name==self.cities[icity].name)and(state==self.cities[icity].state):
                                self.cities[icity].fields[fieldname] = int(row[2])
                                self.update_info(self.cities[icity])

    def merge(self,cities2):
        for icity in self.range():
            for city2 in cities2.cities:
                if ((city2.name.upper()==self.cities[icity].name.upper()) 
                        and (city2.state==self.cities[icity].state)):
                    for key2 in city2.fields:
                        #print(city2.name + "," + city2.state + ": " + key2 + " - " + str(city2.fields[key2]))
                        cityhasfield = False
                        for key in self.cities[icity].fields:
                            if key==key2:
                                cityhasfield = True
                        if not cityhasfield:
                            self.cities[icity].fields[key2]=city2.fields[key2]

    def get_sorted_cities_by_int_field(self, fieldname):
        cities_temp = self
        cities_return = Cities()

        for cont in self.range():
            icity_max = 0
            max_field_value = 0
            for icity in cities_temp.range():
                if fieldname in cities_temp.cities[icity].fields:
                    if cities_temp.cities[icity].fields[fieldname]>max_field_value:
                        max_field_value = cities_temp.cities[icity].fields[fieldname]
                        icity_max = icity
            
            cities_return.append(cities_temp.cities[icity_max])
            cities_temp.cities.pop(icity_max)

        return(cities_return)