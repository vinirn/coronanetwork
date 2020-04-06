import shapefile
import matplotlib.pyplot as plt
import numpy as np

i = 0
sf = shapefile.Reader('shapefile')
sr = sf.shapeRecords()
max = 10


while i < max:
    sr_obj = sr[i]
    sr_points = np.array(sr_obj.shape.points)
    records = sf.record(i)
    numfloors = records[42]
    x = sr_points[:,0]
    y = sr_points[:,1]
    sr_plot = zip(*sr_points)
    plt.plot(*sr_plot)
    i = i + 1

plt.show()