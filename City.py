import numpy as np

class City:
    code = ""
    name = ""
    state = ""
    population = 100
    long = 0.0
    lat = 0.0
    plotsize = 1.0
    plotfontsize = 10.0
    plotcolor = [0.0,0.0,0.0,1.0]
    plottext = ""
    showname = True
    fields = {}

    def __init__(self):
        self.fields={}

    def unify_ambiguous_names(self):
        if (self.name.upper()=="ASSU") and (self.state=="RN"):
            self.name = "Açu"
