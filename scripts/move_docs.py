#!/usr/bin/env python3
import subprocess, shlex, os, sys
from pathlib import Path

base = Path("/home/pi/playground/wiki")
# mapping: src (relative to repo) -> dst (relative to repo), keep original filename
moves = [
    # linux/distro
    ("docs/posts/archlinux install record.md", "docs/linux/distro/archlinux install record.md"),
    ("docs/posts/Gentoo Linux 安装指南.md", "docs/linux/distro/Gentoo Linux 安装指南.md"),
    ("docs/posts/gentoo 源设置.md", "docs/linux/distro/gentoo 源设置.md"),
    ("docs/posts/rock5b 设置记录.md", "docs/linux/distro/rock5b 设置记录.md"),
    ("docs/posts/Ubuntu 彻底移除Snap.md", "docs/linux/distro/Ubuntu 彻底移除Snap.md"),
    ("docs/posts/Ubuntu 没有网络连接.md", "docs/linux/distro/Ubuntu 没有网络连接.md"),
    ("docs/posts/ubuntu 设置虚拟显示器输出.md", "docs/linux/distro/ubuntu 设置虚拟显示器输出.md"),
    ("docs/posts/删除Ubunut Pro.md", "docs/linux/distro/删除Ubunut Pro.md"),
    ("docs/posts/LFS 记录.md", "docs/linux/distro/LFS 记录.md"),
    # linux/filesystem
    ("docs/posts/Arch linux ext4 文件系统转 Btrfs.md", "docs/linux/filesystem/Arch linux ext4 文件系统转 Btrfs.md"),
    ("docs/posts/Arch Linux 硬盘扩容迁移.md", "docs/linux/filesystem/Arch Linux 硬盘扩容迁移.md"),
    ("docs/posts/linux 缩小分区大小.md", "docs/linux/filesystem/linux 缩小分区大小.md"),
    # linux/system (includes network config)
    ("docs/posts/linux 用户使用.md", "docs/linux/system/linux 用户使用.md"),
    ("docs/posts/linux 中使用 ctrl+z 停止任务后如何恢复任务.md", "docs/linux/system/linux 中使用 ctrl+z 停止任务后如何恢复任务.md"),
    ("docs/posts/linux 网络排查.md", "docs/linux/system/linux 网络排查.md"),
    ("docs/posts/查看linux 版本信息 & 更改密码.md", "docs/linux/system/查看linux 版本信息 & 更改密码.md"),
    ("docs/posts/设置静态 IP 地址.md", "docs/linux/system/设置静态 IP 地址.md"),
    # embedded/buildroot
    ("docs/posts/Buildroot 使用 crontab 和 crond 完成定时任务.md", "docs/embedded/buildroot/Buildroot 使用 crontab 和 crond 完成定时任务.md"),
    ("docs/posts/buildroot  如何仅获取 toolchain.md", "docs/embedded/buildroot/buildroot  如何仅获取 toolchain.md"),
    ("WIP/buildroot  静态ip 设置.md", "docs/embedded/buildroot/buildroot  静态ip 设置.md"),
    ("docs/posts/repo 拉取仓库.md", "docs/embedded/buildroot/repo 拉取仓库.md"),
    # embedded/yocto
    ("docs/posts/Yocoto 调试总结.md", "docs/embedded/yocto/Yocoto 调试总结.md"),
    ("docs/posts/OpenWrt 使用记录.md", "docs/embedded/yocto/OpenWrt 使用记录.md"),
    # embedded/kernel
    ("docs/posts/Linux 内核开发.md", "docs/embedded/kernel/Linux 内核开发.md"),
    ("docs/posts/内核内存管理.md", "docs/embedded/kernel/内核内存管理.md"),
    ("docs/posts/内核网络设备驱动.md", "docs/embedded/kernel/内核网络设备驱动.md"),
    ("docs/posts/内核驱动初始化顺序.md", "docs/embedded/kernel/内核驱动初始化顺序.md"),
    ("docs/posts/ELF 文件查看.md", "docs/embedded/kernel/ELF 文件查看.md"),
    ("docs/posts/手把手解析ELF文件格式：从Hello World到二进制奥秘.md", "docs/embedded/kernel/手把手解析ELF文件格式：从Hello World到二进制奥秘.md"),
    # embedded/hardware
    ("docs/posts/CMOS Sensor 的一些基本概念.md", "docs/embedded/hardware/CMOS Sensor 的一些基本概念.md"),
    ("docs/posts/imx8mm sai rx 时钟线配置.md", "docs/embedded/hardware/imx8mm sai rx 时钟线配置.md"),
    ("docs/posts/linux Fan driver.md", "docs/embedded/hardware/linux Fan driver.md"),
    ("docs/posts/openocd 使用.md", "docs/embedded/hardware/openocd 使用.md"),
    ("WIP/gpio keypad.md", "docs/embedded/hardware/gpio keypad.md"),
    # git
    ("docs/posts/git cherry-pick 代码片段.md", "docs/git/git cherry-pick 代码片段.md"),
    ("docs/posts/git diff 生成patch 并应用.md", "docs/git/git diff 生成patch 并应用.md"),
    ("docs/posts/git  Merge vs Rebase.md", "docs/git/git  Merge vs Rebase.md"),
    ("docs/posts/git pull request.md", "docs/git/git pull request.md"),
    ("docs/posts/git 修剪分支.md", "docs/git/git 修剪分支.md"),
    ("docs/posts/git 修改第一个commit 信息.md", "docs/git/git 修改第一个commit 信息.md"),
    ("docs/posts/git 修改配置文件.md", "docs/git/git 修改配置文件.md"),
    ("docs/posts/git分割commit 推送到远程仓库.md", "docs/git/git分割commit 推送到远程仓库.md"),
    ("docs/posts/git 分块推送.md", "docs/git/git 分块推送.md"),
    ("docs/posts/git 合并commit.md", "docs/git/git 合并commit.md"),
    ("docs/posts/git 同步Fork 源仓库.md", "docs/git/git 同步Fork 源仓库.md"),
    ("docs/posts/git 将token 添加到远程仓库链接中.md", "docs/git/git 将token 添加到远程仓库链接中.md"),
    ("docs/posts/git 打包仓库.md", "docs/git/git 打包仓库.md"),
    ("docs/posts/git 查看历史记录.md", "docs/git/git 查看历史记录.md"),
    ("docs/posts/git 设置和取消代理.md", "docs/git/git 设置和取消代理.md"),
    ("WIP/gitea 部署记录.md", "docs/git/gitea 部署记录.md"),
    # network/proxy
    ("docs/posts/cloudflared 内网代理.md", "docs/network/proxy/cloudflared 内网代理.md"),
    ("docs/posts/openvpn 局域网内分享网络.md", "docs/network/proxy/openvpn 局域网内分享网络.md"),
    ("docs/posts/wireguard 部署记录.md", "docs/network/proxy/wireguard 部署记录.md"),
    ("docs/posts/v2ray 脚本安装.md", "docs/network/proxy/v2ray 脚本安装.md"),
    ("docs/posts/trojan-gfw 安装记录.md", "docs/network/proxy/trojan-gfw 安装记录.md"),
    ("docs/posts/搭建clash 并且分享网络.md", "docs/network/proxy/搭建clash 并且分享网络.md"),
    ("WIP/安装FreeBSD 并搭建clash.md", "docs/network/proxy/安装FreeBSD 并搭建clash.md"),
    ("docs/posts/钉钉无法输入中文.md", "docs/network/proxy/钉钉无法输入中文.md"),
    # tools/apt
    ("docs/posts/add-apt-repository 命令安装,卸载和使用.md", "docs/tools/apt/add-apt-repository 命令安装,卸载和使用.md"),
    ("docs/posts/apt certificate verification failed.md", "docs/tools/apt/apt certificate verification failed.md"),
    ("docs/posts/apt-key 添加公钥.md", "docs/tools/apt/apt-key 添加公钥.md"),
    ("docs/posts/apt 命令使用代理.md", "docs/tools/apt/apt 命令使用代理.md"),
    # tools/ssh
    ("docs/posts/ssh 向linux添加公钥.md", "docs/tools/ssh/ssh 向linux添加公钥.md"),
    ("docs/posts/ssh 快速删除known_hosts记录.md", "docs/tools/ssh/ssh 快速删除known_hosts记录.md"),
    ("docs/posts/ssh 添加使用私钥.md", "docs/tools/ssh/ssh 添加使用私钥.md"),
    ("docs/posts/ssh 端口转发.md", "docs/tools/ssh/ssh 端口转发.md"),
    ("docs/posts/ssh 设置代理.md", "docs/tools/ssh/ssh 设置代理.md"),
    # tools/samba
    ("docs/posts/samba 分享文件.md", "docs/tools/samba/samba 分享文件.md"),
    ("docs/posts/samba 用户管理.md", "docs/tools/samba/samba 用户管理.md"),
    ("docs/posts/freebsd 13 安装 samba server.md", "docs/tools/samba/freebsd 13 安装 samba server.md"),
    # tools/misc
    ("docs/posts/tmux 使用.md", "docs/tools/misc/tmux 使用.md"),
    ("docs/posts/zsh 增加命令历史记录.md", "docs/tools/misc/zsh 增加命令历史记录.md"),
    ("docs/posts/使用UEFI Shell引导U盘启动.md", "docs/tools/misc/使用UEFI Shell引导U盘启动.md"),
    ("docs/posts/vscode 设置 compare view.md", "docs/tools/misc/vscode 设置 compare view.md"),
    ("docs/posts/查看python所支持的wheel包.md", "docs/tools/misc/查看python所支持的wheel包.md"),
    ("docs/posts/在 FreeBSD 13 上安装 gitea.md", "docs/tools/misc/在 FreeBSD 13 上安装 gitea.md"),
    # windows
    ("docs/posts/Windows 10 分享网络设置.md", "docs/windows/Windows 10 分享网络设置.md"),
    ("docs/posts/windows 中添加右键菜单 - 在vscode 中打开.md", "docs/windows/windows 中添加右键菜单 - 在vscode 中打开.md"),
    ("WIP/google chrome 强制启用 secure dns.md", "docs/windows/google chrome 强制启用 secure dns.md"),
    # programming/c-cpp
    ("docs/posts/c 文件IO.md", "docs/programming/c-cpp/c 文件IO.md"),
    ("docs/posts/c 预处理器.md", "docs/programming/c-cpp/c 预处理器.md"),
    ("docs/posts/去掉宏__FILE__的路径.md", "docs/programming/c-cpp/去掉宏__FILE__的路径.md"),
    ("docs/posts/嵌入式C功能代码片段.md", "docs/programming/c-cpp/嵌入式C功能代码片段.md"),
    # programming/python
    ("docs/posts/python pip 设置代理.md", "docs/programming/python/python pip 设置代理.md"),
    ("docs/posts/python 查看动态链接库地址.md", "docs/programming/python/python 查看动态链接库地址.md"),
    # programming/shell
    ("docs/posts/Shell 命令去除字符串中回车符.md", "docs/programming/shell/Shell 命令去除字符串中回车符.md"),
    ("docs/posts/创建ASCII码的目录树.md", "docs/programming/shell/创建ASCII码的目录树.md"),
    # cheatsheet
    ("docs/posts/Markdown 速查表.md", "docs/cheatsheet/Markdown 速查表.md"),
    ("WIP/DWM shortcuts cheetsheet.md", "docs/cheatsheet/DWM shortcuts cheetsheet.md"),
]

