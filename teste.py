import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np

from plot_map import plot_brazil

state_sel = "all"

bordercolor = .7*np.array([1.0,1.0,1.0])
plot_brazil(state_sel, bordercolor)

