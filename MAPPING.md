# 文档重组映射表

> 83 篇 `docs/posts` + 6 篇 `WIP` → 8 物理目录，`nav` 合并为 7 节
> 原文件名保留（中文+空格），仅移动路径；`categories` 归一为 `categories:`

## 目录结构

```
docs/
  index.md
  linux/
    index.md
    distro/        # 发行版安装/镜像/源
    filesystem/    # 文件系统/分区/扩容
    system/        # 系统管理/用户/网络配置
  embedded/
    index.md
    buildroot/
    yocto/
    kernel/
    hardware/
  git/
    index.md
  network/
    index.md
    proxy/         # VPN/代理/穿透
  tools/
    index.md
    apt/
    ssh/
    samba/
    misc/
  programming/
    index.md
    c-cpp/
    python/
    shell/
  windows/
    index.md
  cheatsheet/
    index.md
  blog/tags.md  # 保留
  assets/
```

## 映射（原 → 新）

### 1. linux/distro (10)
| 原 | 新 | categories | tags 修正 |
|---|---|---|---|
| `docs/posts/archlinux install record.md` | `docs/linux/distro/archlinux-install-record.md` | `linux` | `linux, system`→`linux, distro` |
| `docs/posts/Arch linux ext4 文件系统转 Btrfs.md` | `docs/linux/filesystem/arch-ext4-to-btrfs.md` | `linux` | `linux` |
| `docs/posts/Arch Linux 硬盘扩容迁移.md` | `docs/linux/filesystem/arch-disk-migration.md` | `linux` | `linux` |
| `docs/posts/Gentoo Linux 安装指南.md` | `docs/linux/distro/gentoo-install.md` | `linux` | `linux` (去 `category: www`) |
| `docs/posts/gentoo 源设置.md` | `docs/linux/distro/gentoo-mirror.md` | `linux` | `linux` |
| `docs/posts/rock5b 设置记录.md` | `docs/linux/distro/rock5b-setup.md` | `linux` | `linux` |
| `docs/posts/Ubuntu 彻底移除Snap.md` | `docs/linux/distro/ubuntu-remove-snap.md` | `linux` | `linux` |
| `docs/posts/Ubuntu 没有网络连接.md` | `docs/linux/distro/ubuntu-no-network.md` | `linux` | `linux` |
| `docs/posts/ubuntu 设置虚拟显示器输出.md` | `docs/linux/distro/ubuntu-virtual-display.md` | `linux` | `linux` |
| `docs/posts/删除Ubunut Pro.md` | `docs/linux/distro/remove-ubuntu-pro.md` | `linux` | `linux` |
| `docs/posts/LFS 记录.md` | `docs/linux/distro/lfs-record.md` | `linux` | `linux` |

### 2. linux/filesystem + system (11)
| `linux 缩小分区大小.md` | `docs/linux/filesystem/shrink-partition.md` | `linux` | `linux` |
| `linux 网络排查.md` | `docs/linux/system/network-troubleshoot.md` | `linux` | `linux` |
| `linux 用户使用.md` | `docs/linux/system/user-management.md` | `linux` | `linux` |
| `linux 中使用 ctrl+z 停止任务后如何恢复任务.md` | `docs/linux/system/ctrl-z-resume.md` | `linux` | `linux` |
| `查看linux 版本信息 & 更改密码.md` | `docs/linux/system/version-and-passwd.md` | `linux` | `linux` |
| `设置静态 IP 地址.md` | `docs/linux/system/static-ip.md` | `linux` | `linux` |
| `freebsd 13 安装 samba server.md` | `docs/tools/samba/freebsd13-samba.md` | `tools` | `samba, tool→tool` (实际归 samba) |
| 备注：`freebsd` 暂归 `tools/samba` 更贴切，见下 |

### 3. embedded (15)
| `Buildroot 使用 crontab 和 crond 完成定时任务.md` | `docs/embedded/buildroot/crontab-crond.md` | `embedded` | `linux→embedded, buildroot` |
| `buildroot  如何仅获取 toolchain.md` | `docs/embedded/buildroot/toolchain-only.md` | `embedded` | `linux→embedded, buildroot` |
| `WIP/buildroot  静态ip 设置.md` | `docs/embedded/buildroot/static-ip.md` | `embedded` | `linux, buildroot` |
| `Yocoto 调试总结.md` | `docs/embedded/yocto/debug-summary.md` | `embedded` | `linux→embedded, yocto` |
| `OpenWrt 使用记录.md` | `docs/embedded/yocto/openwrt-record.md` | `embedded` | `linux, wip→embedded, openwrt` |
| `openocd 使用.md` | `docs/embedded/hardware/openocd.md` | `embedded` | `linux→embedded, openocd` |
| `Linux 内核开发.md` | `docs/embedded/kernel/linux-kernel-dev.md` | `embedded` | `kernel→kernel, embedded` |
| `内核内存管理.md` | `docs/embedded/kernel/memory-management.md` | `embedded` | `kernel` |
| `内核网络设备驱动.md` | `docs/embedded/kernel/net-device-driver.md` | `embedded` | `kernel` |
| `内核驱动初始化顺序.md` | `docs/embedded/kernel/driver-init-order.md` | `embedded` | `linux→kernel, embedded` |
| `CMOS Sensor 的一些基本概念.md` | `docs/embedded/hardware/cmos-sensor.md` | `embedded` | `kernel→embedded, hardware` |
| `imx8mm sai rx 时钟线配置.md` | `docs/embedded/hardware/imx8mm-sai-rx.md` | `embedded` | `kernel→embedded, hardware` |
| `linux Fan driver.md` | `docs/embedded/hardware/fan-driver.md` | `embedded` | `linux→embedded, hardware` |
| `ELF 文件查看.md` | `docs/embedded/kernel/elf-inspect.md` | `embedded` | `linux→embedded, elf` |
| `手把手解析ELF文件格式：从Hello World到二进制奥秘.md` | `docs/embedded/kernel/elf-format-deep.md` | `embedded` | `linux→embedded, elf` |
| `WIP/gpio keypad.md` | `docs/embedded/hardware/gpio-keypad.md` | `embedded` | `linux, gpio` |
| `repo 拉取仓库.md` | `docs/embedded/buildroot/repo-manifest.md` | `embedded` | `linux→embedded, repo` |

