import numpy as np
import matplotlib.pyplot as plt

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

from htmlutils import prettify 
from stringUtils import formatDate

from Cities import Cities
from get_cities_from_coronacsv import get_cities_from_coronacsv
from plot_cities import plot_cities
from plot_map import plot_brazil
from process_g1data import process_g1_data

state_sel = "all"

day = "2020-04-07"

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

pngfile = state_sel + day + ".png"
pngfilepath= "./html/images/"
plot_cities(cities.cities, state_sel,pngfilepath+pngfile)




taghtml = Element('html')

comment = Comment('By Marcos Vinicius Candido Henriques, UFERSA-RN-Brazil')
taghtml.append(comment)

taghead = SubElement(taghtml, 'head')
tagcss  = SubElement(taghead, 'link',{'rel':"stylesheet",'type':"text/css",'href':"style.css"})
tagbody = SubElement(taghtml, 'body')

cities_sorted = cities.get_sorted_cities_by_int_field(fieldname)
cities_sorted.print()

tagdiv      = SubElement(tagbody, 'div',{'align':"center"})

tagimg      = SubElement(tagdiv,'img',{'src':'images/'+pngfile})

tagh1       = SubElement(tagdiv,'h1')
tagh1.text  = cities.fieldsdescriptions[fieldname]
tagp       = SubElement(tagdiv,'p')
tagp.text  = 'Fonte: G1'
tagtable    = SubElement(tagdiv, 'table',{'id':"customers"})
tagtr       = SubElement(tagtable, 'tr')
tagth       = SubElement(tagtr, 'th')
tagth.text  = "#"
tagth       = SubElement(tagtr, 'th')
tagth.text  = "Cidade"
tagth       = SubElement(tagtr, 'th')
tagth.text  = "UF"
tagth       = SubElement(tagtr, 'th')
tagth.text  = "Casos Confirmados"
cont = 0
for city in cities_sorted.cities:
    if fieldname in city.fields:
        cont += 1
        if cont<= 10:
            tagtr       = SubElement(tagtable, 'tr')
            tagtd       = SubElement(tagtr,'td')
            tagtd.text  = str(cont)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.name)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.state)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.fields[fieldname])
        else:
            break



htmlfilename = "./html/index.html"
with open(htmlfilename, "w") as htmlfile:
    line = prettify(taghtml)
    print(line)
    htmlfile.write(str(line)+"\n")
