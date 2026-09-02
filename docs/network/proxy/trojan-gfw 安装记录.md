---
title: trojan-gfw 安装记录
date: 2024-10-15
categories:
  - network
tags:
  - linux
  - proxy
---

# trojan 安装记录


```bash
# 创建用户账户
sudo useradd -m -s /bin/bash trojanuser  
sudo passwd trojanuser  
sudo usermod -G sudo trojanuser  
su -l trojanuser

# 创建服务账户
sudo groupadd certusers  
sudo useradd -r -M -G certusers trojan  
sudo useradd -r -m -G certusers acme

# 安装依赖

sudo apt update

## 安装acme.sh需要的依赖。
sudo apt install -y socat cron curl

## 启动crontab
sudo systemctl start cron
sudo systemctl enable cron

## 安装Trojan需要的依赖。
sudo apt install -y libcap2-bin xz-utils nano

## 安装Nginx。
sudo apt install -y nginx

```


#### 配置Nginx

**_若你已经有配置Nginx虚拟主机，配置Nginx之前请，可以自己使用`cp`命令备份一下原来的虚拟主机，等介绍完基本配置再讲如何与现有服务集成。_**

##### 关闭默认虚拟主机

由于Nginx配置在Debian系列系统和CentOS系列系统组织方式不同，所以配置文件位置和使用方式有细微区别，为了统一，我将CentOS系列系统的组织结构做细微调整。

在Debian系列系统中，Nginx的虚拟主机配置文件在`/etc/nginx/sites-available/`文件夹中，如果要开启某一个虚拟主机，则建立一个软连接到`/etc/nginx/sites-enabled/`文件夹并重启Nginx即可。默认虚拟主机在`/etc/nginx/sites-enabled/`文件夹，需要关闭掉，否则会冲突。

在CentOS系列系统中，Nginx的虚拟主机配置文件在`/etc/nginx/conf.d/`文件夹中以`.conf`后缀保存，写入之后就可以使用。默认虚拟主机集成在Nginx配置文件`/etc/nginx/nginx.conf`中，需要打开将其中的server块删除，否则会冲突。Debian系列系统中的`/etc/nginx/sites-enabled/`和`/etc/nginx/sites-available/`文件夹结构在CentOS系列系统中是没有的，不过这个策略很不错，可以很方便的开启和关闭虚拟主机，我这里手动调整一下。

###### CentOS

按上述分析，我们使用下面两条命令在`/etc/nginx/`中添加两个文件夹。

|   |   |
|---|---|
|1  <br>2|sudo mkdir /etc/nginx/sites-available  <br>sudo mkdir /etc/nginx/sites-enabled|

复制

执行如下命令使用nano打开Nginx配置文件，删除其中server块，并添加对`/etc/nginx/sites-enabled/`文件夹的索引。

|   |   |
|---|---|
|1|sudo nano /etc/nginx/nginx.conf|

复制

