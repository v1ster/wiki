---
title: 在 FreeBSD 13 上安装 gitea
date: 2024-04-24
categories:
  - tools
tags:
  - tool
---

# 在 FreeBSD 13 上安装 gitea

## 操作

```Shell
# 安装git
sudo pkg install git git-lfs

# 下载gitea
wget https://dl.gitea.io/gitea/1.18.3/gitea-1.18.3-freebsd12-amd64

mv gitea-*-freebsd12-amd64 /usr/local/bin/gitea
chmod +x /usr/local/bin/gitea

# 创建用户
[root@freebsd ~]# adduser
Username: git
Full name:
Uid (Leave empty for default):
Login group [git]:
Login group is git. Invite git into other groups? []:
Login class [default]:
Shell (sh csh tcsh bash rbash git-shell nologin) [sh]:
Home directory [/home/git]:
Home directory permissions (Leave empty for default):
Use password-based authentication? [yes]: no
Lock out the account after creation? [no]:
Username   : git
Password   : <disabled>
Full Name  :
Uid        : 1002
Class      :
Groups     : git
Home       : /home/git
Home Mode  :
Shell      : /bin/sh
Locked     : no
OK? (yes/no): yes
adduser: INFO: Successfully added (git) to the user database.
Add another user? (yes/no): no
Goodbye!

# 启动服务
mkdir -p /var/lib/gitea/{custom,data,log}
chown -R git:git /var/lib/gitea
chmod -R 750 /var/lib/gitea
# 编写rc 启动脚本 /usr/local/etc/rc.d/gitea
#!/bin/sh
#
# $FreeBSD$
#
# PROVIDE: gitea
# REQUIRE: NETWORKING SYSLOG
# KEYWORD: shutdown
#
# Add the following lines to /etc/rc.conf to enable gitea:
#
#   gitea_enable="YES"
#
# https://github.com/go-gitea/gitea/blob/main/contrib/init/freebsd/gitea

. /etc/rc.subr

name="gitea"
rcvar="gitea_enable"

load_rc_config $name

: ${gitea_user:="git"}
: ${gitea_enable:="NO"}
: ${gitea_directory:="/var/lib/gitea"}

command="/usr/local/bin/gitea web"
procname="$(echo $command |cut -d' ' -f1)"

pidfile="${gitea_directory}/${name}.pid"

start_cmd="${name}_start"
stop_cmd="${name}_stop"

gitea_start() {
	cd ${gitea_directory}
	export USER=${gitea_user}
	export HOME=/home/${gitea_user}
	export GITEA_WORK_DIR=${gitea_directory}
	/usr/sbin/daemon -f -u ${gitea_user} -p ${pidfile} $command
}

gitea_stop() {
	if [ ! -f $pidfile ]; then
		echo "GITEA PID File not found. Maybe GITEA is not running?"
	else
		kill $(cat $pidfile)
	fi
}

run_rc_command "$1"

# 编辑rc脚本权限

chmod 755 /usr/local/etc/rc.d/gitea

# 启动服务

sysrc 'gitea_enable=YES'
service gitea start
# 访问web 站点初始化

http://192.168.1.3:3000

```

# trubleshooting

```shell
(.venv) [mars@mapc ~/workspace/pyground/encrypted_bin]$ git push upstream master
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 16 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (21/21), 222.82 KiB | 4.55 MiB/s, done.
Total 21 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
remote: env: bash: No such file or directory
To 192.168.1.3:workspace/encrypted_bin.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to '192.168.1.3:workspace/encrypted_bin.git'
# freebse 没有bash, 需要手动安装
sudo pkg install bash
```

## 参考

[在 FreeBSD 12 上安装 Gitea](https://www.cnblogs.com/Gitea/p/setup-gitea-on-freebsd.html)
