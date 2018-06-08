# 免密登录
	用户目录下.netrc，可以实现免密登录，如git,ftp
	machine 192.168.0.1login ftpuser 
	password ftpuser_password
	https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html

# ubuntu添加启动项
	运行命令创建desktop文件：
	    sudo gedit /usr/share/applications/android_studio.desktop
	打开窗口后输入以下内容，注意Exec和Icon要修改成自己系统下Android Studio的路径。
	[Desktop Entry]
	Type=Application
	Name=Android Studio
	Exec="/opt/android-studio/bin/studio.sh" %f
	Icon=/opt/android-studio/bin/studio.png
	Categories=development;IDE;
	Terminal=false
	StartupNotify=true
	StartupWMClass=jetbrains-android-studio
	保存关闭文件，运行以下命令添加执行权限：
	sudo chmod +x /usr/share/applications/android_studio.desktop
	之后，使用命令打开applications文件夹：
	sudo nautilus /usr/share/applications
	找到android_studio.desktop文件，把文件拖动到Launcher条上。

