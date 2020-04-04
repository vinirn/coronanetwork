import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from plot_map import plot_brazil

state_sel = "ALL"
text_population_threshold = 1000000

bordercolor = .7*np.array([1.0,1.0,1.0])

plot_brazil(state_sel, bordercolor)

csvfilename = "./data/cities2.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    num=0
    names = []
    states=[]
    longs = []
    lats = []
    populations = []
    for row in spamreader:
        num+=1
        #print(';\t'.join(row))
        
        citycode        = row[0]
        cityname        = row[1]
        citystate       = row[2]
        citypopulation  = row[3]
        citylong        = row[4]
        citylat         = row[5]
        
        #if citystate=="CE":
        names.append(cityname)
        states.append(citystate)
        longs.append(float(citylong))
        lats.append(float(citylat))
        populations.append(float(citypopulation))

        print("("+str(num)+"/"+str(numlines)+") "+"Reading "+cityname)
 
sizes = np.log(np.array(populations))**1.0
sizes = sizes - np.min(sizes) + 1
print(sizes)
print(np.min(sizes))
print(np.max(sizes))

crainbow = cm.rainbow(np.linspace(1, 0, len(sizes)))
colors = crainbow
maxpopulation = np.max(populations)
ncities = len(populations)
for icity in range(0,ncities):
    population = populations[icity]
    cindex = np.floor((population/maxpopulation)*ncities)
    colors[icity] = crainbow[icity]
    
print(colors)

#plt.scatter(longs,lats, s=sizes, c=colors)


for icity in range(0,ncities):
    if (states[icity]==state_sel) or (state_sel=="ALL"):
        plt.plot(longs[icity],lats[icity],'o',
                markerfacecolor=colors[icity],markeredgecolor=colors[icity],
                markersize = sizes[icity])
        if populations[icity]>text_population_threshold:
            plt.text(longs[icity], lats[icity], names[icity], 
                        fontsize=sizes[icity],
                        bbox=dict(facecolor=colors[icity], edgecolor='none', alpha=0.2, pad=0.0))

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()
