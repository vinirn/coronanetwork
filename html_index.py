from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

from stateUtils import getStateName
from htmlutils import prettify 
from html_table_field import html_table_field

def html_index(cities,fieldname,htmlfilename,pngfilename):

    taghtml = Element('html')

    comment = Comment('By Marcos Vinicius Candido Henriques, UFERSA-RN-Brazil')
    taghtml.append(comment)

    taghead = SubElement(taghtml, 'head')
    tagcss  = SubElement(taghead, 'link',{'rel':"stylesheet",'type':"text/css",'href':"style.css"})
    tagbody = SubElement(taghtml, 'body')

    cities_sorted = cities.get_sorted_cities_by_int_field(fieldname)
    cities_sorted.print()

    tagdiv      = SubElement(tagbody, 'div',{'align':"center"})

    tagimg      = SubElement(tagdiv,'img',{'src':'images/'+pngfilename})

    tagh1       = SubElement(tagdiv,'h1')
    tagh1.text  = getStateName(cities.state_sel)
    tagh2       = SubElement(tagdiv,'h2')
    tagh2.text  = cities.fieldsdescriptions[fieldname]
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

    with open(htmlfilename + ".html", "w") as htmlfile:
        line = prettify(taghtml)
        print(line)
        htmlfile.write(str(line)+"\n")

    htmlfilename = htmlfilename + "table"
    html_table_field(cities_sorted,fieldname,htmlfilename)