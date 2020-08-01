# HoshinoBot-v1
Forked from Ice-Cirno/[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)

[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)的v1版（原版是v2）。

## 部署

### Windows部署

下载以下软件，notepad++和vscode二选一。
安装Python时，请务必勾选add python 3.8 to PATH.

- Python 3.8：https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe
- Git：https://github.com/git-for-windows/git/releases/download/v2.27.0.windows.1/Git-2.27.0-64-bit.exe
- Notepad++（可选）：https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.9/npp.7.8.9.Installer.x64.exe
- vscode(可选)：https://code.visualstudio.com/docs/?dv=win

运行 酷Q，启用 CQHTTP插件，CQHTTP插件的配置文件填入以下配置：

```
    {
        "use_http": false,
        "use_ws": false,
        "use_ws_reverse": true,
        "ws_reverse_use_universal_client": true,
        "ws_reverse_url": "ws://127.0.0.1:9222/ws/",
        "serve_data_files": false
    }
```
新建文件夹（最好是英文名），

```bash
    git clone https://github.com/pcrbot/HoshinoBot-v1.git
    cd HoshinoBot-v1
    #境内服务器：
    pip install -r requirements-Windows.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    #境外服务器：
    pip install -r requirements-Windows.txt
```
    
将config.example.py重命名为config.py,用notepad++或者vscode编辑，在SUPERUSER填入自己的QQ账号。

启动：

```bash
    python run.py
```

缝合yobot：

```bash
    #当前路径为xxx/HoshinoBot
    cd hoshino/modules/yobot
    git init
    git clone https://github.com/pcrbot/yobot.git
    #回到HoshinoBot，用vscode或者notepad++编辑config.py，将MODULES_ON中yobot的注释取消。
    #启动bot
    python run.py
```

控制台输出以下信息即为部署成功：

```bash
    [2020-07-17 15:50:26,435] 127.0.0.1:56363 GET /ws/ 1.1 101 - 7982
```

### Linux部署
以CentOS为例：

首先，编译安装Python3.8。

一条命令即可：

```bash
    #境外CentOS/RHEL:
    yum -y update&&yum -y groupinstall "Development tools"&&yum -y install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc* libffi-devel make git vim screen&&wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz&&tar -zxvf Python-3.8.3.tgz&&cd Python-3.8.3&&./configure&&make&&make install&&pip3 install --upgrade pip&&cd
    #境内CentOS/RHEL:
    yum -y update&&yum -y groupinstall "Development tools"&&yum -y install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc* libffi-devel make git vim screen&&wget http://npm.taobao.org/mirrors/python/3.8.3/Python-3.8.3.tgz&&tar -zxvf Python-3.8.3.tgz&&cd Python-3.8.3&&./configure&&make&&make install&&pip3 install --upgrade pip&&cd
```

#### 酷q部署

1，下载docker

CentOS7的场合：

```bash
curl -sSL https://get.docker.com/ | sh
systemctl start docker
systemctl enable docker
```

CentOS8的场合：

自行谷歌。

下载酷q的docker镜像：

首先，使用这行命令`ip addr show docker0 | grep -Po 'inet \K[\d.]+'`查看你的docker桥ip，若与`CQHTTP_WS_REVERSE_URL`中的链接不一致则替换掉。

```bash
    sudo docker run -d --name=hoshino \
    -v $(pwd)/coolq:/home/user/coolq \
    -p 9000:9000 --restart=always \
    -e VNC_PASSWD=自定义8位密码 \
    -e COOLQ_ACCOUNT=机器人的账号 \
    -e COOLQ_URL=https://dlsec.cqp.me/cqp-full \
    -e CQHTTP_SERVE_DATA_FILES=no \
    -e CQHTTP_USE_HTTP=no \
    -e CQHTTP_USE_WS=no \
    -e CQHTTP_USE_WS_REVERSE=yes \
    -e CQHTTP_WS_REVERSE_URL=ws://172.17.0.1:9222/ws/ \
    -e CQHTTP_WS_REVERSE_USE_UNIVERSAL_CLIENT=yes \
    richardchien/cqhttp:latest
```
    
然后访问 `http://<你的IP>:9000/` 进入 noVNC（密码是VNC_PASSWD中自定义的密码），登录 酷Q

#### Mirai部署

Mirai现在已经很稳定了。

```bash
 #若您的服务器是amd64构架
 mkdir mirai&&cd mirai&&wget -c http://t.imlxy.net:64724/mirai/MiraiOK/miraiOK_linux_amd64 && chmod +x miraiOK* && ./miraiOK*
 #若您的服务器不是amd64构架
 mkdir mirai&&cd mirai&&wget -c http://t.imlxy.net:64724/mirai/MiraiOK/miraiOK_linux_arm64 && chmod +x miraiOK* && ./miraiOK*
```
Ctrl+C退出MiraiOK后当前目录下应该生成了plugins文件夹和mirai的一些文件，接下来使用以下指令：

```bash
 #需要了解vim编辑器的用法
 cd plugins&&wget https://github.com/yyuueexxiinngg/cqhttp-mirai/releases/download/0.1.4/cqhttp-mirai-0.1.4-all.jar&&mkdir CQHTTPMirai&&cd CQHTTPMirai&&vim setting.yml
```

在setting.yml里，填入以下配置

```bash
"bot的账号":
  ws_reverse:
    enable: true
    postMessageFormat: string
    reverseHost: 127.0.0.1
    reversePort: 9222
    reversePath: /ws/
    accessToken: null
    reconnectInterval: 3000
```

详细说明请参考 https://github.com/yyuueexxiinngg/cqhttp-mirai
然后，

