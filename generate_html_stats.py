import numpy as np
import matplotlib.pyplot as plt

from stringUtils import formatDate

from Cities import Cities
from get_cities_from_coronacsv import get_cities_from_coronacsv
from plot_cities import plot_cities
from plot_map import plot_brazil
from process_g1data import process_g1_data

from html_index import html_index

state_sel = "all"

day = "2020-04-08"

bordercolor = .7*np.array([1.0,1.0,1.0])
plot_brazil(state_sel, bordercolor)

csvfilename = "./data/cities2.csv"

cities = Cities()
cities.state_sel = state_sel
cities.get_cities_from_csv(csvfilename)

#cities2 = Cities()
process_g1_data(day)

fieldname = "coronacases"+day
dayformated = formatDate(day)
cities.fieldsdescriptions[fieldname] = "Casos confirmados de COVID-19 no dia " + dayformated

print(cities.ncities())
csvcoronafilename = "./data/corona/" + day + ".csv"
cities.include_int_field_from_csv(csvcoronafilename,fieldname)

cities.print_info()

text_threshold_factor = 0.01

plotexp = 1.0
cities.config_plot_from_field(plotexp, text_threshold_factor,fieldname)

pngfilename = state_sel + day + ".png"
pngfilepath= "./html/images/"
plot_cities(cities.cities, state_sel,pngfilepath+pngfilename)

htmlfilename = "./html/index"
html_index(cities,fieldname,htmlfilename,pngfilename)