import matplotlib.pyplot as plt

def plot_cities(cities, state_sel="ALL", pngfile = "cities.png"):

    ncities = len(cities)

    for icity in range(ncities-1,-1,-1):
        if (cities[icity].state==state_sel.upper()) or (state_sel.upper()=="ALL"):
            plt.plot(cities[icity].long,cities[icity].lat,'o',
                    markerfacecolor=cities[icity].plotcolor,
                    markeredgecolor=cities[icity].plotcolor,
                    markersize = cities[icity].plotsize)
            if cities[icity].showname:
                plt.text(
                            cities[icity].long, 
                            cities[icity].lat, 
                            cities[icity].plottext,
                            color = [0.0, 0.0, 0.0, cities[icity].plotcolor[3]], 
                            fontsize = cities[icity].plotfontsize,
                            bbox = dict(
                                facecolor=cities[icity].plotcolor, 
                                edgecolor='none', 
                                alpha=0.2, 
                                pad=0.0)
                            )

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    #mng = plt.get_current_fig_manager()
    #mng.frame.Maximize(True)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.savefig(pngfile)
    #plt.show()
    
