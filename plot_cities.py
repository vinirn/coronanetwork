import numpy as np
import csv
import matplotlib.pyplot as plt

csvfilename = "./data/cities2.csv"

with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    numlines = len(list(spamreader))


with open(csvfilename, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    num=0
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

        longs.append(float(citylong))
        lats.append(float(citylat))
        populations.append(float(citypopulation))

        print("("+str(num)+"/"+str(numlines)+") "+"Reading "+cityname)
        
#plt.plot(longs, lats, 'ro', markersize=1)
#plt.axis([0, 6, 0, 20])
#plt.gca().set_aspect('equal', adjustable='box')
#plt.show()
        
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

print(np.log(populations))

plt.scatter(longs,lats, s=np.log(populations))
plt.gca().set_aspect('equal', adjustable='box')
plt.show()