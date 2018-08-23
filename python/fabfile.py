#coding=utf-8
'''
Created on 2018年03月1日

@author: ningruhu

-l #显示定义好的任务函数名
-f #指定fab入口文件，默认入口文件名为fabfile.py
-f #指定网关（中转）设备，比如堡垒机环境，填写堡垒机IP即可
-H #指定目标主机，多台主机用‘,’号分隔
-p #远程账号的密码，fab执行时默认使用root账户
-P #以异步并行方式运行多主机任务，默认为串行运行
-R #指定role（角色），以角色名区分不同业务组设备
-t #设置设备连接超时时间（秒）
-T #设置远程主机命令执行超时时间（秒）
-w #当命令执行失败，发出警告，而非默认中止任务。
'''
from fabric.api import *
import os,time

# 登录用户和主机名：
env.user = 'root'
env.password = '123456'
env.hosts = ['172.16.15.108'] # 如果有多个主机，fabric会自动依次部署

if os.path.exists("ip_list.txt"):
    with open("ip_list.txt") as f:
        env.hosts = map(lambda x: x.strip(), f.readlines())
local_agent_file = '/mnt/install_agent/raptorAgent1.3.6.zip'


def upgrade_all(): # 升级所有机器的相关文件
    remote_agent_dir = "/opt/raptorAgent"
    run('service supervisor stop') # 停止监控服务
    time.sleep(2)
    with settings(warn_only=True):
        run('killall java') # 删除所有java进程
    with settings(warn_only=True):
        run('killall adb') # 删除所有adb进程
    time.sleep(5)
    run('rm -rf %s'%remote_agent_dir) # 删除agent所有文件
    put(local_agent_file,'/opt/raptorAgent.zip')
    with cd('/opt'):
        run('unzip raptorAgent.zip')
        run('cd raptorAgent;chmod +x raptor-agent.sh')
    run('rm /opt/raptorAgent.zip')
    # 恢复服务
    run('service supervisor start') # 开启监控服务
    try:
      reboot(wait=5)
    except:
      pass

def upgrade_jar(): # 升级所有机器的jar包
    # 远程服务器的临时文件：
    remote_opt_tar = '/opt/raptorAgent/raptorAgent.jar'
    run('rm  %s' % remote_opt_tar)
    # 上传tar文件至远程服务器：
    put('/mnt/install_agent/raptorAgent.jar', remote_opt_tar) 
    #重启服务器
    run('killall java')

def install_agent_resource():
    #上传所需文件
    put('/mnt/install_agent/android-sdk.tar.gz','/opt/android-sdk.tar.gz')
    put('/mnt/install_agent/node.zip','/opt/node.zip')
    put(local_agent_file,'/opt/raptorAgent.zip')
    with cd('/opt'):
        #解压文件
        run('tar zxvf android-sdk.tar.gz')
        run('unzip node.zip')
        run('unzip raptorAgent.zip')
        run('cd raptorAgent;chmod +x raptor-agent.sh') #赋予执行权限
        #删除原始文件
        run('rm android-sdk.tar.gz')
        run('rm node.zip')
        run('rm raptorAgent.zip')
    #配置环境变量
    run('echo "export ANDROID_HOME=/opt/android-sdk">>/etc/profile')
    run('echo "export NODE_HOME=/opt/node">>/etc/profile')
    run("echo 'export PATH=$NODE_HOME/bin:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH' >>/etc/profile")
    run('rm -rf /usr/bin/adb')
    run('ln -s /opt/android-sdk/platform-tools/adb /usr/bin/adb')
    run('rm -rf /usr/bin/node')
    run('ln -s /opt/node/bin/node /usr/bin/node')
    run('source /etc/profile')
    #配置所需环境
    run('add-apt-repository -y ppa:openjdk-r/ppa')
    run('apt-get update')
    run('apt-get install -y openjdk-8-jdk')
    run('apt-get install -y supervisor nfs-kernel-server')
    #配置共享目录
    with cd('/mnt'):
        run('mkdir raptor_result')
    run('echo "/mnt/raptor_result *(rw,no_root_squash)" >>/etc/exports')
    run('service nfs-kernel-server restart')
    #配置自动重启
    run('cd /etc/supervisor/conf.d;touch raptorAgent.conf')
    run('echo [program:raptor-agent] >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo command=/opt/raptorAgent/raptor-agent.sh >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo numprocs=1 >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo autostart=true >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo autorestart=true >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo user=root >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo startsecs=10 >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo startretries=5 >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo redirect_stderr=true >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('echo stdout_logfile=/var/log/raptor-agent.log >>/etc/supervisor/conf.d/raptorAgent.conf')
    run('service supervisor restart')

def install_older_test():
    run('apt-get install -y python-pip python-opencv curl')
    run('pip install nose uiautomator uiautomatorplug urllib3 customnoseplugins raptorlink -i http://pypi.douban.com/simple')
def install_tmp():
    run('pip install -U customnoseplugins raptorlink -i http://pypi.douban.com/simple')  	
def new_machine():
    install_agent_resource()
    install_older_test()
    reboot(wait=5)
