## 背景

CQU 校园网支持网页登录了，但是登出窗口会单独打开一个页面，还不能关闭，所以做了一个脚本来避免登出窗口



## 环境

python3

requests模块



## 使用

` python login.py`或`python3 login.py`

我是创建一个`login.bat`文件到开机启动文件夹，内容是

``` bash
cd H:\代码\CQU服务\校园网
python login.py
pause
```

这样就可以自动登录了



