# IOS18_Fake_Location

## 项目结构
```tree
├── HNlocation.txt
├── README.md
├── config.py
├── config.yaml
├── driver
│   ├── connect.py
│   └── location.py
├── init
│   ├── init.py
│   ├── set_location.py
│   └── tunnel.py
├── main.py
├── requirements.txt
└── utils
    └── location.py
```

## 前置条件

1. `iphone` 或者`ipad` 的系统版本至少大于17
2. 系统最好是`macOS`
3. `windows`系统需要安装`iTunes`

## How to Setup

1. 建议使用虚拟环境，也可以使用自己已经建立好的环境
2. `pip install -r requirements.txt`安装实验所需要的依赖
3. 在终端中运行`sudo python3 main.py`(需要 root 权限为了创建 tun 设备 )
4. 将设备连接到电脑，解锁，如果请求信任的提示框，请点击信任
5. 打开[路径设置网站](https://fakerun.myth.cx/),将坐标数据复制到剪贴板,注意只需要复制一个就可以
6. 打开脚本目录里的`HNlocation.txt`文件，将刚复制的内容原封不动的粘贴进去，保存并退出
7. 请确保`iTunes`已经成功安装，然后运行该程序
8. 系统最后执行`ctrl+c`会自动退出程序，并且返回原始定位，无需重启