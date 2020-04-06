import numpy as np
import matplotlib.pyplot as plt

from Cities import Cities
from get_cities_from_csv import get_cities_from_csv
from plot_cities import plot_cities
from plot_map import plot_brazil

state_sel = "all"

bordercolor = .7*np.array([1.0,1.0,1.0])
plot_brazil(state_sel, bordercolor)

csvfilename = "./data/cities2.csv"

cities = Cities()

cities = get_cities_from_csv(csvfilename)

text_population_threshold_factor = 0.1
text_population_threshold = cities.maxpopulation_state(state_sel) * text_population_threshold_factor

plotexp = 1.0
cities.config_plot(plotexp, state_sel, text_population_threshold)

plot_cities(cities.cities, state_sel)