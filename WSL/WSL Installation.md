# Windows Subsystem for Linux Installation Notes

## 0. Why WSL?

* 相比于VMware等虚拟机, WSL占用内存和CPU资源更少, 在WSL上运行软件的消耗和直接在Windows上差不多.
* Windows可以与WSL共享文件.
* 无需重启Linux系统, WSL下只需要把软件关掉重开即可.
* 可以直接在Windows下其它地方复制文本内容, 粘贴到WSL.

## 1. Preparation

* This section is for Windows build 16215 or later.
* 在`设置`->`更新和安全`->`开发者选项`中选择开发人员模式.
* 在`控制面板`->`程序`->`启用或关闭Windows功能`中勾选`适用于Linux的Windows子系统`.
* 在微软的应用商店中搜索Linux, 选择合适的Linux分发版(本文以Ubuntu18.04lts为例).

可参考官方说明: [here](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

## 2. Configuration

* 在安装成功后, 首次进入系统需要一点时间, 等待结束后输入`用户名`和`密码`.
* 由于默认的软件源连接速度较慢, 建议切换到国内其他源, 本文以aliyun为例:
  * 将原配置文件备份:
  ```
  sudo cp /etc/apt/sources.list /etc/apt/sources_backup.list
  ```
  * 查看默认源的地址: 
  ```   
  sudo vim /etc/apt/sources.list 
  ```
  * 用vim命令替换: 
  ```
  :%s/security.ubuntu/mirrors.aliyun/g
  :%s/archive.ubuntu/mirrors.aliyun/g
  ```
  * 更新:
  ```
  sudo apt update
  sudo apt upgrade
  ```
  * 关于其他国内源, 参考: [here](https://cloud.tencent.com/developer/article/1538304)
* 其他关于常用工具的配置参考: [here](https://blog.csdn.net/qq_36620040/article/details/90301526?depth_1-utm_source=distribute.pc_relevant)

## 3. GUI

* 由于笔者并不需要用到桌面, 但又需要用到某些GUI软件, 此时可以通过`XServer`实现监听WSL的图形界面数据, 用到的软件是`VcXsrv`.
* 下载地址: [Download VcXsrv](https://sourceforge.net/projects/vcxsrv/)
* 安装与运行一律选择默认.
* 在需要运行WSL的GUI软件之前, 需要提前打开VcXsrv.
* 修改环境参数:
  * 打开~/.bashrc:
  ```
  sudo vim ~/.bashrc
  ```
  * 末尾添加:
  ```
  export DISPLAY=:0.0
  export LIBGL_ALWAYS_INDIRECT=1
  ```
  * 保存并退出vim.
* 此时在WSL中运行GUI软件便可显示在Windows桌面中.

参考: [here](https://blog.csdn.net/Function_RY/article/details/104136732)

笔者遇到的问题: 
```
D-Bus library appears to be incorrectly set up; failed to read machine uuid: Failed to open “/var/lib/dbus/machine-id”
```
解决方案参考: [here](http://www.torkwrench.com/2011/12/16/d-bus-library-appears-to-be-incorrectly-set-up-failed-to-read-machine-uuid-failed-to-open-varlibdbusmachine-id/)

run as root: 
```
dbus-uuidgen > /var/lib/dbus/machine-id
```

## 4. Git

在clone一些国外的repository时, 下载速度经常为几Kib/s 到 几十Kib/s 不等, 为解决该问题, 本文通过在WSL中配置Git代理来实现下载加速.

* 采用命令行:
  ```
  # 具体端口看代理软件的端口
  # http代理：
  git config --global https.proxy http://127.0.0.1:10800 
  git config --global https.proxy https://127.0.0.1:10800
  # socks5代理：
  git config --global http.proxy 'socks5://127.0.0.1:10800'
  git config --global https.proxy 'socks5://127.0.0.1:10800'
  ```
* 或修改文件:
  ```
  # 在文件~/.gitconfig添加：
  [http]
  proxy = socks5://127.0.0.1:10800
  [https]
  proxy = socks5://127.0.0.1:10800
  ```
* 若要取消代理:
  ```
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```

## 5. Windows Terminal

* 在应用商店中下载Windows Terminal.
* 在 `C:\Users\Username\AppData\Local\` 下新建文件夹 `Terminal` .
* 在`Terminal`文件夹中存放图标`Terminal.icon` , 可在本repository `\wt` 中下载.
* 将`Windows Terminal`添加至右键菜单
  *  新建.reg文件添加至注册表
  ```
  Windows Registry Editor Version 5.00

  [HKEY_CLASSES_ROOT\Directory\Background\shell\wt]
  @="Windows Terminal here"
  "Icon"="C:\\Users\\Username\\AppData\\Local\\Terminal\\terminal.ico"

  [HKEY_CLASSES_ROOT\Directory\Background\shell\wt\command]
  @="C:\\Users\\Username\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe"
  ```
  * 修改注册表
  在`HKEY_CLASSES_ROOT\Directory\Background\shell\wt`下, 可以修改显示名称和图标.
* 配置Windows Terminal, 可参考[\wt\profiles.json](\wt\profiles.json).
* 关于Windows Terminal的美化, 可参考: [here](https://blog.csdn.net/Jioho_chen/article/details/100624029).

