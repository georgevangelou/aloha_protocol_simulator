'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import ini
import numpy as np
from ini import black_width_ratio as bwr
from matplotlib import pyplot as plt


'''---------------------------------------------Classes--------------------------------------------------------------'''

'''
class Plot1

Description:
    Provides methods to create a one plot figure with
    one or more graphs on the same plot

Constructor:
    - Inputs:
        - x (list of floats):
            vector to be plotted on the x - axis
            
            Default: none (Mandatory)
            
        - y (2D list - list of vectors):
            vectors to be plotted on the y - axis
            If y contains only one vector, one plot will be drawn
            If y contains multiple vectors (hence the 2D list), 
            multiple graphs will be drawn on the same plot
            All graphs will be plotted versus x
            
            Default: none (Mandatory)
            
        - colors (list of strings):
            each of its elements represents the color
            of the corresponding graph to be plotted
            
            Default: ["blue"]
            
        - labels (list of strings):
            each of its elements represents the label
            of the corresponding graph if a legend is shown
            
            Default: ["First"]
            
        - linewidth (float):
            represents the linewidth of all graphs
            
            Default: 1.5
                
Fields:     
    - x (list of floats)      
    - y (2D list - list of vectors)  
    - colors (list of strings)
    - labels (list of strings)
    - linewidth (float)

Methods:
    - setLabels:
        - Description:
            Sets the field labels
        - Inputs:
            labels (list of strings): labels to be set
        - Outputs:
            none
            
    - setFig:
        - Description:
            Creates a figure with a specified title and size
        - Inputs:
            figTitle (string): Title of the figure to be created
            figsize (2 element tuple): Size of the figure
                Default: (8,8)
        - Outputs:
            none
            
    - setPlotTitle:
        - Description:
            Creates a plot with a specified title
        - Inputs:
            plotTitle (string): Title of the plot to be created
        - Outputs:
            none
            
    - setXLabel:
        - Description:
            Sets the specified plot's xlabel 
        - Inputs:
            xlabel (string): xlabel of the plot to be created
            color (string): xlabel's color
                Default: "black"
        - Outputs:
            none
     
    - setYLabel:
        - Description:
            Sets the specified plot's ylabel 
        - Inputs:
            ylabel (string): ylabel of the plot to be created
            color (string): ylabel's color
                Default: "black"
        - Outputs:
            none  
            
    - draw:
        - Description:
            Draws the graph vectors contained in y versus
            vector x
        - Inputs:
            none
        - Outputs:
            none
            
    - show:
        - Description:
            Shows the current plot on the figure window
        - Inputs:
            none
        - Outputs:
            none
            
    - enableGrid:
        - Description:
            Enables grid on the current plot
        - Inputs:
            none
        - Outputs:
            none
    
    - enableAutoscale:
        - Descrption:
            Autoscales axes to match plotted vectors min / max values
        - Inputs:
            none
        - Outputs:
            none
            
    - showLegend:
        - Description:
            Shows the legend on the plot
        - Inputs:
            location (string): Specifies the location in which
            the legend will be put
                Default: "upper right"
        - Outputs:
            none            
'''
class Plot1:
    x = []
    y = []
    colors = ["blue"]
    labels = ["First"]
    linewidth = 1.5

    def __init__(self, x, y, colors=["blue"], labels=["First"], linewidth=1.5):
        self.x = x
        self.y = y
        self.colors = colors
        self.labels = labels
        self.linewidth = linewidth

    def setLabels(self, labels):
        self.labels = labels

    def setFig(self, figTitle, figsize=(8, 8)):
        plt.figure(figTitle, figsize=figsize)

    def setPlotTitle(self, plotTitle):
        plt.title(plotTitle)

    def setXLabel(self, xlabel, color="black"):
        plt.xlabel(xlabel, color=color)

    def setYlabel(self, ylabel, color="black"):
        plt.ylabel(ylabel, color=color)

    def draw(self):
        for i in range(len(self.y)):
            width = self.linewidth
            if (self.colors[i]=='black'): width = bwr*width
            plt.plot(self.x, self.y[i], color=self.colors[i], linewidth=width, label=self.labels[i])

    def show(self):
        plt.show()

    def enableGrid(self):
        plt.grid(True)

    def enableAutoscale(self):
        plt.autoscale(enable=True, axis="both", tight=True)

    def showLegend(self, location="upper right"):
        plt.legend(loc=location)


'''---------------------------------------------Functions--------------------------------------------------------------'''

def random_colors(numberofcolors):
    d = int(numberofcolors/3)
    colors = []
    space = int(255/d)
    for i in range(1,255, space): 
        for j in range(1, 255, space): 
            for k in range(1, 255, space): 
                red = (int(255/i)+randint(1,30)) % 255
                green = (int(255/j)+randint(1,30)) % 255
                blue = (int(255/k)+randint(1,30)) % 255
                colors.append(rgb2hex(red, green, blue))
    return colors


def plot2functions(x, y, colors=['blue', 'red'], labels=['function1','function2'],
                   figTitle='Figure', plotTitle='Plot', xlabel='x', ylabel='y'):
    plot = Plot1(x, y, colors=colors, labels=labels, linewidth=1.5)
    plot.setFig(figTitle=figTitle, figsize=(5, 5))
    plot.setPlotTitle(plotTitle)
    plot.draw()

    plot.setXLabel(xlabel=xlabel)
    plot.setYlabel(ylabel=ylabel)
    plot.showLegend()
    plot.enableGrid()
    plot.enableAutoscale()
    plot.show()
    return plot

def plotMultipleFunctions(x, y, colors, labels, figTitle='Figure',
                          plotTitle='Plot', xlabel='x', ylabel='y', indexX=0, indexY=0):
    plot = Plot1(x, y, colors=colors, labels=labels, linewidth=2)
    plot.setFig(figTitle=figTitle)
    plot.setPlotTitle(plotTitle)
    plot.draw()

    plot.setXLabel(xlabel=xlabel)
    plot.setYlabel(ylabel=ylabel)
    plot.showLegend()
    plot.enableGrid()
    #plot.enableAutoscale()
    #plot.show()
    mngr = plt.get_current_fig_manager()
    wsX = ini.window_size_X 
    wsY = ini.window_size_Y 
    geom = str( str(wsX)+'x'+str(wsY)+'+'+str(wsX*indexX)+'+'+str(wsY*indexY)  )
    mngr.window.geometry(geom)
   
    return plot

