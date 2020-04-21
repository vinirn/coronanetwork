from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

from htmlutils import prettify 
from stateUtils import getStateName

def html_table_field(cities_sorted,fieldname,htmlfilename):

    taghtml = Element('html')

    comment = Comment('By Marcos Vinicius Candido Henriques, UFERSA-RN-Brazil')
    taghtml.append(comment)

    taghead = SubElement(taghtml, 'head')
    tagcss  = SubElement(taghead, 'link',{'rel':"stylesheet",'type':"text/css",'href':"style.css"})
    tagbody = SubElement(taghtml, 'body')

    tagdiv      = SubElement(tagbody, 'div',{'align':"center"})
    tagh1       = SubElement(tagdiv,'h1')
    tagh1.text  = getStateName(cities_sorted.state_sel)
    tagh2       = SubElement(tagdiv,'h2')
    tagh2.text  = cities_sorted.fieldsdescriptions[fieldname]
    tagp        = SubElement(tagdiv,'p')
    tagp.text   = 'Fonte: G1'
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
            tagtr       = SubElement(tagtable, 'tr')
            tagtd       = SubElement(tagtr,'td')
            tagtd.text  = str(cont)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.name)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.state)
            tagtd       = SubElement(tagtr, 'td')
            tagtd.text  = str(city.fields[fieldname])

    with open(htmlfilename + ".html", "w") as htmlfile:
        line = prettify(taghtml)
        print(line)
        htmlfile.write(str(line)+"\n")
