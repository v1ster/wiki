#!/usr/bin/env python3
import subprocess, pathlib

base = pathlib.Path("/home/pi/playground/wiki")

def run(cmd, cwd=base):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        print(f"FAILED {result.returncode}")
    return result

# mapping per category: list of (src, dst)
# reuse from earlier mapping
moves = [
    ("docs/posts/archlinux install record.md", "docs/linux/distro/archlinux install record.md"),
    ("docs/posts/Gentoo Linux 安装指南.md", "docs/linux/distro/Gentoo Linux 安装指南.md"),
    ("docs/posts/gentoo 源设置.md", "docs/linux/distro/gentoo 源设置.md"),
    ("docs/posts/rock5b 设置记录.md", "docs/linux/distro/rock5b 设置记录.md"),
    ("docs/posts/Ubuntu 彻底移除Snap.md", "docs/linux/distro/Ubuntu 彻底移除Snap.md"),
    ("docs/posts/Ubuntu 没有网络连接.md", "docs/linux/distro/Ubuntu 没有网络连接.md"),
    ("docs/posts/ubuntu 设置虚拟显示器输出.md", "docs/linux/distro/ubuntu 设置虚拟显示器输出.md"),
    ("docs/posts/删除Ubunut Pro.md", "docs/linux/distro/删除Ubunut Pro.md"),
    ("docs/posts/LFS 记录.md", "docs/linux/distro/LFS 记录.md"),
    ("docs/posts/Arch linux ext4 文件系统转 Btrfs.md", "docs/linux/filesystem/Arch linux ext4 文件系统转 Btrfs.md"),
    ("docs/posts/Arch Linux 硬盘扩容迁移.md", "docs/linux/filesystem/Arch Linux 硬盘扩容迁移.md"),
    ("docs/posts/linux 缩小分区大小.md", "docs/linux/filesystem/linux 缩小分区大小.md"),
    ("docs/posts/linux 用户使用.md", "docs/linux/system/linux 用户使用.md"),
    ("docs/posts/linux 中使用 ctrl+z 停止任务后如何恢复任务.md", "docs/linux/system/linux 中使用 ctrl+z 停止任务后如何恢复任务.md"),
    ("docs/posts/linux 网络排查.md", "docs/linux/system/linux 网络排查.md"),
    ("docs/posts/查看linux 版本信息 & 更改密码.md", "docs/linux/system/查看linux 版本信息 & 更改密码.md"),
    ("docs/posts/设置静态 IP 地址.md", "docs/linux/system/设置静态 IP 地址.md"),
    # embedded
    ("docs/posts/Buildroot 使用 crontab 和 crond 完成定时任务.md", "docs/embedded/buildroot/Buildroot 使用 crontab 和 crond 完成定时任务.md"),
    ("docs/posts/buildroot  如何仅获取 toolchain.md", "docs/embedded/buildroot/buildroot  如何仅获取 toolchain.md"),
    ("WIP/buildroot  静态ip 设置.md", "docs/embedded/buildroot/buildroot  静态ip 设置.md"),
    ("docs/posts/repo 拉取仓库.md", "docs/embedded/buildroot/repo 拉取仓库.md"),
    ("docs/posts/Yocoto 调试总结.md", "docs/embedded/yocto/Yocoto 调试总结.md"),
    ("docs/posts/OpenWrt 使用记录.md", "docs/embedded/yocto/OpenWrt 使用记录.md"),
    ("docs/posts/Linux 内核开发.md", "docs/embedded/kernel/Linux 内核开发.md"),
    ("docs/posts/内核内存管理.md", "docs/embedded/kernel/内核内存管理.md"),
    ("docs/posts/内核网络设备驱动.md", "docs/embedded/kernel/内核网络设备驱动.md"),
    ("docs/posts/内核驱动初始化顺序.md", "docs/embedded/kernel/内核驱动初始化顺序.md"),
    ("docs/posts/ELF 文件查看.md", "docs/embedded/kernel/ELF 文件查看.md"),
    ("docs/posts/手把手解析ELF文件格式：从Hello World到二进制奥秘.md", "docs/embedded/kernel/手把手解析ELF文件格式：从Hello World到二进制奥秘.md"),
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
    # network
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
    # programming
    ("docs/posts/c 文件IO.md", "docs/programming/c-cpp/c 文件IO.md"),
    ("docs/posts/c 预处理器.md", "docs/programming/c-cpp/c 预处理器.md"),
    ("docs/posts/去掉宏__FILE__的路径.md", "docs/programming/c-cpp/去掉宏__FILE__的路径.md"),
    ("docs/posts/嵌入式C功能代码片段.md", "docs/programming/c-cpp/嵌入式C功能代码片段.md"),
    ("docs/posts/python pip 设置代理.md", "docs/programming/python/python pip 设置代理.md"),
    ("docs/posts/python 查看动态链接库地址.md", "docs/programming/python/python 查看动态链接库地址.md"),
    ("docs/posts/Shell 命令去除字符串中回车符.md", "docs/programming/shell/Shell 命令去除字符串中回车符.md"),
    ("docs/posts/创建ASCII码的目录树.md", "docs/programming/shell/创建ASCII码的目录树.md"),
    # cheatsheet
    ("docs/posts/Markdown 速查表.md", "docs/cheatsheet/Markdown 速查表.md"),
    ("WIP/DWM shortcuts cheetsheet.md", "docs/cheatsheet/DWM shortcuts cheetsheet.md"),
]

