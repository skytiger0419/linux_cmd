1. git clone https://github.com/novnc/noVNC.git


2.安装证书
cd utils
openssl req -new -x509 -days 365 -nodes -out self.pem -keyout self.pem


3. ./utils/launch.sh --vnc localhost:5901


4. 中转模式

1、创建token文件

　　在websockify目录中创建目录token，并在该目录下创建token文件，写入以下内容：
token:  host_ip:port

　　这里需要注意的坑是token:后面是有一个空格的（少了这个空格让我调试了一个夜晚）。



2、启动websockify

　　进入websockify目录 --web ../ 是为了使用noVNC的vnc.html和vnc_lite.html文件
./run --web ../ --target-config ./token/token localhost:8888




3、浏览器测试

　http://localhost:8888/vnc_lite.html?path=?token=vm004　　(这里我直接使用的是虚拟机vm004的名称来作为Token，只需要修改Token就能够访问相应的虚拟机) 







https://www.cnblogs.com/vincenshen/articles/7923402.html