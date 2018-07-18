## 查看慢查询
	mysql> show variables like 'slow_query%'; 
	Variable_name             | Value                            |
	|slow_query_log            | OFF                              |
	| slow_query_log_file       | /mysql/data/localhost-slow.log   |
	
	mysql> show variables like 'long_query_time';
	+-----------------+-----------+| 
	Variable_name   | Value     |
	+-----------------+-----------+|
	long_query_time | 10.000000 |
	+-----------------+-----------+
## 开启慢查询收集
	将 slow_query_log 全局变量设置为“ON”状态
	mysql> set global slow_query_log='ON'; 
	设置慢查询日志存放的位置
	mysql> set global slow_query_log_file='/usr/local/mysql/data/slow.log';
	查询超过1秒就记录
	mysql> set long_query_time=1;