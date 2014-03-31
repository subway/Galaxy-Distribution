#!/usr/bin/env python
import sys.argv as arg

def makeScatterPlot(path, header, xval, yval, xlabel, ylabel, plotTitle):
    tmp = plt.scatter(xval, yval)
    plt.axis([0, max(xval)+5, 0, max(yval)+5])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plotTitle)
    #plt.legend(tmp, header, scatterpoints=1, loc='lower left', ncol=3, fontsize=10)
    plt.savefig(path+'/latestXYplot.jpeg')
    plt.close()
makeScatterPlot(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6]):
    
