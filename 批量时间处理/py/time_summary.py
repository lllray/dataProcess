from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import sys
fig = plt.figure()

def call_back(event):
    axtemp=event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    fanwei = (x_max - x_min) / 10
    fanwei1 = (y_max - y_min) / 10
    if event.button == 'up':
        axtemp.set(xlim=(x_min + fanwei, x_max - fanwei))
        axtemp.set(ylim=(y_min + fanwei1, y_max - fanwei1))
        #print('up')
    elif event.button == 'down':
        axtemp.set(xlim=(x_min - fanwei, x_max + fanwei))
        axtemp.set(ylim=(y_min - fanwei1, y_max + fanwei1))
        #print('down')
    fig.canvas.draw_idle()  
fig.canvas.mpl_connect('scroll_event', call_back)
fig.canvas.mpl_connect('button_press_event', call_back)
# load data from file
# you can replace this using with open
items = [ 'Timer_FeatureExtraction', 'Timer_FeatureAssociation',  'Timer_processPointcloud']

def readFileAndPlot(file, path = None):
    data = np.loadtxt(file)
    first_1 = data[:, 0]
    second_1 = data[:, 1]
    first_2 = data[:, 2]
    second_2 = data[:, 3]
    first_3 = data[:, 4]
    second_3 = data[:, 5]

## draw the figure, the color is r = read
#'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'
    seq = 311 + 0
    plt_temp1 = plt.subplot(seq)
    plt.title("Time Summary")
    plt_temp1.plot(second_1, c='r',alpha=0.9,linewidth=2,label=items[0]+" Max")
    plt_temp1.plot(first_1, c='r',alpha=0.5,linewidth=2,label=items[0]+" Average")

    plt_temp1.legend()

    seq = 311 + 1
    plt_temp2 = plt.subplot(seq)
    plt_temp2.plot(second_2, c='g',alpha=0.9,linewidth=2,label=items[1]+ ' Max')
    plt_temp2.plot(first_2, c='g',alpha=0.5,linewidth=2,label=items[1]+ ' Average')

    plt_temp2.legend()

    seq = 311 + 2
    plt_temp3 = plt.subplot(seq)
    plt_temp3.plot(second_3, c='b',alpha=0.9,linewidth=2,label=items[2] + ' Max')
    plt_temp3.plot(first_3, c='b',alpha=0.5,linewidth=2,label=items[2] + ' Average')

    plt_temp3.legend()
#plt.plot(first_4, second_4, c='black',label='5_3')
    plt.legend()
#plt.gcf().set_facecolor(np.ones(3)* 240 / 255) 
#plt.grid(ls='--')
#plt.hlines(0, 0, 50, colors = "y", linestyles = "dashed")
#plt.hlines(1, 0, 50, colors = "y", linestyles = "dashed")
#plt.xlim(30, 100)
    plt.xlabel("req")
    plt.ylabel("time consuming/ms")
#plt.scatter
    #plt.show()
    plt.savefig(path +"/time_summary.png", dpi = 300)

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 cpuloading_plot.py filename writepath")
    else:
        readFileAndPlot(sys.argv[1], sys.argv[2])