### 4. git (16)
| `git cherry-pick 代码片段.md` | `docs/git/cherry-pick.md` | `git` | `git` |
| `git diff 生成patch 并应用.md` | `docs/git/diff-patch.md` | `git` | `git, tool→git` |
| `git  Merge vs Rebase.md` | `docs/git/merge-vs-rebase.md` | `git` | `git, tool→git` |
| `git pull request.md` | `docs/git/pull-request.md` | `git` | `git` (去 `category: www`) |
| `git 修剪分支.md` | `docs/git/prune-branch.md` | `git` | `git, tool→git` |
| `git 修改第一个commit 信息.md` | `docs/git/edit-first-commit.md` | `git` | `git, tool→git` |
| `git 修改配置文件.md` | `docs/git/config-file.md` | `git` | `git, tool→git` |
| `git分割commit 推送到远程仓库.md` | `docs/git/split-push.md` | `git` | `git, tool→git` |
| `git 分块推送.md` | `docs/git/chunked-push.md` | `git` | `git, tool→git` |
| `git 合并commit.md` | `docs/git/squash-commit.md` | `git` | `git, tool→git` |
| `git 同步Fork 源仓库.md` | `docs/git/sync-fork.md` | `git` | `git, tool→git` |
| `git 将token 添加到远程仓库链接中.md` | `docs/git/token-remote.md` | `git` | `git, tool→git` |
| `git 打包仓库.md` | `docs/git/archive-repo.md` | `git` | `git, tool→git` |
| `git 查看历史记录.md` | `docs/git/log-history.md` | `git` | `git, tool→git` |
| `git 设置和取消代理.md` | `docs/git/proxy.md` | `git` | `git, tool→git` |
| `WIP/gitea 部署记录.md` | `docs/git/gitea-deploy.md` | `git` | `git, tool, wip→git, gitea` |

### 5. network/proxy (9)
| `cloudflared 内网代理.md` | `docs/network/proxy/cloudflared.md` | `network` | `linux, tool→network, proxy` |
| `openvpn 局域网内分享网络.md` | `docs/network/proxy/openvpn-share.md` | `network` | `linux→network, vpn` |
| `wireguard 部署记录.md` | `docs/network/proxy/wireguard.md` | `network` | `linux→network, vpn` |
| `v2ray 脚本安装.md` | `docs/network/proxy/v2ray.md` | `network` | `linux→network, proxy` (清 `abbrlink`) |
| `trojan-gfw 安装记录.md` | `docs/network/proxy/trojan.md` | `network` | `linux→network, proxy` |
| `搭建clash 并且分享网络.md` | `docs/network/proxy/clash-share.md` | `network` | `linux, tool→network, proxy` |
| `WIP/安装FreeBSD 并搭建clash.md` | `docs/network/proxy/freebsd-clash.md` | `network` | `wip→network, clash` |
| `在 FreeBSD 13 上安装 gitea.md` | `docs/network/proxy/freebsd-gitea.md` | `network` | `tool→network` (移至 network 更合适，备选 tools/misc) |
| `钉钉无法输入中文.md` | `docs/network/proxy/dingtalk-cjk.md` | `network` | `linux, tool→network, tool` |

