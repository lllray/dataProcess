#单个时间处理

运行脚本time_count_plot.py
#三个参数，第一个为脚本文件路径，第二个为时间log路径，第三个为输出路径，如下：
python3 time_count_plot.py ~/logs/LegoLoam/2020-12-21-18-39-47_time.txt ~/Data/lego_loam_data/time_output/





1. 安装matplotlib
#ImportError: No module named 'matplotlib'

执行：
pip3 install --upgrade pip --user
pip3 install matplotlib

2. 安装python3-tk
#ImportError: No module named '_tkinter', please install the python3-tk package

执行：
sudo apt-get install python3-tk 

3. 运行脚本time_count_plot.py
修改脚本time_count_plot.py
#将items修改为自己需要可视化的item，2-5个为佳，3个最合适
items = {"Timer_FeatureExtraction": {}, "Timer_FeatureAssociation": {}, "Timer_MapFilter":{}}

#修改下面代码，若可视化三个item，则为311; 若为四个item，则为411
seq = 311 + count

运行脚本time_count_plot.py
#三个参数，第一个为脚本文件路径，第二个为时间log路径，第三个为输出路径，如下：
python3 time_count_plot.py ~/logs/LegoLoam/2020-12-21-18-39-47_time.txt ~/Data/lego_loam_data/time_output/


