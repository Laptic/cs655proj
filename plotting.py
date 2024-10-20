import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Pool, Process

x_vals = []
y_vals = []

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['timeOf']
    y = data['throughput']

    plt.cla()

    plt.plot(x,y)

def createPlot():
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.tight_layout()
    plt.show()

def startPlotting():
    p = Process(target=createPlot)
    p.start()
