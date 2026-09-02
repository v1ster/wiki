---
title: Buildroot 使用 crontab 和 crond 完成定时任务
date: 2025-01-14
categories:
  - embedded
tags:
  - buildroot
  - linux
---

# Buildroot 使用 crontab 和 crond 完成定时任务

新建定时文件配置
```shell

mkdir -p /var/spool/cron/crontabs

crontab -e 
# 手动输入下面的配置
# do daily/weekly/monthly maintenance
# min   hour    day     month   weekday command
*/1     *       *       *       *       run-parts /etc/periodic/15min
0       *       *       *       *       run-parts /etc/periodic/hourly
0       2       *       *       *       run-parts /etc/periodic/daily
0       3       *       *       6       run-parts /etc/periodic/weekly
0       5       1       *       *       run-parts /etc/periodic/monthly


mkdir -p /etc/periodic/15min /etc/periodic/hourly /etc/periodic/daily /etc/periodic/mo
nthly /etc/periodic/weekly

cat <<EOF > /etc/periodic/15min/test 
#!/bin/sh
echo "[$0]$(date) Hi Mars ~" >> /root/log.txt
EOF

# 启动定时任务, -f 前台运行,默认后台运行
crond -l 2 -f 
```
