下载
使用基于关系的度量标准 对CARMEN -logfiles和关系文件的评估工具：
下载度量评估程序（.tar.gz，ANSI C ++源文件）。
参数：
make
 error: ‘vasprintf’ was not declared in this scope
add
#include <stdio.h> 
#include <stdarg.h> 
#include <stdlib.h> 
#include <string.h> 
用法：./ metricEvaluator [options]

选项：
-------------------------------------------
-s <name>包含ROBOTLASER1数据的slam日志文件
-r <relations>关系文件
-o <odometry>原始odometry日志文件
-w“{wx，wy，wz，wphi，wtheta，wpsi}”错误权重向量（单位米/拉）
-q使用平方误差计算平均值（而不是平方误差的平方）
-e <errorfile>写入avg，std偏差，测量次数
-eu <errorfile>写入错误列表（未排序）
-em <errorfile>写入错误列表（按大小排序）
-e1 <errorfile>写入错误列表（按第一关系时间戳排序）
-e2 <errorfile>写入错误列表（按第二关系时间戳排序）
两个基本输入是SLAM日志文件，它应包含carmen样式的ROBOTLASER1或FLASER消息以及下面描述格式的关系文件。另外，程序想要一个错误权重向量来计算一个数字。合理的值是1.0,1.0,1.0,0.0,0.0,0.0得到平移，0.0,0.0,0.0,1.0,1.0,1.0得到旋转误差。可选地，当在关系的0.1s内没有找到相应的时间戳时，您可以传递包含测距数据（作为CARMEN ODOM）的日志文件，该日志文件将用于校正SLAM位置。通过激活-q选项，将计算平方误差。如果没有-q，您将获得正常的欧几里德距离误差（用于翻译）。
输出
有两种不同的输出：
平均错误和其他参数可以作为文档（-e）写入文件。
此外，-eX选项可以使用不同的排序选项将各个关系引入的错误写入文件。未排序将保持关系文件中的顺序，以便以后进行匹配。
Gnuplot可用于轻松显示此数据：

gnuplot>带点的情节“文件名”
文档
目前有两种文件格式：
我们自己的.relations文件
CARMEN日志文件
关系文件
关系以简单的基于文本的格式给出，如下所示：

#timestamp1 timestamp2 xyz roll pitch yaw
1232658478.161285 1232658644.149293 1.031273 -0.003531 0.000000 0.000000 -0.000000 -0.009755
1232658478.161285 1232658647.058497 2.039538 -0.014451 0.000000 0.000000 -0.000000 -0.016492
每行描述从时间戳1到时间戳2的由x，y，z，滚动，俯仰和偏航给出的关系。时间戳必须与要评估的日志文件中的时间戳匹配。
CARMEN日志文件
CARMEN样式日志文件是基于文本的文件，每行包含一个数据元素。为解析odometry信息，我们支持标准ODOM格式。为解析SLAM输出，我们解析ROBOTLASER1或旧FLASER消息的位置。
以下是具体格式的快速概述：

ODOM xy theta tv rv accel timestamp hostname logger_timestamp
在一行：
ROBOTLASER1 laser_type start_angle field_of_view angular_resolution maximum_range准确度
   remission_mode num_readings [range_readings] num_remissions [remission values] 
   laser_pose_x laser_pose_y laser_pose_theta robot_pose_x robot_pose_y robot_pose_theta laser_tv laser_rv 
   forward_safety_dist side_safty_dist turn_axis timestamp hostname logger_timestamp
FLASER num_readings [range_readings] xy theta odom_x odom_y odom_theta timestamp hostname logger_timestamp
由于我们只关心机器人位置，其他数据，尤其是激光测量可能是不完整的，即，如果机器人没有测距仪，则提供0范围读数。
简单的例子
使用关系评估日志时的工作流程如下：
从网站下载日志文件（例如example.log）并使用您的算法处理ROBOTLASER1日志文件。将结果命名为slam.log
下载引用关系，例如example.relations。
运行metricEvaluator：
metricEvaluator -s slam.log -r example.relations -o example.log -w“{1.0,1.0,1.0,0.0,0.0,0.0}”-eu unsorted.errors
此命令将转换错误写入unsorted.errors并打印出slam.log的平均错误和标准偏差。在大多数情况下，将example.log作为odometry传递，因为原始日志应包含odometry。
