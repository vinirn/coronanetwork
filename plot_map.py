import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import re

from stateUtils import getStateAbbreviation

class Ring:
    coordstxt = ""
    coordslist = ""
    longs = []
    lats = []

class StateBounds:
    name = ""
    region = ""
    rings = []
    def func(self):
        print("This is a message inside the class.")

def plot_brazil(param_state = "ALL", bordercolor=[0.0,0.0,0.0]):

    tree = ET.parse("./maps/br_unidades_da_federacao/unidades_federacao.gml")

    root = tree.getroot()

    states = []

    for unit in root.findall(
            "{http://www.opengis.net/gml}featureMember/"
            "{http://ogr.maptools.org/}unidades_federacao"):
        state = StateBounds()
        state.coordslist = []
        state.rings = []
        for coordinate in unit.findall(
                "{http://ogr.maptools.org/}geometryProperty/"
                "{http://www.opengis.net/gml}MultiPolygon/"
                "{http://www.opengis.net/gml}polygonMember/"
                "{http://www.opengis.net/gml}Polygon/"
                "{http://www.opengis.net/gml}outerBoundaryIs/"
                "{http://www.opengis.net/gml}LinearRing/"
                "{http://www.opengis.net/gml}coordinates"):
            ring = Ring()
            ring.coordstxt = coordinate.text
            ring.coordslist = re.split(',| ',ring.coordstxt)
            ring.longs=[]
            ring.lats=[]
            state.rings.append(ring) 
        
        statename = unit.find("{http://ogr.maptools.org/}NM_ESTADO")
        state.name = getStateAbbreviation(statename.text)
        print(state.name,end=" ")
        
        states.append(state)

    for istate in range(0,len(states)):
        for iring in range(0,len(states[istate].rings)):
            coord_num = 0
            for coord in states[istate].rings[iring].coordslist:
                coord_num+=1
                if (coord_num % 2) ==1:
                    states[istate].rings[iring].longs.append(float(coord))
                else:
                    states[istate].rings[iring].lats.append(float(coord))
        

    for state in states:
        if (param_state.upper()=="ALL") or (state.name == param_state.upper()):
            for ring in state.rings:
                plt.plot(ring.longs,ring.lats,'-',linewidth = 1, color=bordercolor)
    plt.gca().set_aspect('equal', adjustable='box')
    #plt.show()   

            