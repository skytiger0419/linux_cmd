# fabric 批量运维机器
	fab -l 查看可运行任务
	1.单个任务运行
	  fab task:host=xxx.xx.xx.xx --此处为ip地址
	2. 批量运行
	  vim ip_list.txt 添加ip列表
	  fab task -P -z 5    --此处5为并发运行数，可视实际情况而定
	资源样例文件 resource/fabfile.py
	
	选择机器配置
	1. 如果是单台机器 fab new_machine:host=xxx.xx.xx.xx  --此处为ip地址
	2. 如果是多台机器，请在ip_list.txt加入ip列表，运行fab new_machine -P -z 5   --此处5为并行运行机器数量，视情况而定