### 6. tools (16)
| `add-apt-repository 命令安装,卸载和使用.md` | `docs/tools/apt/add-apt-repository.md` | `tools` | `apt, tool` |
| `apt certificate verification failed.md` | `docs/tools/apt/cert-verify-failed.md` | `tools` | `apt, tool` |
| `apt-key 添加公钥.md` | `docs/tools/apt/apt-key.md` | `tools` | `apt, tool` |
| `apt 命令使用代理.md` | `docs/tools/apt/apt-proxy.md` | `tools` | `apt, tool` |
| `ssh 向linux添加公钥.md` | `docs/tools/ssh/add-pubkey.md` | `tools` | `ssh, tool` |
| `ssh 快速删除known_hosts记录.md` | `docs/tools/ssh/clean-known_hosts.md` | `tools` | `ssh, tool` |
| `ssh 添加使用私钥.md` | `docs/tools/ssh/use-private-key.md` | `tools` | `ssh, tool` |
| `ssh 端口转发.md` | `docs/tools/ssh/port-forward.md` | `tools` | `ssh, tool` |
| `ssh 设置代理.md` | `docs/tools/ssh/ssh-proxy.md` | `tools` | `ssh, tool` |
| `samba 分享文件.md` | `docs/tools/samba/share-file.md` | `tools` | `linux, tool→samba` |
| `samba 用户管理.md` | `docs/tools/samba/user-mgmt.md` | `tools` | `linux, tool→samba` |
| `freebsd 13 安装 samba server.md` | `docs/tools/samba/freebsd13-samba.md` | `tools` | `tool→samba` |
| `tmux 使用.md` | `docs/tools/misc/tmux.md` | `tools` | `tool` |
| `zsh 增加命令历史记录.md` | `docs/tools/misc/zsh-history.md` | `tools` | `tool→shell, tool` |
| `使用UEFI Shell引导U盘启动.md` | `docs/tools/misc/uefi-shell-boot.md` | `tools` | `tool→boot, uefi` |
| `vscode 设置 compare view.md` | `docs/tools/misc/vscode-compare.md` | `tools` | `vscode, tool` |
| `windows 中添加右键菜单 - 在vscode 中打开.md` | `docs/windows/vscode-context-menu.md` | `windows` | `tool→windows, vscode` (归 windows) |
| `查看python所支持的wheel包.md` | `docs/tools/misc/wheel-support.md` | `tools` | `tool→python, tool` |
| `创建ASCII码的目录树.md` | `docs/programming/shell/ascii-tree.md` | `programming` | `shell, tool→shell` |
| `Shell 命令去除字符串中回车符.md` | `docs/programming/shell/strip-crlf.md` | `programming` | `linux→shell` |

### 7. programming (8)
| `c 文件IO.md` | `docs/programming/c-cpp/file-io.md` | `programming` | `cheatsheet→c, io` |
| `c 预处理器.md` | `docs/programming/c-cpp/preprocessor.md` | `programming` | `cheatsheet→c` |
| `去掉宏__FILE__的路径.md` | `docs/programming/c-cpp/strip-file-macro.md` | `programming` | `c/cpp→c` |
| `嵌入式C功能代码片段.md` | `docs/programming/c-cpp/embedded-snippets.md` | `programming` | `c/cpp→c, embedded` |
| `python pip 设置代理.md` | `docs/programming/python/pip-proxy.md` | `programming` | `python→python` (去 `category: tool`) |
| `python 查看动态链接库地址.md` | `docs/programming/python/dynlib-path.md` | `programming` | `python→python` (去 `category: code`) |
| `Shell 命令去除字符串中回车符.md` | `docs/programming/shell/strip-crlf.md` | `programming` | 见上 |
| `创建ASCII码的目录树.md` | `docs/programming/shell/ascii-tree.md` | `programming` | 见上 |

### 8. windows & cheatsheet
| `Windows 10 分享网络设置.md` | `docs/windows/win10-share.md` | `windows` | `windows` |
| `windows 中添加右键菜单 - 在vscode 中打开.md` | `docs/windows/vscode-context-menu.md` | `windows` | 见上 |
| `WIP/google chrome 强制启用 secure dns.md` | `docs/windows/chrome-doh.md` | `windows` | `windows` |
| `Markdown 速查表.md` | `docs/cheatsheet/markdown.md` | `cheatsheet` | `cheatsheet` |
| `c 文件IO.md` / `c 预处理器.md` | `docs/cheatsheet/` 不重复，主归 `programming/c-cpp`，`cheatsheet` 索引用 tag 聚合 |
| `WIP/DWM shortcuts cheetsheet.md` | `docs/cheatsheet/dwm-shortcuts.md` | `cheatsheet` | `linux→cheatsheet, dwm` |

### 9. 其他
| `搭` |  |
| `在 FreeBSD 13 上安装 gitea.md` | 备选 `docs/tools/misc/freebsd-gitea.md` 若 network 不合适可调至 `tools/misc` |

> 注：最终执行时保留原中文名亦可，此表为 slug 建议；为兼容历史链接，优先保留原文件名仅改目录（下文脚本保留原名）。本表 slug 列仅作导航可读性参考，实际 `git mv` 保留原名更稳妥。
> **执行策略**：保留原文件名，仅移动目录，避免大量重命名导致外链失效。slug 化可在 FrontMatter `slug:` 另加。

## 实际执行：保留原名移动

为最小惊动，实际执行：
- `docs/posts/<原名>.md` → `docs/<分类>/<原子目录>/<原名>.md`（原名不变）
- 如 `docs/posts/git 合并commit.md` → `docs/git/git 合并commit.md`
- `WIP/*` 同理

此 MAPPING.md 的 slug 列仅文档化意图，最终脚本以“目录归类”为准。