# group by category
groups = {
    "linux": [m for m in moves if m[1].startswith("docs/linux/")],
    "embedded_buildroot": [m for m in moves if m[1].startswith("docs/embedded/buildroot/")],
    "embedded_yocto": [m for m in moves if m[1].startswith("docs/embedded/yocto/")],
    "embedded_kernel": [m for m in moves if m[1].startswith("docs/embedded/kernel/")],
    "embedded_hardware": [m for m in moves if m[1].startswith("docs/embedded/hardware/")],
    "git": [m for m in moves if m[1].startswith("docs/git/")],
    "network": [m for m in moves if m[1].startswith("docs/network/")],
    "tools_apt": [m for m in moves if m[1].startswith("docs/tools/apt/")],
    "tools_ssh": [m for m in moves if m[1].startswith("docs/tools/ssh/")],
    "tools_samba": [m for m in moves if m[1].startswith("docs/tools/samba/")],
    "tools_misc": [m for m in moves if m[1].startswith("docs/tools/misc/")],
    "programming_c": [m for m in moves if m[1].startswith("docs/programming/c-cpp/")],
    "programming_python": [m for m in moves if m[1].startswith("docs/programming/python/")],
    "programming_shell": [m for m in moves if m[1].startswith("docs/programming/shell/")],
    "windows": [m for m in moves if m[1].startswith("docs/windows/")],
    "cheatsheet": [m for m in moves if m[1].startswith("docs/cheatsheet/")],
}

# merge embedded subgroups for commit
# we will do 4 embedded commits: buildroot, yocto, kernel, hardware
# but for finer granularity, keep them separate as above, but combine for final commits? Do per group commit.

# Define commit plan: (message, list of groups or explicit files)
commit_plan = [
    ("chore: add reorganization plan and scripts", ["MAPPING.md", "TODO.md", "scripts/"]),
    ("docs(linux): reorganize distro (9篇)", ["linux"]), # will handle linux group (all linux)
    ("docs(embedded): reorganize buildroot (4篇)", ["embedded_buildroot"]),
    ("docs(embedded): reorganize yocto & openwrt (2篇)", ["embedded_yocto"]),
    ("docs(embedded): reorganize kernel (6篇)", ["embedded_kernel"]),
    ("docs(embedded): reorganize hardware (5篇)", ["embedded_hardware"]),
    ("docs(git): reorganize git (16篇)", ["git"]),
    ("docs(network): reorganize proxy & vpn (8篇)", ["network"]),
    ("docs(tools): reorganize apt (4篇)", ["tools_apt"]),
    ("docs(tools): reorganize ssh (5篇)", ["tools_ssh"]),
    ("docs(tools): reorganize samba & misc (9篇)", ["tools_samba", "tools_misc"]),
    ("docs(programming): reorganize c-cpp/python/shell (8篇)", ["programming_c", "programming_python", "programming_shell"]),
    ("docs(windows): reorganize windows (3篇)", ["windows"]),
    ("docs(cheatsheet): reorganize cheatsheet (2篇)", ["cheatsheet"]),
    ("docs: add category indexes and navigation", ["indexes", "config"]),
]

