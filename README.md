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

    ```json
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
    reversePort: 8080
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
