import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys
import os

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
# "Timer_pointTrans": {}, ,  

items = {"Timer_FeatureExtraction": {}, "Timer_FeatureAssociation": {}, "Timer_MapFilter":{}}
color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#48D1CC', '#FF7F50',  '#778899',  'y', 'k', 'coral','darkcyan','gold','teal','pink']

def readFileAndPlot(file, path = None):
    f = open(file, 'r')
    acc_time_dict = {}
    for line in f.readlines():
        lst = line.split(" ")
        print(lst[0])
        timestamp = eval(lst[0][-7:-1])
        acc_time_dict[timestamp] = 0
        key = lst[2][:-1]
        if key in items:
            time = eval(lst[-1][:-3])
            if time > 1000:
                print(time)
            #     continue
            items[key][timestamp] = time
    items_keys = list(items.keys())
    count = 0
    for item_key in items_keys:
        time_dict = items[item_key]
        timestamp_lst = list(time_dict.keys())
        timestamp_lst.sort()
        timelst = []
        last_y = []
        for timestamp in timestamp_lst:
            timelst.append(time_dict[timestamp])
            # last_y.append(acc_time_dict[timestamp])
            # # timelst = [timelst[i]+last_y[i] for i in range(len(timelst))]
            # acc_time_dict[timestamp] += time_dict[timestamp]
        # plt.plot(timestamp_lst, timelst, color=color_list[count], label = item_key)
        avt_time = round(np.mean(timelst),2)
        seq = 311 + count
        plt_temp = plt.subplot(seq)
        #plt.bar(range(len(timestamp_lst)), timelst, width = 0.8, color = color_list[count],label=[items_keys[count]+ "  average: " + str(avt_time)+"ms"])
        plt_temp.plot(timestamp_lst, timelst, color = color_list[count],label=[items_keys[count]+ "  average: " + str(avt_time)+"ms"])
        plt_temp.legend()
        count += 1
    plt.ylabel("use time/(ms)")
    plt.xlabel("timestamp")
    #plt.ylim(-10, 1000)
    #plt.xlim(30, 45)
    if path != None:
        filetime = file.split("/")[-1][:-9]
        if not os.path.exists(path+ "/"+filetime):
            os.mkdir(path+ "/"+filetime)
        plt.savefig(path + "/" + filetime + "/" + item_key + ".png", dpi = 300)
    if path == None:
        plt.show()

    plt.show()


if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 cpuloading_plot.py filename writepath")
    else:
        readFileAndPlot(sys.argv[1], sys.argv[2])