# But we have linux group includes all 3 sub, we will split linux into one commit for simplicity, but could split into 3.
# For this plan, linux will be one commit with 17 files + index.

# For indexes/config commit: includes docs/*/index.md, mkdocs.yml, docs/index.md, docs/blog/tags.md, 分类.md, home.md, template

import os

def git_add(paths):
    # paths may be directories or files, need to handle spaces
    # use git add --all with pathspec?
    for p in paths:
        # use git add -A for that path, but need to handle deletions
        # For directories, git add will add new files but not deletions of old
        # So we need to use git add -A -- <path> and also for old src deletions we need to add -u
        # For new dirs, just git add
        if p in ["MAPPING.md", "TODO.md", "scripts/"]:
            run(f'git add -- "{p}"')
        elif p == "indexes":
            # add all index.md files
            for idx in ["docs/linux/index.md","docs/embedded/index.md","docs/git/index.md","docs/network/index.md","docs/tools/index.md","docs/programming/index.md","docs/windows/index.md","docs/cheatsheet/index.md"]:
                run(f'git add -- "{idx}"')
        elif p == "config":
            run(f'git add -- "mkdocs.yml" "docs/index.md" "docs/blog/tags.md" "分类.md" "home.md" "template/Front-matter.md"')
        else:
            # p is group key
            group = groups[p]
            # add new files (dst)
            for src, dst in group:
                # add new file
                run(f'git add -- "{dst}"')
                # stage deletion of old (src) - if src exists as deleted, git add -u will stage it
                # Use git rm if file no longer exists but git still tracks it as deleted?
                # git add -u will stage deletion
                run(f'git add -u -- "{src}"')
            # also add index if relevant? For linux group, also need docs/linux/index.md
            if p == "linux":
                run(f'git add -- "docs/linux/index.md"')
            # for embedded subgroups, the embedded/index.md should be added with one of them, say buildroot
            if p == "embedded_buildroot":
                run(f'git add -- "docs/embedded/index.md"')
            if p == "git":
                run(f'git add -- "docs/git/index.md"')
            if p == "network":
                run(f'git add -- "docs/network/index.md"')
            if p == "tools_samba":
                # tools index will be added with samba group
                run(f'git add -- "docs/tools/index.md"')
            if p == "programming_c":
                run(f'git add -- "docs/programming/index.md"')
            if p == "windows":
                run(f'git add -- "docs/windows/index.md"')
            if p == "cheatsheet":
                run(f'git add -- "docs/cheatsheet/index.md"')

# Execute plan
for msg, items in commit_plan:
    print(f"\n=== COMMIT: {msg} ===")
    # clean any previous staged? Ensure we start clean per commit: add only those items
    for item in items:
        git_add([item])
    # check staged
    run("git status --porcelain --staged | head -n 50")
    staged = subprocess.run("git diff --cached --name-only | wc -l", shell=True, cwd=base, capture_output=True, text=True)
    count = staged.stdout.strip()
    print(f"Staged files count: {count}")
    if count == "0":
        print("SKIP empty commit")
        continue
    # commit
    # need to ensure commit message with proper quoting
    # use file for message to handle special chars
    msg_file = base / "/tmp/commit_msg.txt"
    # write msg
    pathlib.Path("/tmp/commit_msg.txt").write_text(msg + "\n\nCo-authored-by: pi <pi@playground>\n", encoding="utf-8")
    run(f'git commit -F /tmp/commit_msg.txt')
    run("git log --oneline -1")
    run("git status --porcelain | head -n 20")

print("\n=== FINAL LOG ===")
run("git log --oneline -20")
run("git status --porcelain | head -n 100")