# Check all src exist, dst not exist
fail = []
for src, dst in moves:
    s = base / src
    d = base / dst
    if not s.exists():
        print(f"MISSING src: {src}")
        fail.append(src)
    if d.exists():
        print(f"EXISTS dst: {dst}")
print(f"Total moves: {len(moves)}, missing: {len(fail)}")
if fail:
    sys.exit(1)

for src, dst in moves:
    # ensure parent exists
    dst_path = base / dst
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    # git mv
    cmd = ["git", "mv", src, dst]
    print(f"git mv {src!r} -> {dst!r}")
    result = subprocess.run(cmd, cwd=base, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED: {result.stderr}")
        # try fallback mv + git add?
        subprocess.run(["mv", str(base/src), str(dst_path)], cwd=base)
        subprocess.run(["git", "add", dst], cwd=base)
        subprocess.run(["git", "rm", src], cwd=base)
    else:
        if result.stdout.strip():
            print(result.stdout)
        if result.stderr.strip():
            print(result.stderr)

print("Done")
# show remaining
remaining = list((base / "docs/posts").glob("*"))
print(f"Remaining in docs/posts: {len(remaining)}")
for r in remaining:
    print(r)
remaining_wip = list((base / "WIP").glob("*")) if (base/"WIP").exists() else []
print(f"Remaining in WIP: {len(remaining_wip)}")
for r in remaining_wip:
    print(r)
