# 查看并发连接数：
	netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'返回结果示例： 
	LAST_ACK 5   (正在等待处理的请求数) 
	SYN_RECV 30 
	ESTABLISHED 1597 (正常数据传输状态) 
	FIN_WAIT1 51
	FIN_WAIT2 504 
	TIME_WAIT 1057 (处理完毕，等待超时结束的请求数)  
	状态：描述 
	CLOSED：无连接是活动的或正在进行 
	LISTEN：服务器在等待进入呼叫 
	SYN_RECV：一个连接请求已经到达，等待确认
	SYN_SENT：应用已经开始，打开一个连接 
	ESTABLISHED：正常数据传输状态 
	FIN_WAIT1：应用说它已经完成 
	FIN_WAIT2：另一边已同意释放 
	ITMED_WAIT：等待所有分组死掉
	CLOSING：两边同时尝试关闭 
	TIME_WAIT：另一边已初始化一个释放
	LAST_ACK：等待所有分组死掉
	只查看当前正在传 netstat -nat|grep ESTABLISHED|wc -l
	查看有多少个进程数 ps aux |grep httpdwc -l

# kill 进程
	 kill -9 pid, killall process name
	 kill -9 `ps aux | grep <proc_key_word> | grep -v grep | awk '{print $2}' `或者
	 ps aux | grep  <proc_key_word> | grep -v grep | awk '{print $2}' | xargs kill -9 

1. 修改时区
   dpkg-reconfigure tzdata 立即生效
   tzselect
2. 查看网络ip,dns
   nm-tool
3. 同步网络时间
   ntpdate cn.pool.ntp.org
4. 查看内存cpu占用
   htop
5. 查看进程号
   ps aux |grep python
6. 网络并发
    netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'