配置文件修改结果如下图所示。![etc_nginx_nginx_conf](https://web.archive.org/web/20220412083230im_/https://trojan-tutor.github.io/2019/04/10/p41/etc_nginx_nginx_conf.jpg)

CentOS反向代理需要配置SELinux允许httpd模块可以联网，否则服务器会返回502错误。

|   |   |
|---|---|
|1|sudo setsebool -P httpd_can_network_connect true|

复制

###### Ubuntu or Debian

使用如下命令关闭Nginx默认虚拟主机。

|   |   |
|---|---|
|1|sudo rm /etc/nginx/sites-enabled/default|

复制

##### 写入虚拟主机到Nginx配置文件

1.执行如下命令，使用`nano`添加虚拟主机。(**_注意域名`<tdom.ml>`改为你自己的域名，这是虚拟主机的文件名，只是用来自己识别的。_**)

|   |   |
|---|---|
|1|sudo nano /etc/nginx/sites-available/<tdom.ml>|

复制

基于综述部分讲解的Trojan工作原理，现给定Nginx虚拟主机如下所示。这些虚拟主机可以直接拷贝到上面虚拟主机配置文件中再修改为你自己的，其中要修改的地方包括：

1. 第4行的`server_name`的值`<tdom.ml>`改为你自己的域名；
2. 第7行的`proxy_pass`随便指向一个没有敏感信息的网站都可以，这就是你要反向代理的网站，这里我是用了RFC文档的地址；
3. 第15行的`server_name`的值`<10.10.10.10>`改为你自己的IP；
4. 第17行`<tdom.ml>`改为自己的域名，注意别填错了。

|   |   |
|---|---|
|1  <br>2  <br>3  <br>4  <br>5  <br>6  <br>7  <br>8  <br>9  <br>10  <br>11  <br>12  <br>13  <br>14  <br>15  <br>16  <br>17  <br>18  <br>19  <br>20  <br>21  <br>22  <br>23  <br>24  <br>25  <br>26  <br>27  <br>28  <br>29  <br>30  <br>31  <br>32  <br>33|server {  <br>    listen 127.0.0.1:80 default_server;  <br>  <br>    server_name <tdom.ml>;  <br>  <br>    location / {  <br>        proxy_pass https://www.ietf.org;  <br>    }  <br>  <br>}  <br>  <br>server {  <br>    listen 127.0.0.1:80;  <br>  <br>    server_name <10.10.10.10>;  <br>  <br>    return 301 https://<tdom.ml>$request_uri;  <br>}  <br>  <br>server {  <br>    listen 0.0.0.0:80;  <br>    listen [::]:80;  <br>  <br>    server_name _;  <br>  <br>    location / {  <br>        return 301 https://$host$request_uri;  <br>    }  <br>  <br>    location /.well-known/acme-challenge {  <br>       root /var/www/acme-challenge;  <br>    }  <br>}|

复制

解释一下这些虚拟主机的一些细节：第一个server接收来自Trojan的流量，与上面Trojan配置文件对应；第二个server也是接收来自Trojan的流量，但是这个流量尝试使用IP而不是域名访问服务器，所以将其认为是异常流量，并重定向到域名；第三个server接收除127.0.0.1:80外的所有80端口的流量并重定向到443端口，这样便开启了全站https，可有效的防止恶意探测，其中`.well-known`是为申请证书所准备的，下文用到的时候自然明白。注意到，第一个和第二个server对应综述部分原理图中的蓝色数据流，第三个server对应综述部分原理图中的红色数据流，综述部分原理图中的绿色数据流不会流到Nginx。

2.使能配置文件**_注意域名`<tdom.ml>`改为你自己的域名_**

|   |   |
|---|---|
|1|sudo ln -s /etc/nginx/sites-available/<tdom.ml> /etc/nginx/sites-enabled/|

复制

##### 启动Nginx

Nginx启动命令和Trojan一样，就不过多解释了。

|   |   |
|---|---|
|1  <br>2|sudo systemctl restart nginx  <br>sudo systemctl status nginx|

复制

#### 配置证书

当从Let’s Encrypt获得证书时，Let’s Encrypt会验证证书中域名的控制权。一般采用HTTP-01或DNS-01方式来验证，详情参考官方文档[验证方式](https://web.archive.org/web/20220412083230/https://letsencrypt.org/zh-cn/docs/challenge-types/)。本文使用HTTP-01方式验证，若需要使用DNS-01方式验证，参考acme.sh官方文档[How to use DNS API](https://web.archive.org/web/20220412083230/https://github.com/acmesh-official/acme.sh/wiki/dnsapi)。

##### 创建证书文件夹

第一条命令新建一个文件夹`/etc/letsencrypt/live`用于存放证书。第二条命令将证书文件夹所有者改为`acme`，使得用户`acme`有权限写入证书。

|   |   |
|---|---|
|1  <br>2|sudo mkdir -p /etc/letsencrypt/live  <br>sudo chown -R acme:acme /etc/letsencrypt/live|

复制

##### 创建webroot并修改所有者

本文使用acme.sh的http方式申请证书，http方式需要在网站根目录下放置一个文件来验证域名所有权，故需要acme.sh和nginx均对webroot目录有权限，故将运行Nginx的worker进程加入certusers组，下文再将webroot目录附加给certusers组即可。

在不同的Linux发新版本中，nginx可能使用不同的用户运行`worker process`，可能为`www-data`，`nginx`，`nobody`中的一个，故需要自己运行下述命令查找`nginx: worker process`所属用户：

|   |   |
|---|---|
|1|ps -eo user,command\|grep nginx|

复制

上述命令输出第二行第一列即为`nginx: worker process`所属用户，然后根据实际情况，运行下面三个命令之一：

|   |   |
|---|---|
|1|sudo usermod -G certusers www-data|

复制

|   |   |
|---|---|
|1|sudo usermod -G certusers nginx|

复制

|   |   |
|---|---|
|1|sudo usermod -G certusers nobody|

复制

运行下面两条命令，第一条命令新建一个文件夹`/var/www/acme-challenge`用于给acme.sh存放域名验证文件。第二条命令将证书文件夹所有者改为`acme`，使得用户`acme`有权限写入文件，同时当验证的时候Nginx可以读取该文件。

|   |   |
|---|---|
|1  <br>2|sudo mkdir -p  /var/www/acme-challenge  <br>sudo chown -R acme:certusers /var/www/acme-challenge|

复制

##### 安装acme.sh自动管理CA证书脚本

**_分别_**执行如下命令，注意看是否报错。第一条命令切换到用户`acme`。第二条命令安装acme.sh。第三条命令退出当前用户。第四条命令再次切换到用户`acme`。注意到这里两次切换用户的操作不能省略，因为安装完acme.sh之后要重新登录当前用户，否则无法识别出acme.sh命令。

|   |   |
|---|---|
|1|sudo su -l -s /bin/bash acme|

复制

|   |   |
|---|---|
|1  <br>2|curl  https://get.acme.sh \| sh  <br>exit|

复制

|   |   |
|---|---|
|1|sudo su -l -s /bin/bash acme|

复制

##### 申请证书

执行如下命令将默认CA修改为Let's Encrypt：

|   |   |
|---|---|
|1|acme.sh --set-default-ca  --server  letsencrypt|

复制

执行如下命令（**_注意域名`<tdom.ml>`改为你自己的域名_**），等待一会儿。

|   |   |
|---|---|
|1|acme.sh --issue -d <tdom.ml> -w /var/www/acme-challenge|

复制

看到下图的提示表示证书申请成功。![证书申请成功提示](https://web.archive.org/web/20220412083230im_/https://trojan-tutor.github.io/2019/04/10/p41/%E8%AF%81%E4%B9%A6%E7%94%B3%E8%AF%B7%E6%88%90%E5%8A%9F%E6%8F%90%E7%A4%BA.jpg)

**_申请失败怎么办？_**证书申请失败的可能性一般有：1. 文件夹权限问题，请仔细检查每一步是否都正确；2. 证书申请次数超限，此时**_切忌反复尝试_**。证书每一个周申请次数是有限制的（20次），如果超限了就需要等一个周或者更换域名了（这个限制是争对每一个子域单独做的限制，所以万一超限了还可以用子域名继续部署）。解决方案是：在上述命令后加`--staging`参数继续测试。测试通过之后，删除上图所示四个证书文件以及该域名对应文件夹并**_取消`--staging`参数_**再执行一次。`--staging`参数申请的证书只作为测试用，客户端是无法认证通过的（提示`SSL handshake failed: tlsv1 alert unknown ca`），所以使用`--staging`参数申请到了证书之后要去掉`--staging`参数重新申请一次。

##### 安装证书

执行如下命令（**_注意域名`<tdom.ml>`改为你自己的域名_**），第一条命令使用acme.sh将证书安装到`certfiles`目录，这样acme.sh更新证书的时候会自动将新的证书安装到这里。第二条命令是配置acme.sh自动更新和自动更新证书，这样配置完Trojan之后一般不用管服务器。

|   |   |
|---|---|
|1|acme.sh --install-cert -d <tdom.ml> --key-file /etc/letsencrypt/live/private.key --fullchain-file /etc/letsencrypt/live/certificate.crt|

复制

|   |   |
|---|---|
|1|acme.sh  --upgrade  --auto-upgrade|

复制

##### 修改权限

最后还要允许组内用户访问证书。可通过如下命令实现。第一条命令将证书文件夹所在用户组改为`certusers`。第二条命令是赋予证书文件夹组内用户读取权限。运行这两条命令之后用户`trojan`就有权限读取证书了。第三条命令退出用户`acme`，因为证书已经安装完成。

|   |   |
|---|---|
|1  <br>2  <br>3|chown -R acme:certusers /etc/letsencrypt/live  <br>chmod -R 750 /etc/letsencrypt/live  <br>exit|

复制

#### 配置Trojan

##### 安装Trojan

分别执行如下四个命令，注意看是否报错。第一个命令是安装Trojan，安装完成一般会提示版本号注意看是否是最新版本。第二个命令是将Trojan配置文件的所有者修改为用户`trojan`，由于使用`sudo`安装的Trojan，该配置文件默认是属于`root`用户的，而我们需要使用用户`trojan`运行Trojan，不修改所有者会导致启动Trojan遇到权限问题。第三个命令备份Trojan配置文件，以防万一。第四个命令是使用nano修改配置文件。

|   |   |
|---|---|
|1|sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"|

复制

|   |   |
|---|---|
|1  <br>2  <br>3|sudo chown -R trojan:trojan /usr/local/etc/trojan  <br>sudo cp /usr/local/etc/trojan/config.json /usr/local/etc/trojan/config.json.bak  <br>sudo nano /usr/local/etc/trojan/config.json|

复制

第四个命令执行完之后屏幕会显示Trojan的配置文件，定位到`password`、`cert`和`key`并修改。密码按自己喜好，`cert`和`key`分别改为`/etc/letsencrypt/live/certificate.crt`和`/etc/letsencrypt/live/private.key`。编辑完成配置文件之后按屏幕下方快捷键提示（`^O`和`^X`即：`Ctrl+O`和`Ctrl+X`）保存并退出nano。修改之后的config文件如图所示。另外，如果有`IPv6`地址，将`local_addr`的`0.0.0.0`改为`::`才可以使用。![修改config](https://web.archive.org/web/20220412083230im_/https://trojan-tutor.github.io/2019/04/10/p41/%E4%BF%AE%E6%94%B9config.jpg)

##### 启动Trojan

###### 修改Trojan启动用户

执行如下命令，打开`trojan.service`文件，并将用户修改为`trojan`。

|   |   |
|---|---|
|1|sudo nano /etc/systemd/system/trojan.service|

复制

添加用户效果如图所示，注意等号旁边没有空格。![添加trojan用户到trojan.service](https://web.archive.org/web/20220412083230im_/https://trojan-tutor.github.io/2019/04/10/p41/changeUser.jpg)

然后重新加载配置文件。

|   |   |
|---|---|
|1|sudo systemctl daemon-reload|

复制

###### 赋予Trojan监听443端口能力

执行如下命令，赋予Trojan监听1024以下端口的能力，使得Trojan可以监听到443端口。这是由于我们使用非`root`用户启动Trojan，但是Linux默认不允许非`root`用户启动的进程监听1024以下的端口，除非为每一个二进制文件显式声明。

|   |   |
|---|---|
|1|sudo setcap CAP_NET_BIND_SERVICE=+eip /usr/local/bin/trojan|

复制

###### 使用systemd启动Trojan

Trojan启动、查看状态命令分别如下，第一条是启动Trojan，第二条是查看Trojan运行状态。启动之后再查看一下状态，Trojan显示active (running)即表示正常启动了。如果出现`fatal: config.json(n): invalid code sequence`错误，那么是你的配置文件第`n`行有错误，请检查。如果启动失败，还可以用`journalctl -f -u trojan`查看`systemd`的日志。

|   |   |
|---|---|
|1  <br>2  <br>3|sudo systemctl enable trojan  <br>sudo systemctl restart trojan  <br>sudo systemctl status trojan|

复制

##### 更新证书

当acme.sh重新安装证书之后，需要通知Trojan重新加载证书。最简单的方案是每三个月登录服务器重启Trojan，但是不够完美，毕竟重启的时候会导致服务中断。其实Trojan有实现[reload certificate and private key](https://web.archive.org/web/20220412083230/https://github.com/trojan-gfw/trojan/commit/53ca5f80fcd6239c28c8520886692e9186e3fcf6)功能，只需要在证书更新后给Trojan发送`SIGUSR1`消息即可。Trojan收到`SIGUSR1`消息后便会自动加载新的证书和密钥文件，这样就不用重启Trojan了。手动给Trojan发送`SIGUSR1`消息的命令是`sudo -u trojan killall -s SIGUSR1 trojan`，但是这样也不够完美，也得每三个月登录服务器运行一次该命令。其实我们可以给用户`trojan`添加定时任务，使其每个月运行一次该命令即可。实现如下。

首先，编辑用户`trojan`的crontab文件

|   |   |
|---|---|
|1|sudo -u trojan crontab -e|

复制

在文件末尾添加一行如下，该行表示每个月1号的时候运行命令`killall -s SIGUSR1 trojan`，由于是使用用户`trojan`运行的，故不需要在前面加`sudo -u trojan`。

|   |   |
|---|---|
|1|0 0 1 * * killall -s SIGUSR1 trojan|

复制

最后查看crontab是否生效。

|   |   |
|---|---|
|1|sudo -u trojan crontab -l|

复制

##### 更新Trojan

如果Trojan版本有更新（可以去[这里](https://web.archive.org/web/20220412083230/https://github.com/trojan-gfw/trojan/releases)查看是否有更新），那么使用本教程搭建的服务器端更新Trojan版本只需要三条命令即可，不过要注意的是，第一条命令会提示是否覆盖配置文件，如果没有必要请回答n，否则配置文件将会被覆盖（如果不小心覆盖了就得自己重新编辑了）。第二条命令重新赋予Trojan监听443端口的能力。第三条命令重启Trojan。

|   |   |
|---|---|
|1|sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"|

复制

|   |   |
|---|---|
|1  <br>2|sudo setcap CAP_NET_BIND_SERVICE=+eip /usr/local/bin/trojan  <br>sudo systemctl restart trojan|

复制

#### 配置Trojan和Nginx开机自启

虽然开机自启一般用不着，除非vultr机房停电，但是反正也没什么代价，弄一下吧。

|   |   |
|---|---|
|1  <br>2|sudo systemctl enable trojan  <br>sudo systemctl enable nginx|

复制

#### 检查服务器是否配置成功

到这里服务器就配置完成了。此时你可以在浏览器里面访问你的网站看是否能够访问，如果你的网站可以访问了，那么就一切正常啦。

另外，基于以上考虑到的可能的恶意探测，可以验证一下以下情况是否正常。

1. 浏览器中使用ip访问：重定向到[https://tdom.ml](https://web.archive.org/web/20220412083230/https://tdom.ml/);
2. 浏览器中使用[https://ip](https://web.archive.org/web/20220412083230/https://ip/)访问：重定向到[https://tdom.ml](https://web.archive.org/web/20220412083230/https://tdom.ml/)(跳转的时候浏览器可能提示不安全是正常的);
3. 浏览器中使用[tdom.ml](https://web.archive.org/web/20220412083230/https://trojan-tutor.github.io/2019/04/10/tdom.ml)访问：重定向到[https://tdom.ml](https://web.archive.org/web/20220412083230/https://tdom.ml/)。

#### 启动bbr（可选，建议）

启动bbr需要Linux内核版本在4.10及以上，如果低于该版本需要自己升级（这不在本教程范围之后）内核版本，保证内核版本不低于4.10。查看系统内核版本命令如下。

|   |   |
|---|---|
|1|uname -a|

复制

bbr是谷歌开发的网络控制算法，可以加快访问速度。执行下面命令查看当前系统是否启用bbr。

|   |   |
|---|---|
|1|sudo sysctl net.ipv4.tcp_congestion_control|

复制

执行完成之后如果**_提示`net.ipv4.tcp_congestion_control = bbr`_**即表示启动了bbr，可以跳过下面启动bbr的步骤。

直接将下面三条命令拷贝粘贴到Xshell里面执行即可启动bbr，检查启动状态同上。

|   |   |
|---|---|
|1  <br>2  <br>3|sudo bash -c 'echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf'  <br>sudo bash -c 'echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf'  <br>sudo sysctl -p|

复制

#### 配置防火墙（可选）

只打开22、80和443端口可以有效的阻止外部恶意流量，降低服务器暴露的风险。此步骤非必须，而且自己有其他服务记得其他服务的端口也要处理。

本文以ufw为例配置防火墙，ufw是一个很好用的防火墙配置命令，可以简化操作，减少错误的发生。

**_Debian or Ubuntu_**执行如下命令安装ufw

|   |   |
|---|---|
|1|sudo apt install -y ufw|

复制

**_CentOS_**执行如下两个命令安装ufw

|   |   |
|---|---|
|1  <br>2|sudo yum install -y epel-release  <br>sudo yum install -y ufw|

复制

如果服务器无IPv6地址那么需要执行如下命令，将IPV6=yes修改为IPV6=no。

|   |   |
|---|---|
|1|sudo nano /etc/default/ufw|

复制

执行如下命令即可成功配置防火墙。注意，如果ssh端口不是22那么第一行需要调整（将ssh改为端口号）。

|   |   |
|---|---|
|1  <br>2  <br>3  <br>4  <br>5|sudo ufw disable  <br>sudo ufw allow ssh  <br>sudo ufw allow https  <br>sudo ufw allow http  <br>sudo ufw enable|

复制

|   |   |
|---|---|
|1  <br>2|sudo ufw status  <br>sudo ufw status verbose|

复制

另外，如果对Trojan不放心，那么可以参考[trojan wiki](https://web.archive.org/web/20220412083230/https://github.com/trojan-gfw/trojan/wiki/Limiting-Server-Network-Access)，优化防火墙配置，使得Trojan只能给127.0.0.1:80发送数据和响应外部请求。

#### 与现有Nginx服务集成

如果你本机已经有Nginx服务，那么Nginx配置文件需要做适当修改以和现有服务兼容。

1. 在原服务与Trojan使用同一个域名且原来是监听443端口的情况下，那么需要将你的ssl配置删除并将监听地址改为第一个server监听的地址127.0.0.1:80，然后直接用修改好的server代替上述配置文件中第一个server即可。这样https加密部分将会由Trojan处理之后转发给Nginx而不是由Nginx处理，原来的服务对于客户端来说就没有变化。
    
2. 如果原来的服务与Trojan使用不同的域名，建议是修改Trojan与原来的服务使用同一个域名，如果非要使用不同的域名，请参考第3点。
    
3. 如果原来的服务就监听了多个域名，那么请自己琢磨Nginx的sni，参考连接：[ngx_stream_ssl_preread_module](https://web.archive.org/web/20220412083230/https://nginx.org/en/docs/stream/ngx_stream_ssl_preread_module.html)。
    
4. 如果原来的服务是监听80端口，想要继续监听80端口那么直接去除第三个server即可（将域名验证相关location与自己的虚拟主机组合，否则无法更新证书），如果要改为监听443端口参考第1点。

## 参考

[自建梯子教程 --Trojan版本](https://web.archive.org/web/20220412083230/https://trojan-tutor.github.io/2019/04/10/p41.html)