```bash
  #使用screen创建一个窗口
  screen -S mirai
  cd ~/mirai&&./miraiOK*
  # （mirai-console内）
  login 账号 密码
  #最后使用Ctrl+a,d挂起这个shell
```
克隆本仓库并安装依赖包

```bash
    cd&&git clone https://github.com/pcrbot/HoshinoBot-v1.git&&cd HoshinoBot-v1&&python3 -m pip install -r requirements-Linux.txt
    #安装yobot,重启插件，兰德索尔失信人员名单
    cd ~/HoshinoBot-v1/hoshino/modules/yobot&&git init&&git clone https://github.com/yuudi/yobot.git&&cd ~/HoshinoBot-v1/hoshino/modules&&cd custom&&git init&&git clone https://github.com/Lancercmd/Reloader.git&&git clone https://github.com/Lancercmd/Landsol-Distrust.git&&cd ~/HoshinoBot-v1
    #编辑配置文件
    cp config.example.py config.py&&vim config
    #取消yobot注释
    #启动bot
    screen -S hoshino
    python3 ~/HoshinoBot-v1/run.py
    #Ctrl+a,d 挂起这个窗口
```

HoshinoBot部署完成。

更多功能的获取：
#### 静态图片资源

> 发送图片的条件：  
> 1. 酷Q Pro版  
> 2. 将`config.py`中的`IS_CQPRO`设为`True`  
> 3. 静态图片资源

您可能希望看到更为精致的图片版结果，若希望机器人能够发送图片，首先需要您购买酷Q Pro版，其次需要准备静态图片资源，其中包括：

- 公主连接角色头像和卡面（来自 [干炸里脊资源站](https://redive.estertion.win/) 的拆包）
- 公主连接官方四格漫画
- 公主连接每月rank推荐表
- 表情包杂图

等资源。自行收集可能较为困难，所以我们准备了一个较为精简的资源包以及下载脚本，可以满足公主连接相关功能的日常使用。如果需要，可以从[这里](https://akiraxx.cn/res.zip)下载res.zip并解压至您的资源文件夹。



#### pcrdfans授权key

竞技场查询功能的数据来自 [公主连结Re: Dive Fan Club - 硬核的竞技场数据分析站](https://pcrdfans.com/) ，查询需要授权key。您可以在 [这里](https://www.pcrdfans.com/bot) 进行申请，审批完成后即可获得授权key

若您已有授权key，创建文件`hoshino/modules/priconne/arena/config.json`编写以下内容：

```json
{"AUTH_KEY": "your_auth_key"}
```



#### 蜜柑番剧 RSS Token

> 请先在`config.py`的`MODULES_ON`中取消`mikan`的注释  
> 本功能默认关闭，在群内发送 "启用 bangumi" 即可开启

番剧订阅数据来自[蜜柑计划 - Mikan Project](https://mikanani.me/)，您可以注册一个账号，添加订阅的番剧，之后点击Mikan首页的RSS订阅，复制类似于下面的url地址：

```
https://mikanani.me/RSS/MyBangumi?token=abcdfegABCFEFG%2b123%3d%3d
```

保留其中的`token`参数，创建文件`hoshino\modules\mikan\config.json`编写以下内容：

```json
{"MIKAN_TOKEN" : "abcdfegABCFEFG+123=="}
```

注意：`token`中可能含有url转义，您需要将`%2b`替换为`+`，将`%2f`替换为`/`，将`%3d`替换为`=`。



#### 时报文本

> 请先在`config.py`的`MODULES_ON`中取消`hourcall`的注释  
> 本功能默认关闭，在群内发送 "启用 hourcall" 即可开启

报时功能使用/魔改了艦これ中各个艦娘的报时语音，您可以在[舰娘百科](https://zh.kcwiki.org/wiki/舰娘百科)或[艦これ 攻略 Wiki](https://wikiwiki.jp/kancolle/)找到相应的文本/翻译，当然您也可以自行编写台词。在此，我们向原台词作者[田中](https://bbs.nga.cn/read.php?tid=9143913)[谦介](http://nga.178.com/read.php?tid=14045507)先生和他杰出的游戏作品表达诚挚的感谢！

若您已获取时报文本，创建文件`hoshino/modules/hourcall/config.json`编写以下内容：

```json
{
    "HOUR_CALLS": [
        "HOUR_CALL_1",
        "HOUR_CALL_2"
    ],
    "HOUR_CALL_1": [
        "午夜零点", "〇一〇〇", "〇二〇〇", "〇三〇〇", "〇四〇〇", "〇五〇〇",
        "〇六〇〇", "〇七〇〇", "〇八〇〇", "〇九〇〇", "一〇〇〇", "一一〇〇",
        "一二〇〇", "一三〇〇", "一四〇〇", "一五〇〇", "一六〇〇", "一七〇〇",
        "一八〇〇", "一九〇〇", "二〇〇〇", "二一〇〇", "二二〇〇", "二三〇〇"
	],
    "HOUR_CALL_2": [
        "0","1","2","3","4","5","6","7","8","9","10","11","12",
        "13","14","15","16","17","18","19","20","21","22","23"
    ]
}    
```

您可以编入多组报时文本，机器人会按`HOUR_CALLS`中定义的顺序循环日替。



#### 推特转发

推特转发功能需要推特开发者账号，具体申请方法请自行[Google](http://google.com)。注：现在推特官方大概率拒绝来自中国大陆的新申请，自备海外手机号及大学邮箱可能会帮到您。

若您已有推特开发者账号，创建文件`hoshino/modules/twitter/config.json`编写以下内容：

```json
{
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token_key": "your_access_token_key",
    "access_token_secret": "your_access_token_secret"
}
```

若您已经获取所有的apikey，恭喜你，你的Hoshino的功能已经完整。

若您想要更多功能，您可加入PCRbot交流群，群文件有大量各位大佬写的功能。

群号你猜。

