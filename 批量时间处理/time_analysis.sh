#!/bin/bash
project_path=$(cd `dirname $0`; pwd)
TimePlot=$project_path"/py/time_count_plot.py"
TimeSummary=$project_path"/py/time_summary.py"
TimeSummaryTxt="time_summary.txt"
Node="LegoLoam"
Time="time"
function plot_time(){
for file in `ls $1` #遍历所有文件
do
 if [ -d $1"/"$file ]&&[[ $file == *$Node* ]] #判断子目录是否需要遍历
 then
    plot_time $1"/"$file $2
 elif [[ $file == *$Time* ]] #判断是否为时间文本
 then
   echo "Process: "$1"/"$file #在此处处理文件即可
   python3 $TimePlot $1"/"$file $2
 else
   echo "Ignore: "$1"/"$file
 fi
done
}

#第一个参数是输入文件 第二个参数是输出文件夹
plot_time $1 $2

python3 $TimeSummary $2"/"$TimeSummaryTxt $2
