import numpy as np
import matplotlib.cm as cm

class Cities:
    cities = []

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

    
    def config_plot(self, plotexp = 1.0, state_sel = "ALL", text_population_threshold=10000):
        ncities = self.ncities()

        sizes = np.log(np.array(self.populations()))**1.0
        sizesmin = np.min(sizes)
        for icity in self.range():
            self.cities[icity].plotsize = np.log(self.cities[icity].population)**plotexp
            self.cities[icity].plotsize += - sizesmin + 1.0
            self.cities[icity].plotfontsize = self.cities[icity].plotsize

        crainbow = cm.rainbow(np.linspace(1, 0, ncities))

        for icity in self.range():
            if (self.cities[icity].state==state_sel.upper()) or (state_sel.upper()=="ALL"):
                cexp = 0.2
                popul_factor = ((self.cities[icity].population-1)**cexp)/(self.maxpopulation_state(state_sel)**cexp)
                colorindex = ncities-int(np.floor(popul_factor*ncities))
                self.cities[icity].plotcolor = crainbow[colorindex]
                self.cities[icity].plotcolor[3] = popul_factor #alpha
                if self.cities[icity].population>text_population_threshold:
                    self.cities[icity].showname = True
                else:
                    self.cities[icity].showname = False

