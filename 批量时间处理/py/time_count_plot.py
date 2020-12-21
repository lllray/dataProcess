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
items = { "Timer_FeatureExtraction":{}, "Timer_FeatureAssociation": {},  "Timer_processPointcloud": {}}
color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#48D1CC', '#FF7F50',  '#778899',  'y', 'k', 'coral','darkcyan','gold','teal','pink']

def readFileAndPlot(file, path = None):
    f = open(file, 'r')
    f_t = open(path+"/time_summary.txt", 'a+')
    acc_time_dict = {}
    start_time = 0
    for line in f.readlines():
        lst = line.split(" ")
        if len(lst)!=4 :
               break;
        if lst[3][-2]!='s':
               break;
        #if len(lst[0])!=17:
         #      break;
        if start_time == 0:
               start_time = 36000*eval(lst[0][4:5]) + 3600*eval(lst[0][5:6]) + 600 * eval(lst[0][7:8]) + 60 * eval(lst[0][8:9]) + eval(lst[0][-7:-1])

        timestamp = 36000*eval(lst[0][4:5]) + 3600*eval(lst[0][5:6]) + 600 * eval(lst[0][7:8]) + 60 * eval(lst[0][8:9]) + eval(lst[0][-7:-1]) - start_time
	
        acc_time_dict[timestamp] = 0
        key = lst[2][:-1]
        if key in items:
            time = eval(lst[-1][:-3])
            #if time > 1000:
            #     print(time)
            #     continue
            items[key][timestamp] = time
    items_keys = list(items.keys())
    count = 0
    num = 0
    for item_key in items_keys:
        time_dict = items[item_key]
        #print(len(time_dict))
        if len(time_dict)>0 :
             num=num+1
    if num!=3 :
        return;
    for item_key in items_keys:
        time_dict = items[item_key]
        timestamp_lst = list(time_dict.keys())
        timestamp_lst.sort()
        timelst = []
        last_y = []
        #if len(timelst)==0 :
         #    f_t.write("0 0 ")
          #   break;
        for timestamp in timestamp_lst:
            timelst.append(time_dict[timestamp])
            # last_y.append(acc_time_dict[timestamp])
            # # timelst = [timelst[i]+last_y[i] for i in range(len(timelst))]
            # acc_time_dict[timestamp] += time_dict[timestamp]
        # plt.plot(timestamp_lst, timelst, color=color_list[count], label = item_key)
        avt_time = round(np.mean(timelst),2)
        f_t.write(str(avt_time)+" "+str(max(timelst))+" ")
        seq = 311 + count
        plt_temp = plt.subplot(seq)
        #plt.xlim(0, 60)
        #plt.ylim(0, 60)
        #plt.bar(range(len(timestamp_lst)), timelst, width = 0.8, color = color_list[count],label=[items_keys[count]+ "  average: " + str(avt_time)+"ms"])
        plt_temp.plot(timestamp_lst, timelst, color = color_list[count],label=[items_keys[count]+ "  average: " + str(avt_time)+"ms"])
        plt_temp.legend()
        count += 1
    plt.ylabel("time-consuming/(ms)")
    plt.xlabel("timestamp")
    #plt.ylim(-10, 1000)
    #plt.xlim(150, 250)
    f_t.write('\n')
    if path != None:
        filetime = file.split("/")[-1][:-4]
        if not os.path.exists(path+ "/figure"):
            os.mkdir(path+ "/figure")
        plt.savefig(path + "/figure" + "/" + filetime + ".png", dpi = 300,bbox_inches='tight')

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 cpuloading_plot.py filename writepath")
    else:
        readFileAndPlot(sys.argv[1], sys.argv[2])
