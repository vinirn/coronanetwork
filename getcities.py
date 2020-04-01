import sys
import urllib.request, urllib.error, urllib.parse
from stringUtils import getQuotesParam
from stateAbbreviation import getStateAbbreviation

csvfilename = "cities.csv"
csvfile = open(csvfilename, 'w')

url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o'

print("Getting URL...")
response = urllib.request.urlopen(url)
webContent = str(response.read())

pos = webContent.find(r'<table class="wikitable sortable" style="text-align: center;">')
num=0
while True:

    lineStart = webContent.find(r'<tr>',pos)
    if lineStart<1:
        break
    pos = lineStart

    num+=1
    print(num,end='\t')

    href, pos = getQuotesParam(webContent,"href",pos)

    cityName, pos = getQuotesParam(webContent,"title",pos)
    cityPrint = cityName.ljust(32,' ')
    print(cityPrint,end='\t')

    stateName, pos = getQuotesParam(webContent,"title",pos)
    stateName = stateName.replace(" (estado)","")
    stateName = stateName.strip()
    stateAbbreviation = getStateAbbreviation(stateName)
    statePrint = stateAbbreviation.ljust(4,' ')
    print(statePrint,end='\t')

    token = r'<td style="text-align:right;">'
    paramStart = webContent.find(token,pos)
    paramEnd = webContent.find(r'\n</td>',paramStart+len(token))
    population = webContent[(paramStart+len(token)):(paramEnd)]
    print(population,end='\t')

    print(href,end='\t')

    csvfile.write(str(num)+";"+cityName+";"+stateAbbreviation+";"+str(population)+";"+href+"\n")

    print()

csvfile.close()